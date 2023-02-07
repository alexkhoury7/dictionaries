person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person.values())
print(type(person['pets']))

##print(person['children'][1])

print(person['pets']['cat'])

for i in person['children']:
    print(i)

for i in person['pets']:
    print(person['pets'][i])

