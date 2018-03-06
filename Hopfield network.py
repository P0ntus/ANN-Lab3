import numpy as np

def count_errors(x, y):
	count = 0
	for i in range(0, len(x)):
		if (x[i] != y[i]):
			count = count + 1
	return(count)

def sgn(x):
	for i in range(0, len(x)):
		if (x[i] >= 0):
			x[i] = 1
		else:
			x[i] = -1
	return(x)

nodes = []
input_patterns = []
weights = []
output_pattern = []

# Input pattern initiation
input_patterns.append([-1, -1, 1, -1, 1, -1, -1, 1])            #x1
input_patterns.append([-1, -1, -1, -1, -1, 1, -1, -1])          #x2
input_patterns.append([-1, 1, 1, -1, -1, 1, -1, 1])             #x3

# Distorted
distorted_input_patterns = []
distorted_input_patterns.append([1, -1, 1, -1, 1, -1, -1, 1])   #x1d
distorted_input_patterns.append([1, 1, -1, -1, -1, 1, -1, -1])  #x2d
distorted_input_patterns.append([1, 1, 1, -1, 1, 1, -1, 1])     #x3d

input_patterns = np.array(input_patterns)
original_input = np.copy(input_patterns)

for runs in range (0, 5):
	print("")
	print("INPUT PATTERNS")
	print(input_patterns)	
	print("")
	print("WEIGHTS")
	weights = np.matmul(input_patterns.T, input_patterns)
	print(weights)

	# Check if the network can recall the patterns
	print("")
	for i in range(1, len(input_patterns)):
		output_pattern = np.dot(weights, input_patterns[i])
		#output_pattern = np.dot(weights, distorted_input_patterns[i])
		input_patterns[i] = sgn(output_pattern)
		print("Bit error: ", count_errors(input_patterns[i], original_input[i]))
	
