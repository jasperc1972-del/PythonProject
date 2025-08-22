
# 猜數字遊戲
import random

mi = 1
ma = 100
num = random.randint(mi, ma)  # 隨機產生目標數字
guesses = 0

print("歡迎來玩猜數字遊戲！")
print(f"我已經想好了一個 {mi} ~ {ma} 之間的數字。")

while True:
    try:
        guess = int(input(f"\n請猜一個 {mi} ~ {ma} 之間的數字: "))
        guesses += 1

        if guess < num:
            print("你猜的數字太小了！")
        elif guess > num:
            print("你猜的數字太大了！")
        else:
            print(f"🎉 恭喜你猜對了！這個數字就是 {num} 🎉")
            print(f"總共猜了 {guesses} 次。")
            break

    except ValueError:
        print("⚠️ 輸入錯誤！請輸入一個整數。")
    except KeyboardInterrupt:
        print("\n遊戲被中斷，再見！")
        break
