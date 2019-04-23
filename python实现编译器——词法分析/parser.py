"""
语法分析
"""
import sys, os
sys.path.append(os.pardir)
from other.wenfa import *
from lexer.lexer import word_list

filename = './test/test.c'
w_list = word_list(filename)
word_table = w_list.word_list
table_size = len(word_table)
index = 0
next_w = word_table[index]

def next_taken():
    global index
    global table_size
    global next_w
    index += 1
    if index < table_size:
        next_w = word_table[index]

