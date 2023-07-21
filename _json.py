import json

person_string = '{"name": "Ali","languages":["python","C#"]}' # string json formatı bu şekilde
# result = person["languages"]  dışındaki ' olmadan bu şekilde kullanılabilir
# result = person["languages"][0]


# JSON string to dict
# result = json.loads(person_string) #artık istenilen bilgiye ulaşılabilir

# with open ("person.json") as f:  dosyadan bilgiler bu şekilde alınabilir
#     data = json.load(f)
#     print(data)

person_dict = {
    "name": "Ali",
    "langueges" : ["python","C#"]
}

# with open("person.json","w") as f:
#     json.dump(person_dict, f)
#print(type(result))
# print(result)