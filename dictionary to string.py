st = input("Enter a string: ")
dic = {}
for ch in st:
    if ch in dic:
        dic[ch] += 1
    else:
        dic[ch] = 1
print(dic)
