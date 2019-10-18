#Quadroots.py "PGR" Reference Craig Coleman, who referenced Amit Sarah

def roots(a,b,c):
	D = (b*b - 4*a*c)
	print()
	print("D = " + str(D))
	if (D >= 0): #check for positive D
		print("REAL ROOTS")
		D = D**0.5 # Calculate square root of D
		x1 = (-b + D) / (2*a)
		x2 = (-b - D)/ (2*a)
		print("x1 = " + str(x1)+" x2 = "+str(x2))
		
	elif(D < 0): #check for negative D
		D= (D * -1)**0.5; #Change D to a positive
		# Take square root of D then represent with "i"
		print("IMAGINARY ROOTS")
		print ("x1 = -"+str(b/(2*a))+" - "+str(D/(2*a))+"i")
		print ("x1 = -"+str(b/(2*a))+" + "+str(D/(2*a))+"i")

if __name__ == '__main__':
	print("Input a,b and c for the quadratic (ax^2 + bx + c)")
	a = input("Enter a: ")
	b = input("Enter b: ")
	c = input("Enter c: ")
	roots(float(a), float(b), float(c))
