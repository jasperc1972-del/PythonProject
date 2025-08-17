# for loop
# 1 to 10
# in + 可迭代物件


# for num in range(1,11):
#     print(num)

# 倒著數  10.9.8.7....1

# for reversed_num in reversed(range(1,11)):
#     print(reversed_num)
# print(".......................")


credit_card="1234-5678-9012-3456"
for c in credit_card:
    if c=="8":
        #continue
        break
    else:
        print(c)



