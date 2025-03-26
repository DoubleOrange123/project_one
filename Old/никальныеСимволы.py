a = 'qwertyujmjg'
t = 0

for i in a:
    if a.count(i) == 1:
        t += 1
    else:
        pass
if t == len(a):
    print('уникально')
else:
    print('не уникально')