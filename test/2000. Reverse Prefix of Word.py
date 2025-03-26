word = "abcdefd"
ch = "d"
answer = ''
l = []
for i in range(len(word)):
    if word[i] != ch:
        answer += word[i]
    else:
        l.append(answer)
        answer = ''
for i in range(len(l) -1, -1, -1):
    l[i] += ch
print(l)

        