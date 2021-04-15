# 36.有效的数独

给定一个`n×n`的二维矩阵`matrix`表示一个图像。请你将图像顺时针旋转`90`度。  
!> 你必须在`原地`旋转图像，这意味着你需要直接修改输入的二维矩阵。请**不要**使用另一个矩阵来旋转图像。

**示例 1：**

```math
\begin{bmatrix}1&2&3\\4&5&6\\7&8&9\end{bmatrix}\Rightarrow\begin{bmatrix}7&4&1\\8&5&2\\9&6&3\end{bmatrix}
```
```code
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
```

**示例 2：**
```math
\begin{bmatrix}5&1&9&11\\2&4&8&10\\13&3&6&7\\15&14&12&16\end{bmatrix}\Rightarrow\begin{bmatrix}15&13&2&5\\14&3&4&1\\12&6&8&9\\16&7&10&11\end{bmatrix}
```
```code
输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

**示例 3：**
```code
输入：matrix = [[1]]
输出：[[1]]
```

**示例 4：**
```code
输入：matrix = [[1,2],[3,4]]
输出：[[3,1],[4,2]]
```


**思路一：**
```math
\begin{bmatrix}1&\;&\;\\4&\;&\;\\7&\;&\;\end{bmatrix}\Rightarrow\begin{bmatrix}7&4&1\\&&\\&&\end{bmatrix}
```
由竖向的`1`、`4`、`7`，旋转90°得到横向`7`、`4`、`1`，那么只需要得到`matrix`的一份拷贝，都拷贝进行遍历，对原数组重新赋值即可。


**源码一：**
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = m[n-j-1][i]
```
**性能分析：**  
时间复杂度：O(N²)  
空间复杂度：O(N²)  
执行用时：`36 ms`, 在所有 Python3 提交中击败了`83.32%`的用户  
内存消耗：`14.9 MB`, 在所有 Python3 提交中击败了`27.04%`的用户

**思路二：**
```math
\begin{bmatrix}1&2&3\\4&5&6\\7&8&9\end{bmatrix}\Rightarrow\begin{bmatrix}\overbrace7^1&2&\overbrace1^2\\4&5&6\\\overbrace9^4&8&\overbrace3^3\end{bmatrix}\Rightarrow\begin{bmatrix}7&\overbrace4^1&1\\\overbrace8^4&5&\overbrace2^2\\9&\overbrace6^3&3\end{bmatrix}
```
-----------------------
```math
\begin{bmatrix}5&1&9&11\\2&4&8&10\\13&3&6&7\\15&14&12&16\end{bmatrix}\Rightarrow\begin{bmatrix}\overbrace{15}^{1\rightarrow}&1&9&\overbrace5^{2\rightarrow}\\2&4&8&10\\13&3&6&7\\\overbrace{16}^{\leftarrow4}&14&12&\overbrace{11}^{\leftarrow3}\end{bmatrix}\Rightarrow\begin{bmatrix}15&\overset{\overbrace{}1}{13}^\rightarrow&9&5\\2&3&4&\overbrace1^{\leftarrow2}\\\overbrace{12}^{4\rightarrow}&6&8&7\\16&14&\overbrace{10}^{\leftarrow3}&11\end{bmatrix}\Rightarrow\begin{bmatrix}15&13&\overset{\overbrace{}1}2^\rightarrow&5\\\overbrace{14}^{4\rightarrow}&3&4&1\\12&6&8&\overbrace9^{\leftarrow2}\\16&\overbrace7^{\leftarrow3}&10&11\end{bmatrix}\Rightarrow\begin{bmatrix}15&13&2&5\\14&\overbrace3^{1\rightarrow}&\overbrace4^{2\rightarrow}&1\\12&\overbrace6^{\leftarrow4}&\overbrace8^{\leftarrow3}&9\\16&7&10&11\end{bmatrix}
```
使用`原地旋转`，一次性将数字转移到需要的位置即，`a,b,c,d=d,a,b,c`，之后需要控制循环的深度，如果采用全循环，那么相当于
转了一圈又回了原位。  
所以用`i`控制深度即`n // 2`，`j`控制宽度即`(n+1) // 2`。  
此时需要获取每次循环`a`、`b`、`c`、`d`对应的值  
```python
a=matrix[i][j]  
b=matrix[i][n-j-1]
c=matrix[n-i-i][n-j-1]
d=matrix[n-i-i][j]
```


**源码二：**
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] = \
                matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
```
**性能分析：**  
时间复杂度：O(N²)  
空间复杂度：O(1)  
执行用时：`36 ms`, 在所有 Python3 提交中击败了`83.32%`的用户  
内存消耗：`14.8 MB`, 在所有 Python3 提交中击败了`72.15%`的用户
