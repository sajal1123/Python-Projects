# find Least Common Multiple of two numbers - Recursion

def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

def lcm(x, y):
    if x%y == 0 or y%x == 0:
        return max(x, y)
    return x*y//gcd(x, y)

n = int(input("Enter the first number:"))
m = int(input("Enter the second number:"))
print(lcm(n, m))
