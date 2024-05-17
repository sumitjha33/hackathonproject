lst = [0,12]

lst2 = []
multi = 1
for i in lst:
    multi *= i

for i in lst:
    sel = int(multi/i)
    lst2.append(sel)

print(lst2)