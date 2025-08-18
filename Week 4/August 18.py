'''
# Problem: Word
# Description: 
Vasya is very upset that many people on the Net mix uppercase and lowercase letters in one word. 
That's why he decided to invent an extension for his favorite browser that would change the letters' register in every word so that it either only consisted of lowercase letters or, vice versa, only of uppercase ones. 
At that as little as possible letters should be changed in the word. 
For example, the word HoUse must be replaced with house, and the word ViP — with VIP. 

If a word contains an equal number of uppercase and lowercase letters, you should replace all the letters with lowercase ones. 
For example, maTRIx should be replaced by matrix. Your task is to use the given method on one given word.
'''

s = input()
upper_count = 0
lower_count = 0
for i in s:
    if i.isupper() == True:
        upper_count += 1
    else:
        lower_count += 1
if upper_count > lower_count:
    print(s.upper())
else:
    print(s.lower())