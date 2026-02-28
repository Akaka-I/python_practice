"""
随机生成n组双色球号码
"""
import random
n=int(input("请输入要生成的双色球号码组数："))
red_balls = list(range(1, 34))  # 红球号码范围
blue_balls = list(range(1, 17))  # 蓝球号码范围
for _ in range(n):
    red_selection = random.sample(red_balls, 6)  # 从红球中随机选择6个
    blue_selection = random.choice(blue_balls)  # 从蓝球中随机选择1个
    print(f"红球: {sorted(red_selection)}, 蓝球: {blue_selection}")