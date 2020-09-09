#https://dmoj.ca/problem/pwindsor18p1

string1 = input()
result = string1.find("java")
if result > -1:
    print(result)
else:
    print(len(string1))
