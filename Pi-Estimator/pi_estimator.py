#Given a function that uniformly generates random values between -1 and 1,
#Find the value of pi.

import random
import matplotlib.pyplot as plt
def pi_estimator(n):
    dots_in_circle = 0
    dots_total = 0
    x_coors = []
    y_coors = []
    for _ in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        x_coors.append(x)
        y_coors.append(y)
        dist = x**2 + y**2
        if dist <= 1:
            dots_in_circle += 1
        dots_total += 1
    print("Pi = ", (4*dots_in_circle/dots_total))

    figure, ax = plt.subplots()
    circle = plt.Circle((0,0), 1, color='black', fill=False)
    
    ax.add_patch(circle)
    plt.scatter(x_coors, y_coors)
    plt.show()
    
n = int(input("Enter the number of points to be plotted: "))
pi_estimator(n)
