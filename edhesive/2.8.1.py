#2.8.1.py - PGR

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a > b:
	b = a

if b > c:
	c = b

if c > b:
	b = c
	
print(b)
