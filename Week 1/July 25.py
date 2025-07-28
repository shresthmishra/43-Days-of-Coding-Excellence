'''
Problem: Find Numbers with Even Number of Digits
Description: Given an array nums of integers, return how many of them contain an even number of digits.

'''

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count