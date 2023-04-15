def beaufort_cipher(plaintext, key):
    """Encrypts or decrypts plaintext using the Beaufort Cipher with the given key."""
    ciphertext = ""
    for i in range(len(plaintext)):
        # Convert the characters to uppercase and subtract 'A' to get a value between 0 and 25
        char_value = (ord(plaintext[i].upper()) - ord('A')) % 26
        key_value = (ord(key[i % len(key)].upper())-ord('A')) % 26
        # Apply the Beaufort Cipher algorithm to obtain the encrypted or decrypted character
        encrypted_char = chr(((key_value - char_value) % 26) + ord('A'))
        ciphertext += encrypted_char

    return ciphertext

