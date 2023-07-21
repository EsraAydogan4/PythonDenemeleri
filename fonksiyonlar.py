# 

# def yetki(page):
#     def inner(role):
#         if role == "admin":
#             return " {0} rolu {1} sayfasına ulaşabilir.".format(role, page)
#         else:
#             return " {0} rolu {1} sayfasına ulaşamaz.".format(role, page)
#     return inner
# user1 = yetki("product Edit")
# print(user1("admin"))
# print(user1("User"))

def my_decorator(func):
    def wrapper(name): # beraber çalışması gereken bir fonk. varsa aynı parametreleri alması gerekiyor
        print("önce")
        func(name) # işte bu 4. boyut hello çalıştı
        print("sonra")
    return wrapper
# def sayHello():
#     print("hello")
# def sayGreeting():
#     print("greeting")
# sayHello = my_decorator(sayHello) # iç içe burası önemli
# sayGreeting = my_decorator(sayGreeting)
# sayHello()
# sayGreeting()

@my_decorator # işlem kalabalığı azaldı ana fonksiyon otomatik helloyu çalıştırır
def sayHello(name): # parametre gönderir gibi gönderiyor
    print("hello", name)
sayHello("esra") # name bilgisini bu şekilde göndermek yeterli olmuyor 
