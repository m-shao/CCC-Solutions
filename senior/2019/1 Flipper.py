line = input()

arr1 = [1,2]
arr2 = [3,4]

order = 1
order2 = 1

for character in line:
    if character == "H":
        if order == 2:
            order = 1
        else:
            order = 2
    elif character == "V":
        if order2 == 2:
            order2 = 1
        else:
            order2 = 2

if order2 == 2:
    arr1[0], arr1[1] = arr1[1], arr1[0]
    arr2[0], arr2[1] = arr2[1], arr2[0]
if order == 1:
    print(arr1[0], arr1[1])
    print(arr2[0], arr2[1])
else:
    print(arr2[0], arr2[1])
    print(arr1[0], arr1[1])