import numpy as np

# Count how many bits differ between pattern x and y
def count_errors(x, y):
	count = 0
	for i in range(0, len(x)):
		if (x[i] != y[i]):
			count = count + 1
	return(count)

# Set any value in x >= 0 to 1 and any value < 0 to -1
def sgn(x):
	for i in range(0, len(x)):
		if (x[i] >= 0):
			x[i] = 1
		else:
			x[i] = -1
	return(x)

# Generate all possible input patterns of the chosen size
def get_all_possible_inputs(input, sub_part, size, depth):
	if(size == depth + 1):
		input.append(sub_part + [1])
		input.append(sub_part + [-1])
		return
	get_all_possible_inputs(input, sub_part + [1], size, depth + 1)
	get_all_possible_inputs(input, sub_part + [-1], size, depth + 1)

# Remove duplicate patterns
def remove_duplicates(input):
	for i in range(0, len(input)):
		for j in range (i + 1, len(input)):
			if(count_errors(input[i], input[j]) == 0):
				input = np.delete(input, j, 0)
				input = remove_duplicates(input)
				return input
	return input

# Memory pattern initiation
memory_patterns = []
memory_patterns.append([-1, -1, 1, -1, 1, -1, -1, 1])            #x1
memory_patterns.append([-1, -1, -1, -1, -1, 1, -1, -1])          #x2
memory_patterns.append([-1, 1, 1, -1, -1, 1, -1, 1])             #x3
memory_patterns = np.array(memory_patterns)
print("TRAINING PATTERNS")
print(memory_patterns)
print("")

# Weight initiation
weights = np.matmul(memory_patterns.T, memory_patterns)
# Remove self connections
for i in range (0, len(weights)):
	weights[i][i] = 0
print("WEIGHTS")
print(weights)
print("")

# Distorted pattern initation
x1d = [1, -1, 1, -1, 1, -1, -1, 1]
x2d = [1, 1, -1, -1, -1, 1, -1, -1]
x3d = [1, 1, 1, -1, 1, 1, -1, 1]

# Apply update rule
input_pattern = x2d
print("ORIGINAL INPUT PATTERN")
print(input_pattern)
iterations = 0
while (iterations < 4):
	input_pattern = sgn(np.dot(weights, input_pattern))
	iterations = iterations + 1
	print("")
	print("Iterations: ", iterations)
	print("CURRENT PATTERN")
	print(input_pattern)
	print("DIFFERENCE TO ORIGINAL PATTERNS")
	print(count_errors(input_pattern, memory_patterns[0]))
	print(count_errors(input_pattern, memory_patterns[1]))
	print(count_errors(input_pattern, memory_patterns[2]))


	
