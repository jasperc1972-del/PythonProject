import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams


# yfinance → 下載股票資料
# pandas → 處理股票資料
# matplotlib → 繪圖
# font_manager → 解決中文字型顯示問題
# 設定中文字型（Windows 系統建議微軟正黑體）
rcParams['font.family'] = 'Microsoft JhengHei'
# 避免負號顯示成方塊
rcParams['axes.unicode_minus'] = False

print("程式開始執行...")

# -----------------------------
# 股票清單（可自行增減）
# -----------------------------
stock_list = [
    {"code": "2330.TW", "name": "台積電"},
    {"code": "2317.TW", "name": "鴻海"},
    {"code": "2454.TW", "name": "聯發科"},
    {"code": "6763.TWO", "name": "綠界科技"},
    # {"code": "2615.TW", "name": "萬海"},
    # {"code": "1101.TW", "name": "台泥"},
    # {"code": "1102.TW", "name": "亞泥"},
    # {"code": "3008.TW", "name": "大立光"},
    # 可以繼續加入更多股票
]

# -----------------------------
# 均線參數
# -----------------------------
short_window = 5
long_window = 20

# -----------------------------
# 主程式：檢測黃金交叉
# -----------------------------
for stock in stock_list:
    code = stock["code"]
    name = stock["name"]
    print(f"\n===== {code} ({name}) =====")

    # 下載 6 個月日線資料
    try:
        df = yf.download(code, period="6mo", interval="1d", auto_adjust=False)
    except Exception as e:
        print(f"下載失敗: {e}")
        continue

    if df.empty:
        print("資料空白，跳過此股票。")
        continue

    # 計算均線
    df['MA5'] = df['Close'].rolling(window=short_window).mean()
    df['MA20'] = df['Close'].rolling(window=long_window).mean()

    # 偵測黃金交叉
    df['GoldenCross'] = (df['MA5'].shift(1) < df['MA20'].shift(1)) & (df['MA5'] > df['MA20'])
    golden_cross_days = df[df['GoldenCross']]

    # 列出黃金交叉日期
    if not golden_cross_days.empty:
        print("黃金交叉日期：")
        for date in golden_cross_days.index:
            print(date.strftime('%Y-%m-%d'))
    else:
        print("最近沒有黃金交叉。")

    # 📈 繪圖
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Close'], label="收盤價", color="blue")
    plt.plot(df.index, df['MA5'], label="MA5", color="orange")
    plt.plot(df.index, df['MA20'], label="MA20", color="green")
    # 標註黃金交叉
    plt.scatter(golden_cross_days.index, golden_cross_days['Close'],
                label="黃金交叉", color="red", marker="^", s=100)
    plt.title(f"{code} ({name}) 均線黃金交叉偵測")
    plt.xlabel("日期")
    plt.ylabel("價格 (NTD)")
    plt.legend()
    plt.grid(True)
    plt.show()

print("\n程式執行完成！")
