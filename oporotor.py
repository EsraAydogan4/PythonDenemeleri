# x, y, z = 2, 5, 10

# numbers = 1, 5, 7, 10, 6

# a = int(input("1. sayı: "))
# b = int(input("2. sayı: "))
# result = (a * b) - (x+y+z)
# print(result)

# result = y//x
# print(result)

# result = (x+y+z)%3
# print(result)

# result = y**x
# print(result)

# x, *y, z = numbers # y ortadaki tüm elemanları alır
# print(z)
# names =('esma', 'esra', 'esin')

# for n in names: # n = names
#     #print(f"isimler {n} ")
#     print(n)

# sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# for sayi in sayilar:
#     if sayi%3 == 0:
#         print(sayi)

# for n in sayilar:
#     if n%2 == 1:
#         print(n**2)

# sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']
# for s in sehirler:
#     if len(s)<=5:
#         print(s)
numbers = [ x for x in range(10)]
print(numbers)
numbers = []
for x in range(10):
    numbers.append(x)
print(numbers)

result = [x if x%2==0 else 'TEK' for x in range(1,10)]
print(result)

# for x in range(3):
#     for y in range(3):
#         result.append((x,y))

s =[(x,y) for x in range(3) for y in range(3)]
print(s)    