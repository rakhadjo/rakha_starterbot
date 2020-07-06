import os
import time
import random
from slackclient import SlackClient

#starterbot's id as an enviro table
BOT_ID = "U2M7F4CLB"

#constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"
exCommand = "gg"
guesscommand = "g"

secretNum = 0
guess = 0
tries = 2
gameMode = False
hi = "hi!"
hey = "hey!"
respondings = ["Howdy", "Hey There", "What Is Up Bruh", "How goes life", "Wallah", "Hi!"]


#to instantiate Slack and Twilio clients
slack_client = SlackClient('xoxb-89253148691-FoNk3AavkfRQ1SkxTMhxzTnP')

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
	#playGame()

def playGame(guessing):
	MSG_SMALL = 'Enter a smaller number'
	MSG_BIG = 'Enter a larger number'
	#MSG_SUCCESS = 'Congratulations! You guessed it in ' + str(tries) + ' tries!'

	global tries
	global guess
	global secretNum
	try:
		guess = [int(s) for s in guessing.split() if s.isdigit()]

		if guess[0] != secretNum and guess != 0:
			response = 'This is try number ' + str(tries + 1) + ' and the answer is not ' + str(guess[0])
			slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
			tries = tries + 1
		

		MSG_SUCCESS = 'Congratulations! You guessed it in ' + str(tries + 1) + ' tries!'


		if guess[0] > secretNum and guess != 0:
			slack_client.api_call("chat.postMessage", channel=channel, text=MSG_SMALL, as_user=True)
		elif guess[0] < secretNum and guess != 0:
			slack_client.api_call("chat.postMessage", channel=channel, text=MSG_BIG, as_user=True)
		#else:
		
	

		if guess[0] == secretNum:
			#print('Congratulations! You guessed it in ' + str(tries) + ' tries!')
			slack_client.api_call("chat.postMessage", channel=channel, text=MSG_SUCCESS, as_user=True)
			gameMode = False
	except ValueError:
		gameMode = False
		respondent = "Game Over"
		slack_client.api_call("chat.postMessage", channel=channel, text=respondent, as_user=True)


def handle_command(command, channel):
	response = ''

	# Case 1 : Example
	if command.startswith(EXAMPLE_COMMAND):
		response = "Sure...write some more code then I can do that!"
	# Case 2 : Init
	elif command.startswith(exCommand):
		guessingGame()
	# Case 3 : Game play
	elif command.startswith(hey) or command.startswith(hi):
		z = random.randint(0, 5)
		response = respondings[z]
	elif gameMode == True:
		playGame(command)
	else:
		response = "Not sure what u mean. use the 'do' command"
	slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
	print(slack_rtm_output)
	
	output_list = slack_rtm_output
	if output_list and len(output_list) > 0:
		for output in output_list:
			if (output) and ('text' in output) and (output['user'] != BOT_ID):
				#return text after the @mention, whitespace removed(?)
				#echoMsg = "You said: ```" + output['text'] + "```"
				#slack_client.api_call("chat.postMessage", channel=output['channel'], text=echoMsg, as_user=True)
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
