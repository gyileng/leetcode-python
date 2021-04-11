# 136.只出现一次的数字

给定一个**非空**整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

**说明：**  
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

**示例 1：**

```code
输入: [2,2,1]
输出: 1
```

**示例 2：**

```code
输入: [4,1,2,1,2]
输出: 4
```

**解题思路:**  
[异或运算](http://www.ruanyifeng.com/blog/2021/01/_xor.html)

**源码1**  
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]
```

执行用时：`52 ms`, 在所有 Python3 提交中击败了`60.52%`的用户  
内存消耗：`16.6 MB`, 在所有 Python3 提交中击败了`44.69%`的用户
