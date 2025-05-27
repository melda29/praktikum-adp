def menu():
    print("Menu:")
    print("1. Tabel perkalian modulo n")
    print("2. Mencari nilai Σ x")
    print("3. Mencari nilai n!")
    print("4. Total dan rata-rata suatu data")
    print("5. Keluar")

def tabel_modulo():
    n = 0
    while n<= 0 or n >10:
        n = int(input("Masukkan nilai n(1-10):"))

    print(f"Tabel perkalian modulo {n}:")
    print("    ", end="")
    for i in range(n):
        print(f"{i:3}", end="")
    print()
    print(" "*4 + "-"*(n* 3))

    for i in range(n):
        print(f"{i:2} |", end="")
        for j in range(n):
            hasil = (i*j)%n
            print(f"{hasil:3}", end="")
        print()

def sigma():
    bawah = int(input("Batas bawah: "))
    atas = int(input("Batas atas: "))
    while atas<bawah:
        print("Batas atas harus lebih besar atau sama dengan batas bawah.")
        bawah = int(input("Batas bawah: "))
        atas = int(input("Batas atas: "))

    total = 0
    for i in range(bawah, atas + 1):
        total += i
    print(f"Σ x = {total}")

def faktorial():
    n = -1
    while n < 0:
        n = int(input("n = "))

    hasil = 1
    for i in range (1, n+1):
        hasil *= i
    print(f"{n}! = {hasil}")

def total_dan_rerata():
    n = 0
    while n<=0:
        n = int(input("Masukkan banyak data (n): "))

    data = []
    i = 0
    while i < n:
        x = float(input(f"Data ke-{i+1}: "))
        data.append(x)
        i = i +1

    total = 0
    i = 0
    while i < n:
        total = total + data[i]
        i = i + 1
    rata = total / n

    print("---------")
    print("|  Data  |")
    print("---------")
    i = 0
    while i < n:
        print(f"|  {data[i]:<5} |")
        i = i + 1
    print("--------")

    print("Total =", total)
    print("Rata-rata =", rata)

pilihan = "0"
while pilihan != "5":
    menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tabel_modulo()
    elif pilihan == "2":
        sigma()
    elif pilihan == "3":
        faktorial()
    elif pilihan == "4":
        total_dan_rerata()
    elif pilihan == "5":
        print("keluar dari program. Terima kasih!")
    else:
        print("Pilihan tidak valid. Coba lagi")