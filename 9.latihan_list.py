# latihan list

list_buku = []

while True:
    print("\n Masukan data Buku")
    judul = input("judul\t: ")
    penulis = input("penulis\t: ")

    buku_baru = (judul, penulis)
    list_buku.append(buku_baru)

    print("\n\n", "="*20, "data buku", "="*20, "\n")
    for index, buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n\n", "=" * 20)
    isLanjut = input("Apakah masih lanjut y/n :")

    if isLanjut == "n":
        break


print("\nProgram selesai")





