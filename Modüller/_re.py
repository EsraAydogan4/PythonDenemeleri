import re
result = dir(re)
# re module
str = "Python kursu: Python Programlama Rehberiniz | 40 saat"
# re.findall()
result = re.findall("Python", str)
result = len(result)
# regular expression  düzenli ifadeler
# result = re.split(" ",str) # bboşluk olan kısımları böler  R dersek ifadeler rlerden itibare ayrılır

#result = re.sub(" ", "-",str) # boşlukları - ile değiştirir
# re.search("Python",str) arama yapar ve kaçıncı karakter göserir
# re.group() re.end() re.string
result = re.findall("sa*t",str) # 15. bölüm 3. video
result = re.findall("\APython",str) # | () \  \A \Z  \$a \b


print(result)