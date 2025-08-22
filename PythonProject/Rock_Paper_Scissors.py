#剪刀石頭布的遊戲規則
# 剪刀石頭布的遊戲規則很簡單：
# 至少兩個人同時比出「石頭」（握拳）、「剪刀」
# （食指與中指伸直）或「布」（五指伸直張開手掌）
# 三種手勢之一。 其勝負關係為：石頭贏剪刀、剪刀贏布，而布則贏石頭。
# 若比出相同的手勢，則為平手，需重新比一次

import random



player=None
computer=None
running=True
op1=("scissors","rock","paper")
while running:
    player=input("key in scissors,rock,paper:")
    while player not in op1:
        input("key in error, please key in scissors,rock,paper")
    computer=random.choice(op1)
    print(f"玩家:{player},電腦:{computer}")
    if player == computer:
        print("平手")
    elif player=="scissors" and computer=="paper":
        print("玩家勝利")
    elif player=="rock" and computer=="scissors":
        print("玩家勝利")
    elif player=="paper" and computer=="rock":
        print("玩家勝利")
    else:
        print("電腦贏了")
    play_again=input("還要再玩嗎? (y/n)").lower()
    if not play_again == "y":
        running=False

print("謝謝你玩這遊戲!")
