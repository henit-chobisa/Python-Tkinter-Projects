n1 = int(input())
n2 = int(input())
n3 = int(input())
n = int(input())
k = []
for x in range(0,n1+1):
    for y in range(0,n2+1):
        for z in range(0,n3+1):
            if x + y + z==n:
                k.append([x,y,z])
            else:
                continue

print(k) 