import math

# A function to print all prime factors of
# a given number n
def primeFactors(n): # https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
	output = []
	# Print the number of two's that divide n
	while n % 2 == 0:
		output.append(2)
		n = n / 2
		
	# n must be odd at this point
	# so a skip of 2 ( i = i + 2) can be used
	for i in range(3,int(math.sqrt(n))+1,2):
		
		# while i divides n , print i and divide n
		while n % i== 0:
			output.append(i)
			n = n / i
			
	# Condition if n is a prime
	# number greater than 2
	if n > 2:
		output.append(n)

	return(output)		

def factor_palindromes():
	palindromes = {}
	for num in range(1000,10000):
		string = str(num) 
		if string == string[::-1]: #if the number is palindromic
			palindromes[num] = primeFactors(num)
	
	for key in palindromes.keys():
		print(key, ": ", palindromes[key])
factor_palindromes()

def is_divisible_by_11():
	for num in range(int("1"+"0"*16), int("1"+"0"*16)):
		string = str(num)
		if string == string[::-1]:
			print(num)
