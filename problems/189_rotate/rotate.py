# -*- coding: utf-8 -*-
from typing import List


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        旋转数组
        """
        length = len(nums)
        nums[:] = nums[length - k:] + nums[:length - k]
        print(nums)


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        旋转数组
        """
        length = len(nums)
        k = k % length
        nums[:] = nums[::-1][:k][::-1] + nums[::-1][k:][::-1]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        旋转数组
        """
        n = len(nums)
        k = k % n

        def swap(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        swap(0, n - k - 1)
        swap(n - k, n - 1)
        swap(0, n - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.rotate([1, 2, 3, 4, 5, 6, 7], 8))
