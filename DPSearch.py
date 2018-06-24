# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    #if value is 999, it is unopened
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    closedlist = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    #start with goal stat
    x = goal[0]
    y = goal[1]
    openlist = [[x,y]]
    #print("goal: {}".format(goal))
    #set value of goal to 0
    value[x][y] = 0
    while True:
        val = openlist.pop()
        x = val[0]
        y = val[1]
        #print("exploring: [{},{}]".format(x,y))
        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                if grid[x2][y2] != 1 and closedlist[x2][y2] != 1:
                    value[x2][y2] = min(value[x][y] + cost, value[x2][y2])
                    x = x2
                    y = y2
                    openlist.append([x,y])
                    closedlist[x][y] = 1
                    #print("added: [{},{}]".format(x,y))
                    #print(openlist)
        
        if len(openlist) == 0:
            break
    return value 

for val in compute_value(grid, goal, cost):
    print(val)