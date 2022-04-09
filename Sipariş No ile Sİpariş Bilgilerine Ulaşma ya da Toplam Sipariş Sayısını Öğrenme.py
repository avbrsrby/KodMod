Siparisler = {
    101  : {'Ürün Adı : ' : 'Telefon' , 'Ürün Fiyatı : ' : '5000'+ ' ₺' , 'Sipariş Tarihi : ' : '15.02.2021'},
    105  : {'Ürün Adı : ' : 'Bilgisayar' , 'Ürün Fiyatı : ' : '1000'+ ' ₺' , 'Sipariş Tarihi : ' : '23.08.2021' },
    108  : {'Ürün Adı : ' : 'Projeksiyon' , 'Ürün Fiyatı : ' : '3500'+ ' ₺' , 'Sipariş Tarihi : ' : '07.01.2022'}
             }
cevap = input('Toplam kaç adet siparişiniz olduğunu öğrenmek istiyorsanız ADET , siparis detaylarınızı görmek için DETAY yazınız. :  ')
cevap_liste = [cevap.upper()]
if 'DETAY' in cevap_liste:
    x = (Siparisler[int(input('Sipariş Numaranızı Giriniz : '))])
    print('Ürün Adı : ' , x['Ürün Adı : '])
    print('Ürün Fiyatı : ' , x['Ürün Fiyatı : '])
    print('Sipariş Tarihi : ' , x['Sipariş Tarihi : '])

if 'ADET' in cevap_liste:
    print('Toplam' , len(Siparisler) , 'adet siparişiniz bulunmaktadır.')
    print(f'Sipariş Numaralarınız {list(Siparisler.keys())} ')
