# 217.存在重复元素

给定一个整数数组，判断是否存在重复元素。
如果存在一个值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

**示例 1：**

```code
输入: [1,2,3,1]  
输出: true
```

**示例 2：**

```code
输入: [1,2,3,4]
输出: false
```

**解题思路：**  
利用集合去重即可

**源码：**  
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```
执行用时： `40 ms` , 在所有 Python3 提交中击败了 `89.11%` 的用户  
内存消耗： `20.2 MB` , 在所有 Python3 提交中击败了 `47.76%` 的用户
