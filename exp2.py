k = input()
b = []
t  = len(k)
for i in range (0,t-1):
    if k[i] == 'a' or k[i]=='i' or k[i] =='e' or k[i]=='o' or k[i]=='u':
        b.append(k[i])
        
    else:
        continue
    
print(len(b))
