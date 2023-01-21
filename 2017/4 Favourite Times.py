m = int(input())
hours = 12
minutes = 00
total = 0
extra = m % (12 * 60)

if m > 720:
    dayNum = m // (12 * 60)
    total += 31 * dayNum
    while extra > 0:
        minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        if hours == 13:
            hours = 1
        
        if hours >= 10:
            if (hours // 10 - hours % 10) == (hours % 10 - minutes // 10) == (minutes//10 - minutes % 10):
                total += 1
        else: 
            if (hours % 10 - minutes // 10) == (minutes//10 - minutes % 10):
                total += 1
        extra -= 1
else:
    while m > 0:
        minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        if hours == 13:
            hours = 1
        
        if hours >= 10:
            if (hours // 10 - hours % 10) == (hours % 10 - minutes // 10) == (minutes//10 - minutes % 10):
                total += 1
        else: 
            if (hours % 10 - minutes // 10) == (minutes//10 - minutes % 10):
                total += 1
        m -= 1
    
print(total)