import pymysql
import random
debug = True

# mysql://user:password@host/db?reconnect=true
db = pymysql.connect(host = 'us-cdbr-iron-east-05.cleardb.net', user = 'bcd13fd218388b', password = '2cb6b6c9', db = 'heroku_c725ae86619cb3a', autocommit = True, sql_mode = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION')
cur = db.cursor()
cur.execute('set @@auto_increment_increment=1')

class Exercise:
	def __init__(self, name = None, guide = None, url = None, difficulty = None, part = None, weight = None, time = None, reps = None, sets = None):
		self.name = name
		self.guide = guide
		self.url = url
		self.difficulty = difficulty
		self.part = part
		self.weight = weight
		self.time = time
		self.reps = reps
		self.sets = sets

class Routine:
	def __init__(self, id = None, criteria = None, split_cnt = None, exercise_list_list = None):
		self.id = id
		self.criteria = criteria
		self.split_cnt = split_cnt
		self.exercise_list_list = exercise_list_list

class User:
	def __init__(self, id = None, purpose = None, criteria = None, preffered_split_cnt = None, level = None, split_cnt = None, current_split_no = None):
		self.id = id
		self.purpose = purpose
		self.criteria = criteria
		self.preffered_split_cnt = preffered_split_cnt
		self.level = level
		self.split_cnt = split_cnt
		self.current_split_no = current_split_no

class History:
	def __init__(self, user_id = None, log_dic = None):
		self.user_id = user_id
		self.log_dic = log_dic

def get_query():
	q = ''
	while True:
		print('> ', end = '')
		p = input()
		if p == '':
			break
		q += p + '\n'
	return q

def execute_query(q):
	if debug:
		print(f'executing query..\n{q}')
	rows = None
	try:
		db.ping(reconnect=True)
		cur.execute(q)
		rows = cur.fetchall()
		if debug:
			for row in rows:
				print(row)
			print()	
	except Exception as e:
		print(f'ERROR({e.args[0]}): {e.args[1]}')
		print()
	return rows

def create_part_type(part_list):
	q = 'insert into part_type values '
	for part in part_list:
		q += f', (\'{part}\')'
	q = q.replace(', ', '', 1)
	execute_query(q)

def delete_part_type(part):
	q = f'delete from part_type where part=\'{part}\''
	execute_query(q)

def create_problem_part_type(part_list):
	q = 'insert into problem_part_type values '
	for part in part_list:
		q += f', (\'{part}\')'
	q = q.replace(', ', '', 1)
	execute_query(q)

def delete_problem_part_type(part):
	q = f'delete from problem_part_type where part=\'{part}\''
	execute_query(q)

def get_problem_part_types():
	q = f'select * from problem_part_type'
	rows = execute_query(q)
	types = []
	for row in rows:
		types.append(row[0])
	return types

def create_purpose_type(purpose_list):
	q = 'insert into purpose_type values '
	for purpose in purpose_list:
		q += f', (\'{purpose}\')'
	q = q.replace(', ', '', 1)
	execute_query(q)

def delete_purpose_type(purpose):
	q = f'delete from purpose_type where purpose=\'{purpose}\''
	execute_query(q)

def create_criteria_type(criteria_list):
	q = 'insert into criteria_type values '
	for criteria in criteria_list:
		q += f', (\'{criteria}\')'
	q = q.replace(', ', '', 1)
	execute_query(q)

def delete_criteria_type(criteria):
	q = f'delete from criteria_type where criteria=\'{criteria}\''
	execute_query(q)

def create_general_exercise(exercise_list):
	q = 'insert into general_exercise values '
	for exercise in exercise_list:
		q += f', (\'{exercise.name}\', \'{exercise.guide}\', \'{exercise.url}\', {exercise.difficulty}, \'{exercise.part}\', {exercise.weight}, {exercise.time}, {exercise.reps}, {exercise.sets})'
	q = q.replace(', ', '', 1).replace('None', 'NULL').replace('\'None\'', 'NULL')
	execute_query(q)

def update_general_exercise(name, exercise_):
	q = f'update general_exercise set name=\'{exercise_.name}\', guide=\'{exercise_.guide}\', url=\'{exercise_.url}\', difficulty={exercise_.difficulty}, part=\'{exercise_.part}\', weight={exercise_.weight}, time={exercise_.time}, reps={exercise_.reps}, sets={exercise_.sets} where name=\'{name}\''
	q = q.replace('None', 'NULL').replace('\'None\'', 'NULL')
	execute_query(q)

def delete_general_exercise(name):
	q = f'delete from general_exercise where name=\'{name}\''
	execute_query(q)

def get_general_exercise(name):
	q = f'select * from general_exercise where name=\'{name}\''
	rows = execute_query(q)
	exercise = Exercise(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4], rows[0][5], rows[0][6], rows[0][7], rows[0][8])
	return exercise

