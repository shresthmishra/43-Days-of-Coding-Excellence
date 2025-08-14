'''
# Problem: Translation
# Description: The translation from the Berland language into the Birland language is not an easy task. 

Those languages are very similar: a Berlandish word differs from a Birlandish word with the same meaning a little: it is spelled (and pronounced) reversely. 

For example, a Berlandish word code corresponds to a Birlandish word edoc. However, making a mistake during the "translation" is easy. 
Vasya translated the word s from Berlandish into Birlandish as t. Help him: find out if he translated the word correctly.
'''

# Input
s = input()
t = input()
     
# Operations + Output
if s[::-1] == t:
    print("YES")
else:
    print("NO")