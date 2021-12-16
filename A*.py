# 8 puzzle problem with A* approach

### Heuristic function used is number of misplaced tiles in current state compared to target


# 1. Number of misplaced tiles

### Can convert to class and have an arr with 
# positions represented as 1s or 0s so we can just add to get this function

def H_n(state, target):
    # Number of misplaced tiles is the Heuristic function
    return sum(x != y for x, y in zip(state, target))            # sum of all 'True's if x != y
    
    ### Equivalent code
    # s = [] 
    # for i in range(state): # 0-8
    #     if state[i] != target[i]:
    #         s.append(1)
         
    # return sum(s)






# 2. F(n) => function used to decide which node to select next
def F_n(state_with_lvl):
    state, lvl = state_with_lvl
    return H_n(state, target) + lvl # H_n(n) + G_n(n) # 







# 3. Bfs method to find G(n) 
# A star BFS tecnique
def astar(src, target, visited_states):
    
    arr = [[src, 0]] # State, lvl(depth) in a 2 dimentional array
    c = 0
    while arr:
        c += 1                                                  # Calculate Number of Iterations
        
        min_f_n = min(arr,                                      ## Minimum of queue
                      key=F_n)                                  ## F(n) = H(n) + G(n)
        
        print(min_f_n)                                          # Minimum F(n) state and lvl
        
        if min_f_n[0] == target:                                # break if target found
            return 'Found with {} iterations'.format(c)
        
        visited_states.append(min_f_n[0])                       # Append the state
        

        arr += possible_moves(min_f_n, visited_states)          # else Add all possible moves to arr

        arr.remove(min_f_n)                                     # remove checked move from arr










# Same Generations steps as iddfs

def possible_moves(state_with_lvl, visited_states): 
    state, lvl = state_with_lvl
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
        
        if temp not in visited_states:               # add only if not in visited sites                        
            pos_moves.append([temp, lvl+1])          # add temp to possible moves to check if not in visited states
    
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



visited = []
src=[1,2,3,-1,4,5,6,7,8]
target=[1,2,3,4,5,-1,6,7,8]           # given target requires depth of 2 to achieve result
#target=[1,2,3,6,4,5,-1,7,8]          # Only one position is changed(to Test)


print(astar(src, target, visited)) 


