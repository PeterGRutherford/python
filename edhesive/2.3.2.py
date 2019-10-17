#2.3.2.py Peter R
a = int(input("Enter the Feet for the first piece of fabric: "))
b = int(input("Enter the Inches for the first piece of fabric: "))

c = int(input("Enter the Feet for the second piece of fabric: "))
d = int(input("Enter the Inches for the second piece of fabric: "))

#* * * * * * CWC
totalinches = b + d + a *12 + c *12
tf = int(totalinches / 12)
ti = int(totalinches % 12)
print("Feet: "+str(tf)+" Inches: "+str(ti))
#* * * * * * CWC
