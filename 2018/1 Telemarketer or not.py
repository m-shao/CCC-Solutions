number = [int(input()) for i in range(4)]

en = [8,9]
if number[0] in en and number[-1] in en and number[1] == number[2]:
    print("ignore")
else:
    print("answer")