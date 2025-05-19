# Komentar Siva: Program Kalkulator Sederhana

# Deklarasi variabel
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
op = input("Masukkan operator (+, -, *, /): ")

# Proses perhitungan
if op == '+':
    hasil = a + b
elif op == '-':
    hasil = a - b
elif op == '*':
    hasil = a * b
elif op == '/':
    if b != 0:
        hasil = a / b
    else:
        hasil = "Error: Pembagian dengan nol!"
else:
    hasil = "Operator tidak dikenali."

# Output hasil
print("Hasil:", hasil)