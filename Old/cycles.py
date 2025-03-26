count_ages = int(input())
l = []
for i in range(count_ages):
    l.append(int(input()))
for i in range(count_ages):
    if l[i] % 2 == 0:
        l[i] = l[i] * 2
    else: 
        l[i] = l[i] * l[i]
print (l)        