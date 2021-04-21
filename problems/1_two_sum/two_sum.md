# 1.两数之和

给定一个整数数组`nums`和一个整数目标值`target`，请你在该数组中找出`和为目标值`的那两个整数，并返回它们的数组下标。  
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。  
你可以按任意顺序返回答案。

**示例 1：**
```code
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

**示例 2：**
```code
输入：nums = [3,2,4], target = 6
输出：[1,2]
```

**示例 3：**
```code
输入：nums = [3,3], target = 6
输出：[0,1]
```

**思路一：枚举所有情况**
使用`双指针`暴力枚举所有情况，查找`nums[i] + nums[j] == target`成立时的`i,j`。

**源码一：**
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

**性能分析：**  
时间复杂度：O(N²)  
空间复杂度：O(1)  

**思路二：建立哈希表**
创建一个空的字典，用来存储已经遍历过的数字，判断`target - v in hash_d`，如果存在那么就是答案。

**源码二：**
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_d = dict()
        for k, v in enumerate(nums):
            if target - v in hash_d:
                return [k, hash_d[target - v]]
            hash_d[v] = k
        return []
```

**性能分析：**  
时间复杂度：O(N)  
空间复杂度：O(N)
