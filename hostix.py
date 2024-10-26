import os
from datetime import datetime

def call():
    while True:
        # Şuanki Dizini al
        patch = os.getcwd()
        # Kullanıcıdan komut al
        cmdcall = input(patch + "> ")

        if cmdcall == 'cls':
            print("\n" * 1000)  # Ekranı 1000 satır boşlukla doldur
        elif cmdcall == 'dir':
            # Mevcut dizindeki dosyaları al
            dizin = os.getcwd()
            dosyalar = os.listdir(dizin)

            print(f"\n{dizin} dizinindeki dosyalar:")
            print(f"{'Dosya Adı':<30} {'Boyut (KB)':<15} {'Tarih':<25}")

            for dosya in dosyalar:
                # Tam dosya yolunu oluştur
                tam_yol = os.path.join(dizin, dosya)

                # Dosya olup olmadığını kontrol et
                if os.path.isfile(tam_yol):
                    # Dosya boyutunu KB cinsine çevir
                    boyut = os.path.getsize(tam_yol) / 1024
                    # Dosya oluşturulma tarihini al
                    tarih = datetime.fromtimestamp(os.path.getmtime(tam_yol)).strftime('%Y-%m-%d %H:%M:%S')
                    
                    # Bilgileri yazdır
                    print(f"{dosya:<30} {boyut:<15.2f} {tarih:<25}")

        elif cmdcall.startswith('cd '):  # 'cd' komutu ile dizin değiştirme
            # 'cd ' kısmını çıkar
            yeni_dizin = cmdcall[3:]
            şuanki_dizin = os.getcwd()  # Şu anki dizini al
            print("Your Path: " + şuanki_dizin)

            try:
                os.chdir(yeni_dizin)  # Çalışma dizinini değiştir
                print(f"You are now in: {os.getcwd()}")  # Geçerli dizini göster
            except FileNotFoundError:
                print("Error: We don't find your path.")  # Hata mesajı
            except NotADirectoryError:
                print("Error: The path you specified is not a directory.")  # Hata mesajı
            except PermissionError:
                print("Error: You do not have permission to access this directory.")  # Hata mesajı

        elif cmdcall.startswith('start '):  # 'start' komutu ile dosya çalıştırma
            # 'start ' kısmını çıkar
            dosya_adi = cmdcall[6:]

            try:
                os.system(f'start {dosya_adi}' if os.name == "nt" else f'open {dosya_adi}')
                print(f"Starting {dosya_adi}...")
            except Exception as e:
                print(f"Error starting {dosya_adi}: {e}")

        elif cmdcall == 'help':
            print("\nHelp Menu:")
            print("help : Shows Commands")
            print("cls : Clears the screen")
            print("start : Opens a file")
            print("cd : Changes directory")
            print("dir : Lists files in the current directory\n")

        elif cmdcall == 'exit':
            print("Exiting...")
            break
        else:
            print("Invalid Command")

projectCreatedBy = "Wlame"
projectVersion = "1.0"

print("HostiX Python Commander [Version 1.0] Tüm hakları saklıdır.")
call()
