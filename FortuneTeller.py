#Import Relevant Modules here---
import random
import time
from datetime import date
import sys


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
	username = input("What is your name? ")
	print("Thank you, "+ username + ".")
#3 		- Ask for User's Question
def getUserQuestion():
	global userQuestion
	userQuestion = input("What is your question? ")
	print("You have asked: " + '"'+userQuestion+'"')
#4 		- Main Program
#4.2 	- Collect random int
def getRandomNum():
	answerNumber = random.randint(1,10)
	if answerNumber == 1:
		answerStatement = 'It is certain'
	elif answerNumber == 2:
		answerStatement = 'It is decidely so.'
	elif answerNumber == 3:
		answerStatement = 'Yes.'
	elif answerNumber == 4:
		answerStatement = 'Reply hazy, try again.'
	elif answerNumber == 5:
		answerStatement = 'Ask again later.'
	elif answerNumber == 6:
		answerStatement = 'Concentrate and ask again.'
	elif answerNumber == 7:
		answerStatement = 'My replay is no.'
	elif answerNumber == 8:
		answerStatement = 'Outlook not so good.'
	elif answerNumber == 9:
		answerStatement = 'Very doubtful.'
	elif answerNumber == 10:
		answerStatement = 'Hard No.'
	r = (answerStatement)
	
	time.sleep(1)
	print("Question:      "+ userQuestion)
	print("Answer:      " + r)
	print("  ")
	print("  ")
	print("  ")

def creditsList():
	print("Creator: Cody Robertson")
	print("Github: https://bit.ly/2JH7uWC")

def timeLapse():
	print("Please Wait.")
	time.sleep(1)
	print("...")
	time.sleep(1)
	print("..")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print("			")
	
def Main():
	getUserQuestion()
	print("	")
	time.sleep(1)
	print("...")
	getRandomNum()
def gameParamters():
	r = input("How many times do you want to play? Type in appropriate number. ")
	i = 0
	while i <= int(r):
		Main()
		i = i+1
		if i == int(r):
			print("Thank you for playing.")
			creditsList()
			break
def playAgainFunc():
	playAgain = "y"
	playAgain == input("Do you want to play again? Y/N?").lower()
	if playAgain == "y".lower():
		gameParamters()
	elif playAgain == "n".lower():
		sys.exit()
	else:
		sys.exit()



getTimeAndDate()
timeLapse()
getUsername()
timeLapse()
gameParamters()
input("Press any key to end program. ")




