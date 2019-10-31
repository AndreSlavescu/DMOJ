#https://dmoj.ca/problem/ccc13j2

word = input()

rotating_letters = ["I", "O", "S", "H", "Z", "X", "N"]

for i in range(0,len(word)):
    if word[i] in rotating_letters:
        pass
    else:
        pass

if word[i] not in rotating_letters:
    print("NO")
else:
    print("YES")
