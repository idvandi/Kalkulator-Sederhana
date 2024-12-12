def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak bisa membagi dengan nol"

def kalkulator():
    print("=== Kalkulator Sederhana ===")
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    try:
        pilihan = int(input("Masukkan pilihan (1/2/3/4): "))
        if pilihan not in [1, 2, 3, 4]:
            print("Pilihan tidak valid. Silakan coba lagi.")
            return

        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))

        if pilihan == 1:
            print(f"Hasil: {tambah(a, b)}")
        elif pilihan == 2:
            print(f"Hasil: {kurang(a, b)}")
        elif pilihan == 3:
            print(f"Hasil: {kali(a, b)}")
        elif pilihan == 4:
            print(f"Hasil: {bagi(a, b)}")
    except ValueError:
        print("Input tidak valid. Pastikan memasukkan angka.")

if __name__ == "__main__":
    kalkulator()