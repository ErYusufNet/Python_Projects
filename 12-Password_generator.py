# Gerekli modülleri içe aktarıyoruz
import random     # Rastgele seçimler yapmak için
import string     # Hazır karakter kümeleri (harfler, rakamlar, semboller) için

# Kullanıcıdan şifre uzunluğunu alıyoruz
length = int(input("Şifre uzunluğu kaç karakter olsun? "))

# Kullanıcıya hangi karakter türlerini kullanmak istediğini soruyoruz
use_letters = input("Harf kullanılsın mı? (e/h): ").lower()  # ascii_letters (küçük ve büyük harfler)
use_digits = input("Rakam kullanılsın mı? (e/h): ").lower()   # 0-9 rakamlar
use_symbols = input("Sembol kullanılsın mı? (e/h): ").lower() # !@#$ vs gibi özel karakterler

# Boş bir karakter havuzu oluşturuyoruz
allowed_chars = ""

# Kullanıcının seçtiği türlere göre karakter havuzumuzu oluşturuyoruz
if use_letters == "e":
    allowed_chars += string.ascii_letters  # abc...ABC...
if use_digits == "e":
    allowed_chars += string.digits         # 0123456789
if use_symbols == "e":
    allowed_chars += string.punctuation    # !"#$%&'()*+,-./:;<=>?@[]^_`{|}~

# Eğer kullanıcı hiçbir şeyi seçmediyse uyarı verip çıkış yapıyoruz
if allowed_chars == "":
    print("Hiçbir karakter türü seçilmedi. Şifre oluşturulamıyor.")
else:
    # Şifreyi tutacağımız boş bir string tanımlıyoruz
    password = ""

    # Kullanıcının istediği uzunluk kadar rastgele karakter seçip şifreye ekliyoruz
    for i in range(length):
        password += random.choice(allowed_chars)

    # Sonuç olarak oluşturulan şifreyi kullanıcıya gösteriyoruz
    print("Oluşturulan şifre:", password)
