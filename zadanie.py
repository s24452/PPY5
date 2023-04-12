import smtplib


filename = "students1.txt"
lista = []
filename="students1.txt"
#zadanie 5
def zapisDoPliku():
    zapis=""
    for i in lista:
        zapis+=i['imie ']+i['nazwisko ']+i['punkty ']+i['ocena ']+i['status ']
    with open(filename) as file_object:
        file_object.write(zapis)

#zadanie 4
from email.mime.text import MIMEText
def sendmail(subject,body,sender,recipients,password):
    wiadomosc=MIMEText(body)
    wiadomosc['Subject']=subject
    wiadomosc['From']=sender
    wiadomosc['To']=','.join(recipients)
    smtp_server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    smtp_server.login(sender,password)
    smtp_server.sendmail(sender,recipients,wiadomosc.as_string())
    smtp_server.quit()

#zadanie1
with open(filename) as file_object:
    for line in file_object:
        x = line.split(",")
        mail = x[0]
        imie = x[1]
        nazwisko = x[2]
        punkty = x[3]
        slownik = {}
        slownik['mail '] = mail
        slownik['imie '] = imie
        slownik['nazwsisko '] = nazwisko
        slownik['punkty '] = punkty
        lista.append(slownik)
        if len(line)==4:
            ocena=x[4]
            slownik['ocena ']=ocena
        elif len(line)==5:
            ocena=x[4]
            slownik['ocena ']=ocena
            status=x[5]
            slownik['status ']=status


print(lista)

#zadanie 2
with open(filename) as file_object:
    for linie in file_object:
        linia=linie.split(",")
        if len(linie)==5:
            if  str(linia[5])=="GRADED" or str(linie[5])=="MAILED":
               print("")
        else:
            punkty=int(linia[3])
            if punkty<=50:
                ocena=2

            elif punkty >= 51 or punkty<=60:
                ocena=3

            elif punkty>=61 or punkty<=70:
                ocena=3.5

            elif punkty>=71 or punkty<=80:
                ocena=4

            elif punkty>=81 or punkty<=90:
                 ocena=4.5

            else:
                ocena=5


        slownik['ocena']=ocena
        slownik['status ']=''


print("Sprawdzenie")
print(slownik)



#zadanie 3
wybor=input("Wybierz cz chcesz dodac studenta czy usunac (d lub u)")
if wybor == 'd':
    mail=input("Podaj mail ")
    if slownik['mail '] == mail:
        print("Taki student juz istnieje")
    else:
        imie=input("Podaj imie ")
        nazwisko=input("Podaj nazwisko ")
        punkty=input("Podaj ilosc punktow ")
        ocena=input("Podaj ocene ")
        status=input("Podaj status")

elif wybor=='u':
    indeksUsu=input("podaj index osoby do usuniecia")
    if slownik[indeksUsu]:
        lista.pop(int(indeksUsu))
        print()

#zadanie 4
        for i in lista:
            if i['status ']!="MAILED":
                subject="Wystawienie ocen"
                body="Ocena z PPY wynosi: "+i['ocena']
                sender=""
                recipients=i['mail']
                pasword=""
                sendmail(subject,body,sender,recipients,pasword)
        zapisDoPliku()
