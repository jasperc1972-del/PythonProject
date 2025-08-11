#python 重量轉換器

weight=float(input("enter your weight:"))
unit=input("enter your unit? kg/lb ").upper()
#print(f"your weight is {weight} and unit is: {unit}")


if unit == "LB":
    weight = weight /2.205
    new_unit = "KG"
elif unit == "KG":
    weight = weight * 2.205
    new_unit = "LB"
else:
   print("invalid unit")
   exit()
print(f"your weight is {weight} {new_unit}")
