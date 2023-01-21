shelf = list(input())
l = shelf.count("L")
m = shelf.count("M")
s = shelf.count("S")

lSec = shelf[:l]
mSec = shelf[l: l+m]
sSec = shelf[-s:]

lc = 0
mc = 0
sc = 0

oc = 0 

count = 0

for book in lSec:
    if book != "L":
        lc += 1
        if book == "M":
            mc += 1

for book in mSec: 
    if book != "M":
        sc += 1
        if book == "L":
            oc += 1

print(lc + sc - min(mc,oc))