import numpy as np

# THIS FILE PERFORMS ALL THE POSSIABLE CUBE MOVEMENTS
# IT ALSO HAS THE movements ARRAY THAT STORES A STRING VALUE BASED ON THE FUNCTION THAT WAS RAN
def Fclock(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_up = [up_face[3][0], up_face[3][1], up_face[3][2], up_face[3][3]]
    temp_right = [right_face[0][0], right_face[1][0], right_face[2][0], right_face[3][0]]
    temp_down = [down_face[0][0], down_face[0][1], down_face[0][2], down_face[0][3]]
    temp_left = [left_face[0][3], left_face[1][3], left_face[2][3], left_face[3][3]]
    
    up_face[3][0], up_face[3][1], up_face[3][2], up_face[3][3] = temp_left[3], temp_left[2], temp_left[1], temp_left[0]
    right_face[0][0], right_face[1][0], right_face[2][0], right_face[3][0] = temp_up[0], temp_up[1], temp_up[2], temp_up[3]
    down_face[0][0], down_face[0][1], down_face[0][2], down_face[0][3] = temp_right[3], temp_right[2], temp_right[1], temp_right[0]
    left_face[0][3], left_face[1][3], left_face[2][3], left_face[3][3] = temp_down[0], temp_down[1], temp_down[2], temp_down[3]

    front_face = np.rot90(front_face, -1, axes=(0,1))
    return up_face, down_face, left_face, front_face, right_face, back_face
 
def Fanti(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_up = [up_face[3][0], up_face[3][1], up_face[3][2], up_face[3][3]]
    temp_right = [right_face[0][0], right_face[1][0], right_face[2][0], right_face[3][0]]
    temp_down = [down_face[0][0], down_face[0][1], down_face[0][2], down_face[0][3]]
    temp_left = [left_face[0][3], left_face[1][3], left_face[2][3], left_face[3][3]]
    
    up_face[3][0], up_face[3][1], up_face[3][2], up_face[3][3] = temp_right[0], temp_right[1], temp_right[2], temp_right[3]
    right_face[0][0], right_face[1][0], right_face[2][0], right_face[3][0] = temp_down[3], temp_down[2], temp_down[1], temp_down[0]
    down_face[0][0], down_face[0][1], down_face[0][2], down_face[0][3] = temp_left[0], temp_left[1], temp_left[2], temp_left[3]
    left_face[0][3], left_face[1][3], left_face[2][3], left_face[3][3] = temp_up[3], temp_up[2], temp_up[1], temp_up[0]

    front_face = np.rot90(front_face, 1, axes=(0,1))
    return up_face, down_face, left_face, front_face, right_face, back_face

 
def Bclock(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_up = [up_face[0][0], up_face[0][1], up_face[0][2], up_face[0][3]]
    temp_right = [right_face[0][3], right_face[1][3], right_face[2][3], right_face[3][3]]
    temp_down = [down_face[3][0], down_face[3][1], down_face[3][2], down_face[3][3]]
    temp_left = [left_face[0][0], left_face[1][0], left_face[2][0], left_face[3][0]]

    up_face[0][0], up_face[0][1], up_face[0][2], up_face[0][3] = temp_right[0], temp_right[1], temp_right[2], temp_right[3]
    left_face[0][0], left_face[1][0], left_face[2][0], left_face[3][0] = temp_up[3], temp_up[2], temp_up[1], temp_up[0]
    down_face[3][0], down_face[3][1], down_face[3][2], down_face[3][3] = temp_left[0], temp_left[1], temp_left[2], temp_left[3]
    right_face[0][3], right_face[1][3], right_face[2][3], right_face[3][3] = temp_down[3], temp_down[2], temp_down[1], temp_down[0]

    back_face = np.rot90(back_face, -1, axes=(0,1))
    return up_face, down_face, left_face, front_face, right_face, back_face

 
def Banti(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_up = [up_face[0][0], up_face[0][1], up_face[0][2], up_face[0][3]]
    temp_right = [right_face[0][3], right_face[1][3], right_face[2][3], right_face[3][3]]
    temp_down = [down_face[3][0], down_face[3][1], down_face[3][2], down_face[3][3]]
    temp_left = [left_face[0][0], left_face[1][0], left_face[2][0], left_face[3][0]]

    up_face[0][0], up_face[0][1], up_face[0][2], up_face[0][3] = temp_left[3], temp_left[2], temp_left[1], temp_left[0]
    right_face[0][3], right_face[1][3], right_face[2][3], right_face[3][3] = temp_up[0], temp_up[1], temp_up[2], temp_up[3]
    down_face[3][0], down_face[3][1], down_face[3][2], down_face[3][3] = temp_right[3], temp_right[2], temp_right[1], temp_right[0]
    left_face[0][0], left_face[1][0], left_face[2][0], left_face[3][0] = temp_down[0], temp_down[1], temp_down[2], temp_down[3]

    back_face = np.rot90(back_face, 1, axes=(0,1))
    return up_face, down_face, left_face, front_face, right_face, back_face

 
def Uclock (up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[0][0], front_face[0][1], front_face[0][2], front_face[0][3]]
    temp_left = [left_face[0][0], left_face[0][1], left_face[0][2], left_face[0][3]]
    temp_back = [back_face[0][0], back_face[0][1], back_face[0][2], back_face[0][3]]
    temp_right = [right_face[0][0], right_face[0][1], right_face[0][2], right_face[0][3]]

    front_face[0][0], front_face[0][1], front_face[0][2], front_face[0][3] = temp_right[0], temp_right[1], temp_right[2], temp_right[3]
    left_face[0][0], left_face[0][1], left_face[0][2], left_face[0][3] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]
    back_face[0][0], back_face[0][1], back_face[0][2], back_face[0][3] = temp_left[0], temp_left[1], temp_left[2], temp_left[3]
    right_face[0][0], right_face[0][1], right_face[0][2], right_face[0][3] = temp_back[0], temp_back[1], temp_back[2], temp_back[3]

    up_face = np.rot90(up_face, -1, axes=(0,1))
    return up_face, down_face, left_face, front_face, right_face, back_face

 
def Uanti (up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[0][0], front_face[0][1], front_face[0][2], front_face[0][3]]
    temp_left = [left_face[0][0], left_face[0][1], left_face[0][2], left_face[0][3]]
    temp_back = [back_face[0][0], back_face[0][1], back_face[0][2], back_face[0][3]]
    temp_right = [right_face[0][0], right_face[0][1], right_face[0][2], right_face[0][3]]

    front_face[0][0], front_face[0][1], front_face[0][2], front_face[0][3] = temp_left[0], temp_left[1], temp_left[2], temp_left[3]
    left_face[0][0], left_face[0][1], left_face[0][2], left_face[0][3] = temp_back[0], temp_back[1], temp_back[2], temp_back[3]
    back_face[0][0], back_face[0][1], back_face[0][2], back_face[0][3] = temp_right[0], temp_right[1], temp_right[2], temp_right[3]
    right_face[0][0], right_face[0][1], right_face[0][2], right_face[0][3] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]

    up_face = np.rot90(up_face, 1, axes=(0,1))
    return up_face, down_face, left_face, front_face, right_face, back_face

 
def Dclock (up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[3][0], front_face[3][1], front_face[3][2], front_face[3][3]]
    temp_left = [left_face[3][0], left_face[3][1], left_face[3][2], left_face[3][3]]
    temp_back = [back_face[3][0], back_face[3][1], back_face[3][2], back_face[3][3]]
    temp_right = [right_face[3][0], right_face[3][1], right_face[3][2], right_face[3][3]]

    front_face[3][0], front_face[3][1], front_face[3][2], front_face[3][3] = temp_left[0], temp_left[1], temp_left[2], temp_left[3]
    right_face[3][0], right_face[3][1], right_face[3][2], right_face[3][3] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]
    back_face[3][0], back_face[3][1], back_face[3][2], back_face[3][3] = temp_right[0], temp_right[1], temp_right[2], temp_right[3]
    left_face[3][0], left_face[3][1], left_face[3][2], left_face[3][3] = temp_back[0], temp_back[1], temp_back[2], temp_back[3]

    down_face = np.rot90(down_face, -1, axes=(0,1))
    return up_face, down_face, left_face, front_face, right_face, back_face

 
def Danti (up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[3][0], front_face[3][1], front_face[3][2], front_face[3][3]]
    temp_left = [left_face[3][0], left_face[3][1], left_face[3][2], left_face[3][3]]
    temp_back = [back_face[3][0], back_face[3][1], back_face[3][2], back_face[3][3]]
    temp_right = [right_face[3][0], right_face[3][1], right_face[3][2], right_face[3][3]]

    front_face[3][0], front_face[3][1], front_face[3][2], front_face[3][3] = temp_right[0], temp_right[1], temp_right[2], temp_right[3]
    right_face[3][0], right_face[3][1], right_face[3][2], right_face[3][3] = temp_back[0], temp_back[1], temp_back[2], temp_back[3]
    back_face[3][0], back_face[3][1], back_face[3][2], back_face[3][3] = temp_left[0], temp_left[1], temp_left[2], temp_left[3]
    left_face[3][0], left_face[3][1], left_face[3][2], left_face[3][3] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]

    down_face = np.rot90(down_face, 1, axes=(0,1))
    return up_face, down_face, left_face, front_face, right_face, back_face

 
