import matplotlib.pyplot as plt
import math
import numpy as np
from time import time

def simple_stability(real:float, imag:float, max_iterations:int=100) -> int:
    zr = 0
    zi = 0
    for i in range(max_iterations):
        new_zr = zr**2 - zi**2 + real
        zi = 2 * zr * zi + imag
        zr = new_zr
        if math.sqrt(zr**2 + zi**2) > 2:
            return i
    return max_iterations

def main():
    start = time()
    values = []
    for y in np.linspace(-2, 2, 1000):
        line = []
        for x in np.linspace(-2, 2, 1000):
            line.append(simple_stability(x, y))
        values.append(line)
    values = np.array(values)
    print(time() - start)
    plt.imshow(values)
    plt.show()

if __name__ == '__main__':
    main()