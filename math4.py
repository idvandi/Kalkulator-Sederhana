def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error: Pembagian oleh nol tidak bisa dilakukan!"
    return x / y

def kalkulator():
    print("=== Kalkulator Sederhana ===")
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    while True:
        # Pilih operasi
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        # Cek apakah pilihan valid
        if pilihan not in ['1', '2', '3', '4']:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        # Masukkan angka
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        # Lakukan operasi sesuai pilihan
        if pilihan == '1':
            print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
        elif pilihan == '2':
            print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
        elif pilihan == '3':
            print(f"Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")
        elif pilihan == '4':
            hasil = bagi(angka1, angka2)
            print(f"Hasil: {angka1} / {angka2} = {hasil}")

        # Tanya apakah ingin melanjutkan
        lanjut = input("Apakah Anda ingin melakukan perhitungan lain? (ya/tidak): ")
        if lanjut.lower() != 'ya':
            print("Terima kasih telah menggunakan kalkulator!")
            break

# Jalankan kalkulator
if __name__ == "__main__":
    kalkulator()