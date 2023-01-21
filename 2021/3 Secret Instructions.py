a = 0
ins = []
while(1):
    a = int(input())
    if a == 99999:
        break
    ins.append(a)

for a in ins:
    b = a//1000
    sum1 = b//10 + b%10
    
    if sum1 % 2:
        last = "left"
        print(last, end=" ")
    elif sum1 == 0:
        print(last, end=" ")
    else:
        last = "right"
        print(last, end=" ")
    c = a%1000
    print(c)