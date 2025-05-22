# Python'daki 'random' kütüphanesi, rastgele (random) sayılar üretmek için kullanılır.
import random

# Tahmin edilecek sayının alınabileceği en küçük değer
lowest_num = 1

# Tahmin edilecek sayının alınabileceği en büyük değer
highest_num = 100

# Bilgisayar, bu iki sayı arasında rastgele bir sayı seçiyor (ikisi de dahil)
answer = random.randint(lowest_num, highest_num)

# Kullanıcının kaç tahminde bulunduğunu saymak için bir sayaç
guesses = 0

# Oyun devam ederken bu değişken True kalır, doğru tahmin yapılınca False olur ve döngü biter
is_running = True

# Oyunun başlangıcında ekrana bilgilendirici yazı yazdırılır
print("Python number guessing game")  # Oyunun adı
print(f"Select a number between {lowest_num} and {highest_num}")  # Kullanıcıya hangi aralıkta tahmin yapacağını gösterir

# Buradan itibaren döngü başlar. Yani kullanıcı doğru tahmin edene kadar sürekli çalışır
while is_running:
    # Kullanıcıdan tahmin istenir
    guess = input("Enter your guess: ")

    # Kullanıcının girdiği değer rakam mı kontrol edilir. Sadece sayılar kabul edilir.
    if guess.isdigit():
        # Eğer sayıysa, onu tam sayıya (integer) dönüştür
        guess = int(guess)

        # Geçerli bir sayı girildiği için tahmin sayacı 1 arttırılır
        guesses += 1

        # Kullanıcının tahmini belirlenen aralığın dışında mı kontrol edilir
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")  # Uyarı: Sayı aralık dışında
            print(f"Please select a number between {lowest_num} and {highest_num}")  # Doğru aralığı tekrar hatırlat

        # Eğer tahmin, bilgisayarın seçtiği sayıdan küçükse
        elif guess < answer:
            print(f"Your guess is too low, try again")  # Daha yüksek bir sayı girilmesi gerektiğini belirtir

        # Eğer tahmin, bilgisayarın seçtiği sayıdan büyükse
        elif guess > answer:
            print(f"Your guess is too high, try again")  # Daha küçük bir sayı girilmesi gerektiğini belirtir

        # Tahmin doğruysa
        else:
            print(f"You have guessed {guesses} time(s) and finally found the correct number! The answer is {answer}")
            # Oyunun sona ermesini sağlar
            is_running = False

    # Eğer kullanıcı sayı dışında bir şey girdiyse (harf, sembol vs.)
    else:
        print("Invalid input")  # Hatalı giriş uyarısı
        print(f"Please select a number between {lowest_num} and {highest_num}")  # Doğru giriş formatı tekrar hatırlatılır
