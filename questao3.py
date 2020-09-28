matriz = []

for i in range(0,10):
    row = []
    for j in range(0,10):
        row.append(input())
    matriz.append(row)
else:
    for i in range(0,10):
        print(matriz[i])

