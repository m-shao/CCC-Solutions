n = int(input())

data1 = [list(map(int, input().split())) for i in range (n)]

corners = [data1[0][0], data1[0][-1],data1[-1][-1], data1[-1][0]]
small = 10**9 + 1
smallInd = 0


for count, corner in enumerate(corners):
    if corner < small:
        small = corner
        smallInd = count
if smallInd == 0:
    for row in range(n):
        for col in range(n):
            print(data1[row][col], end=" ")
        print("")
elif smallInd == 1:
    for row in range(n - 1, -1, -1):
        for col in range(n):
            print(data1[col][row], end=" ")
        print("")
elif smallInd == 2:
    for row in range(n - 1, -1, -1):
        for col in range(n - 1, -1, -1):
            print(data1[row][col], end=" ")
        print("")
elif smallInd == 3:
    for row in range(n):
        for col in range(n - 1, -1, -1):
            print(data1[col][row], end=" ")
        print("")