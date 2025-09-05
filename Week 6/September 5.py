'''
# Problem: cAPS lOCK
Description:
wHAT DO WE NEED cAPS LOCK FOR?

Caps lock is a computer keyboard key. Pressing it sets an input mode in which typed letters are capital by default. 
If it is pressed by accident, it leads to accidents like the one we had in the first passage.

Let's consider that a word has been typed with the Caps lock key accidentally switched on, if:

- either it only contains uppercase letters;
- or all letters except for the first one are uppercase. 

In this case we should automatically change the case of all letters. 
For example, the case of the letters that form words "hELLO", "HTTP", "z" should be changed.
'''

# word = input()

# if word.isupper() or word[0].isupper() != True:
# 	word = word.lower()
# 	word = word[0].upper() + word[1::]
# 	print(word)
# else:
# 	print(word)

def process(word):
	word = word.lower()
	word = word[0].upper() + word[1::]
	print(word)

word = input()

if word.isupper() == True:
	print(word.lower())
elif len(word) == 1:
	print(word.upper())
elif word[0].isupper() == False and word[1::].isupper() == True:
    process(word)
else:
	print(word)