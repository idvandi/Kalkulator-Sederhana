print("Selamat datang di Kalkulator Sederhana!")

while True:
    print("\nPilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar")

    pilihan = input("Masukkan nomor operasi (1/2/3/4/5): ")

    if pilihan == '5':
        print("Terima kasih! Keluar dari program.")
        break

    if pilihan in ('1', '2', '3', '4'):
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input tidak valid! Masukkan angka yang benar.")
            continue

        if pilihan == '1':
            print(f"Hasil: {angka1} + {angka2} = {angka1 + angka2}")
        elif pilihan == '2':
            print(f"Hasil: {angka1} - {angka2} = {angka1 - angka2}")
        elif pilihan == '3':
            print(f"Hasil: {angka1} * {angka2} = {angka1 * angka2}")
        elif pilihan == '4':
            if angka2 == 0:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
            else:
                print(f"Hasil: {angka1} / {angka2} = {angka1 / angka2}")
    else:
        print("Pilihan tidak valid! Silakan pilih nomor operasi yang benar.")