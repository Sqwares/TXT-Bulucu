import urllib.request
import os
import time
import sys

print("""
░██████╗░██████╗░░██╗░░░░░░░██╗░█████╗░██████╗░███████╗░██████╗
██╔════╝██╔═══██╗░██║░░██╗░░██║██╔══██╗██╔══██╗██╔════╝██╔════╝
╚█████╗░██║██╗██║░╚██╗████╗██╔╝███████║██████╔╝█████╗░░╚█████╗░
░╚═══██╗╚██████╔╝░░████╔═████║░██╔══██║██╔══██╗██╔══╝░░░╚═══██╗
██████╔╝░╚═██╔═╝░░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║███████╗██████╔╝
╚═════╝░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░""")

print(".")
print(".")
print(".")
print(".")
print(".")
print("-")
time.sleep(1)
print("Dikkat ! Hedef Sitenin Sonunda / İşareti Olmasına dikkat edin")
time.sleep(1)
print("-")
url = input("Txt Buluncak Hedef Siteyi Giriniz : " )

kelimeler = ('hesap.txt','hesaplar.txt','kurbanlar.txt','kurban.txt','hesaplar1.txt','hesaplar2.txt','logger.txt','melisa.txt','list.txt','hesaplist.txt','hesaplarlist.txt','hesapliste.txt','hesaplarliste.txt','hesaplistesi.txt','hesaplarlistesi.txt','kurbanlist.txt','kurbanlarlist.txt','kurbanliste.txt','kurbanlarliste.txt','kurbanlistesi.txt','kurbanlarlistesi.txt','b4rutorj.txt','pezny.txt','sezginofficiallz.php','panzergeldi.txt','kurbancık.txt','düşenler.txt','log.txt','enayiler.txt','mami.txt','can.txt','hüso.txt','sanane.txt','hesap.php','hesaplar.php','kurbanlar.php','kurban.php','hesaplar1.php','hesaplar2.php','logger.php','melisa.php','list.php','hesaplist.php','hesaplarlist.php','hesapliste.php','hesaplarliste.php','hesaplistesi.php','hesaplarlistesi.php','kurbanlist.php','kurbanlarlist.php','kurbanliste.php','kurbanlarliste.php','kurbanlistesi.php','kurbanlarlistesi.php','b4rutorj.php','pezny.php','sezginofficiallz.php','panzergeldi.php','kurbancık.php','düşenler.php','log.php','enayiler.php','mami.php','can.php','hüso.php','sanane.php','jroken.txt','jroken.php','password.php','password.txt','s2s.txt','s2x.txt','tht.txt','Recai.txt','recai.txt','hichigo.txt','Hichigo.txt',)
for kelime in kelimeler:
    sonuc =url+kelime
    try:
        openurl=urllib.request.urlopen(sonuc)
        print("_____________________________________________")
        print("                                             ")
        print("Bulduk ya amk ) ===> "+sonuc)
        with open("siteler.txt","a") as file:
            file.write(sonuc+"\n")
    except:
        print("Sonraki Sefere :/ ")
        
