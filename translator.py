# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:11:42 2019

"""
from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger
import pandas as pd
from tkinter import messagebox
import tkinter as tk
from tkinter import simpledialog

#from sklearn import tree
#from sklearn.neural_network import MLPClassifier
#from sklearn.naive_bayes import GaussianNB
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.ensemble import RandomForestClassifier


def detect_language(self):
   return self.translator.detect(self.raw)

def translate(self, from_lang="auto", to="en"):
   return self.__class__(self.translator.translate(self.raw,
                              from_lang=from_lang, to_lang=to))
   
def classify(self):
        if self.classifier is None:
            raise NameError("This blob has no classifier. Train one first!")
        return self.classifier.classify(self.raw)
    
def correct(self):
      tokens = nltk.tokenize.regexp_tokenize(self.raw, r"\w+|[^\w\s]|\s")
      corrected = (Word(w).correct() for w in tokens)
      ret = ''.join(corrected)
      return self.__class__(ret)
    
#country_data=pd.read_csv("F:\\TextBlob\\coutry.csv")
#print(head(country_data))  
      
#inputValue = input("Please Enter Your Input: ")
#print(inputValue)
      
application_window = tk.Tk()

inputValue = simpledialog.askstring("Input", "Hey I can translate for you. Please enter your string text in this provided space                                                                   ",
                                parent=application_window)

#clf = BaggingClassifier()
#clf = tree.DecisionTreeClassifier()
#clf = mlp = MLPClassifier(max_iter=1000,random_state=42)
#clf = MultinomialNB()

if inputValue is not None:
    print("Your Text is ", inputValue)
    
    b=TextBlob(inputValue)
    c=b.detect_language()
    print('Detect Country Code: {}'.format(c))
    #country=country_data.query("Code==bn")
    #print(country['Name'])
    #confusion=confusion_matrix(y_test, predicted, labels=[0,1])
    #print(confusion)

    new_language=b.translate(from_lang=c, to='en')
    new_language=new_language.correct()
    print('Output: {}'.format(new_language))
    messagebox.showinfo("Output",new_language)
    
else:
    print("You don't have a Text?")
    


