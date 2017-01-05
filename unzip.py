#!/usr/bin/python
# -*- coding:UTF-8 -*-
import os
#解压当前目录下的压缩包,目前支持 gz,tar,zip,rar,bz2 等5种打包的压缩包
currentPath = os.popen('pwd').readlines()[0].strip('\n')
print '当前解压目录为:' + currentPath
for root,dirs,files in os.walk(currentPath,topdown=False):
	for eachFile in files:
		if eachFile.endswith('gz'):
			os.system('gunzip ' + eachFile )
		elif eachFile.endswith('tar'):
			os.system('tar xvf ' + eachFile )
		elif eachFile.endswith('zip'):
			os.system('unzip ' + eachFile )	
		elif eachFile.endswith('rar'):
			os.system('rar x ' + eachFile )
		elif eachFile.endswith('bz2'):
			os.system('bunzip2 ' + eachFile )
		else:
			continue
