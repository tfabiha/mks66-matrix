
from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 155, 255 ]
matrix = new_matrix()

'''
m2 = [[1, 2, 3],
      [7, 8, 9],
      [14, 15, 16],
      [20, 21, 22]]

ident( matrix )
print_matrix( matrix )
print("")

print_matrix(m2)
print("")
matrix_mult( matrix, m2 )
print_matrix(m2)
print("")
'''


#print(len(matrix[:]))

def drawlines():
    add_edge( matrix, 0, 0, 0, 400, 400, 0 )
    add_edge( matrix, 0, 400, 0, 400, 0, 0 )
    add_edge( matrix, 50, 100, 0, 200, 300, 0 )
    add_edge( matrix, 500, 0, 0, 0, 400, 0 )

#drawlines()
#print_matrix(matrix)


A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
ident( matrix )



print("\nMultiplying Matrix A and Matrix B:")
matrix_mult( A, B )

print("\nMatrix A:")
print_matrix( A )

print("\nMatrix B:")
print_matrix( B )

print("\nMultiplying Matrix B and Matrix A:")
matrix_mult( B, A )

print("\nMatrix A:")
print_matrix( A )

print("\nMatrix B:")
print_matrix( B )
    
print("\nMutiplying Identity Matrix and Matrix A")
matrix_mult( matrix, A)

print("\nMatrix A:")
print_matrix( A )

#something( matrix, 250, 250, 80, 80 )
render( matrix )

draw_lines( matrix, screen, color )
display(screen)

