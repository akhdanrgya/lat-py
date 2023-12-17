# LIST

list_pake_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_pake_for_if)

# OPERASI

print(50 * "=" + "\n")

# INDEX  0(-3)    1(-2)     2(-1)
data = ["Ucup", "Otong", "Dudung"]

# Mengambil data dari list ini
data_0 = data[0]
print(f"data yang pertama atau index ke 0 adalah {data_0}")

data_terakhir = data[-1]
print(f"data yang terakhir adalah {data_terakhir}")

# Manipulasi dara dari list

print(50*"=" + "\n")

# Menambah Data

print(f"Data sebelum di tambah = {data}")

data.insert(0, "Asep")

print(f"Data Sesudah di tambah = {data}")

print(50*"=" + "\n")

# Menambah data tapi di akhir

data.append("jajang")
print(f"Data sesudah di tambah tapi di akhir = \n{data}")

# Menambah list dengan list

data_baru = ["Ujang", "Usep", "Dadang"]
data.extend(data_baru)

print(f"Data Gabungan = \n{data}")

# Merubah data
# kita ubah data ke 2 menjadi michael

data[2] = "Michael"
print(f"Data yang sudah di masukan Michael = \n{data}")

# Remove data
data.remove("Asep")
print(f"Data remove si asep = \n{data}")
# Jika data yang mau di remove tidak ada di dalem array maka akan error

# Remove data paling belakang

data.pop()
print(f"Remove data paling belakang = \n{data}")
