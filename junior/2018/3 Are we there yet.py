distances = list(map(int, input().split()))
cities = [0]

city = 0

for distance in distances:
    city += distance
    cities.append(city)
    
for a in cities:
    for b in cities:
        print(abs(a-b), end=" ")
    print("")