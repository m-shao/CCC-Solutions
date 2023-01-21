x = int(input())
must = [input().split() for i in range(x)]

y = int(input())
notbe = [input().split() for i in range(y)]

g = int(input())
groups = [input().split() for i in range(g)]

count = 0

tog = {}
apar = {}

for constraint in must:
    if constraint[0] in tog:
        tog[constraint[0]].append(constraint[1])
    else:
        tog[constraint[0]] = [constraint[1]]
    if constraint[1] in tog:
        tog[constraint[1]].append(constraint[0])
    else:
        tog[constraint[1]] = [constraint[0]]

for constraint in notbe:
    if constraint[0] in apar:
        apar[constraint[0]].append(constraint[1])
    else:
        apar[constraint[0]] = [constraint[1]]
    if constraint[1] in apar:
        apar[constraint[1]].append(constraint[0])
    else:
        apar[constraint[1]] = [constraint[0]]
        
for group in groups:
    for person in group:
        if person in tog:
            for constraint in tog[person]:
                if constraint not in group:
                    count += 1
                    tog[constraint].remove(person)
        if person in apar:
            for constraint in apar[person]:
                if constraint in group:
                    count += 1;
                    apar[constraint].remove(person)

print(count)