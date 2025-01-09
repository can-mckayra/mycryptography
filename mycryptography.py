letter_frequencies = {
    'e': 12.70,
    't': 9.06,
    'a': 8.17,
    'o': 7.51,
    'i': 6.97,
    'n': 6.75,
    's': 6.33,
    'h': 6.09,
    'r': 5.99,
    'd': 4.25,
    'l': 4.03,
    'u': 2.76,
    'c': 2.78,
    'm': 2.41,
    'w': 2.36,
    'f': 2.23,
    'g': 2.02,
    'y': 1.97,
    'p': 1.93,
    'b': 1.49,
    'v': 0.98,
    'k': 0.77,
    'j': 0.15,
    'x': 0.15,
    'q': 0.10,
    'z': 0.07
}
letter_frequencies_list = list(letter_frequencies.keys())

def caesar_shift(text, shift, encrypt):
    ciphertext = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shift_value = shift if encrypt else -shift
            ciphertext += chr(shift_base + (ord(char) + shift_value - shift_base) % 26)
        else:
            ciphertext += char
    return ciphertext

def caesar_encrypt(plaintext, shift): return caesar_shift(plaintext, shift, True)

def caesar_decrypt(ciphertext, shift): return caesar_shift(ciphertext, shift, False)

def count_char_instances(text):
    char_instances = {}
    for char in text:
        char = char.lower()
        if char.isalpha(): #or char.isspace():
            if char not in char_instances:
                char_instances[char] = 1
            elif char in char_instances:
                char_instances[char] += 1
    return char_instances

def calculate_char_frequencies(text):
    char_instances = count_char_instances(text)
    char_frequencies = {}
    total_sum = sum(char_instances.values())
    for char in char_instances:
        if char not in char_frequencies:
            char_frequencies[char] = round((char_instances[char] / total_sum * 100), 2)
    char_frequencies = dict(sorted(char_frequencies.items(), key=lambda item: item[1], reverse=True))
    return char_frequencies

def create_char_map(char_frequencies):
    char_map = {}
    keys = list(char_frequencies.keys())
    for i, key in enumerate(keys):
        char_map[key] = letter_frequencies_list[i]
    return char_map

def decrypt_ciphertext(ciphertext, char_map):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                char = char.lower()
                plaintext += char_map[char].upper()
            elif not char.isupper():
                plaintext += char_map[char]
        else:
            plaintext += char
    return plaintext

def decrypt_substitution(ciphertext):
    char_instances = count_char_instances(ciphertext)
    char_frequencies = calculate_char_frequencies(char_instances)
    char_map = create_char_map(char_frequencies)
    return decrypt_ciphertext(ciphertext, char_map)
