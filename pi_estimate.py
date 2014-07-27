from random import random
import sys

def pi_estimate(number_iterations):
	count = 0

	for i in range(number_iterations):
		x = random()
		y = random()

		if x**2 + y**2 < 1:
			count += 1

	return 4 * float(count) / float(number_iterations)



print pi_estimate(int(sys.argv[1]))