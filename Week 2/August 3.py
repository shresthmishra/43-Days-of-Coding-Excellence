'''
# Problem: Next Round
# Description:

"Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round, as long as the contestant earns a positive score..." — an excerpt from contest rules.

A total of n participants took part in the contest (n ≥ k), and you already know their scores. Calculate how many participants will advance to the next round.
'''

n, k = map(int, input().split())
scores = list(map(int, input().split()))

advancing_participants = 0
threshold_score = scores[k - 1]

for score in scores:
    if score > 0 and score >= threshold_score:
        advancing_participants += 1

print(advancing_participants)