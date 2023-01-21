total = []
for i in range(2):
    three = int(input())
    two = int(input())
    one = int(input())
    total.append(three*3+two*2+one)

if total[0] > total[1]:
    print("A")
elif total[0] == total[1]:
    print("T")
else:
    print("B")
    
