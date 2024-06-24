from turtle import * 


speed(4)
width(5)
forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#კუბის დასასრული

## კარი

color("black")
begin_fill()
forward(120)
left(90)
forward(120)
right(90)
forward(70)
right(90)
forward(120)
end_fill()

## სახურავი

penup()
goto(199,200)
pendown()
right(120)
begin_fill()
color("purple") 
forward(117)
left(60)
forward(115)
end_fill()

## ფანჯარა

color("yellow")
begin_fill()
penup()
goto(90,90)
pendown()
right(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()



exitonclick()