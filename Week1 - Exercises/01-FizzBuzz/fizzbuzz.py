"""
Create a function fizz_buzz that returns depending on the argument passed:

    Fizz if the number passed is divisible by 3
    Buzz if the number passed is divisible by 5
    FizzBuzz if the number passed is divisible by both 3 and 5

When the number is not divisible by 3 or 5, the number itself should be returned.
"""
def fizz_buzz(num):
	if num % 3 == 0 and num % 5 == 0:
		return "FizzBuzz"
	elif num % 3 == 0:
		return "Fizz"
	elif num % 5 == 0:
		return "Buzz"
	else:
		return num



print fizz_buzz(300)