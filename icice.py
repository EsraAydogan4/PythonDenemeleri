# import math
# import time

# def calculate_time(func):
#     def  inner(*args, **kwargs):

#         start = time.time()
#         time.sleep(1)

#         FutureWarning(*args, **kwargs) # istenilen sayıda parametre gönderilebilir

#         finish = time.time()
#         print("fonksiyon "+" "+func.__name__+ " "+str(finish-start)+" saniye sürdü")
#     return inner

# @calculate_time
# def usalma(a,b):
#     print(math.pow(a,b))

# @calculate_time  
# def faktoriyel(num):
#     print(math.factorial(num))

# @calculate_time
# def toplama(a,b):
#     print(a+b)


# toplama(3,5)
# usalma(2,3)
# faktoriyel(4)


# print(next(iterator)) # listedeki elemanları tek tek ekranan ayazdırır
# print(next(iterator)) # 6. elemanda bir hata alınır
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# liste = [1,2,3,4,5]
# iterator = iter(liste)

# while True: # hatayı çaılştırmıyor ve kodun çalışmasını devam ettiriyor
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

