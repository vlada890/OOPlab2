import datetime
from enum import Enum
class File_Manager():
    
class Faculty(object):
    def__init__(self,name,abbr,studList,studField,graduates=[]):
        self.fname=fname
        self.abbr=abbr
        self.studList=studList
        self.sField=studField
        self.graduates=[]
    def assgn(element):
        return self.studList.append(element)
    
    def graduate(self,el):
        self.graduates.append(el)
        return self.studList.remove(el)
    def __str__(self):
        return ', '.join(str(s) for s in self.studList)


class Student(Faculty):
    def__init__(self,fname,lname,email,date,birth):
        self.fname=fname
        self.lname=lname
        self.email=email
        self.date=date
        self.birth=birth
    def __str__(self):
        return self.fname
    def belonging(self,fac):
        return self in fac.studList
class StudyField(Enum):
    MechE = [ 'INGINERIE MECANICĂ, INDUSTRIALĂ ȘI TRANSPORTURI','FACULTATEA CONSTRUCȚII, GEODEZIE ȘI CADASTRU']
    SoftE = [' ENERGETICĂ ȘI INGINERIE ELECTRICĂ','CALCULATOARE, INFORMATICĂ ȘI MICROELECTRONICĂ']
    UrbanT =['ARHITECTURĂ']
    FoodT = ['TEHNOLOGIA ALIMENTELOR','ȘTIINȚE AGRICOLE si SILVICE']
    VetT=['MEDICINĂ VETERINARĂ']
    
F1=('fcim','f.c.i.m',[],StudyField.SoftE)

P1=Student('John','Miller','mail',datetime.datetime(2020, 5, 17),datetime.datetime(2000, 5, 17))
'''F1.assgn(P1)
F1.graduate(P1)
print(F1)
print(P1.belonging(F1))'''
        
