import requests
from bs4 import BeautifulSoup

########################## VERİLERİ ÇEKME

response_dolar = requests.get('https://www.bloomberght.com/doviz/dolar')
soup_dolar = BeautifulSoup(response_dolar.text , 'html.parser')                ####### DOLAR
try:
    sonuc_dolar = soup_dolar.body.find(class_='LastPrice downRed').string
    sonson_dolar = float(sonuc_dolar.replace(',' , '.'))
except:
    sonuc_dolar = soup_dolar.body.find(class_='LastPrice upGreen').string
    sonson_dolar = float(sonuc_dolar.replace(',' , '.'))

#########  

response_euro = requests.get('https://www.bloomberght.com/doviz/euro')
soup_euro = BeautifulSoup(response_euro.text , 'html.parser')                ####### EURO                
try:
    sonuc_euro = soup_euro.body.find(class_='LastPrice downRed').string
    sonson_euro = float(sonuc_euro.replace(',' , '.'))
except:
    sonuc_euro = soup_euro.body.find(class_='LastPrice upGreen').string
    sonson_euro = float(sonuc_euro.replace(',' , '.'))

#########

response_sterlin = requests.get('https://www.bloomberght.com/doviz/ingiliz-sterlini')
soup_sterlin = BeautifulSoup(response_sterlin.text , 'html.parser')                ####### EURO                
try:
    sonuc_sterlin = soup_sterlin.body.find(class_='LastPrice downRed').string
    sonson_sterlin = float(sonuc_sterlin.replace(',' , '.'))
except:
    sonuc_sterlin = soup_sterlin.body.find(class_='LastPrice upGreen').string
    sonson_sterlin = float(sonuc_sterlin.replace(',' , '.'))

#####################################  KULLANICIDAN PARAMETRELERİ ALIP SONUÇ VERME

cevrilmek_istenen_cinsi = input('Lütfen TL\'ye çevirmek istediğiniz para cinsini yazınız. (Örn : USD - EUR - GBP ) : ' )
cevrilmek_istenen_miktar = int(input(f'Lütfen çevirmek istediğiniz {cevrilmek_istenen_cinsi} miktarını giriniz : '))

if cevrilmek_istenen_cinsi == 'USD' :
    print(f'----------\nGüncel USD kuru : {sonson_dolar} -[BloombergHT.com verileri baz alınmıştır.]' )
    print(f'Çevirmek istediğiniz {cevrilmek_istenen_miktar} dolar {round((cevrilmek_istenen_miktar*sonson_dolar),2)} TL değerindedir. ')

elif cevrilmek_istenen_cinsi == 'EUR' :
    print(f'----------\nGüncel EUR kuru : {sonson_euro} -[BloombergHT.com verileri baz alınmıştır.]')
    print(f'Çevirmek istediğiniz {cevrilmek_istenen_miktar} euro {round((cevrilmek_istenen_miktar*sonson_euro),2)} TL değerindedir. ' )

elif cevrilmek_istenen_cinsi == 'GBP' :
    print(f'----------\nGüncel GBP kuru : {sonson_sterlin} -[BloombergHT.com verileri baz alınmıştır.]')
    print(f'Çevirmek istediğiniz {cevrilmek_istenen_miktar} sterlin {round((cevrilmek_istenen_miktar*sonson_sterlin),2)} TL değerindedir. ')

else:
    print('Hatalı para cinsi yazdınız. USD - EUR yada GBP yazmanız gerekmektedir.')



