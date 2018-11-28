'''Crie uma lista com notas de 10 alunos, informados pelo usuário, e, em seguida, calcule a
média da sala e imprima. Salve o algoritmo como '''

notas =[]
soma=0
for i in range(10):
    notas.append(float(input("Digite a nota do %d° aluno:"%(i+1))))
    soma+=notas[i]

print("Media:",soma/len(notas))