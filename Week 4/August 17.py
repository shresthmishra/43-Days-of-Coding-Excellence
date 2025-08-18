'''
# Problem: Soldier and Bananas
Description:
A soldier wants to buy w bananas in the shop. 
He has to pay k dollars for the first banana, 2k dollars for the second one and so on (in other words, he has to pay i·k dollars for the i-th banana).

He has n dollars. How many dollars does he have to borrow from his friend soldier to buy w bananas?
'''

x = float(input())
n = int(input())

result = x ** n

print(f"{result:.5f}")