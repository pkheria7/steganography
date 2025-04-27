from PIL import Image ,ImageDraw
from common import message_to_binary, binary_to_message , encode_number , decode_number , generate_starting_points
from encrypt import dfs_encryption
from decrypt import dfs_decryption
from config import get_depth_limit, get_height, get_width, get_password
import random

def binary_to_hex(binary_string):
    """Convert a 256-bit binary string to a 64-digit hexadecimal string."""
    return hex(int(binary_string, 2))[2:].zfill(64)

def hex_to_binary(hex_string):
    """Convert a 64-digit hexadecimal string to a 256-bit binary string."""
    return bin(int(hex_string, 16))[2:].zfill(256)

def encrptying(start_points):
    pixels = img.load()

    message = get_message()
    visited = set()
    for coordinate in start_points:
        visited.add(coordinate)
    path = []
    enc_msg = message_to_binary(message)
    i =0
    data_index = 0
    while True:
        start_x, start_y = start_points[i]
        next_start_x, next_start_y = start_points[i+1]
        next_point_binary = encode_number(next_start_x) + encode_number(next_start_y)
        enc_msg = enc_msg[:data_index]+next_point_binary+enc_msg[data_index:]
        data_index = dfs_encryption(start_x, start_y,False,enc_msg, pixels, visited, path, data_index)
        if data_index >= len(enc_msg):
            break
        i+=1

    img.save("graph_based_hashing.png")

def get_info(binary_message):
    return_lst = []
    for i in range(0,6):
        return_lst.append(decode_number(binary_message[i*16:(i+1)*16]))
    return_lst.append(binary_to_message(binary_to_message(binary_message[96:])))
    return return_lst




def decrypting(password):
    img = Image.open("graph_based_hashing.png").convert("RGBA")
    info = get_info(hex_to_binary(password))
    (width , height) = img.size
    print(info)
    if ( width != info[0] or height != info[1]):
        return "Not the correct Image"
    prime = info[2]
    start_x, start_y = info[3] , info[4]
    seed = info[5]
    word = info[6].rstrip('@')
    pixels = img.load()
    visited = set()
    for i in start_points:
        visited.add(i)
    path = []
    final_message=""
    i=0
    
    while True:
        message_extraction = ""
        message_extraction = dfs_decryption(start_x, start_y,False, pixels, visited, path, message_extraction)
        next_x = decode_number(message_extraction[0:16])
        next_y = decode_number(message_extraction[16:32])
        donne , check = binary_to_message(message_extraction[32:])
        final_message += donne
        start_x, start_y = next_x , next_y
        if check :
            break
        i+=1
    # print("From decryption :",len(final_message))

    return final_message


def get_message():
    return "The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark."

if __name__ == "__main__":
    img = Image.open("/Users/piyushkheria/Desktop/steganography/test.png").convert("RGBA")
    width, height = img.size
    get_width(width)
    get_height(height)
    word = input("Enter a word (must not be more than 10 letters):\n")
    while len(word) <15:
        word += "@"
    if len(word) >15:
        word = word[:15]
    check_point = get_password(word)
    prime = int(input("choose one 17 , 19 , 21 , 23 :\n"))
    get_depth_limit(prime)
    randomise_it = int(input("toggle value : \n"))
    start_points = generate_starting_points(width,height,randomise_it,50)
    start = start_points[0]

    My_password = encode_number(width) + encode_number(height)+ encode_number(prime)+ encode_number(start[0]) + encode_number(start[1])+ encode_number(randomise_it)+ message_to_binary(word)+"11111111111111111111111111111111"

    print("checking :",My_password == hex_to_binary(binary_to_hex(My_password)))
    print(len(My_password))
    encrptying(start_points)
    random.shuffle(start_points)
    print("Your Password :",binary_to_hex(My_password))

    entry = input("Enter the password :\n")
    answer = decrypting(entry)
    print(answer)
    print(answer == get_message())





# def text_to_binary(text):
#     """Convert text to a binary string (8 bits per character)."""
#     return ''.join(format(ord(c), '08b') for c in text)

# def binary_to_text(binary_str):
#     """Convert a binary string to text (8 bits per character)."""
#     chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
#     return ''.join(chr(int(char, 2)) for char in chars if char)

# def binary_to_hex(binary_str):
#     """Convert a binary string to a hex string, preserving leading zeros."""
#     # Pad binary_str to a multiple of 4 bits
#     if len(binary_str) % 4 != 0:
#         binary_str = binary_str.zfill(len(binary_str) + (4 - len(binary_str) % 4))
#     hex_str = format(int(binary_str, 2), 'x')  # no '0x'
#     return hex_str

# def hex_to_binary(hex_str):
#     """Convert a hex string to a binary string, preserving leading zeros."""
#     hex_str = hex_str.lower().lstrip('0x')
#     if not hex_str:
#         return ''
#     binary_str = bin(int(hex_str, 16))[2:]
#     return binary_str.zfill(len(hex_str) * 4)

# def encrypt(plaintext, password):
#     """Encrypt plaintext using a password (simple XOR). Returns hex string."""
#     # Convert plaintext and password to binary strings
#     pt_bin = text_to_binary(plaintext)
#     pw_bin = text_to_binary(password)
#     # Generate key by repeating password bits to the length of plaintext bits
#     key_bin = (pw_bin * (len(pt_bin) // len(pw_bin) + 1))[:len(pt_bin)]
#     # XOR plaintext bits with key bits
#     cipher_bin = ''.join(str(int(a) ^ int(b)) for a, b in zip(pt_bin, key_bin))
#     # Combine password bits, separator, and encrypted message bits
#     separator = '1' * 32
#     combined_bin = pw_bin + separator + cipher_bin
#     # Convert combined bits to hex for output
#     return binary_to_hex(combined_bin)

# def get_info(binary_str):
#     """
#     Decode the combined binary string into password bits and message bits.
#     Structure: [password_bits][32-bit separator][message_bits].
#     """
#     separator = '1' * 32
#     parts = binary_str.split(separator, 1)
#     if len(parts) != 2:
#         return None, None
#     return parts[0], parts[1]

# def decrypt(hex_data, password):
#     """Decrypt hex_data using the password. Returns the plaintext message or None."""
#     combined_bin = hex_to_binary(hex_data)
#     pw_bits, enc_msg_bits = get_info(combined_bin)
#     if pw_bits is None:
#         print("Error: Data format incorrect or separator not found.")
#         return None
#     # Convert extracted password bits to text for verification
#     extracted_password = binary_to_text(pw_bits)
#     # Verify the provided password matches the embedded one
#     if extracted_password != password:
#         print("Error: Incorrect password!")
#         return None
#     # Regenerate key for the encrypted message bits
#     pw_bin = text_to_binary(password)
#     key_bin = (pw_bin * (len(enc_msg_bits) // len(pw_bin) + 1))[:len(enc_msg_bits)]
#     # XOR to get original plaintext bits
#     pt_bin = ''.join(str(int(a) ^ int(b)) for a, b in zip(enc_msg_bits, key_bin))
#     return binary_to_text(pt_bin)

# # Example usage:
# plaintext = "Hello, World!"
# password = "secret"
# # Check binary<->hex conversion for the password bits
# pw_bits = text_to_binary(password)
# print(pw_bits == hex_to_binary(binary_to_hex(pw_bits)))  # Expected: True
# # Encrypt and then decrypt the message
# encrypted = encrypt(plaintext, password)
# decrypted = decrypt(encrypted, password)
# print(decrypted)  # Expected: "Hello, World!"