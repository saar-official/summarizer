from summary import Summary
from keywords import Keywords



class Main_model:
	def __init__(self):
		self.summary_model = Summary()
		self.keyword_model = Keywords()
		
	def return_response(self,text):
		summary = self.summary_model.summary(text)['summary']
		keywords = self.keyword_model.keywords(text)['keywords']
		return {"summary" : str(summary), "keywords":str(keywords)}
		
