t = input()
s = input()
ins = False

for i in range(len(s)):
  s = s[1:] + s[0]
  if s in t:
    ins = True
    print("yes")
    break

if not ins:
  print("no")