# find Greatest Common Divisor of two numbers - Recursion

def gcd(x, y):
    if x%y == 0:
        return y
    return gcd(y, x%y)

x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))

a = max(x,y)
b = min(x,y)

print(gcd(a,b))
