# WorkoutBuddy
WorkoutBuddy는 rasa와 MeCab을 이용하여 구현된 챗봇입니다.  
아래 문서는 Windows, Anaconda Python 3.6.9를 기준으로 작성되었습니다.

## Facebook에서 WorkoutBuddy 실행하기
1. facebook for developers에서 Messenger 앱 추가
	* https://developers.facebook.com/apps
2. 새로운 페이지 만들기 버튼을 눌러 챗봇이 적용될 페이지 생성
3. 페이지에 Messenger 버튼 추가
4. 생성한 facebook 앱에 새로 만든 페이지 추가
5. heroku에 chatbot을 위한 app 생성 (이하 ***chatbot_app***)
6. heroku에 actions를 위한 app 생성 (이하 ***actions_app***)
7. ***actions_app***에 ClearDB Add-on 추가
8. chatbot/endpoints.yml의 action_endpoint 수정
	* url: "https://***actions_app***.herokuapp.com/webhook"
9. chatbot/credentials.yml의 facebook 항목 수정
	* verify: ***verify_token*** (원하는 문자열)
	* secret: ***secret_code*** (설정 - 기본 설정 - 앱 시크릿 코드)
	* page-access-token: ***page_access_token*** (messenger - 토큰 생성)
10. actions/db.py의 pymysql.connect() 매개변수 수정
	* DB의 URL은 ***actions_app***의 설정 창에서 Reveal Config Vars 버튼을 눌러 확인 가능
	* URL의 형태: mysql://user:password@host/db?reconnect=true
11. Heroku 서버에 업로드
> heroku login  
>   
> chatbot 폴더 진입  
> git init  
> heroku git:remote ***chatbot_app***  
> git add .  
> git commit -am "***message***"  
> git push heroku master  
>   
> actions 폴더 진입  
> git init  
> heroku git:remote ***actions_app***  
> git add .
> git commit -am "***message***"  
> git push heroku master
12. facebook 앱에 콜백 URL 추가
	* URL: https://***chatbot_app***.herokuapp.com/webhooks/facebook/webhook
	* 확인 토큰: ***verify_token*** (credentials.yml에서 입력한 문자열)
13. 로컬에서 mypysql 패키지를 설치한 후 actions/init_db.py 실행
14. 생성했던 페이지에 추가했던 메시지 보내기 버튼을 눌러 챗봇과 대화

## 로컬에서 WorkoutBuddy 실행하기
1. rasa[spacy]==1.3.9, pymysql 패키지 설치
> pip install rasa[spacy]==1.3.9  
> pip install pymysql
2. rasa 실행 환경 구축
> python -m spacy download en_core_web_md  
> python -m spacy link en_core_web_md en
3. rasa 폴더에 chatbot/rasa_korean_material/registry.py 파일을 덮어씌우기
	* rasa 폴더 위치의 기본값: C:/Users/user/Anaconda3/envs/***env_name***/Lib/site-packages/rasa
4. rasa/nlu/tokenizers 폴더에 chatbot/rasa_korean_material/korean_tokenizer.py 파일을 복사하기
5. rasa/nlu/extractors 폴더에 chatbot/rasa_korean_material/crf_entity_extractor_korean.py 파일을 복사하기
6. MeCab 설치
7. MeCab의 사전 폴더에 chatbot/rasa_korean_material/dic 폴더의 내용을 덮어씌우기
8. actions/init_db.py 실행
9. chatbot/endpoints.yml의 action_endpoint 수정
	* url: "http://localhost:5055/webhook"
10. chatbot 폴더에서 ```rasa shell``` 명령어 실행하기
11. actions 폴더에서 ```rasa run actions``` 명령어 실행하기
	* Facebook에서 실행하기 과정 중 DB 설정이 되지 않았을 경우 정상적으로 작동하지 않음

## WorkoutBuddy 수정하기
1. 내용

## 유의사항
1. WorkoutBuddy 챗봇이 Facebook에서 정상 동작하지 않는 경우, ***chatbot_app***을 재시작 할 것
