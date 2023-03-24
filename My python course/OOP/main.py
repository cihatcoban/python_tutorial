
import random
import time

class kumanda():

    def __int__(self,tv_durum="kapalı",tv_ses=0,kanal_listesi=["beinsports"],kanal="1"):

        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tv_ac(self):

        if(self.tv_durum=="açık"):
            print("tv açık ")
        else:
            print("tv açılıyor..")
            self.tv_durum="açık"

    def tv_kapat(self):
        if(self.tv_durum=="kapalı"):
            print("tv kapalı")
        else:
            print("tv kapatılıyor..")
            self.tv_durum="kapalı"

    def ses_ayarları(self):

        while True:
            cevap = input("sesi artır:'>'\tsesi azalt:'<'\n çıkış:çıkış")

            if(cevap=="<"):
                if(self.tv_ses!=0):
                    self.tv_ses-=1
                    print("ses:",self.tv_ses)
            elif(cevap==">"):
                if(self.tv_ses!=64):
                    self.tv_ses += 1
                    print("ses:", self.tv_ses)

            else:
                break

    def kanal_eke(self,kanal_adı):
        print("aktarım başarılı")
        time.sleep(1)
        self.kanal_listesi.append(kanal_adı)


    def random_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)

        self.kanal=self.kanal_listesi[rastgele]
        print("kanal adı :",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "tv_durum:{}\ntv_ses:{}\nkanal_listesi:{}\nkanal:{}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)


kumanda==kumanda()
print("""
----------TV kumandası-------------
1. tv aç
2. tv kapat
3. ses ayarları
4. kanla ekleme
5. kanal sayısı
6. rastgele kanal değiştirme
7. tv bilgileri
çıkış yapmak için "q"
""")

while True:
    işlem=input("işlem seçiniz: ")

    if (işlem=="q"):
        print("çıkış yapılıyor")
        break
    elif(işlem=="1"):
        kumanda.tv_ac()
    elif(işlem=="2"):
        kumanda.tv_kapat()
    elif(işlem=="3"):
        kumanda.ses_ayarları()
    elif(işlem=="4"):
        kanal_adı=input("kanal isimlerini ',' ile ayırarak giriniz")
        kanal_listesi=kanal_adı.split(",")
        for i in kanal_listesi:
            kumanda.kanal_eke(i)

    elif(işlem=="5"):
        print("kanal sayısı.",len(kumanda))
    elif(işlem=="6"):
        kumanda.random_kanal()

    elif(işlem=="7"):
        print(kumanda)
    else:
        print("eksik yada hatalı tuşlama")



