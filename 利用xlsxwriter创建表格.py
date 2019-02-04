#首先需要按照第三方库xlsxwriter
#如何讲数据写入表格中
import xlsxwriter
workbook = xlsxwriter.Workbook('chart_data_table1.xlsx') #可以生成.xls文件但是会报错
worksheet = workbook.add_worksheet('Sheet1') #工作页
#准备测试数据
bold = workbook.add_format({'bold': 1})#表的格式
headings = ['Number', 'Batch 1', 'Batch 2']#表的表头
data = [
  [2, 3, 4, 5, 6, 7],#列的形式传入表格
  [10, 40, 50, 20, 10, 50],
  [30, 60, 70, 50, 40, 30],
]
#插入数据
worksheet.write_row('A1', headings, bold)#行插入操作 注意这里的'A1'
worksheet.write_column('A2', data[0])#列插入操作 注意这里的'A2'
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])

workbook.close()
