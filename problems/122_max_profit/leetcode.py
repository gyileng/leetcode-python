# -*- coding: utf-8 -*-
from typing import List


class Solution:
    """买卖股票的最佳时机 II"""
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        i = result = 0

        while i < length-1:
            if prices[i+1] > prices[i]:
                result += (prices[i+1] - prices[i])
            i += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))