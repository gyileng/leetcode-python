# -*- coding: utf-8 -*-
import math
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_len = len(nums)
        nums = list(map(str, nums))
        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

        return str(int(''.join(nums)))


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(lambda x, y: 1 if x + y < y + x else -1))
        res = str(int("".join(nums)))
        return res


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def fun(x):
            if x == 0: return 0
            L = int(math.log10(x)) + 1
            return x / (10 ** L - 1)

        nums.sort(key=fun, reverse=True)
        nums = list(map(str, nums))
        return str(int("".join(nums)))
