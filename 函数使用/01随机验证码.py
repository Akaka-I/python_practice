"""
设计一个生成随机验证码的函数，验证码由数字和英文大小写字母构成，长度可以通过参数设置。
"""
import random
import string
All_CHARACTERS = string.ascii_letters + string.digits
def generate_verification_code(length):
    verification_code = ''.join(random.choice(All_CHARACTERS) for _ in range(length))
    return verification_code

# 示例使用
for _ in range(5):
    print(generate_verification_code(6))  # 生成长度为6的验证码