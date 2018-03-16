import os
import math
import numpy as np
import matplotlib.pyplot as plt

# We format the given data from animals.dat
os.chdir( os.path.dirname(os.path.abspath(__file__)) )

# Open data files
pict_f = open("pict.dat", "r")
pict_a = pict_f.read()
pict_f.close()

raw_pict = pict_a.split(",")

pict_def = 32

pict = [ [ int( raw_pict[j + i * pict_def] ) for j in range(0, pict_def) ] for i in range(0, pict_def) ]

# print( pict )

# HERE the data is ready --- 32x32 matrix


