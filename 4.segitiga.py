# membuat segitiga dari +
# menggunakan metode looping
print("\nMenggunakan while true\n")

sisi = 10
spasi = int(sisi/2)
count = 1
while True :
    if (count%2):
        print(" " * spasi ,"+" * count)
        spasi -= 1
        count += 1
    else :
        count += 1
        continue
    
    if count > sisi :
        break
    
print("\nMenggunakan fungsi dan for loop\n")

def segitiga(n):
    for i in range(1, 1+n):
        print(" " * (n-i) + (" +" * (i)))
segitiga(10)