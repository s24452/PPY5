filename = "students.txt"
slownik = {}
lista = []
with open(filename) as file_object:
    for line in file_object:
        x = line.split(",")
        mail = x[0]
        imie = x[1]
        nazwisko = x[2]
        punkty = x[3]

        slownik['mail '] = mail
        slownik['imie '] = imie
        slownik['nazwsisko '] = nazwisko
        slownik['punkty '] = punkty
        lista.append(slownik)

print(lista)
