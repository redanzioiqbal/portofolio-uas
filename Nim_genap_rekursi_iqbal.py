# PROGRAM NIM GENAP - Redanzio iqbal F. W
def get_fibonacci(n):
    """Menghasilkan list deret fibonacci menggunakan pendekatan iteratif."""
    deret = []
    a, b = 1, 1
    for _ in range(n):
        deret.append(a)
        a, b = b, a + b
    return deret

def hitung_perkalian(m, n):
    """Menghitung m * n menggunakan rekursi penjumlahan."""
    # Base case: jika pengali adalah 0
    if n == 0:
        return 0
    # Jika n negatif, kita ubah logikanya agar tetap akurat
    if n < 0:
        return -hitung_perkalian(m, -n)
    return m + hitung_perkalian(m, n - 1)

def tampilkan_menu():
    print("\n" + "="*20)
    print("      NIM GENAP")
    print("="*20)
    print("1. Deret Fibonacci")
    print("2. Operasi Perkalian (m x n)")
    print("0. Selesai")
    print("="*20)

def main():
    while True:
        tampilkan_menu()
        opsi = input("Pilih opsi (0-2): ")

        if opsi == "1":
            jml = int(input("Masukkan jumlah suku: "))
            hasil = get_fibonacci(jml)
            print(f"\nDeret Fibonacci ({jml} suku):")
            print(" -> ".join(map(str, hasil)))

        elif opsi == "2":
            bil = int(input("Masukkan angka: "))
            pengali = int(input("Masukkan pengali: "))
            total = hitung_perkalian(bil, pengali)
            print(f"\nHasil dari {bil} dikalikan {pengali} adalah: {total}")

        elif opsi == "0":
            print("Program dihentikan. Sampai jumpa!")
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
