d = dict()
a = 'qwertyujmjg'
t = True
for x in a:
    if x not in d.keys():
        d[x] = 1
    else:
        d[x] = d[x] + 1
for x in d.values():
    if x > 1:
        t = False
if t == False:
    print('не уникально') 
else:
    print('уникально') 


