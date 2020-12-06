#fabinocci with formula
import math
def is_sqrt(v):
    f=math.sqrt(v)
    if f==int(f):
        return True
    return False
def is_fib(n):
    x=5*(n**2)-4#formulae
    y=5*(n**2)+4#formulae
    if is_sqrt(x) or is_sqrt(y):
        return True
    else:
        return False
i=int(input())
p=i
o=1
s=0
if is_fib(i)==False:
    while o!=0:
        while is_fib(i)==False:
            i=i-1
            is_fib(i)
        print(i)
        s+=i
        i=p-s
        if s==p:
            o=0

else:
    if is_fib(i)==True:
        i=i-1
    while is_fib(i)==False:
        is_fib(i)
        i=i-1
    print(i)
    print(p-i)
