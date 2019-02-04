import os
os.listdir('.')#列出当前目录的文件
os.makedirs('xx')#在当前目录下创建一个叫xx的目录
os.removedirs('xxxx')#删除xxx目录
os.chdir('')#用于改变当前工作目录到指定的路径。

#可利用poen或者system 来直接执行Linux的命令
#例子 ls
os.system('ls')
os.popen('ls').read()
#区别就是system 执行返回布尔值,poen的返回值可读

