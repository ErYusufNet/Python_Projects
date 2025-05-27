def encrypt(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():#sadece harfler sifrelenir
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char
    return result
def decrypt(text: str, shift: int) -> str:
    return encrypt(text, shift)
print(encrypt("abc", 2))
print(decrypt("cde", 2))
print(decrypt("Hello, World!", 5))


