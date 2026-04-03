# Meminta input jumlah hari dari pengguna
total_hari = int(input("Masukkan jumlah hari proyek: "))

# Menghitung jumlah tahun
# Menggunakan pembagian bulat (//) untuk mendapatkan angka pasti
tahun = total_hari // 365
sisa_hari_setelah_tahun = total_hari % 365

# Menghitung jumlah bulan dari sisa hari tersebut
bulan = sisa_hari_setelah_tahun // 30

# Menghitung sisa hari terakhir
hari = sisa_hari_setelah_tahun % 30

# Menampilkan hasil ke piranti keluaran
print(f"Hasil konversi: {tahun} tahun, {bulan} bulan, {hari} hari")
