from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction

import db
debug = False

def get_user_id(tracker):
	most_recent_state = tracker.current_state()
	sender_id = most_recent_state['sender_id']
	if sender_id == 'default':
		sender_id = 0
	return sender_id

class ActionCheckUserinfo(Action):

	def name(self) -> Text:
		return "action_check_userinfo"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		user_id = get_user_id(tracker)
		u = db.get_user_info(user_id)

		if debug:
			dispatcher.utter_message("action_check_userinfo called!")

		return [SlotSet('new_user', u == None)]
    
class ActionCheckRoutine(Action):

	def name(self) -> Text:
		return "action_check_routine"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		user_id = get_user_id(tracker)
		r = db.get_user_routine(user_id)
		
		if r.exercise_list_list:
			m = f"분할 수: {r.split_cnt}"
			for exercise_list in r.exercise_list_list:
				m += '\n----------'
				for e in exercise_list:
					m += f'\n{e.name}'
					if e.weight != None:
						m += f' {e.weight}kg'
					if e.time != None:
						m += f' {e.time}분'
					if e.reps != None:
						m += f' {e.reps}회'
					if e.sets != None:
						m += f' {e.sets}세트'
			
			dispatcher.utter_message("전체 루틴이야!")
			dispatcher.utter_message(m)
		
		else:
			dispatcher.utter_message("등록된 루틴이 없어.. 먼저 루틴을 추천받아줘!")

		if debug:
			dispatcher.utter_message("action_check_routine called!")

		return []
    
class ActionDeleteUser(Action):

	def name(self) -> Text:
		return "action_delete_user"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		user_id = get_user_id(tracker)
		db.delete_user_info(user_id)
		dispatcher.utter_message("계정 정보가 완전히 삭제되었어. 혹시라도 나중에 돌아올 땐 나한테 인사를 해줘!")

		if debug:
			dispatcher.utter_message("action_delete_user called!")

		return []
    
class ActionLoadUserRoutine(Action):

	def name(self) -> Text:
		return "action_load_user_routine"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		user_id = get_user_id(tracker)
		u = db.get_user_info(user_id)
		r = db.get_user_routine(user_id)
		split_no = u.current_split_no
		exercise_list = r.exercise_list_list[split_no]
		
		if exercise_list:
			m = "오늘의 루틴이야!"
			for e in exercise_list:
				m += f'\n{e.name}'
				if e.weight != None:
					m += f' {e.weight}kg'
				if e.time != None:
					m += f' {e.time}분'
				if e.reps != None:
					m += f' {e.reps}회'
				if e.sets != None:
					m += f' {e.sets}세트'
			m += "\n이대로 진행할래?"
			dispatcher.utter_message(m)
		else:
			m = "루틴에 아무런 운동이 없어 ㅠㅠ"
			dispatcher.utter_message(m)

		if debug:
			dispatcher.utter_message("action_load_user_routine called!")

		return []
	
class ActionRoutineRecommendation(Action):

	def name(self) -> Text:
		return "action_routine_recommendation"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		user_id = get_user_id(tracker)
		r = db.get_routine_recommendation(user_id)
		m = f"분할 수: {r.split_cnt}"
		for exercise_list in r.exercise_list_list:
			m += '\n----------'
			for e in exercise_list:
				m += f'\n{e.name}'
				if e.weight != None:
					m += f' {e.weight}kg'
				if e.time != None:
					m += f' {e.time}분'
				if e.reps != None:
					m += f' {e.reps}회'
				if e.sets != None:
					m += f' {e.sets}세트'
		
		dispatcher.utter_message(m)
		dispatcher.utter_message("네게 추천하는 루틴이야! 어때?")

		if debug:
			dispatcher.utter_message("action_routine_recommendation called!")

		return [SlotSet('recommendation_routine', r.id)]

class ActionRoutineRegister(Action):

	def name(self) -> Text:
		return "action_routine_register"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		user_id = get_user_id(tracker)
		r = db.get_sample_routine(tracker.get_slot('recommendation_routine'))
		db.update_user_routine(user_id, r)

		if debug:
			dispatcher.utter_message("action_routine_register called!")

		return []

