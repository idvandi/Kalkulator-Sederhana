def tambah(x, y):
 return x + y

def kurang(x, y):
 return x - y

def kali(x, y):
 return x * y

def bagi(x, y):
 if y == 0:
  return "Error! Pembagian dengan nol."
 return x / y

print("Pilih operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

while True:
 pilihan = input("Masukkan pilihan (1/2/3/4): ")
 
 if pilihan in ('1', '2', '3', '4'):
  num1 = float(input("Masukkan angka pertama: "))
  num2 = float(input("Masukkan angka kedua: "))

  if pilihan == '1':
   print(num1, "+", num2, "=", tambah(num1, num2))

  elif pilihan == '2':
   print(num1, "-", num2, "=", kurang(num1, num2))

  elif pilihan == '3':
   print(num1, "*", num2, "=", kali(num1, num2))

  elif pilihan == '4':
   print(num1, "/", num2, "=", bagi(num1, num2))
 
 else:
  print("Input tidak valid")