def Rclock(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[0][3], front_face[1][3], front_face[2][3], front_face[3][3]]
    temp_up = [up_face[0][3], up_face[1][3], up_face[2][3], up_face[3][3]]
    temp_back = [back_face[0][0], back_face[1][0], back_face[2][0], back_face[3][0]]
    temp_down = [down_face[0][3], down_face[1][3], down_face[2][3], down_face[3][3]]

    front_face[0][3], front_face[1][3], front_face[2][3], front_face[3][3] = temp_down[0], temp_down[1],  temp_down[2],  temp_down[3]
    up_face[0][3], up_face[1][3], up_face[2][3], up_face[3][3] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]
    back_face[0][0], back_face[1][0], back_face[2][0], back_face[3][0] = temp_up[3], temp_up[2], temp_up[1], temp_up[0]
    down_face[0][3], down_face[1][3], down_face[2][3], down_face[3][3] = temp_back[3], temp_back[2], temp_back[1], temp_back[0]

    right_face = np.rot90(right_face, -1, axes=(0,1))
    return up_face, down_face, left_face, front_face, right_face, back_face

 
def Ranti(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[0][3], front_face[1][3], front_face[2][3], front_face[3][3]]
    temp_up = [up_face[0][3], up_face[1][3], up_face[2][3], up_face[3][3]]
    temp_back = [back_face[0][0], back_face[1][0], back_face[2][0], back_face[3][0]]
    temp_down = [down_face[0][3], down_face[1][3], down_face[2][3], down_face[3][3]]

    front_face[0][3], front_face[1][3], front_face[2][3], front_face[3][3] = temp_up[0], temp_up[1], temp_up[2], temp_up[3]
    up_face[0][3], up_face[1][3], up_face[2][3], up_face[3][3] = temp_back[3], temp_back[2], temp_back[1], temp_back[0]
    back_face[0][0], back_face[1][0], back_face[2][0], back_face[3][0] = temp_down[3], temp_down[2],  temp_down[1], temp_down[0]
    down_face[0][3], down_face[1][3], down_face[2][3], down_face[3][3] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]

    right_face = np.rot90(right_face, 1, axes=(0,1))
    return up_face, down_face, left_face, front_face, right_face, back_face

 
