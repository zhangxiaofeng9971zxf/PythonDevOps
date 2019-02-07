#找到文件夹中后缀为.jpg的文件
#将文件重命名
import os
path ='/home/zxf/PythonCrawler-'
filelist = os.listdir(path)
totale_num = len(filelist)
i =1
for  item in filelist:
    if item.endswith('.jpg'):
        src = os.path.join(os.path.abspath(path),item)
        dist =os.path.join(os.path.abspath(path), ''+str(i) + '.jpg')
        try:
            os.rename(src,dist)#src 是要改的文件名称 #dist是改好的名称
            i = i+1
        except:
            continue
