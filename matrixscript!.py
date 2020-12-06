#Matrix Script!
def validate(x):
    f=['!','@','#','$','%','&',' ']
    while x in f:
        return True
        break
    else:
        return False
q,e=map(int,input().split())
l=[]
w=[]
for i in range(q):
    m=input()
    for j in range(e):
        w.append(m[j])
    l.append(w)
    w=[]
n=len(l[1])
k=''
r=0
o=0
f=0
s=''
g=0
while(n!=0):
    for j in l:
        while (validate(j[r])):
            s+=j[r]
            f+=1
            while g==0:
                k+=s
                s=''
                f=0
                break
            break
        else:
            while f>=1:
                k+=' '
                break
            k+=j[r]
            g=1
            s=''
            f=0
        o=o+1
    r=r+1
    n=n-1
k+=s
print(k)
###Second Least
##k=int(input())
##e=[]
##f=[]
##g=[]
##s=[]
##for i in range(k):
##    m=str(input())
##    l=float(input())
##    e.append(m)
##    f.append(l)
##    g.append(l)
##o=f.count(min(f))
##p=min(f)
##while o!=0:
##    f.remove(p)
##    o=o-1
##q=min(f)
##for i in range(len(g)):
##    if g[i]==q:
##        s.append(e[i])
##for i in s[::-1]:
##    print(i)
