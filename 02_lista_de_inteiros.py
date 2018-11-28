'''2) Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na
lista. Salve o algoritmo como 02_lista_de_inteiros.'''

inteiro=[]

for i in range(5):
    inteiro.append(int(input("Digite um numero:")))

for i in inteiro:
    print("numero %d indice %d"%(i,inteiro.index(i)+1))