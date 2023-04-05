#slownik
users = {}
print(users)


users = {"weronika": "email@gmail.com",
         "test": "test@gmail.com",
         "admin":"admin@gmail.com"}


user1 = {"name": "weronika","email": "email@gmail.com"}
print(users)
print(user1)

print(users.get("weronika"))

#literowka
print(users.get("weronikaa"))
#jelsi nie ma takiego klucza
print(users.get("weronikaa","invalid username"))

print(users["weronika"])
#literowka
#print(users["weronikaa"])
myname = "weronikaa"
if myname in users:
    print(users[myname])

users[myname] = "weronikaa"
print(users)
#usuwanie
if myname in users:
        del users[myname]

print(users)

for e in users:
    print(e)

print("Key")

for e in users.keys():
    print(e)

print("Value")

for e in users.values():
    print(e)

print("Iteams")

print(users.items())

for key, value in users.items():
    print("key "+str(key)+" value: "+value)

sorted_dict={}
for key in sorted(users.keys()):
    value=users[key]
    sorted_dict[key] = value
print(sorted_dict)

users = {
    "weronika":100,
    "joe":90,
    "test": 60,
    "admin": 75
}
print(users)

def get_value(item):
    return item[1] #klucz, wartosc

#posortowac po wartosciach od najmniejszej do najwiekszej
sorted_users = sorted(users.items(), key=get_value)
print(sorted_users)

#po slowniku
sorted_users = dict(sorted_users)
print(sorted_users)

#posortowac po wartosciach od najwiekszej do najmiejszej
sorted_users = sorted(users.items(), key=get_value, reverse=True)
print(sorted_users)

user1={"weronika": "email@gmail.com"}
user2={"test": "test@gmail.com"}
user3={ "admin":"admin@gmail.com"}

print("Lista")
user_list = []

user_list.append(user1)
user_list.append(user2)
user_list.append(user3)
print(len(user_list))

for i in range(0,len(user_list)):
    user_list[i]["password"] = "ahjdhWdeR"

user_list.append({"name": "alice","email": "alice@gmail.com"})

for i in range(0,len(user_list)):
    if "password" not in user_list[i].keys():
        user_list[i]["password"] = "NOWE"

print(user_list)

for i in range(0, len(user_list)):
    user_list[i]["adres"]=["koszykowa 86", "Akademicka 9"]
print(user_list)

for i in range(0, len(user_list)):
    user_list[i]["adresy"]={"adres": "koszykowa 86","adres2": "Akademicka 9"}
print(user_list)

print("PLIK")
#wczytanie pliku
filename = "students.txt"
with open(filename) as file_object:
    for line in file_object:
        print(line)

#tworzenie pliku
students = ["Alice" , "Bob"]
filename = "studentOut.txt"
with open(filename, "w") as file_object:
    for e in students:
        line=f" witaj {e}\n"
        file_object.write(line)


