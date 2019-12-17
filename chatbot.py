print("Hello, My name is Sam the cat.")
a = input("What's your name(first)?")
print("Cool! Nice to meet you " + a + "!")
b = input("So, how was your day? (good/bad)")
if(b == "good" or "Good"):
	print(b)
	print("That's awesome! Most people I ask say they are doing bad or ~tired~")
	c = input("Do you play any sports? Which one, if any?")
	if(c == "Soccer" or "soccer"):
		print(c)
		print("I like soccer too! although, I wouldn't call it soccer. My paws are too small so I use an even smaller plastic ball with a bell in it. It's addicting")
	elif(c == "Football" or "football"):
		print(c)
		print("Hmmmm. I've never really played football. People need aposable thumbs, and I don't have them :(")
	elif(c == "Baseball" or "baseball"):
		print("I like playing baseball too! The only thing I can do is run bases, but I happen to be the best at that.")
	else:
		print("I don't know what that sport is...")
elif(b == "bad" or "Bad"):
	print(b)
	print("Oh, that's too bad. But I cannot change that, you can!")
elif(b == "tired" or "Tired"):
	print(b)
	print("Go get some some sleep dumdum, no one wants to deal with a sleepy person. No one wants to be a sleepy person.")
else:
	print("I don't know exactly what you said, you must've had a typo")
	
