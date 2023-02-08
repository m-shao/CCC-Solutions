names = []
bids = []
n = int(input())
for i in range(n):
    names.append(input())
    bids.append(int(input()))

bids2 = list(bids)
bids.sort()

largest = bids2.index(int(bids[-1]))

print(names[largest])
