# 环境：python3.6
# 编译原理——词法分析器
# 刘金明——320160939811
import re

# 运算符表
y_list = {"+","-","*","/","<","<=",">",">=","=","==","!=","^",",","&","&&","|","||","%","~","<<",">>","!"}
# 分隔符表
f_list = {";","(",")","[","]","{","}", ".",":","\"","#","\'","\\","?"}
# 关键字表
k_list = {
    "auto", "break", "case", "char", "const", "continue","default", "do", "double", "else", "enum", "extern",
    "float", "for", "goto", "if", "int", "long","register", "return", "short", "signed", "sizeof", "static",
    "struct", "switch", "typedef", "union", "unsigned", "void","volatile", "while", "printf"
}
# 括号配对判断
kuo_cp = {'{':'}', '[':']', '(':')'}

# 从文本中分割分隔符
def get_words(filename):
    global f_list
    out_words = []
    f = open(filename,'r+',encoding='UTF-8')
    # 先逐行读取，并记录行号
    lines = f.readlines()
    line_num = 1
    # 判断是否含有注释块的标识
    pass_block = False
    for line in lines:
        words = list(line.split())
        for w in words:
            # 去除注释
            if '*/' in w:
                pass_block = False
                continue
            if '//' in w or pass_block:
                break
            if '/*' in w:
                pass_block = True
                break
            # 分析单词
            ws = w
            for a in w:
                if a in f_list or a in y_list:
                    # index为分隔符的位置，将被分隔符或运算符隔开的单词提取
                    index = ws.find(a)
                    if index!=0:
                        # 存储单词与该单词的所在行号，方便报错定位
                        out_words.append({'word':ws[0:index], 'line':line_num})
                    ws = ws[index+1:]
                    out_words.append({'word':a, 'line':line_num})
            if ws!='':
                out_words.append({'word':ws, 'line':line_num})
        line_num += 1
    return out_words

# 正则表达式判断是否为数字
def if_num(int_word):
    if re.match("^([0-9]{1,}[.][0-9]*)$",int_word) or re.match("^([0-9]{1,})$",int_word) == None:
        return False
    else:
        return True

# 判断是否为为变量名
def if_name(int_word):
    if re.match("[a-zA-Z_][a-zA-Z0-9_]*",int_word) == None:
        return False
    else:
        return True

# 判断变量名是否已存在
def have_name(name_list,name):
    for n in name_list:
        if name == n['name']:
            return True
    return False

# list的换行输出
def printf(lists):
    for l in lists:
        print(l)

# 创建各个表
def creat_table(in_words):
    global k_list
    global y_list
    global f_list
    global kuo_cp
    name_id = 0
    # 各个表存放相应字符
    key_word_table = []     # 关键字
    separator_list = []     # 分隔符
    operator_list = []      # 运算符
    name_list = []          # 变量
    out_word_list = []      # 输出字符串
    kuo_list = []           # 存储括号并判断是否完整匹配
    char_flag = False
    for word in in_words:
        w = word['word']
        line = word['line']
        # 判断是否为字符串
        if char_flag == True:
            out_word_list.append({'line':line, 'type':'chartable', 'word':w})
            continue
        # 判断为关键字
        if w in k_list:
            key_word_table.append({'line':line, 'type':'keyword', 'word':w})
            out_word_list.append({'line':line, 'type':'keyword', 'word':w})
        # 判断为运算符
        elif w in y_list:
            operator_list.append({'line':line, 'type':'operator', 'word':w})
            out_word_list.append({'line':line, 'type':'operator', 'word':w})
        # 判断为分隔符
        elif w in f_list:
            # 是否为引号
            # if w == "\"" or w == "'":
            #     if char_flag == False:
            #         char_flag = True
            #     else:
            #         char_flag = False
            # 检查括号匹配
            if w in kuo_cp.values() or w in kuo_cp.keys():
                # 左括号入栈
                if w in kuo_cp.keys():
                    kuo_list.append({'kuo':w, 'line':line})
                # 右括号判断是否匹配并出栈
                elif w == kuo_cp[kuo_list[-1]['kuo']]:
                    kuo_list.pop()
                else:
                    print("小金提醒：在第" + str(line) + "行的' " + w + " '无法匹配，无法通过编译，请检查代码正确性！")
                    return
            separator_list.append({'line':line, 'type':'separator', 'word':w})
            out_word_list.append({'line':line, 'type':'separator', 'word':w})
        # 其他字符处理
        else:
            if if_num(w):
                out_word_list.append({'line':line, 'type':'number', 'value':w})
            # 如果是变量名要判断是否已经存在
            elif if_name(w):
                if have_name(name_list,w):
                    pass
                else:
                    name_list.append({'line':line, 'id':name_id, 'value':0.0, 'name':w})
                    out_word_list.append({'line':line, 'type':'name', 'word':w, 'id':name_id})
                    name_id += 1
            else:
                print("小金提醒：在第" + str(line) + "行的变量名' " + w + " '不可识别，无法通过编译，请检查代码正确性！")
                return
    if kuo_list!=[]:
        print("小金提醒：在第" + str(kuo_list[0]['line']) + "行的' " + kuo_list[0]['kuo'] + " '无法匹配，无法通过编译，请检查代码正确性！")
        return
    # 返回各个表
    return {'key':key_word_table, 'sep':separator_list, 'op':operator_list, 'name':name_list, 'out':out_word_list}

if __name__ == '__main__':
    filename = input("请输入要编译的.c文件:")
    if filename == '':
        filename = 'test.c'
    word_list = get_words(filename)
    table_list = creat_table(word_list)
    print("\n输出字符串如下")
    printf(table_list['out'])
    print("\n\n输出变量表如下\n")
    printf(table_list['name'])