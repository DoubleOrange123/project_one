#Input: s = "string"
s = 'string'
t = 0
n = ''
l = ''
for i in range(0, len(s), 1):
    if s[i] == 'i':
        t = i
for i in range(0, t, 1):
    n += s[i]   
for i in range(len(n) -1, -1, -1):
    l += n[i]
for i in range(t + 1, len(s), 1):
    l += s[i]
print(l)

#string
#012345


#str
#012

#["leet","code"]
#  