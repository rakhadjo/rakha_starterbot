import os
import time
import random
from slackclient import SlackClient

#starterbot's id as an enviro table
BOT_ID = "U2M7F4CLB"

#BOT Constant
AT_BOT = "<@" + BOT_ID + ">"

#commands
EXAMPLE_COMMAND = "do"
exCommand = "gg"
guesscommand = "g"
arithmeticCommand = "ag"
telmi = "telmi"
confess = "@"

#Boolean Constants
surveyMode = False
gameMode = False
arithmeticMode = False

#Integer Constants
secretNum = 0
guess = 0
tries = 2
ans = 0
age = 0
zum = 0
var1 = 0
var2 = 0
minval = 1
maxval = 100

#String Constants
nama = ""
tempat = ""

#Conversation Constants
respondings = ["Howdy", "Hey There", "What Is Up Bruh", "How goes life", "Wallah", "Hello", "Hi", "Hey"]
hey = "hey!"
hi = "hi!"
hulp = "help"



#to instantiate Slack and Twilio clients
slack_client = SlackClient('xoxb-89253148691-FoNk3AavkfRQ1SkxTMhxzTnP')

def helpResponse():
	
	mainResponse = "Hello! My name is rakhas.bot! I am a slack bot designed by the ultimately handsome `Rakha Djokosoetono` (oh yes he is)"
	secondResponse = "For now I am under development still, and I can only do an arithmetic game and a guessing game"
	thirdResponse = "To play arithmetic game, type `ag`"
	fourthResponse = "To play guessing game, type `gg`"
	fifthResponse = "For me to get to know you better, type `telmi`"
	
	slack_client.api_call("chat.postMessage", channel=channel, text=mainResponse, as_user=True)
	slack_client.api_call("chat.postMessage", channel=channel, text=secondResponse, as_user=True)
	slack_client.api_call("chat.postMessage", channel=channel, text=thirdResponse, as_user=True)
	slack_client.api_call("chat.postMessage", channel=channel, text=fourthResponse, as_user=True)
	slack_client.api_call("chat.postMessage", channel=channel, text=fifthResponse, as_user=True)

def arithmeticSetup():
	
	global arithmeticMode
	arithmeticMode = True
	biz = random.randint(0, 7) #operator
	var1 = random.randint(1, 100) #first variable between one and one hundred
	var2 = random.randint(1, 100) #second variable between one and one hundred
	global ans
	
	if biz == 0:

		#addition
		ans = var1 + var2
		respon = str(var1) +  " + " + str(var2)

	elif biz == 1:

		#subtraction(v1)
		ans = var1 - var2
		respon = str(var1) + " - " + str(var2)

	elif biz == 2:

		#multiplication
		ans = var1 * var2
		respon = str(var1) + " * " + str(var2)

	elif biz == 3:

		#division(v1)
		ans = var1 / var2
		respon = str(var1) + " / " + str(var2)

	elif biz == 4:

		#subtraction(v2)
		ans = var2 - var1
		respon = str(var2) + " - " + str(var1)

	elif biz == 5:

		#division(v2)
		ans = var2 / var1
		respon = str(var2) + " / " + str(var1)

	elif biz == 6:
		
		#modulo(v1)
		ans = var1 % var2
		respon = str(var1) + " mod " + str(var2)

	elif biz == 7:
		#modulo(v2)
		ans = var2 % var1
		respon = str(var2) + " mod " + str(var1)

	slack_client.api_call("chat.postMessage", channel=channel, text=respon, as_user=True)
	
	global guess
	guess = 0
	global tries
	tries = 1

def arithmeticPlay(answ):
	MSG_RIGHT = "Correct!"
	MSG_WRONG = "Incorrect!"

	global tries
	global guess
	global ans

	try:

		guess = [int(s) for s in answ.split() if s.isdigit()]

		if guess[0] != ans:

			slack_client.api_call("chat.postMessage", channel=channel, text=MSG_WRONG, as_user=True)
			
			tries = tries + 1

		MSG_CONGRATS = 'Congratulations! You guessed it in ' + str(tries) + ' tries!'

		if guess[0] == ans:

			response = MSG_RIGHT
			
			slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
			slack_client.api_call("chat.postMessage", channel=channel, text=MSG_CONGRATS, as_user=True)
			
			tries = 0
			arithmeticMode = False

		arithmeticSetup()

	except IndexError:

		arithmeticMode = False
		kondensasi = "Game Over Fam"
		
		slack_client.api_call("chat.postMessage", channel=channel, text=kondensasi, as_user=True)

def guessingGame():

	global gameMode
	gameMode = True
	global secretNum
	secretNum = random.randint(1, 100)

	slack_client.api_call("chat.postMessage", channel=channel, text='Im thinking of a number between 1 and 100. Tell me what you think!', as_user=True)
	slack_client.api_call("chat.postMessage", channel=channel, text='This your first try.', as_user=True)

	global guess
	guess = 0
	global tries 
	tries = 1

