"""
Bit wise operation play ground.
"""


x = 16

# and will simply tell you if the number is odd or even by return a 1 for odd and 0 for even.
# 4&1 = 0 and 5&1 = 1
n = 0
while (x>>n > 0):
	print((x>>n)&1, (x>>n)|1)
	n += 1

print("---------------------------")

# or will convert an even to odd. 
# 5|1 = 5 and 4|1 = 5
n = 0
while (x<<n < 500):
	# print((x>>n)&1)
	print(x<<n, (x<<n)|1)
	n += 1

print("---------------------------")

# xor has the power to convert an even to odd and odd to even. 
# example 4^1 = 5 and 5^1 = 4
n = 0
while (x>>n > 0):
	print((x>>n)^1)
	n += 1

	