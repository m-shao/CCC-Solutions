'''
ONLY 8/15 OF THE POINTS ARE ACHIEVED
'''

r = int(input())
c = int(input())
room = []

for i in range(r):
    room.append(list(map(int, input().split())))

def getFactors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            if i <= r and num / i <= c:
                factors.append([i, int(num / i)])
    return factors

visited = []
    
def findPath(coord):
    og = list(coord)
    if og == [r,c]:
        return True
    if og not in visited:
        visited.append(og)
        coord = [coord[0] - 1, coord[1] - 1]
        factors = getFactors(room[coord[0]][coord[1]])
        if factors == []:
            return False
        for factor in factors:
            if factor != og:
                yes = findPath(factor)
                if yes:
                    return(yes)
        return(yes)
                
if findPath([1,1]):
    print("yes")
else: 
    print("no")