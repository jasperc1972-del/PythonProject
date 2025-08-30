# python map

# map(函式,可迭代[列表])

store=[
    ('襯衫' ,800),
    ('褲子' ,1000),
    ('夾克' ,500),
    ('襪子' ,500)
]
#轉換歐元
# to_euros=lambda data:(data[0],data[1]*0.82)
# store_euros=list(map(to_euros,store))
# print(store_euros)
#轉換台幣
# to_ntd=lambda data:(data[0],data[1]*30)
# store_ntd=list(map(to_ntd,store))
# print(store_ntd)
#轉換美金
to_usd=lambda data:(data[0],round(data[1]/30) )
store_usd=list(map(to_usd,store))
print(store_usd)
#進行迭代
for item in store_usd:
    print(item)