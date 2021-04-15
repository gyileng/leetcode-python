# 344.反转字符串

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组`char[]`的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用`O(1)`的额外空间解决这一问题。
你可以假设数组中的所有字符都是`ASCII`码表中的可打印字符。

**示例 1：**
```code
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
```

**示例 2：**
```code
输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
```


**思路一：原地替换**  
将字符串以中间对折即可，循环次数为`(n+1)//2`


**源码一：**
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range((n + 1) // 2):
            s[i], s[n-i-1] = s[n-i-1], s[i]
```
**性能分析：**  
时间复杂度：O(N)  
空间复杂度：O(1)  
执行用时：`48 ms`, 在所有 Python3 提交中击败了`75.61%`的用户  
内存消耗：`19 MB`, 在所有 Python3 提交中击败了`91.82%`的用户

**思路二：Pythonic**  
使用`Python`内置函数`reverse()`

**源码二：**
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
```
**性能分析：**  
时间复杂度：O(N)  
空间复杂度：O(1)  
执行用时：`48 ms`, 在所有 Python3 提交中击败了`75.61%`的用户  
内存消耗：`19 MB`, 在所有 Python3 提交中击败了`86.52%`的用户
