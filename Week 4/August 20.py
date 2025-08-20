'''
# Problem: Drinks
Description:
Little Vasya loves orange juice very much. That's why any food and drink in his kitchen necessarily contains orange juice. 
There are n drinks in his fridge, the volume fraction of orange juice in the i-th drink equals pi percent.

One day Vasya decided to make himself an orange cocktail. He took equal proportions of each of the n drinks and mixed them. 
Then he wondered, how much orange juice the cocktail has.

Find the volume fraction of orange juice in the final drink.
'''

n = int(input())
percentages = list(map(int, input().split()))

total_sum = sum(percentages)
average = total_sum / n

print(average)