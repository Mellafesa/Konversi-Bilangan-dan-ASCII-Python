#Mellafesa Rofida XII RPL 4

from os import replace, system


def judul():
    system('cls')
    print('===============================================')
    print('Selamat Datang di Program Konversi Bilangan <3'.center(40))
    print('================================================')


def menu():
    judul()
    print('| 1. Desimal                        |')
    print('| 2. Biner                          |')
    print('| 3. Oktal                          |')
    print('| 4. Hexadecimal                    |')
    print('| 5. ASCII                          |')
    print('| 6. Keluar                         |')
    print('=====================================')
    pilih2 = input('Pilih Menu : ')
    if pilih2 == '1':
        desimal()
    elif pilih2 == '2':
        biner()
    elif pilih2 == '3':
        oktal()
    elif pilih2 == '4':
        hexadecimal()
    elif pilih2 == '5':
        ASCII()
    elif pilih2 == '6':
        Keluar()
    else:
        salah()


def salah():
    salah1 = input("Maaf, Menu Tidak Tersedia Ygy! [Enter]")
    menu()


def desimal():
    judul()
    try:
        angka = int(input("Masukkan Bilangan Desimal : "))
    except ValueError:
        error = input("Maaf, Bilangan Tidak Sesuai! Coba Ulangi [Enter]")
        desimal()
    bineri = bin(angka).replace("0b", "")
    oktal = oct(angka).replace("0o", "")
    heks = hex(angka).replace("0x", "")

    print('=====================================')
    print('| Biner : ', bineri)
    print('| Oktal : ', oktal)
    print('| Hexa  : ', heks)
    print('=====================================')
    kembali = input('Ulangi Konversi? [y/t]')
    if kembali == "y" or kembali == "Y":
        desimal()
    else:
        menu()


def biner():
    judul()
    try:
        angka = int(input("Masukkan Bilangan Biner : "), 2)
    except ValueError:
        error = input("Maaf, Bilangan Tidak Sesuai! Coba Ulangi[Enter]")
        biner()
    oktal = oct(angka).replace("0o", "")
    heks = hex(angka).replace("0x", "")

    print('=====================================')
    print('| Decimal : ', angka)
    print('| Oktal   : ', oktal)
    print('| Hexa    : ', heks)
    print('=====================================')
    kembali = input('Ulangi Konversi? [y/t]')
    if kembali == "y" or kembali == "Y":
        biner()
    else:
        menu()


def oktal():
    judul()
    try:
        angka = int(input("Masukkan Bilangan Oktal : "), 8)
    except ValueError:
        error = input("Maaf, Bilangan Tidak Sesuai! Coba Ulangi[Enter]")
        oktal()
    biner = bin(angka).replace("0b", "")
    heks = hex(angka).replace("0x", "")

    print('=====================================')
    print('| Decimal : ', angka)
    print('| biner   : ', biner)
    print('| Hexa    : ', heks)
    print('=====================================')
    kembali = input('Ulangi Konversi? [y/t]')
    if kembali == "y" or kembali == "Y":
        oktal()
    else:
        menu()


def hexadecimal():
    judul()
    try:
        angka = int(input("Masukkan Bilangan Hexadecimal : "), 16)
    except ValueError:
        error = input("Maaf, Bilangan Tidak Sesuai! Coba Ulangi[Enter]")
        hexadecimal()
    biner = bin(angka).replace("0b", "")
    oktal = oct(angka).replace("0o", "")

    print('=====================================')
    print('| Decimal : ', angka)
    print('| Biner   : ', biner)
    print('| Oktal   : ', oktal)
    print('=====================================')

    kembali = input('Ulangi Konversi? [y/t]')
    if kembali == "y" or kembali == "Y":
        hexadecimal()
    else:
        menu()

def ASCII():
    judul()
    try :
        text = input("Masukkan bilangan string untuk dikonversikan ke bilangan ASCII: ")
        ascii_values = [ord(character) for character in text]
    except ValueError:
        error = input ("Maaf, Bilangan Tidak Sesuai! Coba Ulangi[Enter]")
        ascii()
    print('=====================================')
    print('| ASCII : ',ascii_values)
    print('=====================================')
    kembali = input('Ulangi Konversi? [y/t]')
    if kembali == "y" or kembali == "Y":
        ascii()
    else:
        menu()


def Keluar():
    exit()


menu()