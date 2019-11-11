nama = 'Purwadhika Startup & Coding School'

# mencari jumlah huruf c 
cari = 'c'
x = nama.upper().replace(cari.upper(), '')
print(x)
jmlCari = len(nama) - len(x)
print(f'Jumlah huruf \'{cari}\' ada = {jmlCari}')
