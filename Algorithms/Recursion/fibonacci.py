#find n-th term in a Fibonacci Series - Recursion

def fib_n_rec(n):
    if n==1 or n==2:
        return 1
    return fib_n_rec(n-1) + fib_n_rec(n-2)

n = int(input("Enter the n-th term:"))

print(fib_n_rec(n))
