

# Rastgele seçimler yapabilmek için 'random' modülü içe aktarılır.
import random

# Olası seçenekler bir demet (tuple) olarak tanımlanır: taş, kağıt, makas
options = ("rock", "paper", "scissors")

# 'playing' adında bir değişken oluşturulur ve başlangıçta True yapılır.
# Bu sayede while döngüsü oyun oynandığı sürece devam eder.
playing = True

# Ana oyun döngüsü. Kullanıcı oynamaya devam etmek istediği sürece çalışır.
while playing:
    # Oyuncunun seçimi başlangıçta boş olarak tanımlanır
    player = None

    # Bilgisayar için rastgele bir seçim yapılır
    computer = random.choice(options)

    # Oyuncudan geçerli bir seçim yapması istenir.
    # Eğer geçerli (yani options içinde) bir seçim yapılmazsa tekrar sorulur.
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")  # Oyuncudan seçim istenir

    # Oyuncu ve bilgisayarın seçimi ekrana yazdırılır
    print(f"Player choice: {player}")
    print(f"Computer choice: {computer}")

    # Karşılaştırma yapılır: önce beraberlik durumu kontrol edilir
    if player == computer:
        print("It's a tie!")  # Beraberlik durumu

    # Oyuncunun kazanabileceği durumlar kontrol edilir:
    elif player == "rock" and computer == "scissors":
        print("You win!")  # Taş makası yener
    elif player == "scissors" and computer == "paper":
        print("You win!")  # Makas kağıdı keser
    elif player == "paper" and computer == "rock":
        print("You win!")  # Kağıt taşı sarar

    # Yukarıdaki durumlar dışında kalan her durumda oyuncu kaybeder
    else:
        print("You lose!")

    # Oyuncuya tekrar oynamak isteyip istemediği sorulur
    # Eğer 'y' harfi dışında bir şey girilirse oyun biter
    if not input("Play again? (y/n): ").lower() == "y":
        playing = False  # Döngü sona erer

# Oyuncu oynamayı bıraktığında ekrana veda mesajı yazdırılır
print("Thank you for playing!")
