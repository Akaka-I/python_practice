"""
将一颗色子掷6000次，统计每种点数出现的次数
"""
import random
counts = [0] * 6  # 初始化计数器
for _ in range(6000):
    roll = random.randint(1, 6)  # 掷色子，得到1到6之间的随机数
    counts[roll - 1] += 1  # 更新对应点数的计数
# 输出结果
for i in range(6):
    print(f"点数 {i + 1} 出现的次数: {counts[i]}")