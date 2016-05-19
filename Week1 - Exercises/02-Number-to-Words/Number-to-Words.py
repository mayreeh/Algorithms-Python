"""
Number to Words

Create a function num_to_word that outputs the digits of the number passed in words.

e.g num_to_word(438483478) should output four three eight four eight three four seven eight
"""
def num_to_word(num):
	numbers = {
	'zero' : '0' , 'one':'1','two':'2','three':'3' , 'four':'4' , 'five':'5' , 'six': '6' , 'seven':'7' , 'eight':'8' , 'nine':'9' 
	}
	num = str(num)
	mylists = [c for c in num] #split the number as single elements
	for mylist in mylists:
		for key , value in numbers.items():
			if mylist == value:
				print key,


#example
num_to_word(438483478)