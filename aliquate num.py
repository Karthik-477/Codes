k=int(input())
f=k
print(k,end=' ')
def divsors(x,c=0):
    for i in range(1,x):
        if x%i==0:
            c+=i
    return c
while True:
    k=divsors(k)
    if k==f:break
    print(k,end=' ')
    if k==0 :break
    f=k

















