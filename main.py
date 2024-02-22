import random

welcome_message = "KEYAKINAN ADALAH KUNCI"
welcome_message2 = "TERIMA KASIH SUDAH MEMAINKAN GAME SEDERHANA INI"
babi_position = random.randint(1,4)


print("**********************************")
print(f"***** {welcome_message} *****")
print("**********************************")

nama_user = input ("MASUKAN NAMA KAMU : ")

print (f'''
HALO {nama_user}! COBA PERHATIKAN PILIHAN DIBAWAH INI.

|1| |2| |3| |4|

ADA BABI DI DALAM GOA TERSEBUT !!
''')

pilihan_user = int(input (f"MENURUT KAMU, DI GOA NOMOR BERAPA BABI TERSEBUT BERSEMBUNYI :"))


keyakinan_y = "y"
keyakinan_n = "n"
keyakinan = input ("APAKAH KAMU YAKIN DENGAN PILIHAN TERSEBUT [y/n] :") 

jawaban_sebelumnya = pilihan_user
jawaban_baru = pilihan_user


if keyakinan == keyakinan_y:
    print("KAMU SANGAT YAKIN SEKALI DENGAN PILIHANMU !!")
elif keyakinan == keyakinan_n:
    print("KENAPA KAMU TIDAK YAKIN DENGAN PILIHANMU")
    
    ganti_jawaban = input("APAKAH KAMU INGIN MENGGANTI JAWABANMU ? [y/n]: ")
    if ganti_jawaban == keyakinan_y :
        pilihan_user = jawaban_baru = int(input("SILAHKAN MASUKAN JAWABAN BARU : "))
        print(f"JAWABANMU TELAH DIGANTI MENJADI :{pilihan_user}")
        
else:
    input(print("SAYA AKAN MENJAWAB JIKA KAMU MEMILIH [y/n]"))
    
    
    # hasil akhir

if pilihan_user == babi_position:
    print(f"SELAMAT {nama_user} KARENA KEYAKINANMU SANGAT KUAT KAMU MENANG! Posisi BABI berada di goa nomor {babi_position} dan pilihanmu adalah goa nomor {pilihan_user}")
elif babi_position == jawaban_sebelumnya:
    print(f"YAH !! PADAHAL JAWABAN NOMOR {jawaban_sebelumnya} BENAR. NAMUN, KAMU MALAH MENGGANTINYA MENJADI {jawaban_baru}, BABI TERSEBUT BERADA DI GUA NOMOR {babi_position}")
else:
    print(f"PILIHANMU SALAH !!! BABI TERSEBUT BERADA DI GOA NOMOR {babi_position}. SEDANGKAN KAMU MEMILIH GOA NOMOR {pilihan_user}.")
    

print('''
       ''')
print("***********************************************************")
print(f"***** {welcome_message2} *****")
print("***********************************************************")


