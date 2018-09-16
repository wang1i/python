from random import randint
num = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
color = ["clubs", "hearts", "diamonds", "spades"]
print("你抽的扑克牌是", num[randint(0, 12)], "of", color[randint(0, 3)])