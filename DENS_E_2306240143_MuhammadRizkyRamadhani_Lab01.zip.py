#Penamaan Judul Untuk Memperbagus Tampilan
print("Pesan Rahasia Kelompok Zog")
print("''''''''''''''''''''''''''")

#Menginput pesan dalam bahasa zog (Dalam Hexadecimal)
pesan_zog = str(input("Masukkan pesan zog: "))
bytes_pesan_zog = bytes.fromhex(pesan_zog)
ascii_pesan_zog = bytes_pesan_zog.decode("ASCII")

#Menginput Angka 1 dan 2 dari Password
angka1_password = int(input("Masukkan Angka 1: " ))
angka2_password = int(input("Masukkan Angka 2: "))

#Perkalian angka password dan perubahan hasilnya menjadi bilangan biner
hasil_angka = (angka1_password * angka2_password * 13) 
hasil_angkabiner = bin(hasil_angka)
password_akhir = (hasil_angkabiner)

#Print hasil dari input yang telah dimasukkan sebelumnya
print ("Pesan \"" + str(ascii_pesan_zog) + "\" telah diterima dengan password \"" + password_akhir + "\"")
