l = [5,17,3,16,2,7]
# 5, 17,3, 16,2, 7
# 0, 1, 2, 3, 4, 5
# 7, 2, 16,3,17, 5

for i in range(0,len(l) // 2,1):
    l[i], l[len(l)-1-i] = l[len(l)-1-i], l[i]
print(l)