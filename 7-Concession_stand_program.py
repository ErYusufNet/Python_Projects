
# Menü isimli bir sözlük (dictionary) oluşturuluyor.
# Bu sözlükte her bir yiyecek ismi anahtar (key) olarak,
# fiyatı ise değer (value) olarak tanımlanmıştır.
menu = {
    "cola": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "pizza": 5
}

# Alışveriş sepeti olarak kullanılacak boş bir liste oluşturuluyor.
cart = []

# Toplam fiyatı tutmak için bir değişken oluşturuluyor ve başlangıç değeri sıfır yapılıyor.
total = 0

# Menü başlığı yazdırılıyor
print("----- MENU -----")

# Menüdeki her ürünün ismi ve fiyatı ekrana düzgün şekilde yazdırılıyor.
# key = ürün adı, value = fiyat
for key, value in menu.items():
    # f-string ile ürün adı ve fiyatı yazdırılır.
    # {:10} = ürün adını 10 karakterlik bir alana hizalar.
    # .2f = ondalık kısmı 2 basamak gösterir (örnek: 3.00)
    print(f"{key:10}: €{value:.2f}")

# Menü sonu çizgisi yazdırılıyor
print("-----------------")

# Sonsuz bir döngü başlatılıyor.
# Bu döngü kullanıcı "q" tuşlayana kadar devam eder.
while True:
    # Kullanıcıdan ürün ismi istenir.
    # .lower() metodu, girilen metni küçük harfe çevirir (case-insensitive kontrol için)
    food = input("Select an item (q to quit): ").lower()

    # Kullanıcı 'q' tuşladıysa döngüden çıkılır.
    if food == "q":
        break

    # Kullanıcının girdiği ürün menüde varsa sepete eklenir.
    elif menu.get(food) is not None:
        cart.append(food)

    # Eğer ürün menüde yoksa hiçbir şey yapılmaz (istersen buraya uyarı da ekleyebilirsin).

# Sipariş başlığı yazdırılıyor
print("----- YOUR ORDER -----")

# Sepete eklenen her ürün için:
for food in cart:
    # Ürünün fiyatı menüden alınır ve toplam fiyata eklenir.
    total = total + menu.get(food)

    # Ürünün adı aynı satırda yazdırılır (satır atlamadan)
    print(food, end=" ")

# Yeni satıra geç
print()

# Toplam ücret iki ondalıklı şekilde yazdırılır.
print(f"Total is €{total:.2f}")
