# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : Rabu, 28 April 2021 
# Deskripsi   : Program mengubah bilangan dari basis K ke basis 10

N = int(input('masukkan nilai N: '))
K = int(input('masukkan nilai K: '))
Bilangan = 0
for i in range (N):
    a = int(input(f'Masukkan digit ke {i+1}:'))
    Bilangan += a * K**(N-i-1)

print('Bilangan dalam basis 10 adalah', Bilangan)
