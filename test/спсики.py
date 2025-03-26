t = "Never ever just already" + ' '
k = ''
l = []
d = 2
y = ''
for i in t:
    if i != ' ':
        k += i
    else:
        l.append(k)
        k = ''
for i in range(d):
    y += l[i] + ' '    
print(y)

