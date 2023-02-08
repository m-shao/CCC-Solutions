n = int(input())
k = int(input())
t = n

for i in range(k):
    n = n * 10
    t += n
    
print(t)