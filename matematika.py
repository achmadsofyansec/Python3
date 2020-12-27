import os 
import sys 
import system

system.date()
print("\r\n")
print("========================")
print("====== MATEMATIKA ======")
print("========================")
print("\r\n")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pangkat 2")
print("5. Pembagian")
print("6. Modulus")
print("7. Persen")
print("8. Keluar")
print("\r\n")
print("Masukkan operasi matematika yang dipilih : ")
user_select = int(input())

if user_select == 1:
   angka1 = int(input("Masukkan angka pertama : "))
   angka2 = int(input("Masukkan angka kedua : "))
   hasil  = (angka1 + angka2)
   print("Hasil pertambahan dari", angka1, "+", angka2, "=", hasil)
elif user_select == 2:
   angka1 = int(input("Masukkan angka pertama : "))
   angka2 = int(input("Masukkan angka kedua : "))
   hasil  = (angka1 + angka2)
   print("Hasil pengurangan dari", angka1, "-", angka2, "=", hasil)
elif user_select == 3:
   angka1 = int(input("Masukkan angka pertama : "))
   angka2 = int(input("Masukkan angka kedua : "))
   hasil  = (angka1 * angka2)
   print("Hasil pertambahan dari", angka1, "*", angka2, "=", hasil)
elif user_select == 4:
   angka1 = int(input("Masukkan angka pertama : "))
   angka2 = int(input("Masukkan angka kedua : "))
   hasil  = (angka1 ** angka2)
   print("Hasil pemangkatan dari", angka1, "^2", angka2, "=", hasil)
elif user_select == 5:
   angka1 = int(input("Masukkan angka pertama : "))
   angka2 = int(input("Masukkan angka kedua : "))
   hasil  = (angka1 / angka2)
   print("Hasil pembagian dari", angka1, ":", angka2, "=", hasil)
elif user_select == 6:
   angka1 = int(input("Masukkan angka pertama : "))
   angka2 = int(input("Masukkan angka kedua : "))
   hasil  = (angka1 // angka2)
   print("Hasil modulus dari", angka1, "//", angka2, "=", hasil)
elif user_select == 7:
   angka1 = int(input("Masukkan angka pertama : "))
   angka2 = int(input("Masukkan angka kedua : "))
   hasil  = (angka1 % angka2)
   print("Hasil sisa bagi dari", angka1, "%", angka2, "=", hasil)
elif user_select == 8:
   sys.exit()
else:
   print ("Masukkan Pilihan dengan benar")

    