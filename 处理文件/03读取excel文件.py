import xlrd

# 使用xlrd模块的open_workbook函数打开指定Excel文件并获得Book对象（工作簿）
wb=xlrd.open_workbook('处理文件\\2022年股票数据.xls')
sheetnames=wb.sheet_names()  # 获取工作簿中所有工作表的名称
print(sheetnames)
sheet = wb.sheet_by_name(sheetnames[0])  # 根据工作表名称获取工作表对象
print(sheet.nrows,sheet.ncols)  # 获取工作表的行数和列数
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        value = sheet.cell_value(row, col)  # 获取指定单元格的值
        if row>0:
            if col==0:
                value=xlrd.xldate_as_tuple(value,0)  # 将Excel中的日期格式转换为Python的时间元组
                value=f'{value[0]}年{value[1]:>02d}月{value[2]:>02d}日'  # 格式化日期字符串
            else:
                value=f'{value:.2f}'  # 将数值格式化为保留两位小数的字符串
        print(value,end='\t')  # 输出单元格的值，并使用制表符分隔')
    print()  # 换行
last_cell_type=sheet.cell_type(sheet.nrows-1,sheet.ncols-1)  # 获取最后一个单元格的类型
print(last_cell_type)  # 输出最后一个单元格的类型
print(sheet.row_values(0))  # 获取第一行的所有单元格的值
print(sheet.row_slice(3,0,5))  # 获取第四行的第1到第5个单元格的对象列表