#!/usr/bin/python
# -*- coding:UTF-8 -*-

def doSomething(str):
	print str

readFilePath = '/home/jonnyLiu/readFile'
writeFilePath = '/home/jonnyLiu/readFile'

with open(readFilePath,'r') as fr:	#只读
	for eachLine in fr:
		doSomething(eachLine)
toBeWriteContents = ['Hello','JonnyLiu']

with open(writeFilePath,'w' ) as fw: #覆盖写
	for eachLine in toBeWriteContents:
		fw.write(eachLine + '\n')

with open(writeFilePath,'a' ) as fw: #追加
	for eachLine in toBeWriteContents:
		fw.write(eachLine + '\n')