def get_general_exercise_names():
	q = f'select * from general_exercise'
	rows = execute_query(q)
	names = []
	for row in rows:
		names.append(row[0])
	return names

def create_sample_routine(routine_list):
	for routine in routine_list:
		q = f'insert into sample_info (criteria, split_cnt) values (\'{routine.criteria}\', {routine.split_cnt})'
		execute_query(q)
		q = 'insert into sample_routine values '
		for split_no in range(len(routine.exercise_list_list)):
			for position in range(len(routine.exercise_list_list[split_no])):
				exercise = routine.exercise_list_list[split_no][position]
				q += f', (last_insert_id(), {split_no}, {position}, \'{exercise.name}\', {exercise.weight}, {exercise.time}, {exercise.reps}, {exercise.sets})'
		q = q.replace(', ', '', 1).replace('None', 'NULL').replace('\'None\'', 'NULL')
		execute_query(q)

def update_sample_routine(id, routine_):
	q = f'update sample_info set criteria=\'{routine_.criteria}\', split_cnt={routine_.split_cnt} where id={id}'
	execute_query(q)
	q = f'delete from sample_routine where sample_id={id}'
	execute_query(q)
	q = 'insert into sample_routine values '
	for split_no in range(len(routine_.exercise_list_list)):
		for position in range(len(routine_.exercise_list_list[split_no])):
			exercise_ = routine_.exercise_list_list[split_no][position]
			q += f', ({id}, {split_no}, {position}, \'{exercise_.name}\', {exercise_.weight}, {exercise_.time}, {exercise_.reps}, {exercise_.sets})'
	q = q.replace(', ', '', 1).replace('None', 'NULL').replace('\'None\'', 'NULL')
	execute_query(q)

def delete_sample_routine(id):
	q = f'delete from sample_routine where sample_id={id}'
	execute_query(q)
	q = f'delete from sample_info where id={id}'
	execute_query(q)

def get_sample_routine(id):
	q1 = f'select * from sample_info where id={id}'
	rows1 = execute_query(q1)
	q2 = f'select * from sample_routine where sample_id={id} order by split_no, position'
	rows2 = execute_query(q2)
	exercise_list_list = []
	exercise_list = []
	split_no = 0
	for row in rows2:
		while row[1] > split_no:
			exercise_list_list.append(exercise_list)
			exercise_list = []
			split_no += 1
		exercise = Exercise(name = row[3], weight = row[4], time = row[5], reps = row[6], sets = row[7])
		exercise_list.append(exercise)
	while split_no < rows1[0][2]:
		exercise_list_list.append(exercise_list)
		exercise_list = []
		split_no += 1
	routine = Routine(id, rows1[0][1], rows1[0][2], exercise_list_list)
	return routine

def create_user_info(user):
	q = f'insert into user_info values ({user.id}, \'{user.purpose}\', \'{user.criteria}\', {user.preffered_split_cnt}, {user.level}, {user.split_cnt}, {user.current_split_no})'
	execute_query(q)

def update_user_info(id, user_):
	q = f'update user_info set id={user_.id}, purpose=\'{user_.purpose}\', criteria=\'{user_.criteria}\', preffered_split_cnt={user_.preffered_split_cnt}, level={user_.level}, split_cnt={user_.split_cnt}, current_split_no={user_.current_split_no} where id={id}'
	execute_query(q)

