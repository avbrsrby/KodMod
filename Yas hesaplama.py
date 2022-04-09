from calendar import month
import datetime
uye_dogumyili = input('Lütfen dogum tarihinizi gün ay yıl ( örn: 23.08.1997 ) şeklinde yazınız. : ').split('.')
##### print(uye_dogumyili) ['23', '08', '1997']
##### print(int(uye_dogumyili[2]))  #### 1997

simdi = datetime.datetime.now()
girilen_tarih =  datetime.datetime(int(uye_dogumyili[2]) , int(uye_dogumyili[1]) , int(uye_dogumyili[0])) 
yas = simdi.year - girilen_tarih.year

if girilen_tarih.month < simdi.month:
    print(f'Yaşınız : {yas} ')
if girilen_tarih.month == simdi.month:
    if girilen_tarih.day <= simdi.day:
        print(f'Yaşınız : {yas} ')
    else: 
        print(f'Yaşınız : {yas-1} ')
if girilen_tarih.month > simdi.month:
    print(f'Yaşınız : {yas-1} ')

