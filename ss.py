import turtle

wn = turtle.Screen()
wn.title("Heart Shape with Text")
wn.bgcolor("white")

pen = turtle.Turtle()
pen.color("red")
pen.pensize(10)
pen.speed(1)

def draw_heart():
    pen.begin_fill()
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()

def write_text():
    pen.up()
    pen.setpos(0, 50)   # Center the text
    pen.down()
    pen.color("blue")
    pen.write(
        "Hi",
        align="center",
        font=("Arial", 29, "italic", "bold")
    )

# Draw the heart shape
draw_heart()

# Write the text inside the heart
write_text()

# Hide the turtle and finish
pen.hideturtle()
wn.mainloop()