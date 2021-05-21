# check whether a string is a palindrome or not- Recursion

def check_palindrome(s):
    if len(s)<2:
        return True
    if s[0] !=  s[-1]:
        return False
    return check_palindrome(s[1:-1])

s = input("Enter the string:")

string = ''.join(s.split())

if check_palindrome(string.lower()):
    print(s,"is a palindrome.")
else:
    print(s, "is not a palindrome.")
