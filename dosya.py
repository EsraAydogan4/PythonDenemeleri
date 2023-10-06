with open("newfile.txt", "r+", encoding= "utf-8") as file: # dyayı kapatmaya gerek yok
    content = file.read() # reade sayı verirsek ne kadar satır okuyacağını söyleriz
    print(content)      #"r+" hem ookuma hem yazma modu
    print(file.tell()) # cursor un konumunu verir
    file.seek(0) # cursor en başa gelir istenilen konuma gönderilebilir
    content2 = file.read()
    print(content2)

    file.seek(0)
    file.write("deneme\n")
    print(content2)

with open("newfile.txt", "r+", encoding= "utf-8") as file: # a kursoru sona getirir
    content = file.read()
    content = "serife\n" + content
    print(file.read())
    file.seek(0)
    file.write(content)

with open("newfile.txt", "r", encoding= "utf-8") as file: # a kursoru sona getirir
    print(file.read())

with open("newfile.txt", "r+", encoding= "utf-8") as file: # a kursoru sona getirir
    list = file.readlines()
    list.insert(1, "Tuğba Aşık\n")
    
    file.seek(0)
    file.writelines(list) # aşağıdaki kod satırkarını tek sarırda yapar
    # for i in list:
    #     file.write(i)

with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())
    

def not_hesapla(satir):
        satir = satir[:-1]
        liste = satir.split(":")
        print(liste[0])
        print(liste[1])

not_hesapla(2)