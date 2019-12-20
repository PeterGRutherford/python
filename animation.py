import turtle   #Outside_In 
loadWindow = turtle.Screen() 
turtle.screensize(canvwidth=1100, canvheight=1100, bg=None)
turtle.speed(1) 
t = turtle.Turtle()
y = 0; x = -500
t.pendown
mx = 1
if(mx == 1):
	for i in range(4):
		t.forward(100)
		t.right(90)
		
	for i in range(4):
		t.forward(200)
		t.right(90)
		t.forward(100)
		t.right(90)
		t.forward(100)
		t.right(90)
		t.forward(100)
		t.right(90)
		mx = 2
		
if(mx ==2):
	t.penup
	t.setposition(-300,300)
	t.pendown
	t.circle(50)
 
	t.penup()
	t.setposition(-320, 100)
	t.pendown()
	t.circle(50)
 
	t.penup()
	t.setposition(-320,-100)
	t.pendown()
	t.circle(50)
 
	t.penup()
	t.setposition(-300, 200)
	t.pendown()
	t.circle(50)
 
	t.penup()
	t.setposition(-280, -200)
	t.pendown()
	t.circle(50)

turtle.mainloop()



