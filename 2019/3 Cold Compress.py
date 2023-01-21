N = int(input())

msg = [input() for i in range(N)]

for block in msg:
    count = 0
    block = block + " "
    for ind, letter in enumerate(block):
        prev = block[ind - 1]
        if letter != prev and ind != 0:
            print(count, end=" ")
            print(prev, end= " ")
            count = 1
        else:
            count += 1
    print("")

        