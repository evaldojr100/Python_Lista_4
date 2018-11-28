'''Foram anotadas as idades e alturas dos alunos de uma turma e armazenados
em uma lista cujos elementos são sublistas com dois elementos: o primeiro é a idade do aluno
e o segundo a sua altura. Mostre quantos alunos com mais de 13 anos possuem altura inferior
à média de altura desses alunos.'''

soma=0
idade_altura=[]
cont=0
maior13=0

while True:
    idade_altura.append(int(input("Digite a idade do aluno:")))
    cont+=1
    idade_altura.append(float(input("Digite a altura do aluno:")))
    soma+=idade_altura[cont]
    cont+=1
    aux=input("Deseja cadastrar outro aluno? (s/n)")
    print("\n")
    if aux=='n':
        break
media = soma/(len(idade_altura)/2)
for i in idade_altura:
    if idade_altura.index(i)%2==0:
        if i>13 and idade_altura[idade_altura.index(i)+1]<media:
            maior13+=1

print(maior13,"alunos tem mais que 13 anos e estão com altura abaixo da media")





