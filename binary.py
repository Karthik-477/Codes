k=input()
res=0
j=0
for i in range(len(k)-1,-1,-1):
    res+=(2**int(i))*int(k[j])
    j+=1
print(res)
