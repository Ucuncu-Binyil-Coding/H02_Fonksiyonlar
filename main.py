from basit_hesap_makinesi.toplama import toplama
from basit_hesap_makinesi.cikarma import cikarma

birinci_sayi = int(input("Birinci sayıyı giriniz: "))
ikinci_sayi = int(input("İkinci sayıyı giriniz: "))

toplama_sonuc = toplama(birinci_sayi,ikinci_sayi)

print(f"Toplama sonucu: {toplama_sonuc}")

ucuncu_sayi = int(input("Ucuncu sayiyi giriniz: "))

cikarma_sonuc = cikarma(toplama_sonuc,ucuncu_sayi)

print(f"Çıkarma sonucu: {cikarma_sonuc}")

# print(cikarma_sonuc)