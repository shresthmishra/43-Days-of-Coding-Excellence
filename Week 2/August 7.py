'''
# Problem: Word Capitalization
# Description:
Capitalization is writing a word with its first letter as a capital letter. 
Your task is to capitalize the given word.

Note, that during capitalization all the letters except the first one remains unchanged.
'''

word = input()
result = word[0].capitalize() + (word[1::])
print(result)