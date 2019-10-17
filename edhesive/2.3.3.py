#2.3.3.py Peter G Rutherford

h = int(input("Enter the hour: "))
m = int(input("Enter the minute: "))

minutes = (60*h) + m
minutes = minutes + 15

hours = int(minutes / 60)
minute = int(minutes % 60)

#* * * * * * CWC

if(hours > 12):
	hours = hours - 12;
	
print("Hours: "+str(hours))
print("Minutes: "+str(minute))
#* * * * * * CWC
