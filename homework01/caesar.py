import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext_high = plaintext.upper()
    for letter in plaintext_high:
        position = alphabet.find(letter)
        new_position = position + shift
        if letter in alphabet:
            ciphertext = ciphertext + alphabet[new_position]
        else:
            ciphertext = ciphertext + letter
    return ciphertext
print(encrypt_caesar(input("Слово для шифровки "), int(input("Введите ключ "))))

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext_high = ciphertext.upper()
    for letter in ciphertext_high:
        position = alphabet.find(letter)
        new_position = position - shift
        if letter in alphabet:
            plaintext = plaintext + alphabet[new_position]
        else:
            plaintext = plaintext + letter
    return plaintext
print(decrypt_caesar(input("Слово для шифровки "), int(input("Введите ключ "))))


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
