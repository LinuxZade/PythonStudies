#-----------------------------------------
# Turtle Library :
#-----------------------------------------
import turtle 
import time

# define Board and Turtle Instance
'''
drawingBoard = turtle.Screen()
drawingBoard.bgcolor("black")
drawingBoard.title("Python Turtle")
turtleInstance = turtle.Turtle()
'''

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
'''
def polyDraw(sideNum,lineDistance):
    turnAngle = 360/sideNum
    for i in range(sideNum):
        turtleInstance.forward(lineDistance)
        turtleInstance.left(turnAngle)
'''
#polyDraw(6,100)

'''
def shrinkingSquare(numOfSquare,lineLen):
    tempLen = lineLen
    for i in range(numOfSquare):
        for j in range(4):
            turtleInstance.forward(tempLen)
            turtleInstance.left(90)
        
        tempLen = lineLen - (i+1)*(lineLen/numOfSquare)

'''
#shrinkingSquare(10,100)

''' 
def drawEight(radius):
    turtleInstance.circle(radius)
    turtleInstance.circle(-1*radius)
'''
'''
def shrinkingEight(numOfInstance):
    turtleInstance.speed(0)
    colorList = ["red", "purple", "blue", "green", "orange", "yellow"]
    for i in range(numOfInstance):
        turtleInstance.color(colorList[i%len(colorList)])
        drawEight(2*i)
'''

'''
def drawClover(numOfInstance):
    shrinkingEight(numOfInstance)
    turtleInstance.left(90)
    shrinkingEight(numOfInstance)
'''

#drawClover(20)
 
#turtle interactive draw:
'''
turtleInstance.color("yellow")

def drawLine():
    turtleInstance.forward(100)
'''

'''
def rotateRight():
    turtleInstance.right(15)
'''

'''
def rotateLeft():
    turtleInstance.left(15)   
'''

'''
def clearBoard():
    turtleInstance.clear()    
'''

'''
def goHome():
    turtleInstance.up()
    turtleInstance.home()   
    turtleInstance.down()
'''


'''
drawingBoard.listen()
drawingBoard.onkey(fun=drawLine, key="space")    
drawingBoard.onkey(fun=rotateRight, key="Down")  
drawingBoard.onkey(fun=rotateLeft, key="Up")  
drawingBoard.onkey(fun=clearBoard, key="d")   
drawingBoard.onkey(fun=goHome, key="h") 
'''

#--------------------------------------------------------------
# HW : Catch the Ball
#--------------------------------------------------------------
screenInst = turtle.Screen()
screenInst.bgcolor("gray")
screenInst.title("Catch The Ball")
tbound = turtle.Turtle()
tSnake = turtle.Turtle()
tFood1 = turtle.Turtle()
tFood2 = turtle.Turtle()
tFood3 = turtle.Turtle()
tFood4 = turtle.Turtle()
tFood5 = turtle.Turtle()
tScore = turtle.Turtle()
tTime = turtle.Turtle()
tScore.penup()
tTime.penup()
tScore.hideturtle()
tTime.hideturtle()
tFood1.color("blue")
tFood2.color("blue")
tFood3.color("blue")
tFood4.color("blue")
tFood5.color("blue")
tSnake.shape("square")
tSnake.penup()
eps = 1.5
score = 0
gameIn = True


tFood1.shape("circle")
tFood1.shapesize(1,1,1)
tFood2.shape("circle")
tFood2.shapesize(1,1,1)
tFood3.shape("circle")
tFood3.shapesize(1,1,1)
tFood4.shape("circle")
tFood4.shapesize(1,1,1)
tFood5.shape("circle")
tFood5.shapesize(1,1,1)
tFood1.penup()
tFood2.penup()
tFood3.penup()
tFood4.penup()
tFood5.penup()

tFood1.setpos(10,10)
tFood2.setpos(-110,10)
tFood3.setpos(120,20)
tFood4.setpos(10,-110)
tFood5.setpos(20,120)

def drawBoundary(boundLen):
    tbound.hideturtle()
    tbound.penup()
    tbound.setpos(-boundLen/2,-boundLen/2)
    tbound.pendown()
    for i in range(4):
        tbound.forward(boundLen)
        tbound.left(90)

def snakeWalk(delayms):
    if (tSnake.xcor()<200) and (tSnake.xcor()>-200) and (tSnake.ycor()<200) and (tSnake.ycor()>-200):
        tSnake.forward(1)
    else:
        tSnake.goto(0,0)

    turtle.delay(delayms) 

def snakeRight():
    tSnake.right(90)    

def snakeLeft():
    tSnake.left(90) 

def checkSucces():
    global score

    if ((abs(tSnake.xcor() - tFood1.xcor()) < eps) and (abs(tSnake.ycor() - tFood1.ycor()) < eps)): 
        score +=1 
    elif ((abs(tSnake.xcor() - tFood2.xcor()) < eps) and (abs(tSnake.ycor() - tFood2.ycor()) < eps)):   
        score +=1 
    elif ((abs(tSnake.xcor() - tFood3.xcor()) < eps) and (abs(tSnake.ycor() - tFood3.ycor()) < eps)):  
        score +=1 
    elif ((abs(tSnake.xcor() - tFood4.xcor()) < eps) and (abs(tSnake.ycor() - tFood4.ycor()) < eps)):  
        score +=1 
    elif ((abs(tSnake.xcor() - tFood5.xcor()) < eps) and (abs(tSnake.ycor() - tFood5.ycor()) < eps)):  
        score +=1 

def moveSnake():
    screenInst.listen() 
    snakeWalk(0.5)
    screenInst.onkey(fun=snakeRight, key="r") 
    screenInst.onkey(fun=snakeLeft, key="l") 
    checkSucces()
    tScore.clear()
    tScore.write("Score : " +str(score),move=False,font=("Arial",12,"bold"))

drawBoundary(400)  
tScore.setpos(-20,200)
tTime.setpos(-20,250)

startTime = time.time()


print( str(tbound.pos()) )

while(gameIn): 
    moveSnake()
    remain = startTime+50 - time.time() 
    tTime.clear()
    tTime.write("Time : " +str(int(remain)),move=False,font=("Arial",12,"bold"))
     
    if (remain < 0):
        gameIn = False

tTime.clear()
tTime.write("Time is up :( ",move=False,font=("Arial",12,"bold"))

turtle.mainloop()



