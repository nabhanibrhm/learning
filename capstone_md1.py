#test
import sys


# define column name dictionary
data = {
    "id_karyawan": None,
    "nik": None,
    "nama_karyawan": None,
    "alamat_karyawan": None,
    "divisi": None,
    "contact": None
}


#untuk define list untuk data yg mau dimasukkan
entry_list =[]



def create():
    global data # memanggil variable(dictionary) data dari global
    print('\n\nInput Data Karyawan\n\n')

    num_entries = int(input('Berapa kali ingin memasukkan data karyawan? ')) # meminta inputan berapa kali data ingin dimasukkan

    for no in range(num_entries): # membuat perulangan berdasarkan range dari num_entries
        print("\n") #ngasih enter
        entry_data = {} # membuat variable list untuk menyimpan data yang user akan input
        for key in data: # membuat perulangan untuk memasukkan data berdasarkan key dari dictionary data
            entry_data[key] = input(f'Masukkan {key.replace("_", " ").title()} ke {no+1}: ') # input data
        entry_list.append(entry_data) # fungsi untuk memasukkan list pada entry data kedalam entry_list


    print("\n\n")
    menu()


def read():
    print('fungsi membaca data\n\n')
    print("|", end="") # print | dan endofstring
    for key in data.keys():
        print("{:^15} |".format(key), end=" ") # loop berfungsi untuk menampilkan key/ header column dari dictionary data
    print()

    # Print values below each key
    
    for entry_data in entry_list:
        print("|", end="")
        for value in entry_data.values():
            print("{:^15} |".format(str(value)), end=" ") # lop berfungsi untuk menampilkan dictionary entry_data yang sudah kita input sebelumnya
        print()
    print("\n\n")
    menu()

def update():
    print('fungsi update data')

def delete():
    print('fungsi hapus data')


def exit():
    sys.exit()

def menu():
    print('Menu Utama\n')
    print('1. Input Data')
    print('2. Lihat Data')
    print('3. Ubah Data')
    print('4. Hapus Data')
    print('5. Keluar\n\n')


    while True:
        try:
            pilihan = int(input('Masukkan Pilihan: '))
            break
        except Exception:
            print('Pilihan salah. Harap masukkan angka yang valid.')

    if pilihan == 1:
        create()
    elif pilihan == 2:
        read()
    elif pilihan == 3:
        update()
    elif pilihan == 4:
        delete()
    elif pilihan == 5:
        exit()
    



if __name__ == "__main__":
    menu()