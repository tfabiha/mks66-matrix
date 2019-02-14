
from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

m2 = [[1, 2, 3],
      [7, 8, 9],
      [14, 15, 16],
      [20, 21, 22]]

#print_matrix( matrix )
#print("")

#ident( matrix )
#print_matrix( matrix )
#print("")

#print_matrix(m2)
#print("")
#matrix_mult( matrix, m2 )
#print_matrix(m2)
#print("")

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

matrix_mult( A, B )
print_matrix( A )
print_matrix( B )
matrix_mult( B, A )
print_matrix( A )
print_matrix( B )
matrix_mult( matrix, A)
print_matrix( A )

draw_lines( matrix, screen, color )
display(screen)

