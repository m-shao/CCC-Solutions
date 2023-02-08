N = int(input())
yes = input()
tod = input()

count = 0

for a,b in zip(yes, tod):
    if a == b and a == "C":
        count += 1

print(count)