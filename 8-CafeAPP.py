

# Menüdeki ürünleri ve fiyatlarını saklayan sözlük (dictionary)
menu = {
    "coffee": 2.50,
    "tea": 1.80,
    "cake": 3.00,
    "sandwich": 4.50
}

# Kullanıcının siparişlerini tutmak için boş bir sözlük (ürün: adet)
cart = {}


# Menü başlığını yazdır
print("----- MENU -----")
for item, price in menu.items():
    print(f"{item:10} : €{price:.2f}")  # Menüdeki ürünleri düzgün şekilde yazdır
print("----------------")

# Kullanıcı sipariş verene kadar döngü başlat
while True:
    product = input("Please select an item (type 'q' to quit): ").lower()  # Ürünü küçük harfe çevir

    if product == "q":
        break  # Kullanıcı çıkmak istiyorsa döngüden çık

    if product not in menu:
        print("Sorry, we don't have that item.")
        continue  # Menüde olmayan ürünse döngünün başına dön

    try:
        quantity = int(input(f"How many {product}s would you like? "))
        if quantity <= 0:
            print("Please enter a positive number.")
            continue
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        continue

    # Ürünü sepete ekle (önceden varsa üzerine ekle)
    cart[product] = cart.get(product, 0) + quantity

# Sipariş özeti
print("\n----- YOUR ORDER -----")
total = 0

for item, quantity in cart.items():
    price = menu[item]
    item_total = price * quantity
    total += item_total
    print(f"{quantity} x {item:10} = €{item_total:.2f}")  # Her ürünün toplamını yaz

# Toplam fiyatı yaz
print("-----------------------")
print(f"TOTAL: €{total:.2f}")
