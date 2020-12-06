k=input()
res=1
for i in k:
    res*=int(i)
if int(k)%res==0:
    print('YES')
else:
    print('NO')
