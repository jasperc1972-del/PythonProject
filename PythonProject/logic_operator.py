# 邏輯運算子
# and/or/not

#and
# 輸入溫度（攝氏）
temperature = float(input("請輸入目前溫度（°C）："))
#humidity=float(input("請輸入目前濕度 RH）："))
# 判斷環境狀況
# if temperature > 0 and temperature < 30:
#     print("環境狀況：非常舒適")
# else :
#     print("環境狀況：不舒服")

# or
if temperature <= 0 or temperature >= 30:
    print("環境狀況：非常不舒適")
else:
    print("環境狀況：非常舒適")


