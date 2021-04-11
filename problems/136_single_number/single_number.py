from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([60, 13, 45, 32, 13, 60, 45]))
