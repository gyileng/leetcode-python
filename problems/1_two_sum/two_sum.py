# -*- coding: utf-8 -*-
from typing import List


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_d = dict()
        for k, v in enumerate(nums):
            if target - v in hash_d:
                return [k, hash_d[target - v]]
            hash_d[v] = k
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([-3,4,-1,90], -4))