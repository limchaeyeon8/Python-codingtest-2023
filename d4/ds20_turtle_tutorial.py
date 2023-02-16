import turtle

def tri(tri_len):
    if tri_len <= 10:
        for i in range(0,3):
            turtle.forward(tri_len)
            turtle.left(120)
        return
    
    new_len=tri_len/2
    tri(new_len)
    turtle.forward(new_len)
    tri(new_len)
    turtle.backward(new_len)
    turtle.left(60)
    turtle.forward(new_len)
    turtle.right(60)
    tri(new_len)
    turtle.left(60)
    turtle.backward(new_len)
    turtle.right(60)

screen = turtle.Screen()
screen.setup(600, 600)
turtle.speed(100)
tri(100) #함수 호출
turtle.hideturtle()
turtle.done()
screen.update()

turtle.mainloop() # Alt + F4