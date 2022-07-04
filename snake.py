import turtle
import time
import random

delay_mov = 0.2

#Window settings
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=620,height=620)

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0,0)
head.direction = 'stop'


#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()

def snake_food_position():
    x = 20*random.randint(-15,15)
    y = 20*random.randint(-15,15)
    food.goto(x,y)
snake_food_position()    

#Snake body
snake_piece=[]

def new_snake_piece():
    piece = turtle.Turtle()
    piece.speed(0)
    piece.shape('square')
    piece.color('white')
    piece.pencolor('gray')
    piece.penup()
    piece.goto(head.xcor(),head.ycor())
    snake_piece.append(piece)
    
def move_body():
    
    for i in range(len(snake_piece)-1,0,-1):
        snake_piece[i].goto(snake_piece[i-1].xcor(),snake_piece[i-1].ycor())
        


    if len(snake_piece)>0:
        snake_piece[0].goto(head.xcor(),head.ycor())

#functions
def mov_up():
    head.direction = 'up'

def mov_down():
    head.direction = 'down'

def mov_left():
    head.direction = 'left'

def mov_right():
    head.direction = 'right'

def mov_head():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

#keyboard

wn.listen()
wn.onkeypress(mov_up,'Up')
wn.onkeypress(mov_down,'Down')
wn.onkeypress(mov_left,'Left')
wn.onkeypress(mov_right,'Right')

while True:
    wn.update()
    if head.distance(food)<20:
        snake_food_position()
        new_snake_piece()
        
        

    time.sleep(delay_mov)
    move_body()
    mov_head()
    
    
    

