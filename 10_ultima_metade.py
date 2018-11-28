'''0) (PUC-RIO) Faça uma função que receba uma lista e exiba os elementos da última metade
na frente dos elementos da primeira metade. Salve o algoritmo como “​ 10_ultima_metade.py ​ ”.'''

lista=[]

while True:
    lista.append(int(input("Digite um numero:")))
    opcao = input("Deseja inserir um novo numero?:(s/n)")
    if opcao == 'n':
        break

tamanho = len(lista)
aux = len(lista)/2

print(lista[int(aux):tamanho],lista[0:int(aux)])