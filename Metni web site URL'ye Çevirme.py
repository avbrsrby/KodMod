metin = input('Lütfen Metninizi Yazınız : ')
metin_cevrilmis = metin.replace('ş','s').replace('Ş','S').replace('ı','i').replace('İ','I').replace('ü','u').replace('Ü','U').replace('ç','c').replace('Ç','C')
metin_bosluklar_silinmis = metin_cevrilmis.replace(' ','-')
metin_sonuc = metin_bosluklar_silinmis.lower()
metin_sonuc = metin_bosluklar_silinmis.lower()
print(metin_sonuc)