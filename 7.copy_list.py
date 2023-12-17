# Teknik Menduplikat List

a = ["ucup", "dadang", "asep"]
print(f"a = {a}")

b = a
print(f"b = {b}")

# kita akan merubah member dari a
print(50 * "=" + "\n")
# ini akan merubah 2 list

print("Mengubah data b dan a ikut berubah")

a[1] = "michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(50 * "=" + "\n")

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print("address a dan b sama, jadi ketika b di ubah maka a akan berubah juga")

print(50 * "=" + "\n")
# Menduplikat data
print("Menduplikat list dengan copy (.copy)")

c = a.copy()  # data baru atau copy

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data index ke 0")

c[0] = "adan"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