class ActionExerciseRecommendation(Action):

	def name(self) -> Text:
		return "action_exercise_recommendation"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		user_id = get_user_id(tracker)
		part = tracker.get_slot('part')
		t = db.get_exercise_recommendation(user_id, part)
		
		if t == None:
			m = f"미안 지금은 추천해 줄 운동이 없어 ㅠㅠ"
		
		elif part:
			if t[0] == 'absent':
				m = f"운동을 하지 않는 부위니까 내 추천은 {t[1]}!"
			elif t[0] == 'insufficient':
				m = f"운동이 부족한 부위니까 내 추천은 {t[1]}!"
			elif t[0] == 'enough':
				m = f"운동이 충분한 부위니까 다른 운동은 어때? 내 추천은 {t[2]} 빼고 {t[1]}!"
		else:
			if t[0] == 'absent':
				m = f"내 추천은 운동을 하지 않는 부위인 {t[1]}!"
			elif t[0] == 'insufficient':
				m = f"내 추천은 운동을 적게 하는 부위인 {t[1]}!"
			elif t[0] == 'enough':
				m = f"평소랑 다른 운동은 어때? {t[2]} 빼고 {t[1]}!"
		dispatcher.utter_message(m)
		
		if debug:
			dispatcher.utter_message("action_exercise_recommendation called!")

		if t:
			return [SlotSet('recommendation_exercise', t[1])]
		else:
			return[SlotSet("part", None)]

class ActionUpdateUserRoutine(Action):

	def name(self) -> Text:
		return "action_update_user_routine"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		if debug:
			dispatcher.utter_message("action_update_user_routine called!")

		return []

class ActionRecordDaily(Action):

	def name(self) -> Text:
		return "action_record_daily"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		user_id = get_user_id(tracker)
		db.increase_user_history_completion(user_id)
		db.increase_user_current_split_no(user_id)
		
		if debug:
			dispatcher.utter_message("action_record_daily called!")

		return []

class ActionRegisteration(Action):

	def name(self) -> Text:
		return "action_registration"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		user_id = get_user_id(tracker)
		previous_exp = tracker.get_slot('previous_exp')
		objective = tracker.get_slot('objective')
		property = tracker.get_slot('property')
		
		if previous_exp == 'low':
			level = 1
		elif previous_exp == 'middle':
			level = 2
		elif previous_exp == 'high':
			level = 3
		
		if objective == 'muscle':
			purpose = '근육증가'
		elif objective == 'lose_weight':
			purpose = '체중감량'
		elif objective == 'balanced':
			purpose = '균형'
		
		if property == 'a':
			preffered_split_cnt = 1
			criteria = '없음'
		elif property == 'b':
			preffered_split_cnt = 2
			criteria = '상체/하체'
		elif property == 'c':
			preffered_split_cnt = 2
			criteria = '부위별'
		elif property == 'd':
			preffered_split_cnt = 2
			criteria = '부위별'
		elif property == 'e':
			preffered_split_cnt = 3
			criteria = '부위별'
		elif property == 'f':
			preffered_split_cnt = 4
			criteria = '부위별'
		
		u = db.User(user_id, purpose, criteria, preffered_split_cnt, level, 1, 0)
		db.create_user_info(u)
		
		if debug:
			dispatcher.utter_message("action_registration called!")

		return []

class ActionProblemSearch(Action):

	def name(self) -> Text:
		return "action_problem_search"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		user_id = get_user_id(tracker)
		exercise_name = tracker.get_slot('exercise')
		problem_part = tracker.get_slot('problem_part')
		exercise = db.get_general_exercise(exercise_name)
		
		dispatcher.utter_message('아무래도 운동 자세가 잘못 된 것 같아.. 아래 설명과 동영상을 확인해줘!')
		dispatcher.utter_message(exercise.guide)
		dispatcher.utter_message(exercise.url)
		
		if debug:
			dispatcher.utter_message("action_problem_search called!")

		return [SlotSet("exercise", None),SlotSet("problem_part", None)]
	
    
class ActionChangeRoutine(Action):

	def name(self) -> Text:
		return "action_change_routine"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		user_id = get_user_id(tracker)
		exercise_name = tracker.get_slot('changing_exercise')
		number = tracker.get_slot('number')
		
		if number.endswith('회') or number.endswith('번'):
			number = int(number[:-1])
			db.execute_query(f'update user_routine set reps={number} where user_id={user_id} and exercise_name=\'{exercise_name}\'')
			m = f"{exercise_name}의 횟수가 {number}회로 변경되었어!"
		elif number.endswith('분'):
			number = int(number[:-1])
			db.execute_query(f'update user_routine set time={number} where user_id={user_id} and exercise_name=\'{exercise_name}\'')
			m = f"{exercise_name}의 시간이 {number}분으로 변경되었어!"
		elif number.endswith('세트'):
			number = int(number[:-2])
			db.execute_query(f'update user_routine set sets={number} where user_id={user_id} and exercise_name=\'{exercise_name}\'')
			m = f"{exercise_name}의 세트수가 {number}세트로 변경되었어!"
		
		dispatcher.utter_message(m)
		
		if debug:
			dispatcher.utter_message("action_change_routine called!")

		return [SlotSet("changing_exercise", None),SlotSet("number", None)]
    
    
