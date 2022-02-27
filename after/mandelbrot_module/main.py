import matplotlib.pyplot as plt
import numpy as np
from time import time
from mandelbrot_module import Complex, simple_stability

def simple_main():
    start = time()
    values = []
    for y in np.linspace(-2, 2, 1000):
        line = []
        for x in np.linspace(-2, 2, 1000):
            line.append(simple_stability(x, y, 100))
        values.append(line)
    values = np.array(values)
    print("simple time:" + str(time() - start))
    plt.imshow(values)
    plt.show()

def complex_stability(real:float, imag:float, max_iterations:int=100) -> int:
    c = Complex(real, imag)
    z = Complex(0, 0)
    for i in range(max_iterations):
        z = z.mul(z).add(c)
        if z.dist_from_origin() > 2:
            return i
    return max_iterations

def complex_main():
    start = time()
    values = []
    for y in np.linspace(-2, 2, 1000):
        line = []
        for x in np.linspace(-2, 2, 1000):
            line.append(complex_stability(x, y, 100))
        values.append(line)
    values = np.array(values)
    print("complex time:" + str(time() - start))
    plt.imshow(values)
    plt.show()

if __name__ == '__main__':
    simple_main()
    complex_main()