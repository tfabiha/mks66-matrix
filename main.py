from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

m2 = [[1, 2, 3, 4, 5, 6],
      [7, 8, 9, 10, 12, 13],
      [14, 15, 16, 17, 18, 19],
      [20, 21, 22, 23, 24, 25]]

print_matrix( matrix )
print("")

ident( matrix )
print_matrix( matrix )
print("")

print_matrix(m2)
print("")
matrix_mult( matrix, m2 )
print_matrix(m2)
print("")

print(len(matrix[:]))

draw_lines( matrix, screen, color )
display(screen)
