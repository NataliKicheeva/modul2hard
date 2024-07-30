n = int(input())
shifr = []
for i in range(1, n):
    for j in range(1, n):
        if n % (i + j) == 0 and i < j:
            shifr.append(i)
            shifr.append(j)
print(shifr[:len(shifr)])