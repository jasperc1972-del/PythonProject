import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

import matplotlib
print(matplotlib.__version__)
# 設定中文字體（避免繪圖中文字亂碼）
plt.rcParams["font.family"] = "Microsoft JhengHei"

# 均線參數
short_window = 5
long_window = 20

# 讀取上市櫃股票清單 (請先準備 tw_stock_list.csv, 格式: code,name)
try:
    stock_list_df = pd.read_csv("tw_stock_list.csv")  # 第一欄為股票代碼, 第二欄為名稱
except FileNotFoundError:
    print("tw_stock_list.csv 不存在，請先下載或建立股票清單")
    exit()

for idx, row in stock_list_df.iterrows():
    code = row['code']
    name = row['name']
    print(f"\n===== {code} ({name}) =====")

    try:
        # 抓取近 6 個月日線資料
        df = yf.download(code, period="6mo", interval="1d", auto_adjust=True)
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

        # 繪圖
        plt.figure(figsize=(10, 5))
        plt.plot(df.index, df['Close'], label="收盤價", color="blue")
        plt.plot(df.index, df['MA5'], label="MA5", color="orange")
        plt.plot(df.index, df['MA20'], label="MA20", color="green")
        plt.scatter(golden_cross_days.index, golden_cross_days['Close'],
                    label="黃金交叉", color="red", marker="^", s=100)
        plt.title(f"{code} ({name}) 均線黃金交叉偵測")
        plt.xlabel("日期")
        plt.ylabel("價格 (NTD)")
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"股票 {code} 發生錯誤: {e}")

print("程式執行完成！")
