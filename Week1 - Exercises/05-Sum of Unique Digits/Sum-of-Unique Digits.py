"""
Sum of Unique Digits

Write a function sum_of_unique_digits(A), that takes in a list of numbers A, and returns the sum of all the unique digits in the numbers.

e.g. [10, 20, 3, 5, 6, 23] should return 1 + 0 + 2 + 3 + 5 + 6 = 17.
"""

def sum_of_unique_digits(A):
	mylists = []
	sum_of_numbers = 0
	for a in A:
		split_number_list = [c for c in str(a)]
		mylists.extend(split_number_list)

	for unique_digit in set(mylists):
		sum_of_numbers +=  int(unique_digit)
		print "%s +" % unique_digit,
	print " 0 = %d " %sum_of_numbers



def sum_of_unique_digits(A):
	mylists = []
	sum_of_numbers = 0
	for a in A:
		split_number_list = [c for c in str(a)]
		mylists.extend(split_number_list)
	for unique_digit in set(mylists):
		sum_of_numbers +=  int(unique_digit)
	print ' + '.join(set(mylists)),
	print " = %d" %sum_of_numbers




#example
sum_of_unique_digits([10, 20, 3, 5, 6, 23])