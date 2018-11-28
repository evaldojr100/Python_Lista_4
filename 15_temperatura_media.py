'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as
em uma lista. Em seguida, calcule a média anual das temperaturas e mostre a média calculada
juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''

meses=("Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")
temp=[]
for i in range(12):
    temp.append(float(input("Digite a media de temperatura de %s: "%(meses[i]))))

media_anual=sum(temp)/len(temp)
print("A media anual de temperatura é de :",media_anual)
print("Os meses que tivertam temperatura acima disso foram:\n")
for i in range(12):
    if temp[i]>=media_anual:
        print("Mes de",meses[i],"com media de",temp[i])
