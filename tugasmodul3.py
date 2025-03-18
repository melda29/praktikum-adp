while True :
    angka_1 = float(input('Masukkan angka pertama : '))
    angka_2 = float(input('Masukkan angka kedua : '))

    print('Pilih operasi :')
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')
    print('5. Keluar')

    pilihan = input('Pilih : ')

    if pilihan == "1" :
        hasil = angka_1 + angka_2
        print('Hasil : ', hasil)
    elif pilihan == "2" :
        hasil = angka_1 - angka_2
        print('Hasil : ', hasil)
    elif pilihan == "3" :
        hasil = angka_1 * angka_2
        print('Hasil : ', hasil)
    elif pilihan == "4" :
        if angka_2 == 0 :
            print('Error : Pembagian dengan nol tidak di perbolehkan.')
        else :
            hasil = angka_1 / angka_2
            print('Hasil : ', hasil)
    elif pilihan == "5" :
        print('Terima kasih! Keluar dari program.')
        break
    else :
        print('Pilihan tidak valid, silahkan pilih lagi.')