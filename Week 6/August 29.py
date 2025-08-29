'''
# Problem: Lucky Division
Description:
Petya loves lucky numbers. Everybody knows that lucky numbers are positive integers whose decimal representation contains only the lucky digits 4 and 7. 
For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Petya calls a number almost lucky if it could be evenly divided by some lucky number. 
Help him find out if the given number n is almost lucky.
'''

n = int(input())

lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 777]
is_almost_lucky = False

for lucky_num in lucky_numbers:
    if n % lucky_num == 0:
        is_almost_lucky = True
        break

if is_almost_lucky:
    print("YES")
else:
    print("NO")