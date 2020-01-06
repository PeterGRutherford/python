'''
Test this.
https://tritech-testsite.smapply.io/

Get the code: 10.183.1.26 code python
Plot circle data using python

- Change the graph line colors
- Change the plot line color
- Change the plot dot color
- Label the graph with text Plotting Circumference and Diameter
- Label the axis with text (Circumference and Diameter)
- Upload to github with your name initials or name attached (plot-circle-list-cwc.py

'''

import turtle
import math
wdth = 800; hgth = 800; bgstring = "#dddded"
red = "#80143C"; green = "#00EF2A"; blue = "#00D9EF"

def grid(t):
	x = 0; y = 0
	while (x < 400):
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x,y+400)
		x = x + 50
	x = 0; y = 0
	while (y < 400):
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x+400,y)
		y = y + 50
	
	t.penup()

def plotCircles(t):
	d =  [12.26, 17.27, 22.25, 11] 
	c =  [3*9,  3*5.5, 3*7, 3*3.5 ] 
	dsorted = sorted (d, key = float)
	csorted = sorted(c , key = float)
	t.goto(0,0)
	t.pendown()
	t.dot(3, red)
	t.goto(dsorted[0],csorted[0])
	t.dot(3, red)
	t.goto(dsorted[1],csorted[1])
	t.dot(3, red)
	t.goto(dsorted[2],csorted[2])
	t.dot(3, red)
	t.goto(dsorted[3],csorted[3])
	t.dot(3, red)
	
	t.penup()
	t.goto(-20,-20)
	t.pendown()
	t.color('blue')
	style = ('Courier', 10, 'italic')
	t.write('Axis', font=style, align='center')
	t.penup()
	t.goto(0,-200)
	t.pendown()
	t.color('blue')
	style = ('Courier', 10, 'italic')
	t.write('Circumfrance and Diameter Plot', font=style, align='center')
	
def main():
	try:
		turtle.TurtleScreen._RUNNING = True
		# get wdth and hgth globally
		turtle.screensize(canvwidth=wdth, canvheight=hgth, bg=bgstring)
		print(turtle.Screen().screensize())
		w = turtle.Screen()
		t = turtle.Turtle()
		t.hideturtle()
		t.color('magenta')
		grid(t)
		plotCircles(t)
		w.exitonclick()
	finally:
		turtle.Terminator()
	
if __name__ == '__main__':
	main()

'''
	# Using sorted + key 
	Output = sorted(Input, key = float) 
	# Using sorted + key 
	Output = sorted(Input, key = float) 
'''
