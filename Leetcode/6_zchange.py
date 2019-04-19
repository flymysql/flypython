# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串
# 比如："LCIRETOESIIGEDHN"。

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rel = ""
        step = numRows * 2 - 2
        le = len(s)
        for i in range(numRows):
            f = i
            while f < le:
                rel += s[f]
                f += step
                mid = f-i*2
                if i != numRows - 1 and i != 0 and mid < le:
                    rel += s[mid]
        return rel

s = Solution()
print(s.convert("L",2))