import random
num=[1,2,3,4,5,6]
lanc=[]

for i in range(100):
    lanc.append(random.choice(num))

print("Resultado\n")
print("numero 1:",lanc.count(1))
print("numero 2:",lanc.count(2))
print("numero 3:",lanc.count(3))
print("numero 4:",lanc.count(4))
print("numero 5:",lanc.count(5))
print("numero 6:",lanc.count(6))
