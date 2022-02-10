
counter = 0
previous_ball_x, previous_ball_y = 0.0, 0.0


def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    '''return "up" or "down", depending on which way the paddle should go to
    align its centre with the centre of the ball, assuming the ball will
    not be moving
    
    Arguments:
    paddle_frect: a rectangle representing the coordinates of the paddle
                  paddle_frect.pos[0], paddle_frect.pos[1] is the top-left
                  corner of the rectangle. 
                  paddle_frect.size[0], paddle_frect.size[1] are the dimensions
                  of the paddle along the x and y axis, respectively
    
    other_paddle_frect:
                  a rectangle representing the opponent paddle. It is formatted
                  in the same way as paddle_frect
    ball_frect:   a rectangle representing the ball. It is formatted in the 
                  same way as paddle_frect
    table_size:   table_size[0], table_size[1] are the dimensions of the table,
                  along the x and the y axis respectively
    
    The coordinates look as follows:
    
     0             x
     |------------->
     |
     |             
     |
 y   v
    '''          
    global counter, previous_ball_x, previous_ball_y

    counter += 1
    
    paddle_x = paddle_frect.pos[0]
    paddle_y = paddle_frect.pos[1] + paddle_frect.size[1] / 2
    ball_x = ball_frect.pos[0]
    ball_y = ball_frect.pos[1] + ball_frect.size[1] / 2
    
    delta_x = ball_x - previous_ball_x
    delta_y = ball_y - previous_ball_y
    
    if delta_x == 0: # Zero Division ...
        delta_x = 1
    
    previous_ball_x = ball_x
    previous_ball_y = ball_y
    
    if paddle_x > table_size[0] / 2:
        target_x = 400
    else:
        target_x = 25

    virtual_y = ( (delta_y / delta_x) * (target_x - ball_x) + ball_y - 7.5 )
 
    if ( virtual_y // 265 ) % 2 == 1: 
        calculated_y = 265 - (virtual_y % 265) + 7.5
    else:
        calculated_y = virtual_y % 265 + 7.5

    if  (paddle_x > table_size[0] / 2 and delta_x > 0) or \
        (paddle_x < table_size[1] / 2 and delta_x < 0):       
        if paddle_y < calculated_y:  # - 20: 
            return "down"
        else: 
            return "up"
    else: 
        # if paddle_y < table_size[1] / 2:
        #     return "down"
        # else:
        #     return "up"
        
        if paddle_y < ball_y:  
            if paddle_y > 170:
                return "up"
            else:
                return "down"
        else:
            if paddle_y < 110:
                return "down"
            else:
                return "up"            
