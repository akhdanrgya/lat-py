# Perulangan atau looping

for i in range(5):
    print (f"i sekarang adalah : {i + 1}")
    
print (f"Akhir dari Looping \n")
print (20 * "=" + "\n") 


# LATIHAN
print ("Awal Dari Metode For")
# 1. Menggunakan for i in range ()
sisi = int(input("berapa sisi ??"))
# dummy variable
count = 1
for i in range (sisi) :
    print("*"* count)
    count += 1
print ("Akhir Dari Metode For")
    
    
print (20 * "=" + "\n")


print("Awal Dari Metode While")
# 2. Menggunakan While
count = 1
while True:
    print("*"* count)
    count += 1

    if count > sisi:
        break


print("Akhir Dari Metode While")
