import sys
games_played = int(input())
outcomes = sys.stdin.readline().strip()
A = 0
D = 0

for i in outcomes:
    if i == "A":
        A += 1
    else:
        D += 1

if A > D:
    print("Anton")
elif A < D:
    print("Danik")
else:
    print("Friendship")