
# while True:
#     try:
#         x = int(input("x: "))
#         y = int(input("y: "))
#         print(x/y)
#     # except ZeroDivisionError:
#     #     print("0 girilemez")
#     # except ValueError:
#     #     print("sayısal değer girin")
#     except (ZeroDivisionError,ValueError) as e :
#         print("yanlış değer girdiniz")
#         print(e)
#     # except Exception as ex: # hatayı da yazar
#     #     print("yanlış bilgi girdiniz.")
#     else: 
#         print("hey şey yolunda")
#         break # doğru şekilde girilene kadar döngü devam eder
#     # finally:   # dosya kullanıldıktan sonra kapatılmak için kullanılır
#     #     print("try except sonlandı")
# # kendin hata yaratabilirsin 
# if x>5:
#     raise Exception("x 5 ten olamaz")
# def check_password(psw): 
#     import re 
#     if len(psw) < 8:
#         raise Exception("parola en az 8 karakter olmalı")
#     elif not re.search("[a-z]",psw):
#         raise Exception("parola küçük harf içermeli")


# liste = ["1", "2","5a","10b", "10", "50"]
# for s in liste:
#     try:
#         result = int(s)
#         print(result)
#     except ValueError:
#         continue


# while True:
#     sayi = input('sayi: ')
#     if sayi== "q":
#         break
#     try:
#         result = float(sayi)
#         print("girilen sayi: ", result)
#     except:
#         print("geçersiz sayı")
#         continue




# def checkPassword(parola):
#     turkce = "şçğüöıİ"

#     for i in parola:
#         if i in turkce:
#             raise TypeError("türkçe karaketer içeremez")
#         else:
#             pass

#     print("geçerli parola")
# parola = input('parola: ')

# try:
#     checkPassword(parola)
# except TypeError as err:
#     print(err)

def faktoriyel(x):
    x = int(x)

    if x<0:
        raise ValueError("Negatif değer")
    
    result = 1

    for i in range(1, x+1):
        result *= i
    return result

for x in [5, 10, 20, -3, "10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
