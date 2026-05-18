# x=33

# if x>=90:
#     print("A Grade")
# elif x>=80:
#     print("B grade")
# elif x>=70:
#     print("C Grade")
# elif x>=60:
#     print("D Grade")
# x = int(input("enter your age: "))

# if x>=18:
#     print("eligible to vote")
# elif x<18:
#     print("not eligible")
# else:
#     print("invalid")


# temp = int(input("enter your temp: "))

# if temp> 30:
#     print("it is hot")
# if temp> 20:
#     print("it is warm")
# if temp> 10:
#     print("it is cool")
# else:
#     print("it is cold")

# for x in range(3):
#     print("Hello")

# for i in range(5):
#     num = int(input("enter a Number:"))

#     if num > 5:
#         print(num,"is greater than 5")
#     else:
#         print(num,"is not greater than 5")


# m = int(input("enter a number: "))
# if m==1:
#     print("january")
# elif m==2:
#     print("february")
# elif m==3:
#     print("march")
# elif m==4:
#     print("april")
# elif m==5:
#     print("may")
# elif m==6:
#     print("june")
# elif m==7:
#     print("july")
# elif m==8:
#     print("august")
# elif m==9:
#     print("september")
# elif m==10:
#     print("october")
# elif m==11:
#     print("november")
# elif m==12:
#     print("december")
# else :
#     print("invalid month")

import turtle
wn = turtle.screen()
wn.title("Heart shape with text")
wn.bgcolor("white")

pen = turtle.turle()
pen.color("red")
pen.pensize(10)
pen.speed(1)

def drwan_heart():
    pen.begin_fill()
    pen.left(140)
    pen.forward(180)
    pen.circle(-90,200)
    pen.left(170)
    pen.circle(-90,200)
    pen.forward(180)
    pen.end_fill()

def write_text():
    pen.up()
    pen.setpos(0,50)
    pen.down()
    pen.color("blue")
    pen.write("V", align="center",font=("Arial",29,"italic","bold"))

    draw_heart()

    write_text()
    
    pen.hideturtle()
    pen.mainloop()
