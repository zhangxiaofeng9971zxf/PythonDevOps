#模糊查询文件名称
#已知在某个文件夹中,文件名称 中有'08','.jpg'结尾的图片
#利用Python 查找具体文件名称
import os
path = '/home/zxf/PythonCrawler-'
files = os.listdir(path)#os模块中列出所有路径下的文件
#print(files)
for f in files:
     if '08' in f and f.endswith('.jpg') :#.endswit 结尾
        print(f)
