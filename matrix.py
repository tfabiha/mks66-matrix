"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for row in matrix:
        ln = ""
        for column in row:
            ln += "{}\t".format(column)
        print(ln)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for r in range( len(matrix) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[r][c] = 1
            else:
                matrix[r][c] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for r in range( len(m1) ):
        for c in range( len(m2[0]) ):
            copy = [ item[c] for item in m2 ]

            #print(copy)
            m2[r][c] = mult_helper(m1[r], copy)

def mult_helper(r1, r2):
    summ = 0
    for i in range( len(r1) ):
        summ += r1[i] * r2[i]
    return summ

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
