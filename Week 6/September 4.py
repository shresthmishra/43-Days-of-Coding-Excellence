'''
# Problem: Calculating Function
Description:
For a positive integer n let's define a function f:

f(n) =  - 1 + 2 - 3 + .. + ( - 1)^n n

Your task is to calculate f(n) for a given integer n.
'''

n = int(input())

if n % 2 == 0:
    result = n // 2
else:
    result = -(n + 1) // 2

print(result)