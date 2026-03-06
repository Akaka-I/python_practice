import random

import xlwt


student_names = ['张三','李四','王五','赵六','钱七']
scores = [[random.randint(50, 101) for _ in range(3)] for _ in range(5)]  
print(scores)  # 输出生成的学生成绩数据
wb=xlwt.Workbook()  # 创建一个新的Excel工作簿对象
sheet=wb.add_sheet('2022年学生成绩')  # 在工作簿中添加一个新的工作表，并指定名称
#添加表头数据
titles=['姓名','语文','数学','英语']
for index,title in enumerate(titles): #使用enumerate函数获取表头数据的索引和值
    sheet.write(0,index,title)  # 在第一行写入表头数据
for row in range(len(scores)):  # 从第二行开始写入学生成绩数据
    sheet.write(row+1,0,student_names[row])  # 在第一列写入学生姓名
    for col in range(len(scores[row])):  # 写入每个学生的成绩数据
        sheet.write(row+1,col+1,scores[row][col])  # 在对应的单元格写入成绩数据
wb.save('处理文件\\2022年学生成绩.xls')  # 将工作簿保存到指定路径下的Excel文件中