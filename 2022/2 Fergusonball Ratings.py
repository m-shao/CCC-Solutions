n = int(input())
star = [[int(input()), int(input())] for i in range(n)]

gold = True
count = 0

for player in star:
    rating = player[0]*5 - player[1]*3
    if rating > 40:
        count +=1
    else:
        gold = False

if gold:
    print(f"{count}+")
else:
    print(f"{count}")