def increase_user_current_split_no(id):
	q = f'update user_info set current_split_no=if(current_split_no+1<split_cnt, current_split_no+1, 0) where id={id}'
	execute_query(q)

def delete_user_info(id):
	q = f'delete from user_history where user_id={id}'
	execute_query(q)
	q = f'delete from user_routine where user_id={id}'
	execute_query(q)
	q = f'delete from user_info where id={id}'
	execute_query(q)

def get_user_info(id):
	q = f'select * from user_info where id={id}'
	rows = execute_query(q)
	if not rows:
		return None
	user = User(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4], rows[0][5], rows[0][6])
	return user

def create_user_routine(routine):
	q = f'update user_info set split_cnt={routine.split_cnt}, current_split_no=0 where id={routine.id}'
	execute_query(q)
	q = 'insert into user_routine values '
	for split_no in range(len(routine.exercise_list_list)):
		for position in range(len(routine.exercise_list_list[split_no])):
			exercise = routine.exercise_list_list[split_no][position]
			q += f', ({routine.id}, {split_no}, {position}, \'{exercise.name}\', {exercise.weight}, {exercise.time}, {exercise.reps}, {exercise.sets})'
	q = q.replace(', ', '', 1).replace('None', 'NULL').replace('\'None\'', 'NULL')
	execute_query(q)

def create_user_routine_exercise(user_id, split_no, position, exercise):
	q = f'update user_routine set position=position+1 where user_id={user_id} and split_no={split_no} and position>={position} order by position desc'
	execute_query(q)
	q = f'insert into user_routine values ({user_id}, {split_no}, {position}, \'{exercise.name}\', {exercise.weight}, {exercise.time}, {exercise.reps}, {exercise.sets})'
	q = q.replace('None', 'NULL').replace('\'None\'', 'NULL')
	execute_query(q)

def update_user_routine(user_id, routine_):
	delete_user_routine(user_id)
	routine_.id = user_id
	create_user_routine(routine_)

def update_user_routine_exercise(user_id, split_no, position, exercise_):
	q = f'update user_routine set user_id={user_id}, split_no={split_no}, position={position}, exercise_name=\'{exercise_.name}\', weight={exercise_.weight}, time={exercise_.time}, reps={exercise_.reps}, sets={exercise_.sets} where user_id={user_id} and split_no={split_no} and position={position}'
	q = q.replace('None', 'NULL').replace('\'None\'', 'NULL')
	execute_query(q)

def delete_user_routine(user_id):
	q = f'delete from user_routine where user_id={user_id}'
	execute_query(q)

def delete_user_routine_exercise(user_id, split_no, position):
	q = f'delete from user_routine where user_id={user_id} and split_no={split_no} and position={position}'
	execute_query(q)
	q = f'update user_routine set position=position-1 where user_id={user_id} and split_no={split_no} and position>{position} order by position'
	execute_query(q)

def get_user_routine(user_id):
	q = f'select * from user_routine, user_info where user_id={user_id} and id=user_id order by split_no, position'
	rows = execute_query(q)
	if rows:
		exercise_list_list = []
		exercise_list = []
		split_no = 0
		for row in rows:
			while row[1] > split_no:
				exercise_list_list.append(exercise_list)
				exercise_list = []
				split_no += 1
			exercise = Exercise(name = row[3], weight = row[4], time = row[5], reps = row[6], sets = row[7])
			exercise_list.append(exercise)
		while split_no < rows[0][13]:
			exercise_list_list.append(exercise_list)
			exercise_list = []
			split_no += 1
		routine = Routine(user_id, None, rows[0][13], exercise_list_list)
		return routine
	else:
		user = get_user_info(user_id)
		routine = Routine(user_id, None, user.split_cnt, [[]] * user.split_cnt)
		return routine

