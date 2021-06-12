# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : Rabu, 28 April 2021 
# Deskripsi   : Program bot membaca diskon

banyak_barang = int(input('Masukkan banyak barang : '))
harga_ = [0 for i in range(banyak_barang)]
besar_diskon =[0 for i in range(banyak_barang)]
barang = {}
for i in range (1, banyak_barang + 1):
    harga = int(input(f'Masukkan harga barang ke-{i} :'))
    harga_[i-1] = harga

for j in range (1, banyak_barang + 1):    
    diskon = int(input(f'Masukkan besar diskon (dalam persen) barang ke-{j} : '))
    besardiskon = (diskon / 100) * harga_[j-1]
    besar_diskon[j-1]= besardiskon
    barang[j-1] = f'Barang {j}'

x = max(besar_diskon)

a = besar_diskon.index(x)

print('barang', a + 1, 'memiliki diskon paling besar yaitu', x)


