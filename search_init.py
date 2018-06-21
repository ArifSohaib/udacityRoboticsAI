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

grid = [[0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]]
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
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    
    closedlist[init[0]][init[1]] = 1
    
    gVal = 0
    pos = None

    while pos != goal:
        if len(openlist) == 0:
            break
        # print("exploring grid[{}]".format(pos))
        # print(gVal)
        openlist.sort()
        openlist.reverse()
        pos = openlist.pop()
        gVal +=1 
        expand[pos[0]][pos[1]] = gVal
        for idx, d in enumerate(delta):
            chk = [pos[0] + d[0],pos[1] + d[1]]
            # print("checking {}".format(chk))
            if (chk[0]) >= 0 and\
            (chk[1]) >= 0 and \
            (chk[0]) != len(grid) and\
            (chk[1]) != len(grid[0]) and \
            grid[chk[0]][chk[1]] != 1:
                if closedlist[chk[0]][chk[1]] != 1:
                    openlist.append(chk)
                    closedlist[chk[0]][chk[1]] = 1
                    #action[x][y] now contains the index of the delta action that gets to the new list
                    action[chk[0]][chk[1]] = idx
    
    x = goal[0]
    y = goal[1]
    path = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    path[x][y] = '*'
    while x != init[0] and y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        path[x2][y2] = delta_name[action[x][y]]
        x = x2
        y = y2
    return path                


def print2dGrid(grid):
    for row in range(len(grid)):
        print(grid[row])
def main():        
    expand=  search(grid, init, goal, cost)
    # print(result)
    print2dGrid(expand)

if __name__ == '__main__':
    main()