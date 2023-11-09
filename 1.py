# belajar casting
# merubah dari satu tipe ke tipe lain
print("BELAJAR CASTING")
data_int = 9;
print("data =", data_int, ",type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # boolean akan false jika nilai int = 0
print("data =", data_float, ",type =", type(data_float))
print("data =", data_str, ",type =", type(data_str))
print("data =", data_bool, ",type =", type(data_bool))


print(" \n <==================================>")
# belajar mengambil input data dari user
print("INPUT USER")
# Data yang dimasukan pasti string
data = input("Masukan data: ")
print ("Data =", data, "type =", type(data))

# jika kita ingin mengambil int, maka
input_int = int(input("masukan angka: "))
print("data = ", input_int,"type =",type(input_int))

# dan boolean
biner = bool(int(input("masukan nilai boolean: ")))
print("data = ", biner, "type =", type(biner))


print(" \n <==================================>")

# Membuat sistem ganjil genap

print ("GANJIL GENAP")

num = int(input("Masukan Angka : "))

if (num % 2) == 0 :
    print("Genap")
else :
    print("Ganjil")
    
print(" \n <==================================>")