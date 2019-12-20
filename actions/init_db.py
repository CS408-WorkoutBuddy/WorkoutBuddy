import db

part_list = ['상체', '하체', '심장', '전신', '복근 및 코어', '유연성']
problem_part_list = ['무릎', '어깨', '손목', '발목', '허리', '고관절', '골반']
purpose_list = ['체중감량', '근육증가', '균형']
criteria_list = ['없음', '상체/하체', '부위별']

general_exercise_list = [db.Exercise('180도 점프 스쿼트', '(설명)', '(url)', 3, '하체', None, None, 20, 3),
						 db.Exercise('180도 점프', '(설명)', '(url)', 2, '심장', None, None, 20, 3),
						 db.Exercise('4카운트 버피', '(설명)', '(url)', 1, '전신', None, None, 20, 3),
						 db.Exercise('6카운트 버피', '(설명)', '(url)', 3, '전신', None, None, 20, 3),
						 db.Exercise('엘리게이터 푸시업', '(설명)', '(url)', 3, '상체', None, None, 20, 3),
						 db.Exercise('팔 뒤로 돌리기', '(설명)', '(url)', 1, '상체', None, None, 20, 3),
						 db.Exercise('팔 앞으로 돌리기', '(설명)', '(url)', 1, '상체', None, None, 20, 3),
						 db.Exercise('후방 런지', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('딱정벌레 자세', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('벤트 레그 크로스 오버', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 
						 db.Exercise('바이시클 크런치', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('브릿지', '(설명)', '(url)', 1, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('버트 키커 점프 스쿼트', '(설명)', '(url)', 3, '하체', None, None, 20, 3),
						 db.Exercise('카프레이즈', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('고양이 자세', '(설명)', '(url)', 1, '유연성', None, None, 20, 3),
						 db.Exercise('아기 자세', '(설명)', '(url)', 1, '유연성', None, None, 20, 3),
						 db.Exercise('팔 내밀어 뛰기', '(설명)', '(url)', 1, '심장', None, None, 20, 3),
						 db.Exercise('코블러 스트레칭', '(설명)', '(url)', 1, '유연성', None, None, 20, 3),
						 db.Exercise('커맨더 푸시업', '(설명)', '(url)', 2, '상체', None, None, 20, 3),
						 db.Exercise('테이블탑 브릿지', '(설명)', '(url)', 1, '하체', None, 1, None, 2),
						 
						 db.Exercise('교차 펀치', '(설명)', '(url)', 1, '심장', None, None, 20, 3),
						 db.Exercise('크런치', '(설명)', '(url)', 1, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('컬시 런지', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('디클라인 푸시업', '(설명)', '(url)', 3, '상체', None, None, 20, 3),
						 db.Exercise('덩키 킥', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('종아리 스트레', '(설명)', '(url)', 1, '유연성', None, None, 20, 3),
						 db.Exercise('소화전 운동', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('전속력 턱 점프 버피', '(설명)', '(url)', 3, '전신', None, None, 20, 3),
						 db.Exercise('전속력 버피', '(설명)', '(url)', 2, '전신', None, None, 20, 3),
						 db.Exercise('앞 점프 스쿼트', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 
						 db.Exercise('전방 런지', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('개구리 스쿼트', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('하이 니', '(설명)', '(url)', 1, '심장', None, None, 20, 3),
						 db.Exercise('하이 플랭크', '(설명)', '(url)', 1, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('하이 플랭크 더블 니', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('하이 플랭크 잭', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('하이 플랭크 점핑 잭', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('하이 플랭크 점프', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('하이 플랭크 니 크로스', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('하이 플랭크 니 드롭', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 
						 db.Exercise('하이 플랭크 니 투 엘보', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('하이 플랭크 레그 리프트', '(설명)', '(url)', 1, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('하이 플랭크 림 레이즈', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('하이 사이드 플랭크', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('힙 어브덕션', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('힙 어덕션', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('힙 오프너', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('인치웜 턱 점프', '(설명)', '(url)', 3, '심장', None, None, 20, 3),
						 db.Exercise('인치웜', '(설명)', '(url)', 1, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('인클라인 푸시업', '(설명)', '(url)', 1, '상체', None, None, 20, 3),
						 
						 db.Exercise('인워드 카프레이즈', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('제자리 뛰기', '(설명)', '(url)', 1, '심장', None, None, 20, 3),
						 db.Exercise('점프 런지', '(설명)', '(url)', 3, '하체', None, None, 20, 3),
						 db.Exercise('점프 스쿼트', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('팔 벌려 뛰기', '(설명)', '(url)', 1, '심장', None, None, 20, 3),
						 db.Exercise('니 커맨드 푸시업', '(설명)', '(url)', 2, '상체', None, None, 20, 3),
						 db.Exercise('니 내로우 투 와이드 푸시업', '(설명)', '(url)', 2, '상체', None, None, 20, 3),
						 db.Exercise('니 플라이오 푸시업', '(설명)', '(url)', 2, '상체', None, None, 20, 3),
						 db.Exercise('니 푸시업 숄더 탭', '(설명)', '(url)', 2, '상체', None, None, 20, 3),
						 db.Exercise('니 푸시업 사이드 플랭크', '(설명)', '(url)', 2, '상체', None, None, 20, 3),
						 
						 db.Exercise('니 푸시업', '(설명)', '(url)', 1, '상체', None, None, 20, 3),
						 db.Exercise('니 사이드 투 사이드 푸시업', '(설명)', '(url)', 2, '상체', None, None, 20, 3),
						 db.Exercise('니 스태거드 푸시업', '(설명)', '(url)', 2, '상체', None, None, 20, 3),
						 db.Exercise('니 턱 크런치', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('니 업 다운 푸시업', '(설명)', '(url)', 2, '상체', None, None, 20, 3),
						 db.Exercise('니 업 다운', '(설명)', '(url)', 1, '상체', None, None, 20, 3),
						 db.Exercise('닐 앤 스탠드', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('엉덩이 굴근 스트레칭', '(설명)', '(url)', 1, '유연성', None, None, 20, 3),
						 db.Exercise('래터럴 점프 터치다운', '(설명)', '(url)', 3, '심장', None, None, 20, 3),
						 db.Exercise('래터럴 점프', '(설명)', '(url)', 2, '심장', None, None, 20, 3),
						 
						 db.Exercise('레그 레이즈', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('림 레이즈 푸시업', '(설명)', '(url)', 3, '상체', None, None, 20, 3),
						 db.Exercise('로우 플랭크', '(설명)', '(url)', 1, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('로우 플랭크 암 리치', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('로우 플랭크 크런치', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('로우 플랭크 더블 니', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('로우 플랭크 니 크로스', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('로우 플랭크 니 드롭', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('로우 플랭크 니 투 엘보', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('로우 플랭크 트위스트', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 
						 db.Exercise('로우 사이드 플랭크', '(설명)', '(url)', 1, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('로우 사이드 플랭크 레그 리프트', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('로우 사이드 플랭크 트위스트', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('런지 앤 트위스트', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('런지 하이 니 점프', '(설명)', '(url)', 3, '하체', None, None, 20, 3),
						 db.Exercise('런지 투 프론트 킥', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('런지 투 하이 니', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('4자 스트레칭', '(설명)', '(url)', 1, '유연성', None, None, 20, 3),
						 db.Exercise('마칭 월 싯', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('마운틴 클라이머', '(설명)', '(url)', 1, '심장', None, 1, None, 2),
						 
						 db.Exercise('내로우 6카운트 버피', '(설명)', '(url)', 3, '전신', None, None, 20, 3),
						 db.Exercise('내로우 니 푸시업', '(설명)', '(url)', 1, '상체', None, None, 20, 3),
						 db.Exercise('내로우 푸시업', '(설명)', '(url)', 1, '상체', None, None, 20, 3),
						 db.Exercise('내로우 스쿼트', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('내로우 투 와이드 푸시업', '(설명)', '(url)', 3, '상체', None, None, 20, 3),
						 db.Exercise('한발 4카운트 버피', '(설명)', '(url)', 2, '전신', None, None, 20, 3),
						 db.Exercise('한발 6카운트 버피', '(설명)', '(url)', 3, '전신', None, None, 20, 3),
						 db.Exercise('아웃워드 카프레이즈', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('오버헤드 스쿼트', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('오버헤드 트라이셉 스트레칭', '(설명)', '(url)', 1, '유연성', None, None, 20, 3),
						 
						 db.Exercise('펜듈럼 런지', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('파이크 푸시업', '(설명)', '(url)', 2, '상체', None, None, 20, 3),
						 db.Exercise('피스톨 스쿼트', '(설명)', '(url)', 3, '하체', None, None, 20, 3),
						 db.Exercise('피봇 런지', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('플랭크 투 다운 독', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('필레 점프 스쿼트', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('필레 스쿼트', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('플라이오 푸시업', '(설명)', '(url)', 3, '상체', None, None, 20, 3),
						 db.Exercise('프리즈너 스쿼트', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('엑스자 엎드리기', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 
						 db.Exercise('펄싱 스쿼트', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('펀치', '(설명)', '(url)', 1, '심장', None, None, 20, 3),
						 db.Exercise('푸시업 잭', '(설명)', '(url)', 3, '상체', None, None, 20, 3),
						 db.Exercise('푸시업 숄더탭', '(설명)', '(url)', 2, '상체', None, None, 20, 3),
						 db.Exercise('푸시업 사이드 플랭크', '(설명)', '(url)', 2, '상체', None, None, 20, 3),
						 db.Exercise('푸시업', '1. 어깨너비의 1.5배만큼 손을 벌리기\n2. 내려갈 땐 가슴이 양 손 사이에 오도록\n3. 엉덩이가 들리지 않도록 주의\n4. 머리부터 발까지 일직선 유지', 'https://youtu.be/aoH7qNedO8k', 1, '상체', None, None, 20, 3),
						 db.Exercise('네발 니 투 엘보', '(설명)', '(url)', 2, '전신', None, None, 20, 3),
						 db.Exercise('네발 림 레이즈', '(설명)', '(url)', 1, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('퀵 피트', '(설명)', '(url)', 1, '심장', None, None, 20, 3),
						 db.Exercise('리버스 크런치', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 
						 db.Exercise('리버스 플랭크', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('록스타', '(설명)', '(url)', 1, '심장', None, None, 20, 3),
						 db.Exercise('러시안 트위스트 1', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('러시안 트위스트 2', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('한발 균형잡기', '(설명)', '(url)', 1, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('한발 테이블탑 브릿지', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('한발 앞뒤 뛰기', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('한발 점프 스쿼트', '(설명)', '(url)', 3, '하체', None, None, 20, 3),
						 db.Exercise('한발 발 닿기', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('한발 정강이 닿기', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 
						 db.Exercise('한발 스쿼트', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('시저스 킥', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('어깨 스트레칭', '(설명)', '(url)', 1, '유연성', None, None, 20, 3),
						 db.Exercise('사이드 런지 터치다운', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('사이드 런지', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('사이드 플랭크 오블리크 크런치', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('사이드 스타 플랭크', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('사이드 투 사이드 푸시업', '(설명)', '(url)', 2, '상체', None, None, 20, 3),
						 db.Exercise('한발 브릿지', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('한발 데드리프트', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 
						 db.Exercise('한발 파이크 푸시업', '(설명)', '(url)', 3, '상체', None, None, 20, 3),
						 db.Exercise('한발 푸시업', '(설명)', '(url)', 3, '상체', None, None, 20, 3),
						 db.Exercise('한발 브이업', '(설명)', '(url)', 2, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('싯업', '(설명)', '(url)', 1, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('스키 복근 운동', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('스키 점프', '(설명)', '(url)', 2, '심장', None, None, 20, 3),
						 db.Exercise('스피드 스케이팅', '(설명)', '(url)', 2, '심장', None, None, 20, 3),
						 db.Exercise('스쿼트 잭', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('스쿼트 사이드 킥', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('스쿼트 스타', '(설명)', '(url)', 3, '심장', None, None, 20, 3),
						 
						 db.Exercise('스쿼트 투 하이 니', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('스쿼트 투 하이 니 점프', '(설명)', '(url)', 2, '하체', None, None, 20, 3),
						 db.Exercise('스쿼트', '1. 양 발을 어깨너비로 벌리기\n2. 발 끝을 약간 바깥으로 벌리기\n3. 앞뒤로 쏠리지 않도록 체중 분산하기\n4. 복부에 힘주고 허리가 구부러지지 않게 가슴을 펴기', 'https://youtu.be/Fk9j6pQ6ej8', 1, '하체', None, None, 20, 3),
						 db.Exercise('스쿼팅 퀵 피트', '(설명)', '(url)', 2, '심장', None, None, 20, 3),
						 db.Exercise('스태거드 푸시업', '(설명)', '(url)', 2, '상체', None, None, 20, 3),
						 db.Exercise('스탠딩 쿼드리셉스 스트레칭', '(설명)', '(url)', 1, '유연성', None, 1, None, 2),
						 db.Exercise('팔 벌려 점프 뛰기', '(설명)', '(url)', 2, '심장', None, None, 20, 3),
						 db.Exercise('스타 토 터치', '(설명)', '(url)', 1, '유연성', None, None, 20, 3),
						 db.Exercise('스트레이트 레그 바이시클 크런치', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('슈퍼맨 자세', '(설명)', '(url)', 1, '복근 및 코어', None, None, 20, 3),
						 
						 db.Exercise('테이블탑 크런치', '(설명)', '(url)', 1, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('터치다운 런지', '(설명)', '(url)', 1, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('트라이셉 딥', '(설명)', '(url)', 1, '상체', None, None, 20, 3),
						 db.Exercise('턱 점프', '(설명)', '(url)', 3, '심장', None, None, 20, 3),
						 db.Exercise('타입라이터 푸시업', '(설명)', '(url)', 3, '상체', None, None, 20, 3),
						 db.Exercise('얼티밋 버피', '(설명)', '(url)', 3, '전신', None, None, 20, 3),
						 db.Exercise('업 다운 푸시업', '(설명)', '(url)', 2, '상체', None, None, 20, 3),
						 db.Exercise('업 다운', '(설명)', '(url)', 3, '상체', None, None, 20, 3),
						 db.Exercise('브이업', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('워킹 하이 니', '(설명)', '(url)', 1, '심장', None, None, 20, 3),
						 
						 db.Exercise('워킹 런지', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('월 브릿지', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('월 클라임', '(설명)', '(url)', 3, '전신', None, None, 20, 3),
						 db.Exercise('월 핸드스탠드 킥 업', '(설명)', '(url)', 2, '전신', None, None, 20, 3),
						 db.Exercise('월 래터럴 풀 다운', '(설명)', '(url)', 1, '상체', None, None, 20, 3),
						 db.Exercise('벽 짚고 가슴 스트레칭', '(설명)', '(url)', 1, '유연성', None, None, 20, 3),
						 db.Exercise('벽 밀쳐내기', '(설명)', '(url)', 1, '상체', None, None, 20, 3),
						 db.Exercise('월 싯', '(설명)', '(url)', 1, '하체', None, None, 20, 3),
						 db.Exercise('와이드 클라이머 점프', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('와이드 클라이머 트위스트', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3),
						 
						 db.Exercise('와이드 하이 니', '(설명)', '(url)', 1, '심장', None, None, 20, 3),
						 db.Exercise('와이드 니 푸시업', '(설명)', '(url)', 1, '상체', None, None, 20, 3),
						 db.Exercise('와이드 브이업', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3),
						 db.Exercise('와이드 푸시업', '(설명)', '(url)', 1, '상체', None, None, 20, 3),
						 db.Exercise('윈드쉴드 와이퍼', '(설명)', '(url)', 3, '복근 및 코어', None, None, 20, 3)]

"""
general_exercise_list = [db.Exercise('러닝', '(설명)', '(url)', 1, '유산소', None, None, 600, None, None, None),
					     db.Exercise('벤치프레스', '(설명)', '(url)', 3, '가슴', 20, None, None, 8, 5),
						 db.Exercise('인클라인 벤치프레스', '(설명)', '(url)', 3, '가슴', 20, None, None, 8, 5),
						 db.Exercise('랫풀다운', '(설명)', '(url)', 3, '등', 10, None, None, 10, 5),
						 db.Exercise('원암덤벨로우', '(설명)',+ '(url)', 3, '등', 3, None, None, 10, 4),
						 
						 db.Exercise('숄더프레스', '(설명)', '(url)', 3, '어깨', 5, None, None, 10, 5),
						 db.Exercise('레터럴레이즈', '(설명)', '(url)', 3, '어깨', 2, None, None, 25, 5),
						 db.Exercise('레그 익스텐션', '(설명)', '(url)', 3, '하체', 5, None, None, 10, 5),
						 db.Exercise('레그 컬', '(설명)', '(url)', 3, '하체', 5, None, None, 10, 5),
						 db.Exercise('스쿼트', '(설명)', '(url)', 1, '하체', None, None, None, None, 5, 5),
						 
						 db.Exercise('런지', '(설명)', '(url)', 1, '하체', None, None, None, None, 15, 5),
						 db.Exercise('덤벨컬', '(설명)', '(url)', 3, '팔', 2, None, None, 15, 3),
						 db.Exercise('케이블푸시다운', '(설명)', '(url)', 3, '팔', 5, None, None, 12, 3),
						 db.Exercise('크런치', '(설명)', '(url)', 1, '복근', None, None, None, None, 50, 2),
						 db.Exercise('레그레이즈', '(설명)', '(url)', 1, '복근', None, None, None, None, 40, 2)]
"""

sample_routine_list = [db.Routine(None, '없음', 1, [[general_exercise_list[152], general_exercise_list[2], general_exercise_list[143]]]),
					   db.Routine(None, '상체/하체', 2, [[general_exercise_list[152], general_exercise_list[7], general_exercise_list[19], general_exercise_list[53]], [general_exercise_list[33], general_exercise_list[70], general_exercise_list[115], general_exercise_list[162]]]),
					   db.Routine(None, '부위별', 3, [[general_exercise_list[33], general_exercise_list[70], general_exercise_list[115], general_exercise_list[162]], [general_exercise_list[152], general_exercise_list[7], general_exercise_list[19], general_exercise_list[53]], [general_exercise_list[89], general_exercise_list[2], general_exercise_list[48], general_exercise_list[54]]])]

"""
sample_routine_list = [db.Routine(None, None, 'none', 1, [[general_exercise_list[0], general_exercise_list[1], general_exercise_list[8], general_exercise_list[13]]]),
					   db.Routine(None, None, 'upper and lower', 2, [[general_exercise_list[0], general_exercise_list[1], general_exercise_list[6], general_exercise_list[13]], [general_exercise_list[0], general_exercise_list[7], general_exercise_list[11], general_exercise_list[14]]]),
					   db.Routine(None, None, 'torso and limb', 2, [[general_exercise_list[0], general_exercise_list[3], general_exercise_list[1], general_exercise_list[13]], [general_exercise_list[0], general_exercise_list[8], general_exercise_list[5], general_exercise_list[14]]]),
					   db.Routine(None, None, 'pull and push', 2, [[general_exercise_list[0], general_exercise_list[2], general_exercise_list[8], general_exercise_list[13]], [general_exercise_list[0], general_exercise_list[1], general_exercise_list[7], general_exercise_list[14]]]),
					   db.Routine(None, None, 'torso and limb', 3, [[general_exercise_list[0], general_exercise_list[1], general_exercise_list[2], general_exercise_list[13]], [general_exercise_list[0], general_exercise_list[3], general_exercise_list[4], general_exercise_list[14]], [general_exercise_list[0], general_exercise_list[6], general_exercise_list[8], general_exercise_list[13]]]),
					   db.Routine(None, None, 'part by part', 4, [[general_exercise_list[0], general_exercise_list[1], general_exercise_list[2], general_exercise_list[13]], [general_exercise_list[0], general_exercise_list[3], general_exercise_list[4], general_exercise_list[14]], [general_exercise_list[0], general_exercise_list[5], general_exercise_list[11], general_exercise_list[13]], [general_exercise_list[0], general_exercise_list[7], general_exercise_list[8], general_exercise_list[14]]])]
"""

user_list = []
user_routine_list = []
history_list = []


db.execute_query('drop table user_history')
db.execute_query('drop table user_routine')
db.execute_query('drop table user_info')
db.execute_query('drop table sample_routine')
db.execute_query('drop table sample_info')
db.execute_query('drop table general_exercise')
db.execute_query('drop table criteria_type')
db.execute_query('drop table purpose_type')
db.execute_query('drop table problem_part_type')
db.execute_query('drop table part_type')

db.execute_query('create table part_type (part varchar(10) primary key)')
db.execute_query('create table problem_part_type (problem_part varchar(10) primary key)')
db.execute_query('create table purpose_type (purpose varchar(20) primary key)')
db.execute_query('create table criteria_type (criteria varchar(20) primary key)')
db.execute_query('create table general_exercise (name varchar(50) primary key, guide varchar(100), url varchar(50), difficulty int not null, part varchar(10) not null, weight int, time int, reps int, sets int, foreign key (part) references part_type (part))')
db.execute_query('create table sample_info (id int auto_increment primary key, criteria varchar(20) not null, split_cnt int not null, foreign key (criteria) references criteria_type (criteria))')
db.execute_query('create table sample_routine (sample_id int, split_no int, position int, exercise_name varchar(20) not null, weight int, time int, reps int, sets int, foreign key (sample_id) references sample_info (id), foreign key (exercise_name) references general_exercise (name), primary key (sample_id, split_no, position))')
db.execute_query('create table user_info (id bigint primary key, purpose varchar(20) not null, criteria varchar(20) not null, preffered_split_cnt int not null, level int not null, split_cnt int not null, current_split_no int not null, foreign key (purpose) references purpose_type (purpose), foreign key (criteria) references criteria_type (criteria))')
db.execute_query('create table user_routine (user_id bigint, split_no int, position int, exercise_name varchar(20) not null, weight int, time int, reps int, sets int, foreign key (user_id) references user_info (id), foreign key (exercise_name) references general_exercise (name), primary key (user_id, split_no, position))')
db.execute_query('create table user_history (user_id bigint, exercise_name varchar(20), completion int not null, rejection int not null, foreign key (user_id) references user_info (id), foreign key (exercise_name) references general_exercise (name), primary key (user_id, exercise_name))')

db.create_part_type(part_list)
db.create_problem_part_type(problem_part_list)
db.create_purpose_type(purpose_list)
db.create_criteria_type(criteria_list)
db.create_general_exercise(general_exercise_list)
db.create_sample_routine(sample_routine_list)
for user in user_list:
	db.create_user_info(user)
for routine in user_routine_list:
	db.create_user_routine(routine)
for history in history_list:
	db.create_user_history(history)
