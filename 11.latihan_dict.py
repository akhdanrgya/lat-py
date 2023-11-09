#latihan dict
import datetime
import os
import string
import random

# template dict 

mahasiswa_tem = {
    'nama' : 'nama',
    'nim' : '00000000',
    'sks' : 0,
    'lahir' : datetime.datetime(1111,1,11)
}

data_mahasiswa = {} #data kosong dict

while True :
    os.system("cls")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("=" * 20)

    mahasiswa = dict.fromkeys(mahasiswa_tem.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa : ")
    mahasiswa['nim'] = input("NIM : ")
    mahasiswa['sks'] = int(input("SKS : "))
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY) : "))
    BULAN_LAHIR = int(input("Bulan Lahir (1-12) : "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31) : "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range (6)))
    data_mahasiswa.update({KEY:mahasiswa})
    
    print (f"{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS':^10} {'Tanggal Lahir':^10}")
    print ("=" * 60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        
        NAMA = data_mahasiswa[KEY] ['nama']
        NIM = data_mahasiswa[KEY] ['nim']
        SKS = data_mahasiswa[KEY] ['sks']
        LAHIR = data_mahasiswa[KEY] ['lahir'].strftime('%x')
        
        print (f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")
        
    print("\n")
    isDone = input("Lanjut ? y/n : ")
    if isDone == "n":
        break

print("\nProgram Selesai")
