"""
素数是只能被1和自身整除的正整数（不包括1）
"""
for num in range(2, 101): 
    is_prime = True 
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0: 
            is_prime = False 
            break 
    if is_prime: 
        print(num)