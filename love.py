import turtle 
t = turtle.Turtle() 
s = turtle.Screen() 
s.bgcolor('black') 
t.hideturtle() 
t.goto(0,-10)  
t.pensize(3) 
t.color('YELLOW') 
t.begin_fill() 
t.left(140) 
t.forward(180)  
t.circle(-90,200) 
t.setheading(60) 
t.circle(-90,200)
t.forward(178) 
t.end_fill() 
t.penup() 
t.goto(-95,130) 
t.pendown() 
t.color('white') 
t.write("I LOVE TO \nCODE",font=("verdana",25,"bold")) 
turtle.done()
#123
