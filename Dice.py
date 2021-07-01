from random import randint

def rollDice(num):
	x = 0
	while x < num:
		print('Dice', x+1, ':', randint(1, 6))
		x += 1

print('Hello')
print('This program can emulate dice')
num = int(input('How many dice would you like? '))
rollDice(num)