# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def findSum(arr):
     
    # inner map function applies inbuilt function  
    # sum on each row of matrix arr and returns 
    # list of sum of elements of each row
    return sum(map(sum,arr))  

def sense(p, world, sensor_right, Z):
    """
    uses sensor input to update location probalility
    args:
        p: 2D list representing the prior probablity
        world: the state of the world as 2D matrix
        sensor_right: probablity of sensor being right(replacement for pHit in original 1D sense)
        Z: sensor input
    """
    q = []
    totalProb = 0.0
    for row in range(len(p)):
        inner_list = []
        for col in range(len(p[row])):
            hit = (Z == world[row][col])
            val = p[row][col] * ((sensor_right * hit)+((1-sensor_right) * (1-hit)))
            totalProb+= val
            inner_list.append(val)
        q.append(inner_list)
    #normalize
    for row in range(len(q)):
        for col in range(len(q[row])):
            q[row][col] /= totalProb
    return q

def move(p, U, moveProb):
    """
    moves the values
    args:
    p: prior probablity of where we are 
    U: movement in terms of [0,0] = stay, [0,1] = right, [0,-1] = left, [1,0] = down, [-1,0] = up
    moveProb: probablity that move was successfuls
    """
    #initialize a list of 0.0's of shape p
    q = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]
    pStay = 1- moveProb
    for row in range(len(q)):
        #process U[0]
        for col in range(len(q[row])):
            #process U[1]
            q[row][col] =  (moveProb * p[(row-U[0])%len(p)][(col-U[1])%len(p[row])])+(pStay * p[row][col])
    return q

def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    #list to store images for animation
    imgs = []
    # >>> Insert your code here <<<
    for i in range(len(measurements)):
        p = move(p, motions[i],p_move)
        p = sense(p,colors, sensor_right, measurements[i])
        #print max estimated positions
        p = np.array(p)
        print(p.argmax())
        # print("estimated position: {}".format(np.unravel_index(p.argmax(),p.shape)))
        im = plt.imshow(p, animated=True)
        imgs.append([im])
    return p, imgs

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print ('[' + ',\n '.join(rows) + ']')

def main():
    #############################################################
    # For the following test case, your output should be 
    # [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
    #  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
    #  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
    #  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
    # (within a tolerance of +/- 0.001 for each entry)

    # colors = [['R','G','G','R','R'],
    #       ['R','R','G','R','R'],
    #       ['R','R','G','G','R'],
    #       ['R','R','R','R','R']]
    # measurements = ['G','G','G','G','G']
    # motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
    # p, imgs = localize(colors,measurements,motions,sensor_right = 0.7, p_move = 0.8)

    # show(p) # displays your answer
    #print final position
    #make a larger world and more measurements for visualization
    colors = np.random.randint(0,2,(100,100)).tolist()
    for row in range(len(colors)):
        for col in range(len(colors[row])):
            if (colors[row][col]== 1):
                colors[row][col] = 'R'
            else:
                colors[row][col] = 'G'
    measurements = np.random.randint(low=0,high=2,size=100).tolist()
    measurements = list(map(lambda x: 'R' if x == 1 else 'G', measurements))
    motions = np.random.randint(low=0, high=2, size=(100,2)).tolist()
    p, imgs = localize(colors, measurements, motions, sensor_right=0.6,p_move=0.8)
    # show(p)
    # fig = plt.figure()
    #5 images with an interval of 100 milliseconds repeating every 500 milliseconds
    # ani = animation.ArtistAnimation(fig,imgs,interval=50, blit=True, repeat_delay=1000)
    # print(imgs[0])
    # print(type(imgs[0]))
    # plt.show()
if __name__ == '__main__':
    main()
    