n = int(input())
arr = []
largest = []
smallest = []

for i in range(n):
  arr.append(list(map(int, input().split(","))))
largest = [0,0]
smallest = [100, 100]

for j in range(len(arr)):
  for p in range(2):
    if largest[p] < arr[j][p]:
      largest[p] = arr[j][p]
    if smallest[p] > arr[j][p]:
      smallest[p] = arr[j][p]

print(str(smallest[0] - 1) + ",", (smallest[1] - 1))
print(str(largest[0] + 1) + ",", (largest[1] + 1))