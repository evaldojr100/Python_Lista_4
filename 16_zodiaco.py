'''O Zodíaco chinês é composto por animais com ciclo de 12 anos. Uma maneira
simplificada de identificá-lo é verificando-se apenas o ano de seu nascimento do seguinte
modo:
Crie uma lista com os signos
B. Crie uma lista com a data de aniversário dos membros de sua família
C. Usando as listas criadas nos itens a e b, mostre o signo de cada membro de sua família.
Salve o algoritmo como “​ 16_zodiaco.py'''

signos=("Macaco","Galo","Cão","Porco","Rato","Boi","Tigre","Coelho","Dragão","Serpente","Cavalo","Carneiro")
data=[]

membros=int(input("Quantos membros vc quer adicionar? "))

for i in range(membros):
    data.append(input("Digite a data de nascimento do %d membro:" % (i+1)))

for i in data:
    print(data.index(i)+1,"Membro",signos[int(i[0:2]) % 12])
