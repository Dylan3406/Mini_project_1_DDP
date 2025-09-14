# Program Manajemen Data Penerima Bantuan Sosial Kelurahan Sempaja Selatan

# Data Penerima Diisi Dengan 5 Contoh Data
data_penerima = [
    {
        "nama": "Naruto",
        "nik": 1,
        "alamat": "Konoha",
        "jenis bantuan": "Chakra"
    },
    {
        "nama": "Boruto",
        "nik": 2,
        "alamat": "Konoha",
        "jenis bantuan": "Karma"
    },
    {
        "nama": "Saruto",
        "nik": 3,
        "alamat": "Konoha",
        "jenis bantuan": "Chakra"
    },
    {
        "nama": "Ashuto",
        "nik": 4,
        "alamat": "Konoha",
        "jenis bantuan": "Chakra"
    },
    {
        "nama": "Saburo",
        "nik": 5,
        "alamat": "Konoha",
        "jenis bantuan": "Chakra"
    }
]

# Menambahkan Data Penerima Bantuan Sosial (Create)
def tambah_penerima():
    "Fungsi untuk menambahkan data penerima baru."
    print("--- Tambah Data Penerima ---")
    nama = input("Masukkan Nama lengkap: ")
    nik = int(input("Masukkan NIK (Nomor Induk Kependudukan): "))
    alamat = input("Masukkan Alamat lengkap: ")
    jenis_bantuan = input("Masukkan Jenis Bantuan (Contoh: Sembako, Uang Tunai, dll): ")

    penerima_baru = {
        "nama": nama,
        "nik": nik,
        "alamat": alamat,
        "jenis bantuan": jenis_bantuan
    }
    data_penerima.append(penerima_baru)
    print("Data penerima baru telah ditambahkan.")

# Melihat Data Penerima Bantuan Sosial (Read)
def lihat_penerima():
    "Fungsi untuk menampilkan semua data penerima."
    print("--- Daftar Penerima Bantuan Sosial ---")
    
    for X, penerima in enumerate(data_penerima):
        print("=====================")
        print(f"No. {X + 1}")
        print(f"Nama: {penerima['nama']}")
        print(f"NIK: {penerima['nik']}")
        print(f"Alamat: {penerima['alamat']}")
        print(f"Jenis Bantuan: {penerima['jenis bantuan']}")
    print("=====================")

# Mengubah Data Penerima Bantuan Sosial (Update)
def ubah_penerima():
    "Fungsi untuk mengubah data penerima yang sudah ada."
    print("--- Ubah Data Penerima ---")
    nik_cari = int(input("Masukkan NIK penerima yang ingin diubah: "))
    
    ditemukan = False
    for penerima in data_penerima:
        if penerima["nik"] == nik_cari:
            print(f"Data ditemukan! Nama: {penerima['nama']}")
            penerima["nama"] = input("Masukkan Nama baru: ")
            penerima["alamat"] = input("Masukkan Alamat baru: ")
            penerima["jenis bantuan"] = input("Masukkan Jenis Bantuan baru: ")
            print("Data berhasil diperbarui!")
            ditemukan = True
    
    if not ditemukan:
        print("NIK yang Anda masukkan tidak ditemukan!")

# Menghapus Data Penerima Bantuan Sosial (Delete)
def hapus_penerima():
    "Fungsi untuk menghapus data penerima."
    print("--- Hapus Data Penerima ---")
    hapus_nik = int(input("Masukkan NIK penerima yang ingin dihapus: "))
    
    ditemukan = False
    for X, penerima in enumerate(data_penerima):
        if penerima["nik"] == hapus_nik:
            data_yang_dihapus = data_penerima.pop(X)
            print(f"Nama: {data_yang_dihapus['nama']}")
            print(f"NIK: {data_yang_dihapus['nik']}")
            print("Data di atas telah berhasil dihapus!")
            ditemukan = True
    
    if not ditemukan:
        print("NIK yang Anda masukkan tidak ditemukan!")

# Tampilan Menu Awal Program Bantuan Sosial (Menu)
def menu_utama():
    "Fungsi untuk menampilkan menu utama program."
    print("--------------------------")
    print("Program Manajemen Bansos")
    print("Kelurahan Sempaja Selatan")
    print("--------------------------")
    print("Silakan pilih opsi di bawah ini:")
    print("1. Tambah Penerima")
    print("2. Lihat Semua Penerima")
    print("3. Ubah Data Penerima")
    print("4. Hapus Penerima")
    print("5. Keluar")

    pilihan = input("Pilihan Anda (1-5): ") 

    if pilihan == "1":
        tambah_penerima()
    elif pilihan == "2":
        lihat_penerima()
    elif pilihan == "3":
        ubah_penerima()
    elif pilihan == "4":
        hapus_penerima()
    elif pilihan == "5":
        print("Sampai jumpa!")
    else:
        print("Pilihan Anda tidak valid. Silakan coba lagi dengan angka 1 sampai 5.")

# Jalankan program
menu_utama()