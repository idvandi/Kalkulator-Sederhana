def kalkulator():
    while True:
        print("Pilih operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan in ('1', '2', '3', '4'):
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Input harus berupa angka!")
                continue

            if pilihan == '1':
                hasil = angka1 + angka2
                print("Hasil penjumlahan:", hasil)
            elif pilihan == '2':
                hasil = angka1 - angka2
                print("Hasil pengurangan:", hasil)
            elif pilihan == '3':
                hasil = angka1 * angka2
                print("Hasil perkalian:", hasil)
            elif pilihan == '4':
                if angka2 == 0:
                    print("Tidak dapat membagi dengan nol!")
                else:
                    hasil = angka1 / angka2
                    print("Hasil pembagian:", hasil)
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    kalkulator()