def Lclock(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[0][0], front_face[1][0], front_face[2][0], front_face[3][0]]
    temp_up = [up_face[0][0], up_face[1][0], up_face[2][0], up_face[3][0]]
    temp_back = [back_face[0][3], back_face[1][3], back_face[2][3], back_face[3][3]]
    temp_down = [down_face[0][0], down_face[1][0], down_face[2][0], down_face[3][0]]

    front_face[0][0], front_face[1][0], front_face[2][0], front_face[3][0] = temp_up[0], temp_up[1], temp_up[2], temp_up[3]
    up_face[0][0], up_face[1][0], up_face[2][0], up_face[3][0] = temp_back[3], temp_back[2], temp_back[1], temp_back[0]
    back_face[0][3], back_face[1][3], back_face[2][3], back_face[3][3] = temp_down[3], temp_down[2], temp_down[1], temp_down[0]
    down_face[0][0], down_face[1][0], down_face[2][0], down_face[3][0] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]

    left_face = np.rot90(left_face, -1, axes=(0,1))
    return up_face, down_face, left_face, front_face, right_face, back_face

  
def Lanti(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[0][0], front_face[1][0], front_face[2][0], front_face[3][0]]
    temp_up = [up_face[0][0], up_face[1][0], up_face[2][0], up_face[3][0]]
    temp_back = [back_face[0][3], back_face[1][3], back_face[2][3], back_face[3][3]]
    temp_down = [down_face[0][0], down_face[1][0], down_face[2][0], down_face[3][0]]

    front_face[0][0], front_face[1][0], front_face[2][0], front_face[3][0] = temp_down[0], temp_down[1], temp_down[2], temp_down[3]
    up_face[0][0], up_face[1][0], up_face[2][0], up_face[3][0] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]
    back_face[0][3], back_face[1][3], back_face[2][3], back_face[3][3] = temp_up[3], temp_up[2], temp_up[1], temp_up[0]
    down_face[0][0], down_face[1][0], down_face[2][0], down_face[3][0] = temp_back[3], temp_back[2], temp_back[1], temp_back[0]
    
    left_face = np.rot90(left_face, 1, axes=(0,1))
    return up_face, down_face, left_face, front_face, right_face, back_face

 
