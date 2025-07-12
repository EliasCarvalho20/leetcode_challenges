"""
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""


def can_jump(nums: list[int]) -> bool:
    gas = 0
    for n in nums:
        if gas < 0:
            return False
        elif n > gas:
            gas = n
        gas -= 1

    return True

    # list_limit = len(nums) - 1
    #
    # for i in range(len(nums)):
    #     total_fuel = nums[i]
    #
    #     for j in range(i, 0, -1):
    #         index = abs(i - j)
    #         sum_fuel = nums[index] - j
    #         if sum_fuel <= 0:
    #             continue
    #
    #         total_fuel += sum_fuel
    #
    #     if total_fuel <= 0 and nums[i] == 0:
    #         return False
    #     elif nums[i] >= list_limit - i:
    #         return True
    #
    # return False
