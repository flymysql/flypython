"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        rel = []
        for s in self.generateParenthesis(n-1):
            rel.append("(" + s + ")")
            if s.count("()") != len(s)/2:
                rel.append(s + "()")
            rel.append(s + "()")
        return rel
    # 非递归方法
    def generateParenthesis2(self, n: int):
        if n == 0:
            return []
        rel , star = [], "()"
        rel.append(star)
        for _ in range(n-1):
            tmp = []
            for x in rel:
                tmp.append("(" + x + ")")
                if "()" + x not in tmp:
                    tmp.append("()" + x)
                if x + "()" not in tmp:
                    tmp.append(x + "()")
            rel = tmp
        for i in range(int(n/2) -1):
            star = '(' + star + ')'
        star += star
        if n%2 != 0:
            star = '(' + star + ')'
        print(star)
        rel.append(star)
        return rel
    def test(self):
        ins = self.generateParenthesis2(5)
        for i in range(len(ins)):
            if ins[i] in ins[i+1:]:
                print(ins[i])
        out = ["((((()))))","(((()())))","(((())()))","(((()))())","(((())))()","((()(())))","((()()()))","((()())())","((()()))()","((())(()))","((())()())","((())())()","((()))(())","((()))()()","(()((())))","(()(()()))","(()(())())","(()(()))()","(()()(()))","(()()()())","(()()())()","(()())(())","(()())()()","(())((()))","(())(()())","(())(())()","(())()(())","(())()()()","()(((())))","()((()()))","()((())())","()((()))()","()(()(()))","()(()()())","()(()())()","()(())(())","()(())()()","()()((()))","()()(()())","()()(())()","()()()(())","()()()()()"]
        for x in out:
            if x not in ins:
                print(x)
        return True
        

s = Solution()

print(s.test())