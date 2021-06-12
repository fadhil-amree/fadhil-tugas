# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : Rabu, 28 April 2021 
# Deskripsi   : Program menentukan titik terdapat pada garis

N = int(input('Masukkan N : '))
garis_L = [0 for i in range(N)] 
garis_R = [0 for j in range(N)] 
for a in range(N):
    L = int(input(f'Masukkan L[{a+1}] : '))
    R = int(input(f'Masukkan R[{a+1}] : '))
    garis_L[a] = L
    garis_R[a] = R

Q = int(input('Masukkan Q: '))

for b in range(Q):
    count = 0
    x = int(input(f'Masukkan x ke {b+1} :'))
    for c in range(N):
        if (garis_L[c] <= x <= garis_R[c]) or (garis_R[c] <= x <= garis_L[c]):
            print('titik ke -', b+1, 'ada di garis' )
            count += 1
            break
    if count == 0:
        print('titik ke -', b, 'tidak ada di garis')

