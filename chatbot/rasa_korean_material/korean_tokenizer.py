#import re
from typing import Any, List, Text

from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.tokenizers import Token, Tokenizer
from rasa.nlu.training_data import Message, TrainingData
import MeCab

class KoreanTokenizer(Tokenizer, Component):

    #name = "tokenizer_korean"
    provides = ["tokens"]
    #defaults =  {}
    #language_list = ["kr"]

    def train(
        self, training_data: TrainingData, config: RasaNLUModelConfig, **kwargs: Any
    ) -> None:

        for example in training_data.training_examples:
            example.set("tokens", self.tokenize(example.text))

    def process(self, message: Message, **kwargs: Any) -> None:

        message.set("tokens", self.tokenize(message.text))

    @staticmethod
    def tokenize(text: Text) -> List[Token]:

        def mecabsplit(mecab_tagger,inputs, pos):
            r=[]
            inputs = mecab_tagger.parse(inputs)
            t = inputs.split('\n')[:-2]
            for i in t:
                field = i.split('\t')
                if field[1].split(',')[-1] is not '*':
                    r.extend( [ (x.split('/')[0],x.split('/')[1]) for x in field[1].split(',')[-1].split('+') ] )
                else:
                    r.append( (field[0],field[1].split(',')[0]) )
            if pos:
                return r
            else:
                return [ x[0] for x in r ]
            return r
        
        mecab_tagger = MeCab.Tagger()
        
        a = mecab_tagger.parse(text)
        t = a.split('\n')[:-2]
        tokenpointer = []
        pointeroffset = 0

        for i in t:
            field = i.split('\t')
            if field[1].split(',')[-1] is not '*':
                currentptr = text.index(field[0], pointeroffset)
                for x in field[1].split(',')[-1].split('+'):
                    try:
                        w = x.split('/')[0]
                        temp = field[0].index(w)
                        tokenpointer.append((currentptr + temp, currentptr + temp +len(w)))
                    except:
                        tokenpointer.append((currentptr, currentptr + len(field[0])))
                pointeroffset = currentptr + len(field[0])
            else:
                currentptr = text.index(field[0], pointeroffset)
                tokenpointer.append( (currentptr, currentptr + len(field[0])) )
                pointeroffset = currentptr + len(field[0])
        words = mecabsplit(mecab_tagger, text, False)
        tokens = []
        offset = 0
        for word in words:
            word_offset = tokenpointer[words.index(word, offset)][0]
            tokens.append(Token(word, word_offset))
            offset +=1
        
        return tokens