#Import Relevant Modules here---
import random
import time
from datetime import date

#Order of Functions
#1 		- Display Time and Date
def getTimeAndDate():
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)
	today = date.today()
	print("Current Time is", current_time)
	print("Today's Date is", today)
#2 		- Ask for user's name
def getUsername():
	username = input("What is your name?")
	print("Thank you "+ username)
#3 		- Ask for User's Question
def getUserQuestion():
	userQuestion = input("What is your question?")
	print("You have asked: " + userQuestion)
	continueGame = input(str.lower("Is this correct? Y/N"))
	if continueGame == "y":
		break
	else:
		getUserQuestion()

#4 		- Main Program
#4.2 	- Collect random int 
#4.3 	- Display Answer based on int
#4.4 	- Display original Question
#5		- Ask to repeat? Y/N
#6 		- If (N) End program gracefully
#7 		- Wrap functions into main function
def Main():
	getTimeAndDate()
	getUsername()


Main()
