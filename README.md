# WorkoutBuddy
WorkoutBuddy는 rasa와 MeCab을 이용하여 구현된 챗봇입니다.
아래 문서는 Windows, Anaconda Python 3.6.9를 기준으로 작성되었습니다.

## 로컬에서 WorkoutBuddy 실행하기
1. rasa[spacy]==1.3.9, pymysql 패키지 설치
```
pip install rasa[spacy]==1.3.9
pip install pymysql
```
2. rasa 실행 환경 구축
```
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
```
3. rasa 폴더에 chatbot/rasa_korean_material/registry.py 파일을 덮어씌우기
   * rasa 폴더 위치의 기본값 C:/Users/user/Anaconda3/envs/***env_name***/Lib/site-packages/rasa
4. rasa/nlu/tokenizers 폴더에 chatbot/rasa_korean_material/korean_tokenizer.py 파일을 복사하기
5. rasa/nlu/extractors 폴더에 chatbot/rasa_korean_material/crf_entity_extractor_korean.py 파일을 복사하기
6. MeCab 설치
7. MeCab의 사전 폴더에 chatbot/rasa_korean_material/dic 폴더의 내용을 덮어씌우기
8. chatbot 폴더에서 ```rasa shell``` 명령어 실행하기
9. actions 폴더에서 ```rasa run actions``` 명령어 실행하기

## Facebook에서 WorkoutBuddy 실행하기
* 1. 어쩌구

## WorkoutBuddy 수정하기
* 1. 어쩌구

## 유의사항
* 1. 어쩌구
