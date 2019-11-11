nama = 'Purwadhika Startup & Coding School'

#mencari jumlah kata 'startup'
cari = 'startup'
x = nama.upper().replace(cari.upper(), '')
print(x)
jmlCari = int((len(nama) - len(x)) / len(cari))
print(f'Jumlah kata \'{cari}\' ada = {jmlCari}')
