# -*- coding: utf-8 -*-
import os
import math
import numpy as np
import matplotlib.pyplot as plt

#Some usefull functions

# Set any value in x >= 0 to 1 and any value < 0 to -1
def sgn(x):
	if (x >= 0):
		x = 1
	else:
		x = -1
	return(x)

# To update the weights
# As the matrix is symetric with 0 in the diagonal, we will only fill one triangle
def weights_update(weights, patterns) :
	for i in range( 0, len( weights )) :
		for j in range( i+1 , len( weights )) :
			result = 0
			# We take the first pattern dimension, in the begun case, it was 32 lines (in 2D pict).
			dim = len( patterns[0] )
			for k in range( 0, len( patterns )):
				result += patterns[k][i // dim][ i % dim ] * patterns[k][j // dim][ j % dim ]
			weights[i][j] = ( 1 / len( weights ) ) * result
			# The matrix is symetric, we update also the other triangle
			weights[j][i] = ( 1 / len( weights ) ) * result

# To generate the next pattern from the weights
def patterns_update( weights, patterns ):
	for i in range( 0, len( patterns ) ):
		save_pattern = patterns[i]
		result = 0
		dim = len( patterns[0] )
		for l in range( 0, len( weights )) :
			for m in range( 0, len( weights )) :
				result += weights[l][m] * save_pattern[ m // dim][ m % dim ]
			patterns[i][ l // dim][ l % dim ] = sgn( result )
	

# We format the given data from animals.dat
os.chdir( os.path.dirname(os.path.abspath(__file__)) )

# Open data files
pict_f = open("pict.dat", "r")
pict_a = pict_f.read()
pict_f.close()

raw_pict = pict_a.split(",")

# Some Constants
epochs = 10
pict_def = 32
number_patterns = 9
number_nodes = 1024

pict = [ [ [ int( raw_pict[j + i * pict_def + k * number_patterns] ) for j in range(0, pict_def) ] for i in range(0, pict_def) ] for k in range(0, number_patterns) ]

# print( pict )
# plt.imshow(pict[3])



# HERE the data is ready --- 9 patterns of 32x32 pict matrix
# INIT the weights matrix for N nodes, so we have N^2 weights
weights = np.zeros( (number_nodes, number_nodes) , dtype = int)

save_pict = pict


# We udpate the weights with the inital patterns
weights_update(weights, pict)


# LEARNING
for e in range( 0, epochs) :
	patterns_update(weights, pict)
	weights_update(weights, pict)
	

# TESTING
# Here we verify if the patterns are stable :
if np.array_equal(save_pict[:3], patterns_update(weights, save_pict[:3])) == True :  # test if same shape, same elements values, only for the 3 first
	print( "The patterns are stable !" )
else :
	print( "UNSTABLE" )

plt.figure()

plt.imshow(save_pict[0])
plt.imshow(pict[0])

plt.imshow(save_pict[1])
plt.imshow(pict[1])

print( pict[0] )
print(save_pict[0])

plt.show()


