def func1():
    print("HELLO")

print(func1.__doc__)

''' 
"r" = read
"w" = write
"b" = binary
"+" = read and write both
"a" = append
"x" = xclusive file
"t" = text mode'''

def fun(a, b):
    
    try:
        k = int(a)+int(b)
        return k
    except Exception as e:
        print(e)

i = input()
j = input()

print(fun.__doc__)