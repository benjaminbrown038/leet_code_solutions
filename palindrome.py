'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

'''

def palindrome(x:int):
    string = str(x)
    length = len(string)
    iters = None
    if length % 2 == 0:
        iters = int(length/2)
    else:
        iters = int((length-1)/2)
    for i in range(iters):
        if string[i]!=string[-1-i]:
            return False
    return True

print(palindrome(1001))
print(palindrome(123456543))
