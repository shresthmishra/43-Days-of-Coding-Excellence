'''
# Problem: HQ9+
Description: 
HQ9+ is a joke programming language which has only four one-character instructions:

    "H" prints "Hello, World!",
    "Q" prints the source code of the program itself,
    "9" prints the lyrics of "99 Bottles of Beer" song,
    "+" increments the value stored in the internal accumulator.

Instructions "H" and "Q" are case-sensitive and must be uppercase. The characters of the program which are not instructions are ignored.

You are given a program written in HQ9+. You have to figure out whether executing this program will produce any output.
'''

program_code = input()

if 'H' in program_code or 'Q' in program_code or '9' in program_code:
    print("YES")
else:
    print("NO")