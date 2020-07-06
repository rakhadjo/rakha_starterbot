import random
secretNum = random.randint(1, 100)
print('Im thinking of a number between 1 and 100. Git Gud.')

guess = 0
tries = 1

while guess != secretNum:
	print('Take a guess! This is try number ' + str(tries))
	tries = tries + 1
	guess = int(input())

	if guess > secretNum:
		print('Enter a smaller number')
	elif guess < secretNum:
		print('Enter a larger number')
	else:
		break

	

if guess == secretNum:
	print('Congratulations! You guessed it in ' + str(tries) + ' tries!')