import datetime

mahasiswa1 = {
    "nama" : "adan",
    "nim" : "1020230",
    "sks" : 144,
    "beasiswa" : True,
    "lahir" : datetime.datetime(2004,8,14)
}
mahasiswa2 = {
    "nama" : "arya",
    "nim" : "1124432",
    "sks" : 144,
    "beasiswa" : True,
    "lahir" : datetime.datetime(2004,6,10)
}
mahasiswa3 = {
    "nama" : "mamo",
    "nim" : "1020215",
    "sks" : 144,
    "beasiswa" : False,
    "lahir" : datetime.datetime(2002,10,20)
}

data_mahasiswa = {
    'MAH001' : mahasiswa1,
    'MAH002' : mahasiswa2,
    'MAH003' : mahasiswa3
}

print ("=" * 20)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')
    
    print(f"{KEY} | {NAMA} | {NIM} | {SKS} | {BEASISWA} | {LAHIR}")




