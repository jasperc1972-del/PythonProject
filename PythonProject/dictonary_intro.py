#dictionary
# consists of key & value There is order and variability but no repetition

capital={
    "United States":"Washington, D.C.",
    "United Kingdom": "London",
    "Brazil": "Brasília",
    "Canada":"Ottawa",
    "France":"Paris",
    "Germany":"Berlin",
}

# get() 取得鍵值對
print(capital.get("Germany"))
print(capital.get("United States"))
print(capital.get("United Kingdom"))
# update()更新鍵值對
capital.update({"Australia": "Canberra"})
print(capital)
# pop() 刪除鍵值對
capital.pop("Australia")
print(capital)
# values() 所有值鍵值對
print(capital.values())
#items()
print(capital.items())


