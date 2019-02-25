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

def something( matrix, org_x, org_y, top_x, top_y):

    counter = 100
    while( counter > 0):#org_x != top_x, org_y != top_y ):

        add_edge( matrix, top_x - top_y + org_y, top_y - top_x + org_x, 0,
                          top_x + top_y - org_y, top_y + top_x - org_x, 0)
        '''
        draw_line(top_x - top_y + org_y, top_y - top_x + org_x,
                  top_x + top_y - org_y, top_y + top_x - org_x,
                  screen, [(top_x + 50) % 255, (top_y + 70) % 255, (top_x + top_y + 20) % 255])
        '''
        
        top_x -= 5
        org_y -= 5
        counter -= 1

def render( matrix ):

    org_x = 100
    org_y = 100

    block = 8
    num_blocks = 26
    
    
    add_edge( matrix,
              org_x, org_y, 0,
              org_x, org_y + block * num_blocks, 0)
    add_edge( matrix,
              org_x, org_y + block * num_blocks, 0,
              org_x + block * num_blocks / 2, org_y + block * num_blocks, 0)
    add_edge( matrix,
              org_x + block * num_blocks / 2, org_y + block * num_blocks, 0,
              org_x + block * num_blocks / 2, org_y + block * num_blocks / 2, 0)
    add_edge( matrix,
              org_x + block * num_blocks / 2, org_y + block * num_blocks / 2, 0,
              org_x + block * num_blocks, org_y + block * num_blocks / 2, 0)
    add_edge( matrix,
              org_x + block * num_blocks, org_y + block * num_blocks / 2, 0,
              org_x + block * num_blocks, org_y, 0)
    add_edge( matrix,
              org_x, org_y, 0,
              org_x + block * num_blocks, org_y, 0)

    # render front big
    num = 0
    
    while num < num_blocks:

        if num < num_blocks / 2:
            add_edge( matrix,
                      org_x, org_y + block * num, 0,
                      org_x + block * num_blocks, org_y + block * num, 0)
        else:
            add_edge( matrix,
                      org_x, org_y + block * num, 0,
                      org_x + block * num_blocks / 2, org_y + block * num, 0)
            
        num += 1

    UL_x = org_x
    UL_y = org_y + block * num_blocks

    UUL_x = UL_x + block * num_blocks / 2
    UUL_y = UL_y + block * num_blocks / 2

    add_edge( matrix,
              UUL_x, UUL_y, 0,
              UUL_x + block * num_blocks, UUL_y, 0)
    
    add_edge( matrix,
              UL_x, UL_y, 0,
              UUL_x, UUL_y, 0)

    add_edge( matrix,
              UL_x + block * num_blocks / 2, UL_y, 0,
              UL_x + block * num_blocks / 2 + block * num_blocks / 4, UL_y + block * num_blocks / 4, 0)

    add_edge( matrix,
              UL_x + block * num_blocks / 2, UL_y, 0,
              UL_x + block * num_blocks / 2 + block * num_blocks / 4, UL_y + block * num_blocks / 4, 0)

    add_edge( matrix,
              UL_x + block * num_blocks / 2 + block * num_blocks / 4, UL_y + block * num_blocks / 4, 0,
              UL_x + block * num_blocks + block * num_blocks / 4, UL_y + block * num_blocks / 4, 0)

    num = 0

    while num < num_blocks:
        num += 1
        
        if num < num_blocks / 2:
            add_edge( matrix,
                      UL_x + block * num, UL_y, 0,
                      UUL_x + block * num, UUL_y, 0)
        else:
            add_edge( matrix,
                      UL_x + block * num + block * num_blocks / 4, UL_y + block * num_blocks / 4, 0,
                      UUL_x + block * num, UUL_y, 0)
            


    SLL_x = org_x + block * num_blocks
    SLL_y = org_y

    SLR_x = SLL_x + block * num_blocks
    SLR_y = SLL_y + block * num_blocks / 2

    add_edge( matrix,
              SLL_x, SLL_y, 0,
              SLL_x + block * num_blocks / 2, SLL_y + block * num_blocks / 2, 0)

    add_edge( matrix,
              SLL_x, SLL_y + block * num_blocks / 2, 0,
              SLL_x + block * num_blocks / 4, SLL_y + block * num_blocks * 3 / 4, 0)
    
    num = 0

    while num < num_blocks:
        num += 1
        
        x = SLL_x + block * num / 2
        y = SLL_y + block * num / 2
        
        if num < num_blocks / 2:
            
            add_edge( matrix,
                      x, y, 0,
                      x, y + block * num_blocks / 2, 0)
        else:
            add_edge( matrix,
                      x, y, 0,
                      x, y + block * num_blocks, 0)
            
        
    
    
    
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
