'''(PUC-RIO) Dada duas listas:
A. exiba a união destas listas
B. exiba a interseção destas listas
C. exiba a intercalação destas listas, isto é, 1o da 1a lista, 1o da 2a lista, 2o da 1a lista, 2o da
2a lista, etc.'''

num1=[1,2,3,4,5]
num2=[6,7,8,9,1]
inter=[]
for i in num1:
    for j in num2:
       if i == j:
            inter.append(i)
print("Uniao das Listas:",num1+num2)
print("Interseção das listas:",inter)
for i in range(5):
    print(num1[i],num2[i])

