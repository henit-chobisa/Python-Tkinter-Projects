n = int(input("Please Give n"))
k = int(input("Bool 1 for star pattern and 0 for reverse star pattern"))
p = bool(k)
if p == True:
    
    for i in range(1, n+1):
        print("*"*i)
elif p == False:
    
    for j in range(0, n):
        
        j = n-j
        print("*"*j)
