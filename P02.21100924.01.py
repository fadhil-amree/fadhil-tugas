# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : Rabu, 28 April 2021 
# Deskripsi   : Program permainan gunting kertas batu 

N = int(input('masukkan jumlah ronde: '))
score_mor = 0
score_vin = 0

for i in range(1, N+1):
    x = input(f'Masukkan gerakan Tuan Mor ke {i} : ')
    y = input(f'Masukkan gerakan Tuan Vin ke {i} : ')
    if x == 'R' and y == 'S':
        score_mor += 1
    elif x == 'S' and y == 'P':
        score_mor += 1
    elif x == 'P' and y == 'R':
        score_mor += 1
    elif x == y:
        pass
    else:
        score_vin += 1

if score_mor > score_vin:
    print('Pemenangnya adalah Tuan Mor')
elif score_mor < score_vin:
    print('Pemenangnya adalah Tuan Vin')
else:
    print('Permainannya berakhir seri')

print('MOR:', score_mor, ' - ', 'VIN:', score_vin )