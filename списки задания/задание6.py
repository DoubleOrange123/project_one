l=[]
l2=[]
numm = (int(input()))
for i in range(int(numm)):
    l.append(int(input()))
for i in range(1, len(l) - 1):
    if l[i] < l[i-1] and l[i] < l[i+1]:
        l2.append(l[i])
print(l2)