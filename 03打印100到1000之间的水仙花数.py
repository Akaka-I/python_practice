"""
水仙花数是指一个三位数，其各位数字的立方和等于该数本身。例如：153就是一个水仙花数，因为1^3 + 5^3 + 3^3 = 153。
"""
for num in range(100, 1000):
    # 将数字转换为字符串，以便逐位处理
    str_num = str(num)
    n=len(str_num)
    # 计算各位数字的立方和
    sum_of_cubes = sum(int(digit) ** n for digit in str_num)
    
    # 判断是否是水仙花数
    if sum_of_cubes == num:
        print(num)