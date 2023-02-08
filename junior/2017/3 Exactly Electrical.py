a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = int(input())
td = abs(a[0] - b[0]) + abs(a[1] - b[1])

c = c - td
if c < 0:
    print("N")
elif c % 2 == 0:
    print("Y")
else:
    print("N")
