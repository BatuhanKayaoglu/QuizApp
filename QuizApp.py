# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:01:21 2021

@author: pc
"""


class Question:
    def __init__(self,text,choises,answer):
        self.text=text
        self.choises=choises
        self.answer=answer
        
        
        
    def checkAnswer(self,answer):
        return self.answer==answer
    
    
    
       
    
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0 #0 demek question class'ındaki ilk indexi yani q1 sorusunu getirecek.
        
    
    def getQuestion(self):
        return self.questions[self.questionIndex]   

    
   
    def displayQuestion(self): ##  print(question.text) aşağıya bu kodu yazmak yerine bir def tanımlayarak çalıştırıcaz bu kodu.
        question=self.getQuestion() #İlgili question'ı aldık.
        print(f'Soru {self.questionIndex+1}: {question.text}')
        
        
        for q in question.choises: #Her bir liste elemanını yazdırmak istersek..
           print(f'- {q}')
           
           
        answer=input('Cevap: ')
        self.guess(answer)
        self.loadQuestion()
            
        
    def guess(self,answer):
        question=self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score+=1
                    
        self.questionIndex+=1
        
        self.displayQuestion()
        
     
    def loadQuestion(self):
        if len(self.question)==self.questionIndex:
            self.showScore()
            
        else:
            self.displayQuestion()
            
        
    def showScore(self):
        pass        
        
       
        

q1=Question('En iyi Programala dili hangisidir?',['java','Python','C','C#'],'Python')
q2=Question('En cok kullanılan Programala dili hangisidir?',['java','Python','C','C#'],'Python')
q3=Question('En popüler Programala dili hangisidir?',['java','Python','C','C#'],'Python')

questions=[q1,q2,q3]


print(q1.checkAnswer('Python'))  

quiz=Quiz(questions)
question=quiz.getQuestion()
quiz.displayQuestion()   



