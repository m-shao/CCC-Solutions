ins = input()

final = ""
lastIsNum = False
for instruction in ins:
    if instruction.isalpha():
        if lastIsNum:
            final += "\n"
            lastIsNum = False
        final += instruction
    elif instruction == "+":
        final += " tighten "
    elif instruction == "-":
        final += " loosen "
    elif instruction.isnumeric():
        final += instruction
        lastIsNum = True
        
print(final)