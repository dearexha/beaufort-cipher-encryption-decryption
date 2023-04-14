def beaufort_cipher(plaintext, key):
    """Encrypts or decrypts plaintext using the Beaufort Cipher with the given key."""
    ciphertext = ""
    for i in range(len(plaintext)):
        # Convert the characters to uppercase and subtract 'A' to get a value between 0 and 25
        char_value = (ord(plaintext[i].upper()) - ord('A')) % 26