def create_user_history(history):
	q = 'insert into user_history values '
	for exercise_name, log in history.log_dic.items():
		q += f', ({history.user_id}, \'{exercise_name}\', {log[0]}, {log[1]})'
	q = q.replace(', ', '', 1).replace('None', 'NULL').replace('\'None\'', 'NULL')
	execute_query(q)

def update_user_history(user_id, history_):
	delete_user_history(user_id)
	history_.user_id = user_id
	create_user_history(history_)

def delete_user_history(user_id):
	q = f'delete from user_history where user_id={user_id}'
	execute_query(q)

def increase_user_history_completion(user_id):
	q = f'insert into user_history select id, exercise_name, 1, 0 from user_info, user_routine where user_id={user_id} and current_split_no=split_no on duplicate key update completion=completion+1'
	execute_query(q)

def increase_user_history_rejection(user_id, exercise):
	q = f'insert into user_history values ({user_id}, \'{exercise.name}\', 0, 1) on duplicate key update rejection=rejection+1'
	execute_query(q)

def get_routine_recommendation(user_id):
	user = get_user_info(user_id)
	q = 'select * from sample_info'
	rows = execute_query(q)
	candidates = [[], [], [], []]
	for row in rows:
		if row[1] == user.criteria and row[2] == user.preffered_split_cnt:
			candidates[0].append(row[0])
		elif row[1] == user.criteria:
			candidates[1].append(row[0])
		elif row[2] == user.preffered_split_cnt:
			candidates[2].append(row[0])
		else:
			candidates[3].append(row[0])
	if candidates[0]:
		sample_id = random.choice(candidates[0])
	elif candidates[1]:
		sample_id = random.choice(candidates[1])
	elif candidates[2]:
		sample_id = random.choice(candidates[2])
	elif candidates[3]:
		sample_id = random.choice(candidates[3])
	return get_sample_routine(sample_id)

def calculate_user_level(user_id):
	q = f'select level, difficulty, sum(completion) from user_info, user_history, general_exercise where id={user_id} and id=user_id and exercise_name=name group by difficulty'
	rows = execute_query(q)
	if rows:
		user_level = rows[0][0]
		for row in rows:
			if row[2] >= 20 and row[1] + 1 > user_level: # 20 is arbitrary integer number
				user_level = row[1] + 1
		if user_level > rows[0][0]:
			q = f'update user_info set level={user_level} where id={user_id}'
			execute_query(q)
		return user_level
	else:
		user = get_user_info(user_id)
		return user.level

def analyze_user_routine(user_id):
	q = f'select part_type.part, count(if(part_type.part=general_exercise.part, 1, NULL)) from part_type, general_exercise, user_routine where user_id={user_id} and name=exercise_name group by part_type.part'
	rows = execute_query(q)
	total = 0

	if rows:
		for row in rows:
			total += row[1]
		insufficient_boundary = total / len(rows) * 0.3 # 0.3 is arbitrary real number
		absent_part = []
		insufficient_part = []
		enough_part = []
		for row in rows:
			if row[1] == 0:
				absent_part.append(row[0])
			elif row[1] < insufficient_boundary:
				insufficient_part.append(row[0])
			else:
				enough_part.append(row[0])
		return absent_part, insufficient_part, enough_part
	else:
		q = f'select * from part_type'
		rows = execute_query(q)
		absent_part = []
		for row in rows:
			absent_part.append(row[0])
		return absent_part, [], []

def get_exercise_score(user_id):
	q = f'select name, part, count(if(name=exercise_name, 1, NULL)), difficulty, level, (select completion from user_history where user_id=id and name=exercise_name), (select rejection from user_history where user_id=id and name=exercise_name) from general_exercise, user_info, user_routine where id={user_id} and user_id=id group by name'
	rows = execute_query(q)
	exercise_recommendation_score = []
	exercise_replacement_score = []
	if rows:
		for row in rows:
			if row[5] == None:
				row = row[:-2] + (0, 0)
			if row[2] == 0 and row[3] <= row[4]:
				exercise_recommendation_score.append([row[0], row[1], (- row[5] - row[6] * 7) / row[3]]) # arbitrary score function
			else:
				exercise_replacement_score.append([row[0], row[1], (row[5] + row[6] * 7) / row[3]]) # arbitrary score function
	else:
		q = f'select name, part from general_exercise'
		rows = execute_query(q)
		for row in rows:
			exercise_recommendation_score.append([row[0], row[1], 0])
	return exercise_recommendation_score, exercise_replacement_score

