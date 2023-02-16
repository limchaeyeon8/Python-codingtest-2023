# 프랙탈 원들 그리기
import turtle

turtle.setup(width=600, height=600)

t = turtle.Turtle()  
  
turtle.bgcolor("black")  
turtle.pensize(2)  
turtle.speed(0)  
  
while (True):  
    for i in range(6):  
        for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:  
            turtle.color(colors)  
            turtle.circle(100)  
            turtle.left(10)    
            
turtle.hideturtle()  
turtle.mainloop()