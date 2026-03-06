
import csv
import random


with open('scores.csv', 'w') as file:
    writer = csv.writer(file, delimiter='|',quoting=csv.QUOTE_ALL)
    writer.writerow(['姓名', '语文', '数学', '英语'])
    names = ['张三', '李四', '王五']
    for name in names:
        scores = [random.randint(60, 101) for _ in range(3)]
        scores.insert(0, name) # 将名字插入到分数列表的开头
        writer.writerow(scores) # 将名字和分数写入csv文件
