import difflib

text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""

text1_lines = text1.splitlines()

text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""

text2_lines = text2.splitlines()
d = difflib.HtmlDiff()#生成HTML文档
diff = d.make_file(text1_lines, text2_lines)  # 采用compare方法对字符串进行比较
diff = diff.encode('utf-8')#把生产的数据 格式从字节变成str 编码为utf-8
with open('compare.html','wb') as f:
    f.write(diff)