def innerfclock(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_up = [up_face[2][0], up_face[2][1], up_face[2][2], up_face[2][3]]
    temp_right = [right_face[0][1], right_face[1][1], right_face[2][1], right_face[3][1]]
    temp_down = [down_face[1][0], down_face[1][1], down_face[1][2], down_face[1][3]]
    temp_left = [left_face[0][2], left_face[1][2], left_face[2][2], left_face[3][2]]

    up_face[2][0], up_face[2][1], up_face[2][2], up_face[2][3] = temp_left[3], temp_left[2], temp_left[1], temp_left[0]
    right_face[0][1], right_face[1][1], right_face[2][1], right_face[3][1] = temp_up[0], temp_up[1], temp_up[2], temp_up[3]
    down_face[1][0], down_face[1][1], down_face[1][2], down_face[1][3] = temp_right[3], temp_right[2], temp_right[1], temp_right[0]
    left_face[0][2], left_face[1][2], left_face[2][2], left_face[3][2] = temp_down[0], temp_down[1], temp_down[2], temp_down[3] 


    return up_face, down_face, left_face, front_face, right_face, back_face

 
def innerfanti(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_up = [up_face[2][0], up_face[2][1], up_face[2][2], up_face[2][3]]
    temp_right = [right_face[0][1], right_face[1][1], right_face[2][1], right_face[3][1]]
    temp_down = [down_face[1][0], down_face[1][1], down_face[1][2], down_face[1][3]]
    temp_left = [left_face[0][2], left_face[1][2], left_face[2][2], left_face[3][2]]

    up_face[2][0], up_face[2][1], up_face[2][2], up_face[2][3] = temp_right[0], temp_right[1], temp_right[2], temp_right[3]
    right_face[0][1], right_face[1][1], right_face[2][1], right_face[3][1] = temp_down[3], temp_down[2], temp_down[1], temp_down[0]
    down_face[1][0], down_face[1][1], down_face[1][2], down_face[1][3] = temp_left[0], temp_left[1], temp_left[2], temp_left[3]
    left_face[0][2], left_face[1][2], left_face[2][2], left_face[3][2] = temp_up[3], temp_up[2], temp_up[1], temp_up[0]


    return up_face, down_face, left_face, front_face, right_face, back_face

 
def innerbclock(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_up = [up_face[1][0], up_face[1][1], up_face[1][2], up_face[1][3]]
    temp_right = [right_face[0][2], right_face[1][2], right_face[2][2], right_face[3][2]]
    temp_down = [down_face[2][0], down_face[2][1], down_face[2][2], down_face[2][3]]
    temp_left = [left_face[0][1], left_face[1][1], left_face[2][1], left_face[3][1]]

    up_face[1][0], up_face[1][1], up_face[1][2], up_face[1][3] = temp_right[0], temp_right[1], temp_right[2], temp_right[3]
    right_face[0][2], right_face[1][2], right_face[2][2], right_face[3][2] = temp_down[3], temp_down[2], temp_down[1], temp_down[0]
    down_face[2][0], down_face[2][1], down_face[2][2], down_face[2][3] = temp_left[0], temp_left[1], temp_left[2], temp_left[3]
    left_face[0][1], left_face[1][1], left_face[2][1], left_face[3][1] = temp_up[3], temp_up[2], temp_up[1], temp_up[0]

    return up_face, down_face, left_face, front_face, right_face, back_face

 
def innerbanti(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_up = [up_face[1][0], up_face[1][1], up_face[1][2], up_face[1][3]]
    temp_right = [right_face[0][2], right_face[1][2], right_face[2][2], right_face[3][2]]
    temp_down = [down_face[2][0], down_face[2][1], down_face[2][2], down_face[2][3]]
    temp_left = [left_face[0][1], left_face[1][1], left_face[2][1], left_face[3][1]]

    up_face[1][0], up_face[1][1], up_face[1][2], up_face[1][3] = temp_left[3], temp_left[2], temp_left[1], temp_left[0]
    right_face[0][2], right_face[1][2], right_face[2][2], right_face[3][2] = temp_up[0], temp_up[1], temp_up[2], temp_up[3]
    down_face[2][0], down_face[2][1], down_face[2][2], down_face[2][3] = temp_right[3], temp_right[2], temp_right[1], temp_right[0]
    left_face[0][1], left_face[1][1], left_face[2][1], left_face[3][1] = temp_down[0], temp_down[1], temp_down[2], temp_down[3]

    return up_face, down_face, left_face, front_face, right_face, back_face

 
def inneruclock(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[1][0], front_face[1][1], front_face[1][2], front_face[1][3]]
    temp_left = [left_face[1][0], left_face[1][1], left_face[1][2], left_face[1][3]]
    temp_back = [back_face[1][0], back_face[1][1], back_face[1][2], back_face[1][3]]
    temp_right = [right_face[1][0], right_face[1][1], right_face[1][2], right_face[1][3]]

    front_face[1][0], front_face[1][1], front_face[1][2], front_face[1][3] = temp_right[0], temp_right[1], temp_right[2], temp_right[3]
    left_face[1][0], left_face[1][1], left_face[1][2], left_face[1][3] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]
    back_face[1][0], back_face[1][1], back_face[1][2], back_face[1][3] = temp_left[0], temp_left[1], temp_left[2], temp_left[3]
    right_face[1][0], right_face[1][1], right_face[1][2], right_face[1][3] = temp_back[0], temp_back[1], temp_back[2], temp_back[3]

    return up_face, down_face, left_face, front_face, right_face, back_face

 
def inneruanti(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[1][0], front_face[1][1], front_face[1][2], front_face[1][3]]
    temp_left = [left_face[1][0], left_face[1][1], left_face[1][2], left_face[1][3]]
    temp_back = [back_face[1][0], back_face[1][1], back_face[1][2], back_face[1][3]]
    temp_right = [right_face[1][0], right_face[1][1], right_face[1][2], right_face[1][3]]

    front_face[1][0], front_face[1][1], front_face[1][2], front_face[1][3] = temp_left[0], temp_left[1], temp_left[2], temp_left[3]
    left_face[1][0], left_face[1][1], left_face[1][2], left_face[1][3] = temp_back[0], temp_back[1], temp_back[2], temp_back[3]
    back_face[1][0], back_face[1][1], back_face[1][2], back_face[1][3] = temp_right[0], temp_right[1], temp_right[2], temp_right[3]
    right_face[1][0], right_face[1][1], right_face[1][2], right_face[1][3] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]

    return up_face, down_face, left_face, front_face, right_face, back_face

 
def innerdclock(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[2][0], front_face[2][1], front_face[2][2], front_face[2][3]]
    temp_left = [left_face[2][0], left_face[2][1], left_face[2][2], left_face[2][3]]
    temp_back = [back_face[2][0], back_face[2][1], back_face[2][2], back_face[2][3]]
    temp_right = [right_face[2][0], right_face[2][1], right_face[2][2], right_face[2][3]]

    front_face[2][0], front_face[2][1], front_face[2][2], front_face[2][3] = temp_right[0], temp_right[1], temp_right[2], temp_right[3]
    left_face[2][0], left_face[2][1], left_face[2][2], left_face[2][3] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]
    back_face[2][0], back_face[2][1], back_face[2][2], back_face[2][3] = temp_left[0], temp_left[1], temp_left[2], temp_left[3]
    right_face[2][0], right_face[2][1], right_face[2][2], right_face[2][3] = temp_back[0], temp_back[1], temp_back[2], temp_back[3]

    return up_face, down_face, left_face, front_face, right_face, back_face

 
def innerdanti(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[2][0], front_face[2][1], front_face[2][2], front_face[2][3]]
    temp_left = [left_face[2][0], left_face[2][1], left_face[2][2], left_face[2][3]]
    temp_back = [back_face[2][0], back_face[2][1], back_face[2][2], back_face[2][3]]
    temp_right = [right_face[2][0], right_face[2][1], right_face[2][2], right_face[2][3]]

    front_face[2][0], front_face[2][1], front_face[2][2], front_face[2][3] = temp_left[0], temp_left[1], temp_left[2], temp_left[3]
    left_face[2][0], left_face[2][1], left_face[2][2], left_face[2][3] = temp_back[0], temp_back[1], temp_back[2], temp_back[3]
    back_face[2][0], back_face[2][1], back_face[2][2], back_face[2][3] = temp_right[0], temp_right[1], temp_right[2], temp_right[3]
    right_face[2][0], right_face[2][1], right_face[2][2], right_face[2][3] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]

    return up_face, down_face, left_face, front_face, right_face, back_face

 
