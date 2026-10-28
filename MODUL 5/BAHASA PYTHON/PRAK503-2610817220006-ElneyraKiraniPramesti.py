def maximal(a, b):
    return a if a > b else b

def minimal(a, b):
    return a if a < b else b

bilangan = int(input())
data = list(map(int, input().split()))
    
batas = 0
max = -100000
min = 100000
    
while batas < bilangan:
    nilai = data[batas]
    max = maximal(max, nilai)
    min = minimal(min, nilai)
    batas += 1
        
print(f"{max} {min}")