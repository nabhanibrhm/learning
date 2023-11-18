import sys

data = {
    "id_karyawan": None,
    "nik": None,
    "nama_karyawan": None,
    "alamat_karyawan": None,
    "divisi": None,
    "contact": None
}

def create():
    global data
    print('Masukkan Data Karyawan')


    for key in data:
        data[key] = input(f'Masukkan {key.replace("_", " ").title()}: ')
    
    menu()


def read():
    print('fungsi cari data')
    print(data)

def update():
    print('fungsi update data')

def delete():
    print('fungsi hapus data')

def pilihan():
    pilihan = input('Masukkan Pilihan :')

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
        except:
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