# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : Rabu, 28 April 2021 
# Deskripsi   : Program mengembalikan bilangan cantik terkecil yang habis dibagi X

x = int(input('Masukkan X: '))
a = ''
b = []
count = 0
j = 1
for i in range (1,10):
    while j > 0:
        a = str(i) * j
        if int(a) % x == 0:
            b.append(int(a))    
            j = 1
            break 
        j += 1


a = min(b)
print('Bilangan cantik terkecil yang habis dibagi ', x, 'adalah', a )