# 179.最大数 

给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。  
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

**示例 1：**  
```code
输入：nums = [10,2]
输出："210"
```

**示例 2：**  
```code
输入：nums = [3,30,34,5,9] [9,5,34,3,30]
输出："9534330"
```

**示例 3：**  
```code
输入：nums = [1]
输出："1"
```

**示例 4：**  
```code
输入：nums = [10]
输出："10"
```

**思路一：**
选择排序
两个数字对应的字符串a和b，如果字典序a+b>b+a，此时a排在b的前面即可获得更大值  
示例：a=3,b=32,两者拼接的值：332>323，所以3应排在32前面

**源码一：**
```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_len = len(nums)
        nums = list(map(str, nums))
        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return str(int(''.join(nums)))
```
**性能分析一：**
时间复杂度：O(n²)  
空间复杂度：O(n)  
执行用时：`60 ms`, 在所有 Python3 提交中击败了`28.30%`的用户  
内存消耗：`14.9 MB`, 在所有 Python3 提交中击败了`48.59%`的用户

**思路二：**
与思路一一致，更换一种写法  
Python自带的sort排序，使用`cmp_to_key`函数，接收两个参数(x,y),需要满足条件：  
前面的数+后面的数>后面的数+前面的数，即y+x>x+y返回1成立

**源码二：**
```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(lambda x, y: 1 if x + y < y + x else -1))
        res = str(int("".join(nums)))
        return res
```
**性能分析二：**  
时间复杂度：O(nlogn)  
空间复杂度：O(n)  
执行用时：`40 ms`, 在所有 Python3 提交中击败了`89.05%`的用户  
内存消耗：`14.8 MB`, 在所有 Python3 提交中击败了`69.54%`的用户
