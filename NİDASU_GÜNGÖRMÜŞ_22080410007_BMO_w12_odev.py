#verilenen tabloyu sözlük içinde listeler oluşturarak yazdım 

sinav_sonuc = { "isim":["ayşe k.","ahmet m.","nuri c.","nawar t.","suzan t.","ala b."],
"cinsiyet" : ["K","E","E","E","K","K"],
"vize notu" : [80,60,77,25,36,75],
"final notu" : [90,50,53,100,98,66],
'gecmeNotu':[]
}

#fonksiyon oluşturup fonksiyonun içine for dögülerini yapıp kullanıcıdan bilgileri alıp 
#sözlüğün içideki listelere bilgileri kaydettim.

#gecme notunu hesaplattim ama tek tek herkesin ortalamasını hesaplayamadım denedim ama olmadı
#sadece kullanıcıdan aldığı notların ortalamasını alıyor  

def sinav():
 for a in range(2):
  öğrenciad =input("öğrencinin ismi:")
  sinav_sonuc["isim"].append(öğrenciad)


 print(sinav_sonuc["isim"])


 for b in range(2):
  öğrencicinsiyet =input("öğrencinin cinsiyetini girin:")

  sinav_sonuc["cinsiyet"].append(öğrencicinsiyet)


 print(sinav_sonuc["cinsiyet"])


 for c in range(2):
  vize =int (input("öğrencinin vize notunu giriniz:"))
  sinav_sonuc["vize notu"].append(vize)

 print(sinav_sonuc["vize notu"])


 for d in range(2):
  final =int (input("öğrencinin final notunu giriniz:"))
  sinav_sonuc["final notu"].append(final)

 print(sinav_sonuc["final notu"])



 n = vize
 m = final

 for x in range(7):
  
  gecme = (n*0.3)+ (m*0.7)
 print(gecme)
 sinav_sonuc['gecmeNotu'].append(gecme)


# fonksiyonu burda çağırdım 
# güncel sözlügü yazdırdım
sinav()  
print(sinav_sonuc)

