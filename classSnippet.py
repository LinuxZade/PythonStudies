#-----------------------------------------
# Numpy Library :
#-----------------------------------------
import numpy as np

#-----------------------------------------
# Class Declerations :
#-----------------------------------------

class classTemplate:
    
    def __init__(self, x=2, y=3): 
        self.x = x 
        self.y = y 
 
    def setX(self,x):
        self.x = x 
     
    def add(self):
        return (self.x+self.y)
    
    def addTwice(self):
        return ( self.add() + self.add() ) # call other method


myClass = classTemplate()
result = myClass.add()
print(result) # 2+3 = 5

myClass.setX(11)
result = myClass.add()
print(result) # 11+3 = 14

result = myClass.addTwice()
print(result) # 14+14 = 28

# inheritance
class newClass(classTemplate):
    def __init__(self, a=7, b=8): 
        self.a = a 
        self.b = b 
        classTemplate.__init__(self,x=20,y=30)

    def mul(self):
        return (self.a * self.b)

mynewClass = newClass()
result = mynewClass.add() # inherited method
print(result) # 20+30 = 50
result = mynewClass.mul() # self method
print(result) # 7*8 = 56