def playGame(guessing):

	MSG_SMALL = 'Enter a smaller number'
	MSG_BIG = 'Enter a larger number'

	global tries
	global guess
	global secretNum
	global minval
	global maxval

	try:

		guess = [int(s) for s in guessing.split() if s.isdigit()]

		if len(guess) > 1:

			slack_client.api_call("chat.postMessage", channel=channel, text="U cant do this to me fam pls pick one number only ", as_user=True)

		else:

			if guess[0] != secretNum and guess != 0:

				response = 'This is try number ' + str(tries + 1) + ' and the answer is not ' + str(guess[0])
				
				slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
				
				tries = tries + 1		

			MSG_SUCCESS = 'Congratulations! You guessed it in ' + str(tries + 1) + ' tries!'

			if guess[0] > secretNum:

				if guess[0] < maxval:

					maxval = guess[0]

				slack_client.api_call("chat.postMessage", channel=channel, text=MSG_SMALL, as_user=True)
				
				hella = "Clue: It is now between " + str(minval) + " and " + str(maxval)
				
				slack_client.api_call("chat.postMessage", channel=channel, text=hella, as_user=True)

			elif guess[0] < secretNum:

				if guess[0] > minval:

					minval = guess[0]

				slack_client.api_call("chat.postMessage", channel=channel, text=MSG_BIG, as_user=True)
				
				hella2 = "Clue: It is now between " + str(minval) + " and " + str(maxval)
				
				slack_client.api_call("chat.postMessage", channel=channel, text=hella2, as_user=True)

			if guess[0] == secretNum:

				slack_client.api_call("chat.postMessage", channel=channel, text=MSG_SUCCESS, as_user=True)
				
				gameMode = False

	except IndexError:

		gameMode = False
		respondent = "Game Over"
		
		slack_client.api_call("chat.postMessage", channel=channel, text=respondent, as_user=True)

def getToKnow():

	global surveyMode
	surveyMode = True
	global zum
	zum = 0
	global nama
	global tempat

	slack_client.api_call("chat.postMessage", channel=channel, text="Hey there! Tell me about yourself!", as_user=True)
	slack_client.api_call("chat.postMessage", channel=channel, text="Whats ur name", as_user=True)

def getToKnowAns1(jawaban1):

	global zum
	zum = 0
	global nama
	nama = jawaban1
	zum = 1
	
	slack_client.api_call("chat.postMessage", channel=channel, text="nice to meet u " + nama + ", where are you from?", as_user=True)

def getToKnowAns2(jawaban2):

	global zum
	global tempat
	tempat = jawaban2
	
	slack_client.api_call("chat.postMessage", channel=channel, text=tempat + " is a beautiful place :)", as_user=True)
	slack_client.api_call("chat.postMessage", channel=channel, text="How old are you?", as_user=True)
	
	zum = 2

def getToKnowAns3(jawaban3):

	global zum
	global age
	try:

		age = int(jawaban3)
		slack_client.api_call("chat.postMessage", channel=channel, text="Cool! Next year you'll be " + str(age + 1) + " then", as_user=True)

	except ValueError:

		slack_client.api_call("chat.postMessage", channel=channel, text="Hahahah i can only read numbers in this question, mate", as_user=True)

def handle_command(command, channel):

	response = ''
	global zum

	# Case 1 : Example
	if command.startswith(EXAMPLE_COMMAND):

		response = "Sure...write some more code then I can do that!"

	# Case 2 : Guessing Game
	elif command.startswith(exCommand):

		guessingGame()

	# Case 3 : Help
	elif command.startswith(hulp):

		helpResponse()

	# Case 4 : Arithmetic Game
	elif command.startswith(arithmeticCommand):

		arithmeticSetup()

	# Case 5 : Hello
	elif (command in respondings) or (command.lower() in respondings) or (command.upper() in respondings):

		z = random.randint(0, 7)
		response = respondings[z]

	# Case 6 : Get to Know
	elif command.startswith(telmi):

		getToKnow()

	#elif command.startswith(confess):



	# Situation 1 : Play Arithmetic Game
	elif arithmeticMode == True:

		arithmeticPlay(command)

	# Situation 2 : Play Guessing Game
	elif gameMode == True:

		playGame(command)

	#Situation 3 : Survey Mode
	elif surveyMode == True:

		if zum == 0:

			#Prompts user to answer first question
			getToKnowAns1(command)

		elif zum == 1:

			#Prompts user to answer second question
			getToKnowAns2(command)

		elif zum == 2:

			#Prompts user to answer third question
			getToKnowAns3(command)

	else:

		response = "Not sure what you mean. use the `help` or `do` command"

	slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
	
def parse_slack_output(slack_rtm_output):

	print(slack_rtm_output)
	
	output_list = slack_rtm_output

	if output_list and len(output_list) > 0:

		for output in output_list:

			if (output) and ('text' in output) and (output['user'] != BOT_ID):

				return output['text'], output['channel']

	return None, None

if __name__=="__main__":

	READ_WEBSOCKET_DELAY = 1 #1sec delay between reading from firehose(?)

	if slack_client.rtm_connect():

		print("StarterBot connected and running!")
		
		while True:

			command, channel = parse_slack_output(slack_client.rtm_read())
			
			print(command)
			print(channel)
			
			if command and channel:

				handle_command(command, channel)

			
			time.sleep(READ_WEBSOCKET_DELAY)
	else:

		print("Connection failed. Invalid Slack token or bot ID?")