def innerrclock(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[0][2], front_face[1][2], front_face[2][2], front_face[3][2]]
    temp_up = [up_face[0][2], up_face[1][2], up_face[2][2], up_face[3][2]]
    temp_back = [back_face[0][1], back_face[1][1], back_face[2][1], back_face[3][1]]
    temp_down = [down_face[0][2], down_face[1][2], down_face[2][2], down_face[3][2]]

    front_face[0][2], front_face[1][2], front_face[2][2], front_face[3][2] = temp_down[0], temp_down[1], temp_down[2], temp_down[3]
    up_face[0][2], up_face[1][2], up_face[2][2], up_face[3][2] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]
    back_face[0][1], back_face[1][1], back_face[2][1], back_face[3][1] = temp_up[3], temp_up[2], temp_up[1], temp_up[0]
    down_face[0][2], down_face[1][2], down_face[2][2], down_face[3][2] = temp_back[3], temp_back[2], temp_back[1], temp_back[0]

    return up_face, down_face, left_face, front_face, right_face, back_face

 
def innerranti(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[0][2], front_face[1][2], front_face[2][2], front_face[3][2]]
    temp_up = [up_face[0][2], up_face[1][2], up_face[2][2], up_face[3][2]]
    temp_back = [back_face[0][1], back_face[1][1], back_face[2][1], back_face[3][1]]
    temp_down = [down_face[0][2], down_face[1][2], down_face[2][2], down_face[3][2]]

    front_face[0][2], front_face[1][2], front_face[2][2], front_face[3][2] = temp_up[0], temp_up[1], temp_up[2], temp_up[3]
    up_face[0][2], up_face[1][2], up_face[2][2], up_face[3][2] = temp_back[3], temp_back[2], temp_back[1], temp_back[0]
    back_face[0][1], back_face[1][1], back_face[2][1], back_face[3][1] = temp_down[3], temp_down[2], temp_down[1], temp_down[0]
    down_face[0][2], down_face[1][2], down_face[2][2], down_face[3][2] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]

    return up_face, down_face, left_face, front_face, right_face, back_face

 
