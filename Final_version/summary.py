from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
import spacy


class Summary:
        def __init__(self):
            self.model = TFAutoModelForSeq2SeqLM.from_pretrained('./model_file',local_files_only=True)
            self.tokenizer = AutoTokenizer.from_pretrained('./model_file',local_files_only=True)
        
        def summary(self,text):
        	inputs = self.tokenizer("summarize: " + text, return_tensors="tf", max_length=512)
        	outputs = self.model.generate(inputs["input_ids"], max_length=150,min_length=80, length_penalty=2.0, num_beams=4, early_stopping=True)
        	summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        	return {"summary":summary}
