# Binary Search

import time
import numpy as np
import random
import matplotlib.pyplot as plt

def binary_search(arr, x, ind):
    if len(arr) == 0:
        return "{} not found in list.".format(x)
    l, r = 0, len(arr)
    mid = l+r//2
    if arr[mid] == x:
        return ind+mid
    elif arr[mid] > x:
        return binary_search(arr[:mid], x, ind)
    else:
        return binary_search(arr[(mid+1):], x, mid+1+ind)


def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return "{} not found in list.".format(x)


x = np.arange(0, 1000000, 10000)
#n = int(input("Enter the term you want to search for:"))
q1b, q1l, q1t = [], [], []
q2b, q2l, q2t = [], [], []
q3b, q3l, q3t = [], [], []
q4b, q4l, q4t = [], [], []

for i in range(0, 1000000, 10000):
    l = np.arange(0, i, 1)
    n = random.randint(0, len(l)//4)
    st = time.time()
    a = binary_search(l, n, 0)
    q1b.append(time.time() - st)
    st = time.time()
    b = linear_search(l, n)
    q1l.append(time.time() - st)

    n = random.randint(len(l)//4, len(l)//2)
    st = time.time()
    a = binary_search(l, n, 0)
    q2b.append(time.time() - st)
    st = time.time()
    b = linear_search(l, n)
    q2l.append(time.time() - st)

    n = random.randint(len(l)//2, 3*len(l)//4)           
    st = time.time()
    a = binary_search(l, n, 0)
    q3b.append(time.time() - st)
    st = time.time()
    b = linear_search(l, n)
    q3l.append(time.time() - st)

    n = random.randint(3*len(l)//4, len(l))
    st = time.time()
    a = binary_search(l, n, 0)
    q4b.append(time.time() - st)
    st = time.time()
    b = linear_search(l, n)
    q4l.append(time.time() - st)

plt.subplot(2,2,1)
plt.ylim(0, 0.3)
plt.plot(x, q1b, label="Binary Search")
plt.plot(x, q1l, label="Linear Search")
plt.title("Element in first Quartile")
plt.xlabel("Size of array")
plt.ylabel("Time taken(seconds)")


plt.subplot(2,2,2)
plt.ylim(0, 0.3)
plt.plot(x, q2b, label="Binary Search")
plt.plot(x, q2l, label="Linear Search")
plt.title("Element in second Quartile")
plt.xlabel("Size of array")
plt.ylabel("Time taken(seconds)")

plt.subplot(2,2,3)
plt.ylim(0, 0.3)
plt.plot(x, q3b, label="Binary Search")
plt.plot(x, q3l, label="Linear Search")
plt.title("Element in third Quartile")
plt.xlabel("Size of array")
plt.ylabel("Time taken(seconds)")

plt.subplot(2,2,4)
plt.ylim(0, 0.3)
plt.plot(x, q4b, label="Binary Search")
plt.plot(x, q4l, label="Linear Search")
plt.title("Element in fourth Quartile")
plt.xlabel("Size of array")
plt.ylabel("Time taken(seconds)")

plt.legend()
plt.tight_layout()
plt.show()
               
'''
start_time = time.time()
x = binary_search(l, n, 0)


print("Binary Search result ->", x)

print("Binary Search runtime -> %s seconds" %((time.time() - start_time)))

start_time = time.time()
print("Linear Search result ->", linear_search(l,n))
print("Linear Search runtime -> %s seconds" %(time.time() - start_time))
'''
