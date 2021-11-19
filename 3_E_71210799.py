daftar = input("masukkan daftar siswa : ").title().split(",")
print("Daftar siswa :",daftar)

tambah = input("Masukan siswa yang ingin di tambahkan  : ").lower()
if tambah.title() in daftar:
    print("siswa atas nama",tambah.upper(),"sudah berada dalam daftar siswa")
else:
    daftar.append(tambah.upper())
    print("Hasil penambahan pada daftar siswa :",daftar)