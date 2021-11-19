print("==== Kalkulator akar dan pangkat ====")
print("Pilihan menu :")
print("1. Pangkat 2 (Kuadrat)")
print("2. Pangkat 3 (Kubik)")
print("3. Akar kuadrat")
menu = int(input("Masukan menu yang anda pilih : "))

if menu == 1:
    kuadrat = int(input("\nMasukan bilangan yang ingin di pangkatkan : "))
    print(f"Hasil dari pemangkatan bilangan {kuadrat} dengan 2 (Kuadrat) adalah {kuadrat*kuadrat}")
elif menu == 2:
    kuadrat = int(input("\nMasukan bilangan yang ingin di pangkatkan : "))
    print(f"Hasil dari pemangkatan bilangan {kuadrat} dengan 3 (Kubik) adalah {kuadrat**3}")
elif menu == 3:
    kuadrat = int(input("\nMasukan bilangan yang ingin di akarkan : "))
    print(f"Hasil akar kuadrat dari bilangan {kuadrat} adalah {kuadrat**0.5}")
else:
    print("\nPilihan menu yang di masukan tidak sesuai!")
