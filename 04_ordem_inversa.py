'''Ler uma lista de 10 números reais e mostre-os na ordem inversa'''

num=[]

for i in range(10):
    num.append(float(input("Digite um numero:")))

for i in range(9,0,-1):
    print(num[i])