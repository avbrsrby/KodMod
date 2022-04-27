import requests
from bs4 import BeautifulSoup
######## BLOOMBERGTE ARTIŞ OLDUĞU ZAMAN upGreen   indiğinde downRed üzerinden gösteriyor. BUNU çözzzz

response_dolar = requests.get('https://www.bloomberght.com/doviz/dolar')
soup_dolar = BeautifulSoup(response_dolar.text , 'html.parser')                ####### DOLAR
sonuc_dolar = soup_dolar.body.find(class_='LastPrice upGreen').string
sonson_dolar = float(sonuc_dolar.replace(',' , '.'))
     

response_euro = requests.get('https://www.bloomberght.com/doviz/euro')
soup_euro = BeautifulSoup(response_euro.text , 'html.parser')                ####### EURO                
sonuc_euro = soup_euro.body.find(class_='LastPrice downRed').string
sonson_euro = float(sonuc_euro.replace(',' , '.'))

response_sterlin = requests.get('https://www.bloomberght.com/doviz/ingiliz-sterlini')
soup_sterlin = BeautifulSoup(response_sterlin.text , 'html.parser')                ####### EURO                
sonuc_sterlin = soup_sterlin.body.find(class_='LastPrice downRed').string
sonson_sterlin = float(sonuc_sterlin.replace(',' , '.'))

cevrilmek_istenen_cinsi = input('Lütfen TL\'ye çevirmek istediğiniz para cinsini yazınız. (Örn : USD - EUR - GBP ) : ' )
cevrilmek_istenen_miktar = int(input(f'Lütfen çevirmek istediğiniz {cevrilmek_istenen_cinsi} miktarını giriniz : '))

if cevrilmek_istenen_cinsi == 'USD' :
    print(f'----------\nGüncel USD kuru : {sonson_dolar} -[BloombergHT.com verileri baz alınmıştır.]' )
    print(f'Çevirmek istediğiniz {cevrilmek_istenen_miktar} dolar {cevrilmek_istenen_miktar*sonson_dolar} TL değerindedir. ')

elif cevrilmek_istenen_cinsi == 'EUR' :
    print(f'----------\nGüncel EUR kuru : {sonson_euro} -[BloombergHT.com verileri baz alınmıştır.]')
    print(f'Çevirmek istediğiniz {cevrilmek_istenen_miktar} euro {cevrilmek_istenen_miktar*sonson_euro} TL değerindedir. ' )

elif cevrilmek_istenen_cinsi == 'GBP' :
    print(f'----------\nGüncel GBP kuru : {sonson_sterlin} -[BloombergHT.com verileri baz alınmıştır.]')
    print(f'Çevirmek istediğiniz {cevrilmek_istenen_miktar} sterlin {cevrilmek_istenen_miktar*sonson_sterlin} TL değerindedir. ')

else:
    print('Hatalı para cinsi yazdınız. USD - EUR yada GBP yazmanız gerekmektedir.')



