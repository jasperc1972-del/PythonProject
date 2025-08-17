#nest loop 1

rows=int(input("please enter the number of rows:"))
cols=int(input("please enter the number of columns:"))
symbol=input("please enter the symbol:")
for i in range(rows):
    for j in range(cols):
        print(symbol,end=" ")
    print()