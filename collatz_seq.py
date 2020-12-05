def collatz_seq(k,o=[]):
    o.clear()
    while True:
        if k%2==0:
            k=k//2
            o.append(k)
        else:
            k=3*k+1
            o.append(k)
        if k==1:
            return len(o)
i=1000000
z=0
f=0
count=i
while True:
    z=collatz_seq(i)
    if z>f:
        f=z
    count-=1
    i-=1
    if count==0:break
print(f,i)
