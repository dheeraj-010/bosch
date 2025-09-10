def isbalanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack

string1=input("Enter the string: ")

if(isbalanced(string1)):
    print("YES") 
else:
    print("NO")