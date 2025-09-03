'''
# Problem: Arrival of the General
Description:
A Ministry for Defense sent a general to inspect the Super Secret Military Squad under the command of the Colonel SuperDuper. 
Having learned the news, the colonel ordered to all n squad soldiers to line up on the parade ground.

By the military charter the soldiers should stand in the order of non-increasing of their height. 
But as there's virtually no time to do that, the soldiers lined up in the arbitrary order. 
However, the general is rather short-sighted and he thinks that the soldiers lined up correctly if the first soldier in the line has the maximum height and the last soldier has the minimum height. 
Please note that the way other solders are positioned does not matter, including the case when there are several soldiers whose height is maximum or minimum. 
Only the heights of the first and the last soldier are important.

For example, the general considers the sequence of heights (4, 3, 4, 2, 1, 1) correct and the sequence (4, 3, 1, 2, 2) wrong.

Within one second the colonel can swap any two neighboring soldiers. 
Help him count the minimum time needed to form a line-up which the general will consider correct.
'''

n = int(input())
heights = list(map(int, input().split()))

max_height = max(heights)
min_height = min(heights)

max_index = heights.index(max_height)
min_index = n - 1 - heights[::-1].index(min_height)

swaps = max_index
swaps += (n - 1) - min_index

if max_index > min_index:
    swaps -= 1

print(swaps)