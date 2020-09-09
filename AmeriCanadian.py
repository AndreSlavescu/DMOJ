#https://dmoj.ca/src/3006018

#not the best way of solving, but it works.

resume = True
vowels = ["a", "o", "e", "i", "u"]
while resume == True:
    word = input()
    if len(word) > 3 and (word[-3] not in vowels) and (word[-2] == "o" and word[-1] == "r"):
        print(word[:-2]+ word[-2] + "u" + word[-1])
    elif word == "quit!":
        break
    else:
        print(word)
