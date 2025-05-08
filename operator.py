# Program Operator Aritmatika Sederhana

# Input dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Operasi Aritmatika
penjumlahan = angka1 + angka2
pengurangan = angka1 - angka2
perkalian = angka1 * angka2
pembagian = angka1 / angka2
modulus = angka1 % angka2

# Menampilkan hasil
print("\nHasil Operasi Aritmatika:")
print(f"{angka1} + {angka2} = {penjumlahan}")
print(f"{angka1} - {angka2} = {pengurangan}")
print(f"{angka1} * {angka2} = {perkalian}")
print(f"{angka1} / {angka2} = {pembagian}")
print(f"{angka1} % {angka2} = {modulus}")