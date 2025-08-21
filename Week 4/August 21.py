'''
# Problem: Petya and Countryside
Description:
Little Petya often travels to his grandmother in the countryside. 
The grandmother has a large garden, which can be represented as a rectangle 1 x n in size, when viewed from above. This rectangle is divided into n equal square sections. 
The garden is very unusual as each of the square sections possesses its own fixed height and due to the newest irrigation system we can create artificial rain above each section.

Creating artificial rain is an expensive operation. That's why we limit ourselves to creating the artificial rain only above one section. 
At that, the water from each watered section will flow into its neighbouring sections if their height does not exceed the height of the section. 
That is, for example, the garden can be represented by a 1 x 5 rectangle, where the section heights are equal to 4, 2, 3, 3, 2. 
Then if we create an artificial rain over any of the sections with the height of 3, the water will flow over all the sections, except the ones with the height of 4. 
'''

n = int(input())
heights = list(map(int, input().split()))

max_watered_sections = 0

for i in range(n):
    current_watered_count = 1
    for j in range(i - 1, -1, -1):
        if heights[j] <= heights[j + 1]:
            current_watered_count += 1
        else:
            break
    for j in range(i + 1, n):
        if heights[j] <= heights[j - 1]:
            current_watered_count += 1
        else:
            break
    if current_watered_count > max_watered_sections:
        max_watered_sections = current_watered_count

print(max_watered_sections)