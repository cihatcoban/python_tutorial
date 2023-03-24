def not_hesaplama(satır):


    satır=satır[:-1]

    liste=satır.split(",")

    isim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])

    ort=not1*(25/100)+not2*(25/100)+not3*(50/100)

    if(ort>=90):
        harf="AA"
    elif(ort>=85):
        harf="AB"
    elif(ort>=80):
        harf="BB"
    elif(ort>=75):
        harf="BC"
    elif(ort>=70):
        harf="CC"
    elif(ort>=65):
        harf="CD"
    elif(ort>=60):
        harf="DD"
    else:
        harf="FF"

    return isim + "----------------->" + harf + "\n"


with open("5.1 dosya.txt","r",encoding="utf-8") as file:

    ekle=[]

    for i in file:

        ekle.append(not_hesaplama(i))

    with open("harf_not.txt","w",encoding="utf-8") as file2:

        for i in ekle:
            file2.write(i)



with open("harf_not.txt","r",encoding="utf-8") as file2:
    kalan=list()

    for satır in file2:

        satır= satır[:-1]
        satır_elemanı= satır.split("----------------->")
        if (satır_elemanı[1]=="FF"):
            kalan.append(satır+"\n")
    with open("kalanlar.txt","w",encoding="utf-8") as file3:
        for i in kalan:
            file3.write(i)


