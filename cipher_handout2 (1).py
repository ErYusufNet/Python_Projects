def encrypt(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char
    return result

def decrypt(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base - shift) % 26  # Apply negative shift directly
            result += chr(base + shifted)
        else:
            result += char
    return result
print(encrypt("abc", 2))          # Output: 'cde'
print(decrypt("cde", 2))          # Output: 'abc'
print(encrypt("xyz", 2))          # Output: 'zab'
print(encrypt("Hello, world!", 5))

# Output: 'Mjqqt, btwqi!'
print(decrypt("Mjqqt, btwqi!", 5))  # Output: 'Hello, world!'

