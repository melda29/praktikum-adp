print('Daftar paket makanan : ')
print('Ayam : Rp. 20000')
print('Sapi : Rp. 35000')
print('Cumi-cumi : Rp. 45000')

paket =str(input('Paket yang di pesan : '))

if paket=='Ayam' :
    harga=20000
elif paket=='Sapi' :
    harga=35000
elif paket=='Cumi-cumi' :
    harga=45000
else :
    print('Paket tidak tersedia')

jarak =float(input('Masukkan jarak rumah : '))
if jarak<1 : 
    ongkir=0
elif 1<=jarak<=3 : 
    ongkir=7000
else  : 
    ongkir=15000

total_biaya=harga+ongkir
print(f'Paket = {paket} dan Harga paket = Rp {harga}')
print(f'Biaya ongkir = Rp{ongkir}')
print(f'Biaya total = RP{total_biaya}')