import time


class Dükkan ():



    def __init__(self,çiğ_köfte=10000,dondurma=5000,su=50,ayran=100,dürüm=100,dubble_dürüm=50,sepet=0):

        self.çiğ_köfte=çiğ_köfte
        self.dondurma=dondurma
        self.su=su
        self.ayran=ayran
        self.dürüm=dürüm
        self.dubble_dürüm=dubble_dürüm
        self.sepet=sepet


    def çiğ_köfte_satışı(self):

        while True:

            print("Dükkanda bulunan çiğköfte miktarı : {}".format(self.çiğ_köfte))

            print("Lütfen Çiğköfte Miktarını gram olarak giriniz..")

            istenen=int(input("Almak istediğiniz çiğköfte miktarını giriniz:"))

            if (istenen>self.çiğ_köfte):

                print("Maalesef elimizde o miktarda çiğköfte bulunmamaktadır.")
                time.sleep(1)
                print("Dükkanda bulunan çiğköfte miktarı : {}".format(self.çiğ_köfte))
                break

            elif (istenen<=self.çiğ_köfte):
                print("Çiğköfteniz Hazırlanıyor..")
                time.sleep(1)
                print("Çiğköfteniz Hazır.")

                self.çiğ_köfte-=istenen

                self.sepet+=(istenen*0.14)


                print("Çiğköfte Tutarınız : {} Tldir".format(self.sepet))
                return
            else:
                print("Hatalı İşlem Girdiniz!!")
                break

    def dondurma_satışı(self):

        while True:

            print("Dükkanda bulunan dondurma miktarı : {}".format(self.dondurma))

            print("Lütfen Dondurma Miktarını gram olarak giriniz..")

            istenen = int(input("Almak istediğiniz dondurma miktarını giriniz:"))

            if(istenen>self.dondurma):

                print("Maalesef elimizde o miktarda çiğköfte bulunmamaktadır.")

                time.sleep(1)

                print("Dükkanda bulunan çiğköfte miktarı : {}".format(self.çiğ_köfte))
                break

            elif(istenen<=self.dondurma):
                print("Dondurmanız Hazırlanıyor..")
                time.sleep(1)
                print("Dondurmanız Hazır.")

                self.dondurma -= istenen

                self.sepet += (istenen * 0.14)

                print("Dondurma Tutarınız : {} Tldir".format(istenen * 0.14))
                return

            else:
                print("Hatalı İşlem Girdiniz!!")

                break

    def su_satışı(self):

        while True:

            print("Dükkanda bulunan su miktarı : {}".format(self.su))

            print("Lütfen Su Miktarını adet olarak giriniz..")

            istenen = int(input("Almak istediğiniz su miktarını giriniz:"))

            if (istenen > self.su):

                print("Maalesef elimizde o adette su bulunmamaktadır.")

                time.sleep(1)

                print("Dükkanda bulunan su adeti : {}".format(self.su))
                break

            elif (istenen <= self.su):
                print("Suyunuz Hazırlanıyor..")
                time.sleep(1)
                print("Suyunuz Hazır.")

                self.su -= istenen
                self.sepet += (istenen * 3)
                print("Su Tutarınız : {} Tldir".format(istenen * 3))
                return
            else:
                print("Hatalı İşlem Girdiniz!!")

                break

    def ayran_satışı(self):

        while True:

            print("Dükkanda bulunan ayran miktarı : {}".format(self.ayran))

            print("Lütfen Ayran Miktarını adet olarak giriniz..")

            istenen = int(input("Almak istediğiniz ayran miktarını giriniz:"))

            if (istenen > self.ayran):

                print("Maalesef elimizde o miktarda ayran bulunmamaktadır.")

                time.sleep(1)

                print("Dükkanda bulunan ayran miktarı : {}".format(self.ayran))
                break

            elif (istenen <= self.ayran):
                print("Ayranınız Hazırlanıyor..")
                time.sleep(1)
                print("Ayranınız Hazır.")

                self.ayran -= istenen
                self.sepet += (istenen * 5)
                print("Ayran Tutarınız : {} Tldir".format(istenen * 5))
                return
            else:
                print("Hatalı İşlem Girdiniz!!")

                break
    def dürüm_satışı(self):
        while True:

            print("Dürüm içerisinde bulunan çiğköfte miktarımız 100gr'dır.")
            istenen=int(input("Almak istediğiniz dürüm adetini giriniz:"))

            if (istenen*100>self.çiğ_köfte):
                print("Maalesef elimizde o miktarda dürüm bulunmamaktadır.")
                time.sleep(1)
                print("Dükkanda bulunan dürüm miktarı : {}".format(self.çiğ_köfte/100))
                break

            elif (istenen <= self.çiğ_köfte):
                print("Dürümünüz Hazırlanıyor..")
                time.sleep(1)
                print("Dürümünüz Hazır.")

                self.çiğ_köfte -= istenen*100
                self.sepet += (istenen * 20)
                print("Dürüm Tutarınız : {} Tldir".format(istenen * 20))
                return
            else:
                print("Hatalı İşlem Girdiniz!!")
                break

    def dubble_dürüm_satışı(self):
        while True:

            print("Dubble Dürüm içerisinde bulunan çiğköfte miktarımız 200gr'dır.")
            istenen = int(input("Almak istediğiniz dubble dürüm adetini giriniz:"))

            if (istenen * 100 > self.çiğ_köfte):
                print("Maalesef elimizde o miktarda dubble dürüm bulunmamaktadır.")
                time.sleep(1)
                print("Dükkanda bulunan dubble dürüm miktarı : {}".format(self.çiğ_köfte / 200))
                break

            elif (istenen <= self.çiğ_köfte):
                print("Dubble dürümünüz Hazırlanıyor..")
                time.sleep(1)
                print("Dubble dürümünüz Hazır.")

                self.çiğ_köfte -= istenen * 200
                self.sepet += (istenen * 35)
                print("Dubble Dürüm Tutarınız : {} Tldir".format(istenen * 35))
                return
            else:
                print("Hatalı İşlem Girdiniz!!")
                break


    def sepet_göster(self):

        print("Toplam Sepet Tutarınız :{}".format(self.sepet))


dükkan=Dükkan()

print("""
**************************************************
ÇİĞKÖFTECİ ARAS USTA DÜKKANIMIZA HOŞGELDİNİZ!!

------ÜRÜN LİSTESİ------


1. ÇiğKöfte (Kg fiyatı 140tl)

2. Dondurma (Kg fiyatı 140tl)

3. Su (Adet fiyatı 3tl)

4. Ayran (Adet fiyatı 5tl)

5. Dürüm (Adet fiyatı 20tl)

6. Dubble Dürüm (Adet fiyatı 35tl)

7.Sepet

Çıkmak için 'q' ya basın.
**********************************************
""")


while True:

    işlem = input("Almak İstediğiniz Ürünü Seçiniz:")

    if (işlem == "q"):
        print("Program Sonlandırılıyor...")
        break

    elif (işlem=="1"):

        dükkan.çiğ_köfte_satışı()

    elif (işlem=="2"):

        dükkan.dondurma_satışı()

    elif (işlem=="3"):

        dükkan.su_satışı()

    elif (işlem=="4"):

        dükkan.ayran_satışı()

    elif (işlem=="5"):

        dükkan.dürüm_satışı()

    elif (işlem=="6"):

        dükkan.dubble_dürüm_satışı()

    elif (işlem=="7"):

        dükkan.sepet_göster()

    else:
        print("Hatalı İşlem Yaptınız!")









