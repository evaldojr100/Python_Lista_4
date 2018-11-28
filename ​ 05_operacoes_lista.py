''' (PUC-RIO) Dada uma lista de números inteiros:
A.exiba maior elemento
B.exiba a soma dos elementos
C.exiba o número de ocorrências do primeiro elemento da lista
D.exiba a média dos elementos
E.exiba a soma dos elementos com valor negativo'''

num=[-2,-5,1,22,3,41,5,60,5,82,91,10,0]

print("Maior Elemento:",max(num))
print("Soma dos Elementos:",sum(num))
print("número de ocorrências do primeiro elemento da lista:",num.count(num[0]))
print("média dos elementos:",sum(num)/len(num))
print("Soma dos elementos negativos:",sum(i for i in num if i < 0))


