"""
简单起见，我们的扑克只有52张牌（没有大小王），游戏需要将 52 张牌发到 4 个玩家的手上，
每个玩家手上有 13 张牌，按照黑桃、红心、草花、方块的顺序和点数从小到大排列，暂时不实现其他的功能。
"""
from enum import Enum
import random
class Suit(Enum):
    """花色枚举类，包含黑桃、红心、草花、方块四种花色
    """
    SPADES, HEARTS, CLUBS, DIAMONDS = range(4)

class Card:
    """牌类，包含花色和点数两个属性
    """
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

    def __repr__(self):
        suites = ['♠', '♥', '♣', '♦']
        faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return f'{suites[self.suit.value]}{faces[self.face]}'
    
    def __lt__(self, other):
        """定义牌的大小比较方法，先比较花色，再比较点数
        """
        if self.suit.value != other.suit.value:
            return self.suit.value < other.suit.value
        else:
            return self.face < other.face

class Poker:
    """扑克类，包含一副牌和发牌方法
    """
    def __init__(self):
        self.cards = [Card(suit, face) for suit in Suit for face in range(13)]
        self.current = 0 # 当前发牌的位置

    def shuffle(self):
        """洗牌方法，随机打乱牌的顺序
        """
        self.current = 0
        random.shuffle(self.cards) # 使用random模块的shuffle函数打乱牌的顺序

    def deal(self, num_players=4):
        """发牌方法，将牌发给指定数量的玩家，默认是4个玩家
        """
        card=self.cards[self.current]
        self.current += 1
        return card
    @property
    def has_next(self):
        """判断是否还有牌可以发
        """
        return self.current < len(self.cards)

class Player:
    """玩家类，包含玩家的名字和手牌
    """
    def __init__(self, name):
        self.name = name
        self.cards = [] # 玩家手牌列表

    def get_one(self, card):
        """获取一张牌的方法，将牌添加到玩家的手牌列表中
        """
        self.cards.append(card)

    def arrange(self):
        """整理手牌的方法，将手牌按照花色和点数排序
        """
        self.cards.sort() 

poker=Poker() # 创建一副牌
poker.shuffle() # 洗牌
Players = [Player(f'玩家{i}') for i in range(1, 5)] # 创建4个玩家
while poker.has_next: # 当还有牌可以发时
    for player in Players: # 依次给每个玩家发牌
        if poker.has_next: # 如果还有牌可以发
            player.get_one(poker.deal()) # 给玩家发一张牌
for player in Players: # 依次整理每个玩家的手牌
    player.arrange() # 整理玩家的手牌
    print(f'{player.name}的手牌: {player.cards}') # 打印玩家的名字和手牌
