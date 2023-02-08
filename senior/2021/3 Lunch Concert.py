n = int(input())
friends = [list(map(int, input().split())) for i in range(n)]

def find_time(point):
    time = 0
    for friend in friends:
        if point >= friend[0] - friend[2] and point <= friend[0] + friend[2]:
            continue
        time += min(
            abs(point - (friend[0] - friend[2])) * friend[1],
            abs(point - (friend[0] + friend[2])) * friend[1])
    return time

field_length = max(friends, key=lambda x: x[0])[0] + 1

smallest = None;

left = 0
right = field_length
while True:
    length = right - left
    mid = left + length//2
    
    time0 = find_time(mid)
    time1 = find_time(mid - 1)
    time2 = find_time(mid + 1)

    if time0 < time1 and time0 < time2:
        smallest = time0
        break
    if time1 == time2:
        smallest = time0
        break
    elif time1 < time2:
        right = mid
    else:
        left = mid
    
print(smallest)
