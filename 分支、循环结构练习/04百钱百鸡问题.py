"""
百钱百鸡问题：公鸡5元一只，母鸡3元一只，小鸡1元三只。用100元买100只鸡，问公鸡、母鸡、小鸡各多少只？
"""
for rooster in range(0, 21):  # 公鸡最多20只
    for hen in range(0, 34):  # 母鸡最多33只
        chick = 100 - rooster - hen  # 小鸡数量
        if chick % 3 == 0:  # 小鸡必须是3的倍数
            if 5 * rooster + 3 * hen + chick // 3 == 100:  # 满足总价为100元
                print(f"公鸡: {rooster}只, 母鸡: {hen}只, 小鸡: {chick}只")