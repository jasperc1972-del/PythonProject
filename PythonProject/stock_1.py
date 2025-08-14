import yfinance

print("OK", yfinance.__version__)

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 設定 matplotlib 中文字型與負號正常顯示
plt.rcParams['font.family'] = 'Microsoft JhengHei'  # 微軟正黑體
plt.rcParams['axes.unicode_minus'] = False

# 股票清單（可自行新增）
stocks = ["3013.TW", "2317.TW", "2454.TW"]  # 台積電、鴻海、聯發科

# 均線參數
short_window = 5
long_window = 20

for symbol in stocks:
    print(f"\n===== {symbol} =====")
    # 下載 6 個月資料
    df = yf.download(symbol, period="6mo", interval="1d")

    # 計算均線
    df['MA5'] = df['Close'].rolling(window=short_window).mean()
    df['MA20'] = df['Close'].rolling(window=long_window).mean()

    # 偵測黃金交叉
    df['GoldenCross'] = (df['MA5'].shift(1) < df['MA20'].shift(1)) & (df['MA5'] > df['MA20'])
    golden_cross_days = df[df['GoldenCross']]

    # 列出日期
    if not golden_cross_days.empty:
        print(f"黃金交叉日期：")
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

    plt.title(f"{symbol} 均線黃金交叉偵測")
    plt.xlabel("日期")
    plt.ylabel("價格 (NTD)")
    plt.legend()
    plt.grid(True)
    plt.show()