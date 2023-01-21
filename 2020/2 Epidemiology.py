p = int(input())
n = int(input())
r = int(input())
inf = n
total = n
count = 0

while True:
  if total > p:
    break
  total += inf * r
  inf = inf * r
  count += 1
  
print(count)