def innerlclock(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[0][1], front_face[1][1], front_face[2][1], front_face[3][1]]
    temp_up = [up_face[0][1], up_face[1][1], up_face[2][1], up_face[3][1]]
    temp_back = [back_face[0][2], back_face[1][2], back_face[2][2], back_face[3][2]]
    temp_down = [down_face[0][1], down_face[1][1], down_face[2][1], down_face[3][1]]

    front_face[0][1], front_face[1][1], front_face[2][1], front_face[3][1] = temp_down[0], temp_down[1], temp_down[2], temp_down[3]
    up_face[0][1], up_face[1][1], up_face[2][1], up_face[3][1] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]
    back_face[0][2], back_face[1][2], back_face[2][2], back_face[3][2] = temp_up[3], temp_up[2], temp_up[1], temp_up[0]
    down_face[0][1], down_face[1][1], down_face[2][1], down_face[3][1] = temp_back[3], temp_back[2], temp_back[1], temp_back[0]


    return up_face, down_face, left_face, front_face, right_face, back_face

 
def innerlanti(up_face, down_face, left_face, front_face, right_face, back_face):

    temp_front = [front_face[0][1], front_face[1][1], front_face[2][1], front_face[3][1]]
    temp_up = [up_face[0][1], up_face[1][1], up_face[2][1], up_face[3][1]]
    temp_back = [back_face[0][2], back_face[1][2], back_face[2][2], back_face[3][2]]
    temp_down = [down_face[0][1], down_face[1][1], down_face[2][1], down_face[3][1]]

    front_face[0][1], front_face[1][1], front_face[2][1], front_face[3][1] = temp_up[0], temp_up[1], temp_up[2], temp_up[3]
    up_face[0][1], up_face[1][1], up_face[2][1], up_face[3][1] = temp_back[3], temp_back[2], temp_back[1], temp_back[0]
    back_face[0][2], back_face[1][2], back_face[2][2], back_face[3][2] = temp_down[3], temp_down[2], temp_down[1], temp_down[0]
    down_face[0][1], down_face[1][1], down_face[2][1], down_face[3][1] = temp_front[0], temp_front[1], temp_front[2], temp_front[3]


    return up_face, down_face, left_face, front_face, right_face, back_face


