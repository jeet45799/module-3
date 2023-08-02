d1={"Name":"jet" , "Age":25}
d2={"City": "Snagr", "Gender": "Male"}
d3={"Mark":423}
d4 = {}
for d in (d1, d2, d3): d4.update(d)
print(d4)
