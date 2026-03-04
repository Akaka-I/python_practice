def is_prime(n:int):
    """判断一个数是否是素数"""
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# 示例使用
print(is_prime(11))  # 输出: True