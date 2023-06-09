list=["a","c",["j","l","jjdjdjd"]]
for i in list:
    if len(i) > 3:
        print("sublist is present in list")
        break
else:
    print("sublist is not present in list")

