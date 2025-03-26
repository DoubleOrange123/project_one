candies = [2,3,5,1,3]
extraCandies = 3
t = 0
l = []
p = candies[0]
for candy in range(len(candies)):
    if candies[candy] >= p:
                p = candies[candy]
print(p)
for i in range(len(candies)):
    if candies[i] + extraCandies >= p:
        l.append(True)
    else:
        l.append(False)
print(l)

