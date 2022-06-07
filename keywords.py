import numpy as np
from rake_nltk import Rake
import pickle
import nltk 
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Keywords:
	def __init__(self,text):
		self.text = text

	def highlights(self):
		#keywords
            rake_nltk_var = Rake()
            rake_nltk_var.extract_keywords_from_text(self.text)
            keyword_extracted = rake_nltk_var.get_ranked_phrases()
            keywords1,keywords2,keywords3 = [],[],[]
            for words in keyword_extracted:
                if(len(words.split())==3):
                    keywords3.append(words)
                elif(len(words.split())==1 and len(words)>2):
                    keywords1.append(words)
                elif(len(words.split())==2):
                    keywords2.append(words)
            final_list = []
            for w in np.unique(keywords1)[0:6]:
                final_list.append(w)
            for w in np.unique(keywords2)[0:6]:
                final_list.append(w)
            for w in np.unique(keywords3)[0:6]:
                final_list.append(w)
            f1 = [[],[],[]]
            for word in final_list:
                NNS,VB,NN = False,False,False
                for w in nltk.pos_tag(word_tokenize(word)):
                    if(w[1]=='NN'):
                        NN = True
                    elif(w[1]=='NNS'):
                        NNS = True
                    elif(re.search('VB',w[1])):
                        VB = True
                if(NN and VB):
                    f1[2].append(word)
                elif(NN):
                    f1[0].append(word)
                else:
                    f1[2].append(word)
            return f1 