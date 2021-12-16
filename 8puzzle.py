def bfs(src, target):
    arr = [src]
    c = 0
    while arr:
        c += 1                                           # Calculate Number of Iterations
        print(arr[0])                                    # Print current state to check
        
        
        if arr[0] == target:                             # break if target found
            return 'Found with {} iterations'.format(c)
        
        
        
        arr += possible_moves(arr[0])                    # else Add all possible moves to arr

        arr.pop(0)                                       # remove checked move from arr
                                               
    return 'Not Found'                                   # Challenge question: 'Will the code ever reach this line' 
                                                         #                  or 'Will the function ever return 'Not found'




def possible_moves(state):            
    b = state.index(-1)                              # Find index of empty spot
    d=[]                                             #'d' : down, 'u': up ..... directions
    pos_moves=[]                                     # if dir is possible to go then add to state to move

    if b<=5:                                         # to go down, empty spot should be in the first 2 rows
        d.append('d')

    if b>=3 :                                        # to go up, empty spots should be in the bottom 2 rows
        d.append('u')

    if b%3 > 0:                                      # to go left, empty spots should be in the right most 2 columns
        d.append('l')

    if b%3 < 2:                                      # to go right, empty spots should be in the left most 2 columns
        d.append('r')

    for i in d:                                      # for i in "all possble directions"

        temp = gen(state, i, b)                      # generate the state if slide empty spot to one of the directions
                                                  
        pos_moves.append(temp)                       # add temp to possible moves to check if 
    
    return pos_moves                                 # return array of all possible moves


def gen(state, m, b):                                # m(move) is direction to slide, b(blank) is index of empty spot
    temp=state.copy()                                # create a copy of current state to test the move

    if m == 'l':                                     # if move is to slide empty spot to the left
        temp[b], temp[b-1] = temp[b-1], temp[b]      # switch postions so a = b and b = a

    if m == 'r':                                     # if move is to slide empty spot to the right
        temp[b], temp[b+1] = temp[b+1], temp[b]

    if m == 'u':                                     # if move is to slide empty spot to the top
        temp[b], temp[b-3] = temp[b-3], temp[b]

    if m =='d':                                      # if move is to slide empty spot to the bottom
        temp[b], temp[b+3] = temp[b+3], temp[b]
    
    return temp                                      # return new state with tested move to later check if "src == target"

          






src=[1,2,3,-1,4,5,6,7,8]
#target=[1,2,3,4,5,-1,6,7,8]         # given target requires depth of 2 to achieve result
target=[1,2,3,6,4,5,-1,7,8]          # Only one position is changed(to Test)


print(bfs(src, target)) 

# Challenge
# Add memory so it dosent check repeated sites


        
