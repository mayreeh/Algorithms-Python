"""
Factorial

Write a function factorial(n) that returns a factorial of a number n.
"""
def factorial(num):
	product = 1
	for i in range(1,num):
		product = product * i
		print "%d X " %i,
	product = product * num
	print str(num) + " = " + str(product)




#example
print factorial(5)