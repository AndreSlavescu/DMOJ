#https://dmoj.ca/problem/ccc13j3
year = int(input())

nextyear = None

while nextyear is None:
    year = year+1
    nextyear = str(year)
    digits = {}
    for i in range(0, len(nextyear)):
        if not (nextyear[i] in digits):
            digits[nextyear[i]] = 1 
        else:
            nextyear = None
            break

print(nextyear)