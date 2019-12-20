# WorkoutBuddy
WorkoutBuddy는 rasa와 MeCab을 이용하여 구현된 챗봇입니다.  
아래 문서는 Windows, Anaconda Python 3.6.9를 기준으로 작성되었습니다.  

## WorkoutBuddy 예제 실행
1. chatbot app을 활성화합니다.  
> https://rasachatbot1.herokuapp.com/  
> "Hello from Rasa: 1.3.9" 문구 확인  

2. actions app을 활성화합니다.  
> http://rasaactions1.herokuapp.com/
> "Not Found" 문구 확인  

3. 챗봇과 대화가 가능합니다.  
> m.me/105380957537337  

## Facebook에서 WorkoutBuddy 실행

### 1. 새로운 Facebook app 추가
1.1. Facebook for developers에서 Messenger 앱을 추가합니다.  
> https://developers.facebook.com/apps  

1.2. 새로운 페이지 만들기 버튼을 눌러 챗봇이 적용될 페이지를 생성합니다.  
1.3. 페이지에 Messenger 버튼을 추가합니다.  
1.4. 생성한 Facebook 앱에 새로 만든 페이지를 추가합니다.  

### 2. Heroku에  app 업로드
2.1. Heroku에 chatbot을 위한 app을 생성합니다. (이하 ***chatbot_app***)  
> https://www.heroku.com  

2.2. Heroku에 actions를 위한 app을 생성합니다. (이하 ***actions_app***)  
2.3. ***actions_app***에 ClearDB Add-on을 추가합니다.  
2.4. chatbot/endpoints.yml의 action_endpoint를 수정합니다.  
> url: "https://***actions_app***.herokuapp.com/webhook"  

2.5. chatbot/credentials.yml의 facebook 항목을 수정합니다.  
> verify: ***verify_token*** (원하는 문자열)  
> secret: ***secret_code*** (설정 - 기본 설정 - 앱 시크릿 코드)  
> page-access-token: ***page_access_token*** (messenger - 토큰 생성)  

2.6. actions/db.py의 pymysql.connect() 매개변수를 수정합니다.  
> DB의 URL은 ***actions_app***의 설정 창에서 Reveal Config Vars 버튼을 눌러 확인 가능  
> URL의 형태: mysql://user:password@host/db?reconnect=true  

2.7. Heroku 서버에 업로드합니다.  
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

### 3. Facebook app과 Heroku에 업로드한 app 연동
3.1. facebook 앱에 콜백 URL을 추가합니다.  
> URL: https://***chatbot_app***.herokuapp.com/webhooks/facebook/webhook  
> 확인 토큰: ***verify_token*** (credentials.yml에서 입력한 문자열)  

3.2. 로컬에서 mypysql 패키지를 설치한 후 actions/init_db.py를 실행합니다.  
3.3. 생성했던 페이지에 추가했던 메시지 보내기 버튼을 눌러 챗봇과 대화가 가능합니다.  

## 로컬에서 WorkoutBuddy 실행

### 1. 기본 환경 구축
1.1. rasa[spacy]==1.3.9, pymysql 패키지를 설치합니다.  
> pip install rasa[spacy]==1.3.9  
> pip install pymysql  

1.2. rasa 실행 환경을 구축합니다.  
> python -m spacy download en_core_web_md  
> python -m spacy link en_core_web_md en  

### 2. RASA pipeline 한글화
2.1. rasa 폴더에 chatbot/rasa_korean_material/registry.py 파일을 덮어씁니다.  
> rasa 폴더 위치의 기본값: C:/Users/user/Anaconda3/envs/***env_name***/Lib/site-packages/rasa  

2.2. rasa/nlu/tokenizers 폴더에 chatbot/rasa_korean_material/korean_tokenizer.py 파일을 복사합니다.  
2.3. rasa/nlu/extractors 폴더에 chatbot/rasa_korean_material/crf_entity_extractor_korean.py 파일을 복사합니다.  
2.4. mecab-ko(또는 MeCab)를 설치합니다.  
2.5. MeCab의 사전 폴더에 chatbot/rasa_korean_material/dic 폴더의 내용을 덮어씁니다.  

### 3. 실행
3.1. actions/init_db.py를 실행합니다.  
3.2. chatbot/endpoints.yml의 action_endpoint를 수정합니다.  
> url: "http\://localhost:5055/webhook"  

3.3. chatbot 폴더에서 ```rasa shell``` 명령어를 실행합니다.  
3.4. actions 폴더에서 ```rasa run actions``` 명령어를 실행합니다.  
> Facebook에서 실행하기 과정 중 DB 설정이 되지 않았을 경우 정상적으로 작동하지 않습니다.  

## RASA pipeline 한글화

### KoreanTokenizer
문장을 일정 단위로 분해해 주는 pipeline입니다.  
한글에 적용하기 위해 형태소 분석기인 mecab을 사용하였습니다.  
그러므로 실행 환경에 mecab이 설치가 되어 있어야 합니다.  
설치시 현재 환경의 파이썬 버전을 잘 확인해야 합니다.  

### CRFEntityExtractorKorean
Tokenizer에서 parsing한 정보와 원래 문장에서의 entity위치 정보를 토대로 entity를 추출하는 pipeline입니다.  
기존 Extractor에서는 단순히 string에 대해 index함수를 직접 적용하여 원래 문장에서 entity 위치를 검색하는 방식이었지만, 한글의 경우 형태소로 추출하게 되면 원래 문장과 모양이 변하게 되는 경우가 빈번하여 string에 직접 index 함수를 적용할 수 없습니다.  
그래서 기존 CRFEntityExtractor 코드를 한글에 맞도록 약간 변경하였습니다.  

## pipeline 관련 주의사항

### 1. 외래어 오류
현재 tokenizer에서는 외래어를 한글로 그대로 사용하는 경우에는 mecab이 tokenize를 잘못 하는 경우가 많아 오류가 발생하기 쉽습니다.  
그러므로 최대한 외래어를 entity로 사용하지 않는 방향으로 사용해야 하며 꼭 사용해야 할 때는 entity에 대한 용어들을 mecab 사전에 꼭 추가해 주셔야 합니다.  
그러나 사전에 추가를 하더라도 오류가 발생하는 문장들이 있습니다.  
> 거침없이 \[로우 킥\](entity)  

위 문장을 mecab을 이용할 시 "로우 킥" 은 무조건 "롭ㄴ 킥"으로 바뀝니다.  
(자비롭다 or 자비로운 에 사용하는 로우로 해석)  
이 경우 '로우'를 mecab 사전에 추가하여도 발생하는 문제이므로 최대한 이런 문장을 만들지 말아야 합니다.  

### 2. entity 빈칸 오류
entity 양식의 맨 끝에 빈 칸을 넣을 경우에도 오류가 발생합니다.  
> - 지붕뚫고 \[하이 킥 \](entity) : 오류 발생  
> - 지붕뚫고 \[하이 킥\](entity) : 정상 작동  


### 3. 품사 태깅 미활용
현재 KoreanTokenizer는 품사 태깅을 활용하지 않고 있습니다.  
그래서 다음 두 문장을 비슷한 문장으로 인식하지 않습니다.  
> \[홍길동\](entity)이 만든 토크나이저  
> \[철수\](entity)가 만든 토크나이저  

이는 '이'와 '가'를 다른 요소로 학습하기 때문입니다.  
따라서 현재에서 "은 는 이 가 을 를" 등 entity의 종성에 따라 문장 요소가 달라지는 경우, nlu 성능을 높이기 위해서는 각 경우에 대해 전부 학습 데이터를 만들어 주어야 합니다.  
