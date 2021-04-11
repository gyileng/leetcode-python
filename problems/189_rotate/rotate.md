# 189.旋转数组

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

**进阶：**  
- 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
- 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？

**示例 1：**

```code
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
```

**解题思路:**  
本题中心思想是向右顺序旋转  
通过切片，将后半部分与前半部分互换位置相加即可

**源码1**  
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        旋转数组
        """
        length = len(nums)
        nums[:] = nums[length-k:] + nums[:length-k]
```

执行用时：`56 ms`, 在所有 Python3 提交中击败了`25.62%`的用户  
内存消耗：`21 MB`, 在所有 Python3 提交中击败了`5.12%`的用户

**源码2**  
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        旋转数组
        """
        length = len(nums)
        k = k % length
        nums[:] = nums[::-1][:k][::-1] + nums[::-1][k:][::-1]
```

执行用时：`52 ms`, 在所有 Python3 提交中击败了`29.46%`的用户  
内存消耗：`21 MB`, 在所有 Python3 提交中击败了`5.12%`的用户

**源码3**  
```python
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
```

执行用时：`64 ms`, 在所有 Python3 提交中击败了`21.34%`的用户  
内存消耗：`21 MB`, 在所有 Python3 提交中击败了`5.12%`的用户
