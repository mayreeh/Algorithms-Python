"""
Sum of Digits

Write a function sum_of_digits(A), that takes in a list of numbers A, and returns the sum of all the digits in the numbers.

e.g. [10, 20, 3, 5, 6, 23] should return 1 + 0 + 2 + 0 + 3 + 5 + 6 + 2 + 3 = 22.
"""



def sum_of_digits(A):
	mylist = []
	total = 0
	for a in A:
		my_list_compression = [c for c in str(a)]
		mylist.extend(my_list_compression)
	for myly in mylist:
		total += int(myly)

	print ' + '.join(mylist),
	print " = %d" %total


#example
sum_of_digits([10, 20, 3, 5, 6, 23])

