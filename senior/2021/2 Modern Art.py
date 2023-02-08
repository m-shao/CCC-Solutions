m = int(input())
n = int(input())
k = int(input())
arr = [input().split() for i in range(k)]
for i, item in enumerate(arr):
  arr[i][1] = int(item[1])

rowChange = [0 for i in range(m)]
colChange = [0 for i in range(n)]

for ins in arr:
  if ins[0] == "R":
    rowChange[ins[1] - 1] += 1
  if ins[0] == "C":
    colChange[ins[1] - 1] += 1 

totalGold = 0
rowChangeCount = 0

for change in rowChange:
  notChanged = change%2
  if not notChanged:
    totalGold += n
    rowChangeCount += 1

for change in colChange:
  notChanged = change%2
  if not notChanged:
    totalGold += m
    totalGold -= rowChangeCount * 2

print(totalGold)
