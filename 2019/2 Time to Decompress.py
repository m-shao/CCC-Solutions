L = int(input())
code = [input().split() for i in range(L)]

for msg in code:
    print(msg[1]*int(msg[0]))
