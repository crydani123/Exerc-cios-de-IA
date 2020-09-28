import heapq

class Atividade:
    def __init__(self,desc,prior):
        self.desc = desc
        self.prior = prior
    def inserir(self, lista):
        heapq.heappush(lista, (self.prior, self.desc))
    def remover(lista):
	    return heapq.heappop(lista)

fila = []

#inserir
Atividade('Lavar', 4).inserir(fila)
Atividade('Passar', 1).inserir(fila)
Atividade('Arrumar', 3).inserir(fila)
Atividade('Guardar', 2).inserir(fila)
Atividade('Cozinhar', 4).inserir(fila)
Atividade('Fazer a Feira', 5).inserir(fila)
Atividade('Estudar', 5).inserir(fila)
Atividade('Aula', 5).inserir(fila)
Atividade('Limpar', 3).inserir(fila)
Atividade('Organizar', 4).inserir(fila)

#remover
for i in range(len(fila)):
    print(Atividade.remover(fila))
