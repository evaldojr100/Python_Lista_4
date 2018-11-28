lista_inicial=[12,14,15,16,18,20,24,26,28,32,34,38]
limite_inferior=13
limite_superior = 26
lista_aux=[]


for i in lista_inicial:
    if limite_inferior<=i<=limite_superior:
        lista_aux.append(i)

print(lista_aux)        