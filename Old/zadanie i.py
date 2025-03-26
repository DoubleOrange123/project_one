#найти номера всех симоволов i

s = 'imagination'
t = []
k = ''
m = ''
for i in range(0,len(s),1):
    if s[i] == 'i':
        t.append(i)
print (t)
for i in range(t[-1] + 1, len(s), 1):
     k += s[i]
for i in range(len(k) -1, -1, -1):
    m += k[i]
print(m)




#imagination
#i = 0123456789 10

#codeleet"
#01234567

#[4,5,6,7,0,2,1,3]