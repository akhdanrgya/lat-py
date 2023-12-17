# nested list atau list gabungan

data0 = [1, 2, 3]
data1 = [4, 5, 6]
data_biasa = [1, 2, 3, 4, 5, 6,]

print(f"data 0 adalah = {data0}")
print(f"data 1 adalah = {data1}")
print(f"data biasa adalah = {data_biasa}")

print(50 * "=" + "\n")


# digabung menjadi

data_2D = [data0, data1, data_biasa, 1, 2]
print(f"gabungan data yang ada di atas atau list 2D = \n{data_2D}")

print(50 * "=" + "\n")

# contoh penggunaan

peserta0 = ["ucup", 20, "laki-laki"]
peserta1 = ["dadang", 30, "laki-laki"]
peserta2 = ["otong", 10, "laki-laki"]

data_peserta = [peserta0, peserta1, peserta2]
print(f"data pesesta = \n {data_peserta}")

for peserta in data_peserta:
    print(f"Nama \t : {peserta[0]}")
    print(f"Umur \t : {peserta[1]}")
    print(f"Gender \t : {peserta[2]}\n")
