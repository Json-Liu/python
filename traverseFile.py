#!/usr/bin/python
# -*- coding:UTF-8 -*-
filePath = '/home/jonnyLiu/py/fileTest.txt'

def doSomething(str): #定义一个函数 对文件中的字符串做一些操作 这里以打印内容为例子
	print str 

with open(filePath,'r') as fr:
	for line in fr:
		doSomething(line) 
