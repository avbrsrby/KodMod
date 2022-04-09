import random

rastgele = random.randint(1,100)

i = 0
while i < 100 :
    sayi = int(input(' 1 ve 100 arasında bir sayı giriniz : '))
    if sayi == rastgele:
        print ( f' Doğru sayıyı buldunuz. Doğru Sayı : {rastgele} ')
        break
    if sayi < rastgele:
        print ( f' Girdiğiniz {sayi} Daha yukarı çıkın. ')
        
    if sayi > rastgele:
        print ( f' Girdiğiniz {sayi} Daha aşağı inin. ')
        
    
    i += 1 


   