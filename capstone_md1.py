import sys

data = {
    "id_karyawan": None,
    "nik": None,
    "nama_karyawan": None,
    "alamat_karyawan": None,
    "divisi": None,
    "contact": None
}

entry_list =[]

def create():
    global data
    print('\n\nInput Data Karyawan\n\n')

    num_entries = int(input('Berapa kali ingin memasukkan data karyawan? '))

    for no in range(num_entries):
        print("\n")
        entry_data = {}
        for key in data:
            entry_data[key] = input(f'Masukkan {key.replace("_", " ").title()} ke {no+1}: ')
        entry_list.append(entry_data)

    

    # print header key
    print("|", end="")
    for key in data.keys():
        print("{:^15} |".format(key), end=" ")
    print()

    # Print values below each key
    for entry_data in entry_list:
        print("|", end="")
        for value in entry_data.values():
            print("{:^15} |".format(str(value)), end=" ")
        print()


    print("\n\n")
    menu()


def read():
    print('fungsi cari data')
        # print header key
    print("|", end="")
    for key in data.keys():
        print("{:^15} |".format(key), end=" ")
    print()

    # Print values below each key
    
    for entry_data in entry_list:
        print("|", end="")
        for value in entry_data.values():
            print("{:^15} |".format(str(value)), end=" ")
        print()

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