metin = input('Lütfen İngilizce Karaktere Çevirmek İstediğiniz Metninizi Yazınız.')
metin_cevrilmis = metin.replace('ş','s').replace('Ş','S').replace('ı','i').replace('İ','I').replace('ü','u').replace('Ü','U').replace('ç','c').replace('Ç','C').replace('ğ' , 'g').replace('Ğ' , 'G')
print(metin_cevrilmis)