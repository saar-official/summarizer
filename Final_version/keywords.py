from rake_spacy import Rake
import re
import spacy
import string


class Keywords:
	def __init__(self):
		self.nlp = spacy.load("en_core_web_sm")
		self.rake = Rake()
		self.st_words = list(self.nlp.Defaults.stop_words)
	
	def preprocess(self,text):
		s = ""
		punct = list(string.punctuation)
		for letters in text:
			if(letters in punct or letters == " " or letters.isalnum()):
				s = s+ letters
		doc = self.nlp(s)
		sent = " ".join([word.text for word in doc if word.text not in self.st_words])
		return sent
	
	def keywords(self,text):
		text = self.preprocess(text)
		ranklist = self.rake.apply(text)
		ranklist.sort(key = lambda x : x[0])
		length = min(5,len(ranklist))
		return {"keywords": [i[1] for i in ranklist][0:length]}

