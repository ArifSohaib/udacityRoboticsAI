# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']



def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    openlist = []
    openlist.append(init)
    closedlist = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closedlist[init[0]][init[1]] = 1
    gVal = 0
    pos = None

    while pos != goal:
        if len(openlist) == 0:
            break
        print("exploring grid[{}]".format(pos))
        print(gVal)
        pos = openlist.pop()
        gVal +=1 
        for d in delta:
            chk = [pos[0] + d[0],pos[1] + d[1]]
            print("checking {}".format(chk))
            if (chk[0]) >= 0 and\
            (chk[1]) >= 0 and \
            (chk[0]) != len(grid) and\
            (chk[1]) != len(grid[0]) and \
            grid[chk[0]][chk[1]] != 1:
                if closedlist[chk[0]][chk[1]] != 1:
                    openlist.append(chk)
                    closedlist[chk[0]][chk[1]] = 1
                
    if pos != goal:
        return "fail" 
    else:
        return [gVal, pos[0], pos[1]]
print(search(grid, init, goal, cost))