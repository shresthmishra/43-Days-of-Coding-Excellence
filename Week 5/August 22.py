'''
# Problem: Anton and Darik
Description:
Anton likes to play chess, and so does his friend Danik.
Once they have played n games in a row. For each game it's known who was the winner — Anton or Danik. None of the games ended with a tie.
Now Anton wonders, who won more games, he or Danik? Help him determine this.
'''

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