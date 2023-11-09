# Latihan Percabangan (Kalkulator sederhana)

print ("Kalkulator Sederhana")
print (20*"=" + "\n")

angka1 = float(input("Masukan angka pertama :"))
operator = input("Masukan operator (- + * /) :")
angka2 = float(input("Masukan angka kedua :"))

# Percabangannya

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/" :
    hasil = angka1 / angka2
else :
    print("Mohon ulangi lagi")


print (f"Hasilnya adalah : {hasil}")