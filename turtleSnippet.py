#-----------------------------------------
# Turtle Library :
#-----------------------------------------
import turtle 

# define Board and Turtle Instance
drawingBoard = turtle.Screen()
drawingBoard.bgcolor("black")
drawingBoard.title("Python Turtle")
turtleInstance = turtle.Turtle()

# draw square method-1:
'''
turtleInstance.forward(100)
turtleInstance.left(90)
turtleInstance.forward(100)
turtleInstance.left(90)
turtleInstance.forward(100)
turtleInstance.left(90)
turtleInstance.forward(100)
'''
# draw square method-2:
'''
for i in range(4):  
    turtleInstance.forward(100)
    turtleInstance.left(90)
'''

# draw star method:
'''
for i in range(5):  
    turtleInstance.forward(100)
    turtleInstance.left(144)
'''

# draw generic polygon func:

def polyDraw(sideNum,lineDistance):
    turnAngle = 360/sideNum
    for i in range(sideNum):
        turtleInstance.forward(lineDistance)
        turtleInstance.left(turnAngle)

#polyDraw(6,100)



def shrinkingSquare(numOfSquare,lineLen):
    tempLen = lineLen
    for i in range(numOfSquare):
        for j in range(4):
            turtleInstance.forward(tempLen)
            turtleInstance.left(90)
        
        tempLen = lineLen - (i+1)*(lineLen/numOfSquare)


#shrinkingSquare(10,100)

 
def drawEight(radius):
    turtleInstance.circle(radius)
    turtleInstance.circle(-1*radius)


def shrinkingEight(numOfInstance):
    turtleInstance.speed(0)
    colorList = ["red", "purple", "blue", "green", "orange", "yellow"]
    for i in range(numOfInstance):
        turtleInstance.color(colorList[i%len(colorList)])
        drawEight(2*i)

def drawClover(numOfInstance):
    shrinkingEight(numOfInstance)
    turtleInstance.left(90)
    shrinkingEight(numOfInstance)

#drawClover(20)
 
#turtle interactive draw:
turtleInstance.color("yellow")

def drawLine():
    turtleInstance.forward(100)

def rotateRight():
    turtleInstance.right(15)

def rotateLeft():
    turtleInstance.left(15)   

def clearBoard():
    turtleInstance.clear()    

def goHome():
    turtleInstance.up()
    turtleInstance.home()   
    turtleInstance.down()

'''
drawingBoard.listen()
drawingBoard.onkey(fun=drawLine, key="space")    
drawingBoard.onkey(fun=rotateRight, key="Down")  
drawingBoard.onkey(fun=rotateLeft, key="Up")  
drawingBoard.onkey(fun=clearBoard, key="d")   
drawingBoard.onkey(fun=goHome, key="h") 
'''

#--------------------------------------------------------------
# HW : Game
#--------------------------------------------------------------








turtle.mainloop()



