# print(int)+(min({abs(int(sum([2.5,7.5,10.0,4.0])/len([2.5,7.5,10.0,4.0]))-i) for i in [2.5,7.5,10.0,4.0]})))

'''lista,lista2=[2.5,7.5,10,4.0],[]
{lista2.append(abs(i-6.0)) for i in lista}
print(lista[lista2.index(min(lista2))])'''



print(min({abs(i-(sum([2.5,7.5,10.0,4.0])/len([2.5,7.5,10.0,])))if 6.0<i else abs(i+(sum([2.5,7.5,10.0,4.0])/len([2.5,7.5,10.0,4.0])))for i in [2.5,7.5,10,4.0]}))



