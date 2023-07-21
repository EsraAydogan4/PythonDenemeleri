ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci ismi: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefone numarası: ")

# ogrenciler[number] = {
#     'ad' : name,
#     'soyad' : surname,
#     'telefon' : phone,
# }

ogrenciler.update({
    number:{
        'ad' : name,
        'soyad' : surname,
        'telefon' : phone
    }
})
print(ogrenciler)