def get_exercise_recommendation(user_id, part = None):
	user_level = calculate_user_level(user_id)
	absent_part, insufficient_part, enough_part = analyze_user_routine(user_id)
	exercise_recommendation_score, exercise_replacement_score = get_exercise_score(user_id)

	if part:
		if part in absent_part:
			max_score = None
			recommended_exercise_list = None
			for rec in exercise_recommendation_score:
				if rec[1] == part and (max_score == None or max_score < rec[2]):
					max_score = rec[2]
					recommended_exercise_list = [rec[0]]
				elif rec[1] == part and max_score == rec[2]:
					recommended_exercise_list.append(rec[0])
			if recommended_exercise_list:
				return 'absent', random.choice(recommended_exercise_list)
			else:
				return None
		elif part in insufficient_part:
			max_score = None
			recommended_exercise_list = None
			for rec in exercise_recommendation_score:
				if rec[1] == part and (max_score == None or max_score < rec[2]):
					max_score = rec[2]
					recommended_exercise_list = [rec[0]]
				elif rec[1] == part and max_score == rec[2]:
					recommended_exercise_list.append(rec[0])
			if recommended_exercise_list:
				return 'insufficient', random.choice(recommended_exercise_list)
			else:
				return None
		else:
			max_score = None
			exercise_pair_list = None
			for rec in exercise_recommendation_score:
				for rep in exercise_replacement_score:
					if rec[1] == rep[1] == part and (max_score == None or max_score < rec[2] + rep[2]):
						max_score = rec[2] + rep[2]
						exercise_pair_list = [(rec[0], rep[0])]
					elif rec[1] == rep[1] == part and max_score == rec[2] + rep[2]:
						exercise_pair_list.append((rec[0], rep[0]))
			if exercise_pair_list:
				exercise_pair = random.choice(exercise_pair_list)
				return 'enough', exercise_pair[0], exercise_pair[1]
			else:
				return None
	else:
		if absent_part:
			max_score = None
			recommended_exercise_list = None
			for rec in exercise_recommendation_score:
				if rec[1] in absent_part and (max_score == None or max_score < rec[2]):
					max_score = rec[2]
					recommended_exercise_list = [rec[0]]
				elif rec[1] in absent_part and max_score == rec[2]:
					recommended_exercise_list.append(rec[0])
			if recommended_exercise_list:
				return 'absent', random.choice(recommended_exercise_list)
			else:
				return None
		elif insufficient_part:
			max_score = None
			recommended_exercise_list = None
			for rec in exercise_recommendation_score:
				if rec[1] in insufficient_part and (max_score == None or max_score < rec[2]):
					max_score = rec[2]
					recommended_exercise_list = [rec[0]]
				elif rec[1] in insufficient_part and max_score == rec[2]:
					recommended_exercise_list.append(rec[0])
			if recommended_exercise_list:
				return 'insufficient', random.choice(recommended_exercise_list)
			else:
				return None
		else:
			max_score = None
			exercise_pair_list = None
			for rec in exercise_recommendation_score:
				for rep in exercise_replacement_score:
					if rec[1] == rep[1] and (max_score == None or max_score < rec[2] + rep[2]):
						max_score = rec[2] + rep[2]
						exercise_pair_list = [(rec[0], rep[0])]
					elif rec[1] == rep[1] and max_score == rec[2] + rep[2]:
						exercise_pair_list.append((rec[0], rep[0]))
			if exercise_pair_list:
				exercise_pair = random.choice(exercise_pair_list)
				return 'enough', exercise_pair[0], exercise_pair[1]
			else:
				return None

if __name__ == "__main__":
	while True:
		q = get_query()
		if q == '':
			break
		execute_query(q)