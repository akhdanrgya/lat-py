# Operasi list


# Mengitung banyaknya data (count)

data = [1,2,4,4,3,2,5,6,5,5,6,6,2,1,]

print(f"Data nya adalah : {data}")

data_angka_4 = data.count(4)
data_angka_5 = data.count(5)

print(f"jumlah angka 4 adalah : {data_angka_4}")
print(f"jumlah angka 5 adalah : {data_angka_5}")


print(50 * "=" + "\n")

# Mencari index dari data (index)

data2 = ["dudung","ucup", "asep", "agus"]

print (f"Data nama adalah : {data2}")

index_ucup = data2.index("ucup")

print (f"index data dari ucup adalah : {index_ucup}")


print(50 * "=" + "\n")

# mengurutkan list

print(f"data sebelum di sort = \n {data}")
data.sort()
print(f"data sesudah di sort = \n {data}")

print(50 * "=" + "\n")

# balik listnya menggunakan (reverse)

data.reverse()
print(f"data sesudah di reverse = \n {data}")



