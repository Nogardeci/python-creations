from random import randint

a = (randint(0,100))
m = 100.0
g = 0

while True:
	if m < 1:
		print ("You're either very close or very far")
	else:	
		print ("Your current chances of guessing it right are 1/%s") % m
	if g > 0:
		print ("Number of guesses: %s") %g	
	n = input("Type a number from 0 to 100: ")
	if n < a:
		print ("Go higher")
		g = g+1
	if n > a:
		print ("Go lower")
		g = g+1
	if m/2-1 <= n <= m/2+1:
		m = m/2
	else:
		m = m-1		
	if n == a:
		print ("You guessed it, congratulations!")
		break
