'''1) Crie uma lista para armazenar 5 nomes de alunos informados pelo usuário. Imprima a lista.
Salve o algoritmo como 01_nomes_alunos.py'''

alunos=[]

for i in range(5):
    alunos.append(input("Digite o %d° nome:"%(i+1)))


print("\nLista de Alunos\n")
for i in alunos:
    print(i)