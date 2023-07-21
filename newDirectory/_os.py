import os
import datetime

result = dir(os)
result = os.name

# dizin değiştirme
# os.chdir('C:\\')
# os.chdir('../..')

# klasör oluşturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasör")
# os.rename("newdirectory","yeniklasör")
# os.rmdir("newdirectory") # altdizinde klasör yoksa klasörü siler
# os.removedirs("yeniklasör/yeniklasör") # alt klasörü de gösterip siebiliriz

# listeleme
# result = os.listdir()
# result = os.listdir('C:\\')
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)


# etkin dizin öğrenme
# result = os.getcwd()


# result = os.stat("_datetime.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)  # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)  # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # değiştirilme tarihi

# os.system("notepad.exe") # istenilen bir dosy abu şekilde çalıştırılabilir

# path

result = os.path.abspath("_os.py")  # dosyanın konumunu verir
result = os.path.dirname("C:/python/advanced-modules/_os.py") 
result = os.path.dirname(os.path.abspath("_os.py")) # dosya ismi bilinen dosyanın tam yolunu bilir ve dizin ismini getirir
result = os.path.exists("C:/python/advanced-modules/_os1.py") # true false döner
result = os.path.exists("C:/python/advanced-modules")
result = os.path.isdir("C:/python/advanced-modules") #  true-false 
result = os.path.isfile("C:/python/advanced-modules/_os.py") 
result = os.path.join("C:\\","deneme","deneme1") 
result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")  # ismi ve dizini ayırır
# result = result[0]
result = result[1]

print(result)