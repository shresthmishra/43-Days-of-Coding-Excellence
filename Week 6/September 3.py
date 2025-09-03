'''
# Problem: Young Physicist
Description:
A guy named Vasya attends the final grade of a high school. 
One day Vasya decided to watch a match of his favorite hockey team. 
And, as the boy loves hockey very much, even more than physics, he forgot to do the homework. 
Specifically, he forgot to complete his physics tasks. 
Next day the teacher got very angry at Vasya and decided to teach him a lesson. 
He gave the lazy student a seemingly easy task: You are given an idle body in space and the forces that affect it. 
The body can be considered as a material point with coordinates (0; 0; 0). 
Vasya had only to answer whether it is in equilibrium. 
"Piece of cake" — thought Vasya, we need only to check if the sum of all vectors is equal to 0. 
So, Vasya began to solve the problem. But later it turned out that there can be lots and lots of these forces, and Vasya can not cope without your help. Help him. 
Write a program that determines whether a body is idle or is moving by the given vectors of forces.
'''

n = int(input())

sum_x = 0
sum_y = 0
sum_z = 0

for _ in range(n):
    x, y, z = map(int, input().split())
    sum_x += x
    sum_y += y
    sum_z += z

if sum_x == 0 and sum_y == 0 and sum_z == 0:
    print("YES")
else:
    print("NO")