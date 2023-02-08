n = int(input())

count = 0

for i in range(n//5 + 1):
    remainder = n - 5*i 
    if remainder % 4 == 0:
        count += 1

print(count)