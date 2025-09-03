'''
# Problem: George and Accommodation
Description:
George has recently entered the BSUCP (Berland State University for Cool Programmers). 
George has a friend Alex who has also entered the university. Now they are moving into a dormitory.

George and Alex want to live in the same room. The dormitory has n rooms in total. 
At the moment the i-th room has pi people living in it and the room can accommodate qi people in total (pi ≤ qi). 
Your task is to count how many rooms has free place for both George and Alex.
'''

n = int(input())
available_rooms_count = 0

for _ in range(n):
    p, q = map(int, input().split())
    if q - p >= 2:
        available_rooms_count += 1

print(available_rooms_count)