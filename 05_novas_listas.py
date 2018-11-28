'''A partir da lista a informada a seguir, crie novas listas:
numeros = [0, 1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 10, 11, 11, 12, 13]
Intervalo de 1 a 5
Intervalo de 8 a 12
Números pares
Números ímpares
Múltiplos de 3 e 5
Lista reversa'''

num=[0, 1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 10, 11, 11, 12, 13]
lista1=[]
lista2=[]
lista3=[]
lista4=[]
lista5=[]
lista6=[]


for i in num:
    if 1<=i<=5:
        lista1.append(i)
    if 8<=i<=12:
        lista2.append(i)
    if i%2==0:
        lista3.append(i)                    
    if i%2==1:
        lista4.append(i)
    if i%3==0 and i%5==0:
        lista5.append(i)
    lista6.append(i)
lista6.reverse()


print("Intervalo de 1 a 5:",lista1)
print("Intervalo de 8 a 12:",lista2)
print("Números pares:",lista3)
print("Números ímpares:",lista4)
print("Múltiplos de 3 e 5:",lista5)
print("Numeros Reversos:",lista6)