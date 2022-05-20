from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
from keywords import Keywords
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class keywords:
        def __init__(self,text,keyword_array=None):
            self.text = text
            self.keyword_array = []
            self.model = TFAutoModelForSeq2SeqLM.from_pretrained('t5-base')
            self.tokenizer = AutoTokenizer.from_pretrained('t5-base')
        def preprocess(self):
            st_words = stopwords.words('english')
            TEXT = " ".join([word for word in word_tokenize(self.text) if word not in st_words])
            ls = [];s = ""
            for i in TEXT:
                if(i=='‘'):
                    s = ''
                elif(i=='’'):
                    self.keyword_array.append(s.strip())
                else:
                    s = s+i
            return TEXT     
        def keywords_extract(self):
            inputs = self.tokenizer("summarize: " + self.text, return_tensors="tf", max_length=512)
            outputs = self.model.generate(inputs["input_ids"], max_length=150, min_length=80, length_penalty=2.0, num_beams=4, early_stopping=True)
            summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            TEXT = self.preprocess()
            keyword = Keywords(TEXT)
            return {"highlights":keyword.highlights(),"summary":summary}
