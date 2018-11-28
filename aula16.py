import random
num = []
for i in range(0,10):
    num.append(random.randrange(0,100))

num.append(5)
print(num)

if 5 in num:

    print("indice ", num.index(5))
else:
    print("Não achei")
num.sort(reverse=True)
print(num)