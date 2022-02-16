veritabani_mail = 'avbrsrby97@gmail.com'
veritabani_password = '12345'

#########

üyegirisi_mail = input('Lütfen e-mailinizi giriniz : ')
üyegirisi_sifre = input('Lütfen şifrenizi giriniz : ')

sonuc = ( veritabani_mail == üyegirisi_mail ) and (veritabani_password == üyegirisi_sifre )
if sonuc == True:
    print('Kullanıcı Adı ve Şifreniz Onaylanmıştır. Giriş Yapılıyor.')
if sonuc == False:
    print('Kullanıcı Adı veya Şifre Hatalı. Lütfen Tekrar Deneyiniz.')  ##### Tekrar Deneyecek.

    üyegirisi_mail = input('Lütfen e-mailinizi giriniz : ')
    üyegirisi_sifre = input('Lütfen şifrenizi giriniz : ')
    sonuc = ( veritabani_mail == üyegirisi_mail ) and (veritabani_password == üyegirisi_sifre )
    if sonuc == True:
        print('Kullanıcı Adı ve Şifreniz Onaylanmıştır. Giriş Yapılıyor.')
    if sonuc == False:
        print('Kullanıcı Adı veya Şifrenizi tekrar yanlış girdiğiniz için hesabınız blokelenmiştir.')
    

