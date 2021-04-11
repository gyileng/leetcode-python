# -*- coding: utf-8 -*-
from typing import List


class Solution:
    """删除排序数组中的重复项"""
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        length = len(nums)
        while i < length:
            if nums[i] != nums[j]:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        nums = nums[:j+1]
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5]))
