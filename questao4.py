pilha = []

for i in range(0,10):
    pilha.append(input())

print()

for i in range(0,10):
    print(pilha.pop())

if (len(pilha)) == 0:
    print("Sua pilha está vazia")