size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    col=0
    while col < size:
        print("*", end="")
        col = col + 1
    print()
    row=row+1
