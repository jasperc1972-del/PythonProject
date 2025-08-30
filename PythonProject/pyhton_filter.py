#python filter

#可用來過濾可迭代的資料結構(list....)

friends=[
    ('Jasper',37),
    ('kelly',25),
    ('Mary',16),
    ('charles',19),
    ('John',16)
]

age_filter=lambda data: data[1]>=18
can_drink_friends=list(filter(age_filter,friends))
for friend in can_drink_friends:
    print(friend[0])
    print(friend[1])


