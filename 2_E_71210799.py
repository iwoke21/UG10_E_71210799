suhu = float(input("Masukan suhu tubuh Anda : "))
if suhu > 50:
    print("Anda bukan Manusia :)")
elif suhu <= 37.5 and suhu >= 32:
    print("Suhu Anda normal!")
elif suhu >= 37.5 and suhu <= 50:
    print("Anda demam! Jangan berpergian ke tempat fasilitas Umum.")
else:
    print("Anda kedinginan! Silahkan caari sesuatu yang hangat!")