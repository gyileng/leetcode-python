from typing import List


class Solution:
    def bubble_sort(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            for j in range(0, len(nums) - i):
                if nums[j] > nums[j + 1]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.bubble_sort([9, 3, 4, 5, 6, 2, 10, 3]))
