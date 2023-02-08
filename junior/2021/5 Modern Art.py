m = int(input())
n = int(input())
k = int(input())

ins = []
for i in range(k):
    ins.append(input().split())
    ins[i][1] = int(ins[i][1]) - 1

gold = 0

touchedM = [0 for i in range(m)]
touchedN = [0 for i in range(n)]

for i in ins:
    if i[0] == "R":
        touchedM[i[1]] += 1
    if i[0] == "C":
        touchedN[i[1]] += 1

count1 = 0

for i in touchedM:
    if i%2 == 1:
        gold += n
        count1 += 1
for i in touchedN:
    if i%2:
        gold += m
        gold -= 2 * count1

print(gold)
        