class ActionExplainTerminology(Action):

	def name(self) -> Text:
		return "action_explain_terminology"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		user_id = get_user_id(tracker)
		terminology = tracker.get_slot('terminology')
		exercise = db.get_general_exercise(terminology)
		
		dispatcher.utter_message(f'{terminology}에 대한 설명과 동영상이야!')
		dispatcher.utter_message(exercise.guide)
		dispatcher.utter_message(exercise.url)
		
		if debug:
			dispatcher.utter_message("action_explain_terminology called!")

		return [SlotSet("terminology", None)]
    
class ProblemForm(FormAction):
	"""Example of a custom form action"""

	def name(self):
		# type: () -> Text
		"""Unique identifier of the form"""

		return "problem_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		"""A list of required slots that the form has to fill"""

		return ["exercise", "problem_part"]
    
	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        
		return{ "exercise" :[self.from_entity(entity = "exercise"), self.from_entity(entity = "changing_exercise"), self.from_entity(entity = "terminology")], 
                                     "problem_part" : [self.from_entity(entity = "problem_part"), self.from_entity(entity = "part")]}
	def validate_exercise(self,
							value: Text,
							dispatcher: CollectingDispatcher,
							tracker: Tracker,
							domain: Dict[Text, Any]) -> Optional[Text]:
		
		names = db.get_general_exercise_names()
		if value in names:
			return {"exercise": value}
		else:
			dispatcher.utter_template('utter_wrong_exercise', tracker)
			# validation failed, set slot to None
			return None
	
	def validate_part(self,
							value: Text,
							dispatcher: CollectingDispatcher,
							tracker: Tracker,
							domain: Dict[Text, Any]) -> Optional[Text]:
		
		part_types = db.get_part_types()
		if value in part_types:
			return {"problem_part": value}
		else:
			dispatcher.utter_template('utter_wrong_part', tracker)
			# validation failed, set slot to None
			return None
	def submit(self,
			   dispatcher: CollectingDispatcher,
			   tracker: Tracker,
			   domain: Dict[Text, Any]) -> List[Dict]:
		"""Define what the form has to do
			after all required slots are filled"""
		
		# utter submit template
		
		if debug:
			dispatcher.utter_message("problem_form submitted!")
		return [SlotSet("terminology", None), SlotSet("changing_exercise", None), SlotSet("part", None)]
    
    
class TerminologyForm(FormAction):
	"""Example of a custom form action"""

	def name(self):
		# type: () -> Text
		"""Unique identifier of the form"""

		return "terminology_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		"""A list of required slots that the form has to fill"""

		return ["terminology"]
	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
		return{"terminology" :[self.from_entity(entity = "exercise"), self.from_entity(entity = "changing_exercise"), self.from_entity(entity = "terminology")]}
	def validate_terminology(self,
							value: Text,
							dispatcher: CollectingDispatcher,
							tracker: Tracker,
							domain: Dict[Text, Any]) -> Optional[Text]:
		
		'''notimplemented'''
        
        
		return {"terminology": value}
	def submit(self,
			   dispatcher: CollectingDispatcher,
			   tracker: Tracker,
			   domain: Dict[Text, Any]) -> List[Dict]:
		"""Define what the form has to do
			after all required slots are filled"""
		
		# utter submit template
		
		if debug:
			dispatcher.utter_message("terminology_form submitted!")

		return [SlotSet("exercise", None), SlotSet("changing_exercise", None)]
    
    
    
    
class ChangeForm(FormAction):
	"""Example of a custom form action"""

	def name(self):
		# type: () -> Text
		"""Unique identifier of the form"""

		return "change_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		"""A list of required slots that the form has to fill"""

		return ["changing_exercise", "number"]
	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
		return{"changing_exercise" :[self.from_entity(entity = "changing_exercise"), self.from_entity(entity = "terminology"), self.from_entity(entity = "exercise")], 
               "number" : [self.from_entity(entity = "number")]}
	def validate_exercise(self,
							value: Text,
							dispatcher: CollectingDispatcher,
							tracker: Tracker,
							domain: Dict[Text, Any]) -> Optional[Text]:
		
		return {"changing_exercise": value}
	def validate_number(self,
							value: Text,
							dispatcher: CollectingDispatcher,
							tracker: Tracker,
							domain: Dict[Text, Any]) -> Optional[Text]:
		'''notimplemented'''
		return {"number": value}
	def submit(self,
			   dispatcher: CollectingDispatcher,
			   tracker: Tracker,
			   domain: Dict[Text, Any]) -> List[Dict]:
		"""Define what the form has to do
			after all required slots are filled"""
		
		# utter submit template
		
		if debug:
			dispatcher.utter_message("change_form submitted!")
            
		return [SlotSet("terminology", None)]