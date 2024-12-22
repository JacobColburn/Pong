#pong

import turtle
import winsound

screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)

#score
player_1_score = 0
player_2_score = 0


#Player 1

player_1= turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("black")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(-350, 0)

#player 2

player_2= turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("black")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
player_2.goto(350, 0)


#ball

ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = .1
ball.dy = .1

#pen
pen =turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: {} Player 2: {} ".format(player_1_score, player_2_score) , align="center", font=("Courier", 24, "bold"))

#functions
def player_1_up():
    y= player_1.ycor()
    y+= 20
    player_1.sety(y)

def player_1_down():
    y= player_1.ycor()
    y-= 20
    player_1.sety(y)

def player_2_up():
    y= player_2.ycor()
    y+= 20
    player_2.sety(y)

def player_2_down():
    y= player_2.ycor()
    y-= 20
    player_2.sety(y)

def write():
    pen.clear()
    pen.write("Player 1: {} Player 2: {} ".format(player_1_score, player_2_score) , align="center", font=("Courier", 24, "bold"))



#keybinds
screen.listen()
screen.onkeypress(player_1_up, "w",)
screen.onkeypress(player_1_down, "s",)

screen.onkeypress(player_2_up, "Up",)
screen.onkeypress(player_2_down, "Down",)
#main game loop
while True:
    screen.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("sounds\\bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -283:
        ball.setx(-283)
        ball.dy *= -1
        winsound.PlaySound("sounds\\bounce.wav", winsound.SND_ASYNC)
        

    if ball.xcor() >390:
        ball.setx(390)
        ball.goto(0,0)
        ball.dx *= -1
        player_1_score += 1
        write()
        winsound.PlaySound("sounds\classic_hurt.wav", winsound.SND_ASYNC)
    
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.goto(0,0)
        ball.dx *= -1
        player_2_score += 1
        write()
        winsound.PlaySound("sounds\classic_hurt.wav", winsound.SND_ASYNC)

    #collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor()< player_2.ycor() + 50 and ball.ycor() > player_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("sounds\\bounce.wav", winsound.SND_ASYNC)
    
    if (ball.xcor() < -340 and ball.xcor() >-350) and (ball.ycor()< player_1.ycor() + 50 and ball.ycor() > player_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("sounds\\bounce.wav", winsound.SND_ASYNC)
