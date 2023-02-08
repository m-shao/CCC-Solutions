n = int(input())
heights = list(map(int, input().split()))
widths = list(map(int, input().split()))

total = 0
for i in range(n):
    triHeight = abs(heights[i] - heights[i + 1])
    recArea = widths[i] * min(heights[i], heights[i + 1])
    triArea = widths[i] * triHeight / 2
    total += recArea + triArea

print(total)