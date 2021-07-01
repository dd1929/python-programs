def getPrimeFactors(num):
	factors =[]
	x = 2
	while x <= num:
		if num % x == 0:
			factors.append(x)
			num = num/x
		else: x += 1
	return factors
	
def getHCF(num1, num2):
	
	factorsOf1 = getPrimeFactors(num1)
	factorsOf2 = getPrimeFactors(num2)
	hcfFactor = []
	
	for n in factorsOf1:
		if n in factorsOf2:
			hcfFactor.append(n)
		
	hcf = 1
	for factor in hcfFactor:
		hcf *= factor
	return hcf
	
def getLCM(num1, num2):
	return int((num1 * num2)/getHCF(num1, num2))

def takeInput():
	todo = input('\nWhat do you want to do? \nEnter the corresponding letter: \n1. Factorise a single number (f) \n2. Find HCF and LCM of two numbers (h) \n')
	doAsAsked(todo)

def doAsAsked(todo):
	if todo == 'f':
		num = int(input('\nEnter the number: '))
		print('The prime factors are: ')
		factors = getPrimeFactors(num)
		for factor in factors:
			print(factor)
	
	if todo == 'h':
		num1 = int(input('Enter first number: '))
		num2 = int(input('Enter second number: '))
		print('Calculating, please wait...')
		print('\nHCF =', getHCF(num1, num2))
		print('LCM =', getLCM(num1, num2))
	
	else: 
		print('Please enter a valid letter')
		takeInput()
	
print('Hello')
print('This program can factorise numbers.')

takeInput()
	
print('Thanks for using this program. Have a nice day!')