def Fwclock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Fclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerfclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face


def Fwanti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Fanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerfanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face


def Bwclock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Bclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerbclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face


def Bwanti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Banti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerbanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face


def Uwclock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Uclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = inneruclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face


def Uwanti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Uanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = inneruanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face


def Dwclock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Dclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerdclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face


def Dwanti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Danti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerdanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face


def Rwclock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Rclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerrclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face


def Rwanti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Ranti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerranti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face


def Lwclock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Lclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerlclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face


def Lwanti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Lanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerlanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def F2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Fclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Fclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def F2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Fanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Fanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def B2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Bclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Bclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def B2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Banti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Banti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def U2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Uclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Uclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def U2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Uanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Uanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def D2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Dclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Dclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def D2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Danti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Danti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def R2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Rclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Rclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def R2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Ranti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Ranti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def L2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Lclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Lclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def L2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Lanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Lanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def innerf2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = innerfclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerfclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def innerf2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = innerfanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerfanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def innerb2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = innerbclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerbclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def innerb2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = innerbanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerbanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def inneru2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = inneruclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = inneruclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def inneru2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = inneruanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = inneruanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def innerd2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = innerdclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerdclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def innerd2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = innerdanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerdanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def innerr2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = innerrclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerrclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def innerr2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = innerranti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerranti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def innerl2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = innerlclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerlclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def innerl2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = innerlanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = innerlanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def Fw2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Fwclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Fwclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def Fw2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Fwanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Fwanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def Bw2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Bwclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Bwclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def Bw2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Bwanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Bwanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def Uw2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Uwclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Uwclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def Uw2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Uwanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Uwanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def Dw2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Dwclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Dwclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def Dw2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Dwanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Dwanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def Rw2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Rwclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Rwclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def Rw2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Rwanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Rwanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def Lw2clock(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Lwclock(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Lwclock(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

def Lw2anti(up_face, down_face, left_face, front_face, right_face, back_face):
    up_face, down_face, left_face, front_face, right_face, back_face = Lwanti(up_face, down_face, left_face, front_face, right_face, back_face)
    up_face, down_face, left_face, front_face, right_face, back_face = Lwanti(up_face, down_face, left_face, front_face, right_face, back_face)
    return up_face, down_face, left_face, front_face, right_face, back_face

movements = [
    ["FA1", Fanti], ["FC1", Fclock], ["BA1", Banti], ["BC1", Bclock],["UA1", Uanti], ["UC1", Uclock],["DA1", Danti],["DC1", Dclock], ["RA1", Ranti],["RC1", Rclock],
    ["LA1", Lanti],["LC1", Lclock],["IFA1", innerfanti],["IFC1", innerfclock],["IBA1", innerbanti],["IBC1", innerbclock],["IUA1", inneruanti],["IUC1", inneruclock],
    ["IDA1", innerdanti],["IDC1", innerdclock],["IRA1", innerranti],["IRC1", innerrclock],["ILA1", innerlanti],["ILC1", innerlclock],["FWA1", Fwanti],["FWC1", Fwclock],
    ["BWA1", Bwanti],["BWC1", Bwclock],["UWA1", Uwanti],["UWC1", Uwclock],["DWA1", Dwanti],["DWC1", Dwclock],["RWA1", Rwanti],["RWC1", Rwclock],["LWA1", Lwanti],
    ["LWC1", Lwclock],["FA2", F2anti],["FC2", F2clock],["BA2", B2anti],["BC2", B2clock],["UA2", U2anti],["UC2", U2clock],["DA2", D2anti],["DC2", D2clock],["RA2", R2anti],["RC2", R2clock],
    ["LA2", L2anti],["LC2", L2clock],["IFA2", innerf2anti],["IFC2", innerf2clock],["IBA2", innerb2anti],["IBC2", innerb2clock],["IUA2", inneru2anti],["IUC2", inneru2clock],
    ["IDA2", innerd2anti],["IDC2", innerd2clock],["IRA2", innerr2anti],["IRC2", innerr2clock],["ILA2", innerl2anti],["ILC2", innerl2clock],["FWA2", Fw2anti],
    ["FWC2", Fw2clock],["BWA2", Bw2anti],["BWC2", Bw2clock],["UWA2", Uw2anti],["UWC2", Uw2clock],["DWA2", Dw2anti],["DWC2", Dw2clock],["RWA2", Rw2anti],["RWC2", Rw2clock],
    ["LWA2", Lw2anti], ["LWC2", Lw2clock]
]