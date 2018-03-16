import os
import math
import numpy as np
import matplotlib.pyplot as plt

#Some usefull functions

# Set any value in x >= 0 to 1 and any value < 0 to -1
def sgn(x):
	for i in range(0, len(x)):
		if (x[i] >= 0):
			x[i] = 1
		else:
			x[i] = -1
	return(x)

# To update the weights
def weights_update(weights, patterns ) :
	for i in range( 0, len( weights )) :
		for j in range( i, len( weights )) :
			result = 0
			# We take the first pattern dimension, in the begun case, it was 32 lines (in 2D pict).
			dim = len( patterns[0] )
			for k in range( 0, len( patterns )):
				result += patterns[k][i // dim][ i % dim ] * patterns[k][j // dim][ j % dim ]
			weights[i][j] = ( 1 / len( weights ) ) * result

# To generate the next pattern from the weights
def patterns_update( weights, patterns ):
	for i in range( 0, len( patterns ) ):
		save_pattern = patterns[i]
		
	

# We format the given data from animals.dat
os.chdir( os.path.dirname(os.path.abspath(__file__)) )

# Open data files
pict_f = open("pict.dat", "r")
pict_a = pict_f.read()
pict_f.close()

raw_pict = pict_a.split(",")

# Some Constants
pict_def = 32
number_patterns = 9
number_nodes = 1024

pict = [ [ [ int( raw_pict[j + i * pict_def + k * number_patterns] ) for j in range(0, pict_def) ] for i in range(0, pict_def) ] for k in range(0, number_patterns) ]

# print( pict )
plt.imshow(pict[3])

# HERE the data is ready --- 9 patterns of 32x32 pict matrix
#INIT the weights matrix for N nodes, so we have N^2 weights
weights = np.zeros( (number_nodes, number_nodes) , dtype = int)

#We udpate the weights with the inital patterns
weights_update(weights)

# As the matrix is symetric with 0 in the diagonal, we will only fill one triangle



plt.show()
