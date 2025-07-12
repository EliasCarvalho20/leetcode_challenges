"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
"""


def majority_element(nums: list[int]) -> int:
    count = 0
    canditate = None

    for n in nums:
        if count == 0:
            canditate = n
        count += (1 if n == canditate else -1)

    return canditate
