# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        a = [{} for i in range(9)]
        b = [{} for i in range(9)]
        c = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n == '.':
                    continue
                n = int(n)
                c_k = (i // 3) * 3 + j // 3
                a[i][n] = a[i].get(n, 0) + 1
                b[j][n] = b[j].get(n, 0) + 1
                c[c_k][n] = c[c_k].get(n, 0) + 1
                if a[i][n] > 1 or b[j][n] > 1 or c[c_k][n] > 1:
                    return False
        return True
