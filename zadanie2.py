import random

filename="students1.txt"

with open(filename) as file_object:
    for linie in file_object:
        linia=linie.split(",")
        if str(linia[5])!="GRADED" or str(linie[5])!="MAILED":
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
        print(ocena)
        file_object.write(ocena)






