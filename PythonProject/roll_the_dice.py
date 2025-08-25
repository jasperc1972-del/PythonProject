

import random

def roll_dice():
    # 產生 1 到 6 的隨機數字
    return random.randint(1, 6)

print("🎲 歡迎來到擲骰子遊戲！")
while True:
    user_input = input("要擲骰子嗎？(y/n): ")
    if user_input.lower() == "y":
        dice = roll_dice()
        print(f"你擲出了 {dice} 🎲")
    elif user_input.lower() == "n":
        print("遊戲結束，謝謝遊玩！")
        break
    else:
        print("請輸入 y 或 n！")
