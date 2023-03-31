#Mellafesa Rofida - XII RPL 4 - 3103120134
from tkinter import *

#menu pada terminal
def main():
    while True:
        print('===============================================')
        print("Selamat Datang di Program Konversi Bilangan <3")
        print('===============================================')
        print("Mau konversi apa?")
        print("1. Konversi String ke ASCII")
        print("2. Konversi Bilangan antara Biner, Oktal, Desimal, dan Heksadesimal")
        print("3. Keluar")
        option = input("Pilih opsi: ")
        if option == "1":
            string_to_ascii_gui()
        elif option == "2":
            base_converter_gui()
        elif option == "3":
            break
        else:
            print("Opsi tidak valid, mohon coba lagi.")


#================================================================================================
#PERINTAH GUI
#================================================================================================

#perintah GUI untuk konversi string ke ascii
def string_to_ascii_gui():
    def convert():
        string = string_entry.get()
        ascii_list = string_to_ascii(string)
        ascii_text.delete(1.0, END)
        ascii_text.insert(END, "Hasil konversi ASCII untuk " + string + " adalah:\n")
        for ascii_code in ascii_list:
            ascii_text.insert(END, str(ascii_code) + " ")
    #membuat window
    ascii_window = Tk()
    ascii_window.title("Konversi String ke ASCII")

    #ukuran window
    ascii_window.geometry("500x375")
    ascii_window["bg"]= "#EDE7F6"

    #label untuk judul
    string_label = Label(ascii_window, text="Masukkan string:" ,  font=('Bahnschrift', 12), bg="#EDE7F6")
    string_label.pack(pady=10)

    #textbox untuk mengisi string
    string_entry = Entry(ascii_window , width=40, font=('Bahnschrift', 12))
    string_entry.pack(pady= 10)

    #button konversi
    convert_button = Button(ascii_window, text="Konversi", command=convert , width=15 ,font=('Bahnschrift', 12), bg="#9575CD", fg="white")
    convert_button.pack(pady=10)

    #label untuk hasil konversi string ke ascii
    ascii_text = Text(ascii_window, width=40, height=10, font=('Bahnschrift', 12))
    ascii_text.pack(pady=  10)
    ascii_window.mainloop()

#perintah GUI untuk konversi bilangan antara biner, oktal, desimal, dan heksadesimal
def base_converter_gui():
    def convert():
        number = number_entry.get()
        base_from = int(from_menu.get())
        base_to = int(to_menu.get())
        result = convert_base(number, base_from, base_to)
        result_text.delete(1.0, END)
        result_text.insert(END, result)
    #membuat window
    base_window = Tk()
    base_window.title("Konversi Bilangan antara Biner, Oktal, Desimal, dan Heksadesimal")

    #ukuran window
    base_window.geometry("500x515")
    base_window["bg"]= "#EDE7F6"

    #label untuk judul
    number_label = Label(base_window, text="Masukkan bilangan:" ,  font=('Bahnschrift', 12), bg="#EDE7F6")
    number_label.pack(pady=10)

    #textbox untuk mengisi bilangan
    number_entry = Entry(base_window , width=40, font=('Bahnschrift', 12))
    number_entry.pack(pady= 10)

    #label untuk pilihan konversi dari
    from_label = Label(base_window, text="Konversi dari basis:" ,  font=('Bahnschrift', 10), bg="#EDE7F6")
    from_label.pack(pady=5)
    #dropdown
    from_menu = Spinbox(base_window, values=[2, 8, 10, 16] , width=10 , font=('Bahnschrift', 10))
    from_menu.pack(pady=5)

    #label untuk pilihan konversi ke
    to_label = Label(base_window, text="ke basis:" ,  font=('Bahnschrift', 10), bg="#EDE7F6")
    to_label.pack(pady=5)
    #dropdown
    to_menu = Spinbox(base_window, values=[2, 8, 10, 16] , width=10 , font=('Bahnschrift', 10))
    to_menu.pack(pady=5)

    #button konversi
    convert_button = Button(base_window, text="Konversi", command=convert , width=15 ,font=('Bahnschrift', 12), bg="#9575CD", fg="white")
    convert_button.pack(pady=10)

    #label untuk hasil konversi
    result_text = Text(base_window ,width=40, height=10, font=('Bahnschrift', 12))
    result_text.pack(pady=  10)
    base_window.mainloop()


#================================================================================================
#PERINTAH KONVERSI BILANGAN DAN STRING KE ASCII
#================================================================================================
#konversi string ke ascii
def string_to_ascii(string):
    ascii_list = []
    for char in string:
        ascii_code = ord(char)
        ascii_list.append(ascii_code)
    return ascii_list

#perintah 4 konversi bilangan
def convert_base(number, base_from, base_to):
    decimal_number = int(str(number), base_from)
    if base_to == 2:
        return bin(decimal_number)[2:]
    elif base_to == 8:
        return oct(decimal_number)[2:]
    elif base_to == 16:
        return hex(decimal_number)[2:]
    else:
        return str(decimal_number)


if __name__ == "__main__":
    main()