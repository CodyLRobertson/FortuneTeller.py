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
#4 		- Main Program
def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'It is certain'
	elif answerNumber == 2:
		return 'It is decidely so.'
	elif answerNumber == 3:
		return 'Yes.'
	elif answerNumber == 4:
		return 'Reply hazy, try again.'
	elif answerNumber == 5:
		return 'Ask again later.'
	elif answerNumber == 6:
		return 'Concentrate and ask again.'
	elif answerNumber == 7:
		return 'My replay is no.'
	elif answerNumber == 8:
		return 'Outlook not so good.'
	elif answerNumber == 9:
		return 'Very doubtful.'
	elif answerNumber == 10:
		return 'Hard No.'
r = random.randint(1,10)
answer = getAnswer(r)
print(answer)

#4.2 	- Collect random int
#4.3 	- Display Answer based on int


#4.4 	- Display original Question
#5		- Ask to repeat? Y/N
#6 		- If (N) End program gracefully
#7 		- Wrap functions into main function
def Main():
	getTimeAndDate()
	getUsername()
	getUserQuestion()
	getAnswer()


Main()
