import random

rastgele = random.randint(1,100)

i = 0
'''while i < 100 :
    sayi = int(input(' 1 ve 100 arasında bir sayı giriniz : '))
    if sayi == rastgele:
        print ( f' Doğru sayıyı buldunuz. Doğru Sayı : {rastgele} ')   ####### WHİLE İLE DE YAPILIYOR
        break
    if sayi < rastgele:
        print ( f' Girdiğiniz {sayi} Daha yukarı çıkın. ')
        
    if sayi > rastgele:
        print ( f' Girdiğiniz {sayi} Daha aşağı inin. ')
        
    
    i += 1 '''

oynanan_hamle = 0
for i in range(1,100):
    sayi = int(input(' 1 ve 100 arasında bir sayı giriniz : '))
    if sayi == rastgele:
        oynanan_hamle += 1
        print ( f' Doğru sayıyı {oynanan_hamle} hamlede buldunuz. Doğru Sayı : {rastgele} ')
        break
    if sayi < rastgele:
        oynanan_hamle += 1
        print ( f' Girdiğiniz {sayi} Daha yukarı çıkın. ')
        
    if sayi > rastgele:
        oynanan_hamle += 1
        print ( f' Girdiğiniz {sayi} Daha aşağı inin. ')

   