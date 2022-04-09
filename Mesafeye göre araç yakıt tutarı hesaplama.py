arac_yakiti = input('Aracınız benzinliyse  \' benzin \'  ,  dizelse \' dizel \'  yazınız : ').lower().strip()

##############################################################################################################

benzin_fiyati = 20.5
dizel_fiyati = 21


##############################################################################################################

if arac_yakiti == 'benzin' :
    arac_ortalamasi = float(input('Lütfen aracınızın 100 km\'de ortalama kaç litre yaktığını giriniz : ').strip())
    mesafe = round(float(input('Lütfen kaç km mesafe gittiğinizi yazınız : ').strip()) , 2 )
    benzin_kilometre_basi_yakit_tutari = round(arac_ortalamasi * benzin_fiyati / 100 , 2)  
    print('--------------------------------------------------------------')
    print(f'Güncel benzin fiyatı : {benzin_fiyati} TL ')
    print(f'Benzinli aracınızın kilometre başı yakıt tutarı : {benzin_kilometre_basi_yakit_tutari} TL')
    print(f'Aracınızın {mesafe} km\'de yaktığı yakıt tutarı :  {round(benzin_kilometre_basi_yakit_tutari * mesafe , 2 )} TL ')
    print('--------------------------------------------------------------')

elif arac_yakiti == 'dizel' :
    arac_ortalamasi = float(input('Lütfen aracınızın 100 km\'de ortalama kaç litre yaktığını giriniz : ').strip())
    mesafe = round(float(input('Lütfen kaç km mesafe gittiğinizi yazınız : ').strip()) , 2 )
    dizel_kilometre_basi_yakit_tutari = round(arac_ortalamasi * dizel_fiyati / 100 , 2)
    print('--------------------------------------------------------------')
    print(f'Güncel dizel fiyatı : {dizel_fiyati} TL ')
    print(f'Dizel aracınızın kilometre başı yakıt tutarı : {dizel_kilometre_basi_yakit_tutari} TL')
    print(f'Aracınızın {mesafe} km\'de yaktığı yakıt tutarı :  {round(dizel_kilometre_basi_yakit_tutari * mesafe , 2 )} TL ')
    print('--------------------------------------------------------------')
else :
    print('Yakıt tipini yanlış yazdınız. Lütfen tekrar deneyiniz. ')
