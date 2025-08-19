'''
# Problem: Football
# Description:
Petya loves football very much. One day, as he was watching a football match, he was writing the players' current positions on a piece of paper. 
To simplify the situation he depicted it as a string consisting of zeroes and ones. 
A zero corresponds to players of one team; a one corresponds to players of another team. 
If there are at least 7 players of some team standing one after another, then the situation is considered dangerous. 

For example, the situation 00100110111111101 is dangerous and 11110111011101 is not. 

You are given the current situation. Determine whether it is dangerous or not.
'''

n = input()
one_count = 0
zero_count = 0
flag = False

for i in n:
    if i == "1":
        one_count += 1
        zero_count = 0
    else:
        zero_count += 1
        one_count = 0
    if one_count >= 7 or zero_count >= 7:
        flag = True

if flag == True:
    print("YES")
else:
    print("NO")