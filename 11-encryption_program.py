# Gerekli kütüphaneleri içe aktar
import random     # Rastgele karıştırma (shuffle) işlemi için kullanılır
import string     # Harf, sayı ve özel karakterleri almak için kullanılır

# Şifreleme işleminde kullanılacak tüm karakterleri birleştiriyoruz:
# string.punctuation -> !, ?, %, vb.
# string.digits -> 0-9
# string.ascii_letters -> a-z ve A-Z
# Başına bir boşluk (" ") da ekliyoruz çünkü boşluk karakteri de mesajda olabilir
chars = " " + string.punctuation + string.digits + string.ascii_letters

# Bu karakterleri listeye çeviriyoruz (her karakter ayrı eleman olacak şekilde)
chars = list(chars)

# Aynı karakterlerden oluşan bir kopya oluşturuyoruz.
# Bu kopyayı karıştırarak bir "şifreleme anahtarı (key)" elde edeceğiz
key = chars.copy()

# Anahtar listesini rastgele karıştırıyoruz.
# Böylece her karakterin yerine başka rastgele bir karakter gelecek
random.shuffle(key)

# Hem orijinal karakterleri hem de şifreleme anahtarını yazdırıyoruz (kontrol amaçlı)
print(f"chars: {chars}")  # Orijinal karakterler
print(f"key: {key}")      # Şifrelenmiş karakter eşleşmeleri

# Kullanıcıdan şifrelenecek bir mesaj alıyoruz
plain_text = input("Enter a message to encrypt: ")

# Şifrelenmiş (gizlenmiş) mesajı tutmak için boş bir string oluşturuyoruz
cipher_text = ""

# Mesajdaki her harfi tek tek ele alıyoruz
for letter in plain_text:
    # Harfin orijinal listedeki (chars) indeksini bul
    index = chars.index(letter)

    # Aynı index'teki karıştırılmış karakteri (key[index]) al ve cipher_text'e ekle
    cipher_text += key[index]

# Sonuçları ekrana yazdırıyoruz
print(f"Original message: {plain_text}")        # Kullanıcının girdiği orijinal mesaj
print(f"Encrypted message: {cipher_text}")      # Şifrelenmiş hali
