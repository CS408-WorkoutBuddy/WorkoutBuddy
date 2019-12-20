import os

os.system('cp -rf rasa_korean_material/dic/ .heroku/python/lib/python3.6/site-packages/MeCab/')
os.system('cp -f rasa_korean_material/korean_tokenizer.py .heroku/python/lib/python3.6/site-packages/rasa/nlu/tokenizers/')
os.system('cp -f rasa_korean_material/crf_entity_extractor_korean.py .heroku/python/lib/python3.6/site-packages/rasa/nlu/extractors/')
os.system('cp -f rasa_korean_material/registry.py .heroku/python/lib/python3.6/site-packages/rasa/nlu/')

import MeCab
tagger = MeCab.Tagger()
s = 'MeCab의 설치 및 한글화를 확인합니다.'
print(s)
print(tagger.parse(s))

os.system('rasa run -p $PORT')