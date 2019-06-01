"""
语义分析:中间代码产生——四元式
刘金明：16计一
"""
from parser import Node,build_ast
import sys, os, re
sys.path.append(os.pardir)
from lexer import word_list

# 四元式对象，op，arg1,arg2,result 分别对于操作数，两个变量，结果
class Mnode:
    def __init__(self, op="undefined", a1=None, a2=None, re=None):
        self.op = op
        self.arg1 = a1
        self.arg2 = a2
        self.re = re
    # 字符化输出
    def __str__(self):
        return "({0},{1},{2},{3})".format(self.op, self.arg1, self.arg2, self.re)

    def __repr__(self):
        return self.__str__()

"""
两个全局 mid_result 存放四元式对象
tmp记录零时变量id
"""
mid_result = []
tmp = 0

# 递归遍历语法树
def view_astree(root, ft=None):
    # 直接去括号
    if root == None or root.text == "(" or root.text == ")":
        return
    # 返回终结符叶子节点
    elif len(root.child) == 0 and root.text != None:
        return root.text
    global mid_result
    global tmp
    
    """ 下面的代码参照该文法
    "L":["M = E", "M"],
    "M":["name"],
    "E":["T ET"],
    "ET":["+ T ET", "- T ET", "null"],
    "T":["F TT"],
    "TT":["* F TT", "/ F TT", "null"],
    """
    # 变量声明语句，两种情况（直接赋值，不赋值）
    if root.type == "L":
        if len(root.child) == 1:
            mid_result.append(Mnode("=",0,0,view_astree(root.child[0])))
        else:
            mid_result.append(Mnode("=",view_astree(root.child[2]),0,view_astree(root.child[0])))
    # 右递归处理
    elif root.type == "ET" or root.type == "TT":
        if len(root.child) > 1:
            # 临时变量Tn
            t = "T" + str(tmp)
            tmp += 1
            # ft 为父节点传入的操作符左边部分临时id
            mid_result.append(Mnode(view_astree(root.child[0]), view_astree(root.child[1]), ft,t))
            ct = view_astree(root.child[2], t)
            # 判断下一个右递归是否为空
            if ct != None:
                return ct
            return t
    # 赋值语句处理
    elif root.type == "E" or root.type == "T":
        # 如果存在右递归，进行四则运算的解析
        if len(root.child[1].child) > 1:
            t = "T" + str(tmp)
            tmp += 1
            mid_result.append(Mnode(view_astree(root.child[1].child[0]), view_astree(root.child[0]), view_astree(root.child[1].child[1]),t))
            ct = view_astree(root.child[1].child[2], t)
            # 判断下一个右递归是否为空
            if ct != None:
                return ct
            return t
        else:
            # 不存在右递归的话直接赋值
            return view_astree(root.child[0])
    elif len(root.child) == 1:
        return view_astree(root.child[0])
    else:
        re = ""
        # 一条语句肯定只能传回来一个值
        for c in root.child:
            cre = view_astree(c)
            if cre != None:
                re = cre
        return re
    
        
if __name__ == "__main__":
    filename = 'test/test.c'
    w_list = word_list(filename)
    word_table = w_list.word_list
    root = build_ast(word_table)
    view_astree(root)
    for r in mid_result:
        print(r)
    # tmp_code = generate(root)
    # print(tmp_code)
