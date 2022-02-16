daire_yaricap = float(input('Lütfen Yarıçap Giriniz : '))
pi = 3.14
daire_alani = pi*(daire_yaricap**2)
daire_cevresi = 2 * pi * daire_yaricap
print('Daire Alanınız :' + str((daire_alani)) , ('  ---   Daire Çevreniz : ' + str(round(daire_cevresi,2))))
print(f'Daire Alanınız : {daire_alani} ---  Daire Çevreniz : {round(daire_cevresi,2)}' ) 

