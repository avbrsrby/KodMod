from unicodedata import name
import requests

url = 'http://api.weatherapi.com/v1/current.json'
api_key = 'b3bcc0fd85f346688e2111741222204'

dinamik_sehir = input('Lütfen şehir giriniz : ')
response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=b3bcc0fd85f346688e2111741222204&q={dinamik_sehir}&aqi=no&lang=tr')

sonuc = response.json()
sehir = sonuc['location']['name']
durum = sonuc['current']['condition']['text']
derece = sonuc['current']['temp_c']



print(f' {sehir} bölgesinde hava durumu : {durum}  ||| Sıcaklık değeri = {derece}' )