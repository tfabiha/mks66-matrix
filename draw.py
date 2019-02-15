from display import *
from matrix import *
from math import *

def draw_lines( matrix, screen, color ):
    i = 0
    
    while i < len(matrix[0]) :
        x0 = matrix[0][i]
        y0 = matrix[1][i]
        
        x1 = matrix[0][i+1]
        y1 = matrix[1][i+1]

        draw_line( x0, y0, x1, y1, screen, color )

        #print("drew a line")
        #print("{}".format(i))
        i += 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix[0].append(x)
    matrix[1].append(y)
    matrix[2].append(z)
    matrix[3].append(1)

    #print_matrix(matrix)

def draw_shape( x_org, y_org, x0, y0, sides, matrix ):
    if sides < 3:
        return

    points - [[x0], [y0]]
    
    for i in range(sides - 1):
        x_new = (x0 - x_org) * (math.cos( 2 * 3.14 * i / sides))
        x_new -= (y0 - y_org) * (math.cos( 2 * 3.14 * i / sides))
        y_new = (x0 - x_org) * (math.sin( 2 * 3.14 * i / sides)) + (y0 - y_org) * (math.sin( 2 * 3.14 * i / sides))

            x_new = int(x_new)
            y_new = int(y_new)

            points[0].append(x_new)
            points[1].append(y_new)

     for i in range(sides - 1):
         add_edge( matrix, points[0][i], points[1][i], 0, points[0][i+1], points[1][i+1], 0)

     add_edge( matrix, points[0][0], points[0][1], 0, points[0][-1], points[1][-1], 0)
        
def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
