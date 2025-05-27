# Bu fonksiyon bir metni (text) alır ve her harfi belirli sayıda (shift kadar) kaydırarak şifreli hale getirir.
def encrypt(text: str, shift: int) -> str:
    result = ""  # Şifreli sonucu saklayacağımız boş bir metin başlatıyoruz.

    # Metindeki her karakteri tek tek kontrol ediyoruz.
    for char in text:
        if char.isalpha():  # Bu karakter bir harf mi? (A-Z veya a-z). Harfse şifrele.
            # Büyük harfse ord('A') = 65, küçük harfse ord('a') = 97 alınır.
            base = ord('A') if char.isupper() else ord('a')

            # ord(char): karakterin sayısal (ASCII) değerini verir.
            # (ord(char) - base): Harfin alfabedeki sıra numarasını bulur (örnek: 'b' -> 1)
            # Bu sırayı shift kadar kaydırırız, 26'ya göre mod alarak alfabe dışına çıkmayız.
            shifted = (ord(char) - base + shift) % 26

            # Şifrelenmiş yeni harfi hesaplarız ve sonuç metnine ekleriz.
            result += chr(base + shifted)
        else:
            # Eğer karakter harf değilse (örneğin boşluk, virgül, sayı vs.), olduğu gibi bırakırız.
            result += char

    return result  # Şifrelenmiş metni döndür.

# Bu fonksiyon da şifre çözmek için. Aslında yukarıdaki encrypt fonksiyonunu -shift ile tekrar kullanır.
def decrypt(text: str, shift: int) -> str:
    # Önemli: Şifre çözme = Aynı şifreleme algoritmasını TERSTEN uygulamak.
    return encrypt(text, -shift)

# Fonksiyonu test ediyoruz:
print(encrypt("abc", 2))          # Sonuç: 'cde' — Her harf 2 harf ileri alınmış.
print(decrypt("cde", 2))          # Sonuç: 'abc' — Aynı şekilde geri alınmış.
print(decrypt("Hello, World!", 5)) # Sonuç: 'Czggj, Rjmgy!' — 'Hello, World!' 5 geri alınarak çözülmüş.
