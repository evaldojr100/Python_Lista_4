'''Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR
e os números ímpares em uma lista IMPAR. Imprima as listas PAR e IMPAR. Salve o algoritmo
como'''

num =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
par=[]
impar=[]

for i in num:
    if i%2==0:
        par.append(i)
    else:
        impar.append(i)

print("Pares: ",par)
print("Impares: ",impar)