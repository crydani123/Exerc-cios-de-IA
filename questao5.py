from collections import deque

fila = deque([])

for i in range(0,10):
    fila.append(input())

print()

for i in range(0,10):
    print(fila.popleft())

if (len(fila)) == 0:
    print("Sua fila está vazia")