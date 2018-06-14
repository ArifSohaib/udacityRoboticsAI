import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np 

def create_world(size_x = 100, size_y=100):
    """
    creates randomized colors of shape size_x by size_y
    args:
        size_x: x_dim of image
        size_y: y_dim of image
    returns:
        RGB:size_x by size_y by 3 image
        colors: 2D array of containing 'R' or 'G' at colors[i][j]
    """
    colors = np.random.randint(0,2,(size_x,size_y)).tolist()
    for row in range(len(colors)):
        for col in range(len(colors[row])):
            if (colors[row][col]== 1):
                colors[row][col] = 'R'
            else:
                colors[row][col] = 'G'

    r = [[10.0 for i in range(size_y)] for i in range(size_x)]
    g = [[10.0 for i in range(size_y)] for i in range(size_x)]
    b = [[10.0 for i in range(size_y)] for i in range(size_x)]
    RGB = []
    for i in range(size_x):
        for j in range(size_y):
            if colors[i][j] == 'R':
                r[i][j] = 255.0
            else:
                b[i][j] = 255.0
            RGB.append(b[i][j])
            RGB.append(r[i][j])
            RGB.append(g[i][j])
            
    RGB = np.array(RGB).reshape(size_x,size_y,3)
    return RGB, colors

def main():
    RGB, _ = create_world(10,10)

    plt.imshow(RGB,cmap='Accent')

    plt.show()
            

if __name__ == '__main__':
    main()