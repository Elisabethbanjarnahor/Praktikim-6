mahasiswa = {}  # Kamus untuk menyimpan data mahasiswa

def tambah_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    mahasiswa[nama] = nilai
    print("Data mahasiswa berhasil ditambahkan.")

def tampilkan_semua():
    if not mahasiswa:
        print("Tidak ada data mahasiswa.")
    else:
        print("Data Mahasiswa:")
        for nama, nilai in mahasiswa.items():
            print(f"{nama}: {nilai}")

def hapus_mahasiswa():
    nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
    if nama in mahasiswa:
        del mahasiswa[nama]
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("Data mahasiswa tidak ditemukan.")

def ubah_nilai():
    nama = input("Masukkan nama mahasiswa yang ingin diubah nilainya: ")
    if nama in mahasiswa:
        nilai_baru = float(input("Masukkan nilai baru: "))
        mahasiswa[nama] = nilai_baru
        print("Nilai mahasiswa berhasil diubah.")
    else:
        print("Data mahasiswa tidak ditemukan.")

while True:
    print("\nMenu:")
    print("1. Tambah data mahasiswa")
    print("2. Tampilkan semua data mahasiswa")
    print("3. Hapus data mahasiswa")
    print("4. Ubah nilai mahasiswa")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        tambah_mahasiswa()
    elif pilihan == '2':
        tampilkan_semua()
    elif pilihan == '3':
        hapus_mahasiswa()
    elif pilihan == '4':
        ubah_nilai()
    elif pilihan == '5':
        break
    else:
        print("Pilihan tidak valid.")
