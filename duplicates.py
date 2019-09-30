seen = set()
uniq = []
for x in [1,2,3,2,4,5]:
    if x not in seen:
        uniq.append(x)
        seen.add(x)

print(uniq)