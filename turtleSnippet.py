#-----------------------------------------
# Turtle Library :
#-----------------------------------------
import turtle 

# define Board and Turtle Instance
drawingBoard = turtle.Screen()
drawingBoard.bgcolor("light blue")
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
    turtleInstance.forward(300)
    turtleInstance.left(144)
'''

# draw generic polygon func:
'''
def polyDraw(sideNum,lineDistance):
    turnAngle = 360/sideNum
    for i in range(sideNum):
        turtleInstance.forward(lineDistance)
        turtleInstance.left(turnAngle)

polyDraw(5,100)
polyDraw(6,100)
polyDraw(7,100)
polyDraw(8,100)
'''




turtle.done()



