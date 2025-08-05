'''
# Problem: Petya and Strings
Description: 

Little Petya loves presents. His mum bought him two strings of the same size for his birthday. 
The strings consist of uppercase and lowercase Latin letters. 

Now Petya wants to compare those two strings lexicographically.
The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. 

Help Petya perform the comparison.
'''

s1 = input().lower()
s2 = input().lower()

if s1 < s2:
    print(-1)
elif s1 > s2:
    print(1)
else:
    print(0)