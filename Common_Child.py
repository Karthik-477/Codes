# Complete the commonChild function below.
def commonChild(s1, s2):
    count=0
    for i in s1:
        if i in s2:
            s2.remove(i)
            count+=1
    return count
if __name__ == '__main__':
    s1=[]
    s2=[]
    d1 = input()
    for i in d1:
        s1.append(i)

    d2 = input()
    for i in d2:
        s2.append(i)

    result = commonChild(s1, s2)

    print(result)
