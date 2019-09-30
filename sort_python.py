data = [3, 1, 7, 2, 4, -1]
n = len(data)
for i in range(n):
    for j in range(1,n):
        if data[j-1] > data[j]:
          (data[j-1], data[j]) = (data[j], data[j-1])
print(data)
