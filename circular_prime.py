def is_prime(y):
    for i in range(2,y):
        if y%i==0:
            return False
    else:
        return True
def cir_prime(x):
    s=str(x)
    d=0
    f=[]
    for i in s:
        f.append(i)
    z=len(f)
    while z:
        d=f[0]
        f.remove(d)
        f.append(d)
        w=''.join(f)
        if is_prime(int(w))==False:
            return False
        z-=1
    else:
        return True
res=0
for i in range(2,101):
    if is_prime(i):
        if cir_prime(i):
            print(i)
            res+=1
print(res)
