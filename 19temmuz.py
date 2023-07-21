# def basma(*params):
#     dizi = list(params) 3/3=0
#     print(dizi)      3/2=1  3/1=2
#     return dizi
# basma("elma", "armut", "kiwi")  


     
# def asallar(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2 + 1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)

#asallar(3, 17)


# liste = []
# def tambolen(sayi):
#     for s in range(1,sayi + 1):
#         if sayi % s == 0:
#             liste.append(s)
# tambolen(8)

# print(liste)
import random
result = random.randint(1,100)
names = ["Ali", "Zeynep", "Pınar"]
# result = names[random.randint(0,len(names)-1)]
result = random.choice(names) # dizi yerine string bir dizi verirsek bir harf seçer
liste = list(range(100))
result = random.sample(liste,3) # names içinde random seçim yapabiliriz


print(result)

