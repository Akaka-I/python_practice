import csv
with open('处理文件\scores.csv', 'r') as file:
    reader = csv.reader(file, delimiter='|', quoting=csv.QUOTE_ALL)
    for data_list in reader:
        print(reader.line_num, end='\t') # 输出行号
        for elem in data_list: # 输出每个元素
            print(elem, end='\t')
        print()