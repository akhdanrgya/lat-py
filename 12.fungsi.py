def get_day(day_number):
    switch = {
        1: 'Senin',
        2: 'Selasa',
        3: 'Rabu',
        4: 'Kamis',
        5: 'Jumat',
        6: 'Sabtu',
        7: 'Minggu'
    }
    return switch.get(day_number, "Nomor hari tidak valid")

day_number = int(input("Masukkan angka (1-7): "))
print(get_day(day_number))
