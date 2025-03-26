class Solution:
    def __init__(self, jewels: str, stones: str) -> int:
        self.jewels = jewels 
        self.stones = stones
t = Solution("aA","aAAbbbb" )
j = 0
for i in t.stones:
    if i in t.jewels:
        j += 1
print (j)