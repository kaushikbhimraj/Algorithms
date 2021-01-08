
"""
Fizz Buzz:

Write a program that outputs the string representation of numbers from 1 to n. 
But for multiples of three it should output "Fizz" instead to the number and for 
the multiples of five output "Buzz". For numbers which are multiples of both three 
and five output "FizzBuzz".

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


class fizzBuzz:


	def iterative(self, n):
		for i in range(1, n+1):
			if i%3==0 and i%5==0:
				print("FizzBuzz")
			else:
				if i%3==0:
					print("Fizz")
				elif i%5==0:
					print("Buzz")
				else:
					print(i)


	def recursive(self, i, n):
		if i > n:
			return

		if i%3==0 and i%5==0:
			print("FizzBuzz")
		else:
			if i%3==0:
				print("Fizz")
			elif i%5==0:
				print("Buzz")
			else:
				print(i)
		self.recursive(i+1, n)


# fizzBuzz().iterative(15)
# fizzBuzz().recursive(1, 15)
