"""
玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；
玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
玩家如果摇出其他点数则游戏继续，
玩家重新摇骰子，
如果玩家摇出了 7 点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数玩家继续摇骰子，直到分出胜负。
为了增加代码的趣味性，我们设定游戏开始时玩家有 1000 元的赌注，每局游戏开始之前，
玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励，如果庄家获胜，玩家就会输掉自己下注的金额。
游戏结束的条件是玩家破产（输光所有的赌注）。
"""

import random
money = 1000  # 初始赌注
while money > 0:
    bet = int(input(f"你当前有 {money} 元，请下注: "))
    if bet > money:
        print("你的赌注超过了你的总金额，请重新下注。")
        continue

    # 玩家第一次摇骰子
    first_roll = random.randint(1, 6) + random.randint(1, 6)
    print(f"你摇出了 {first_roll} 点。")

    if first_roll in [7, 11]:
        print("你赢了！")
        money += bet
    elif first_roll in [2, 3, 12]:
        print("庄家赢了！")
        money -= bet
    else:
        point = first_roll
        print(f"你的点数是 {point}，继续摇骰子...")
        while True:
            roll = random.randint(1, 6) + random.randint(1, 6)
            print(f"你摇出了 {roll} 点。")
            if roll == 7:
                print("庄家赢了！")
                money -= bet
                break
            elif roll == point:
                print("你赢了！")
                money += bet
                break