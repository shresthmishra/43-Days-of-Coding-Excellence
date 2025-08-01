'''
# Problem: Roman to Integer
Description: Given a roman numeral, convert it to an integer.
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        
        n = len(s)
        num = 0
        
        for i in range(n - 1):
            if roman_map[s[i]] < roman_map[s[i+1]]:
                num -= roman_map[s[i]]
            else:
                num += roman_map[s[i]]
                
        num += roman_map[s[n-1]]
        return num
    
solution = Solution()
print(solution.romanToInt("VII"))