#Nama/NIM:Muhammad Fadhil Amri / 21100924
#Tanggal:26 Juli 2021
#Program menghitung banyak kemunculan kata 'tuan'
c = 0
hrf = input()

for i in range(len(hrf)):
    if hrf[i] =='t':
        for j in range(i+1,len(hrf)):
            if hrf[j]=='u':
                for k in range(j+1,len(hrf)):
                    if hrf[k]=='a':
                        for l in range(k+1,len(hrf)):
                            if hrf[l]=="n":
                                c+=1


print(f'Ada {c} buah kemunculan')
