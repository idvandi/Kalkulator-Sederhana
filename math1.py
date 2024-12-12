# Fungsi untuk menambahkan dua angka
def tambah(x, y):
    return x + y

# Fungsi untuk mengurangi dua angka
def kurang(x, y):
    return x - y

# Fungsi untuk mengalikan dua angka
def kali(x, y):
    return x * y

# Fungsi untuk membagi dua angka
def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Pembagian dengan nol tidak diperbolehkan."

# Menu operasi
print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Meminta input dari pengguna
pilihan = input("Masukkan pilihan (1/2/3/4): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == '1':
    print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
elif pilihan == '2':
    print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
elif pilihan == '3':
    print(f"Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")
elif pilihan == '4':
    print(f"Hasil: {angka1} / {angka2} = {bagi(angka1, angka2)}")
else:
    print("Pilihan tidak valid.")