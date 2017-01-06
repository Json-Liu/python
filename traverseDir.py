#!/usr/bin/python
# -*- coding:UTF-8 -*-
import os

def doSomething(str): #定义一个函数 做一些操作 这里以打印输入内容为例
	print str 
	
def traverseDir(rootPath):
	for root,dirs,files in os.walk(rootPath,topdown=False):
		for name in files:
			doSomething(name) #打印文件名
			doSomething( os.path.join(root,name) ) #打印文件的绝对路径

rootPath = '/home/jonnyLiu/py'
traverseDir(rootPath)
