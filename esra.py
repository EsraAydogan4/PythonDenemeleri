liste = ["Bmw", "Mercedes", "Opel", "Mazda"]
# print(len(liste))

result = liste[0]
result = liste[-1]
#liste[-1] = "Toyota" 
result = liste
result = "Mercedes" in liste
result = liste[-2]
result = liste[:3]
liste[-2:] = ["Toyota", "Renault"]

result = liste + ["Audi", "Nissan"] # halen 4 elemanlı 
del liste[-1]
result= liste[::-1]
liste.append("Nissan")
result = liste
print(result)