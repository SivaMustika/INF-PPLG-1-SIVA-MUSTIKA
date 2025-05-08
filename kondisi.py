# Input nama dan umur
nama = input("Siva: ")
umur = int(input("Siva: "))

# Kondisi berdasarkan nama dan umur
if nama == "Siva":
    if umur < 13:
        print("Halo Siva, kamu masih anak-anak.")
    elif umur < 18:
        print("Halo Siva, kamu remaja.")
    else:
        print("Halo Siva, kamu sudah dewasa.")
else:
    print("Nama Anda bukan Siva, program hanya untuk Siva.")