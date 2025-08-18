# Sets ,list,tuple,Dictionary


#list列表

# fruits = ["apple", "banana", "cherry","guava"]
#print(fruits[1])
# for f in fruits:
#     print(f)

# fruits.append("orange")
#print(fruits)

# fruits.remove("banana")
# print(fruits)
#
# print(fruits.index("guava"))


# fruits.append("apple")
# fruits.append("apple")


#顯示有幾個apple
#print(fruits.count("apple"))

# fruits.reverse()
#
# print(fruits)

#set
fruits_set={"🍎","🍌","🍇","🫐"}
print(fruits_set)
fruits_set.add("🍎")
print(fruits_set)
#fruits_set.add("🍉")
#print(fruits_set)

# for f in fruits_set:
#     print(f,end=" ")

if "🍎" in fruits_set:
    print("there are an apple")
if "🍉" in fruits_set:
    print("there are an watermelon")
else:
    print("there are without watermelon")


