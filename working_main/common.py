import hashlib
import random

# Shared directions
directions = [(-3, -3), (-3, 0), (-3, 3),
              (0, -3),         (0, 3),
              (3, -3),  (3, 0), (3, 3)]
def message_to_binary(message):
    return ''.join(format(ord(char), '08b') for char in message) + '11111111'

def binary_to_message(mess_convert):
    message = ""
    flag = False
    for i in range(0, len(mess_convert), 8):
        byte = mess_convert[i:i+8]
        if byte == '11111111':
            flag = True
            break
        message += chr(int(byte, 2))
    return message, flag

def get_neighbors(x, y, width, height):
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            neighbors.append((nx, ny))
    return neighbors

def get_seeded_neighbors(x, y, width, height):
    from config import password
    neighbors = get_neighbors(x, y, width, height)
    seed_input = f"{x}-{y}-{password}"
    seed = int(hashlib.sha256(seed_input.encode()).hexdigest(), 16) % (2**32)
    rng = random.Random(seed)
    rng.shuffle(neighbors)
    return neighbors

def encode_number(num):
    if num >= 2000:
        raise ValueError("Number must be less than 2000")
    
    # Get 12-bit binary of the number
    bin_num = format(num, '012b')  # Always 12 bits
    
    # Split into two 6-bit parts
    first_6 = bin_num[:6]
    second_6 = bin_num[6:]
    
    # Add '00' padding before each 6 bits
    encoded = '00' + first_6 + '00' + second_6
    
    return encoded  # returns string of 16 bits
def decode_number(encoded):
    if len(encoded) != 16:
        raise ValueError("Encoded input must be 16 bits")
    
    # Extract the two 6-bit parts (after skipping '00')
    first_6 = encoded[2:8]
    second_6 = encoded[10:16]
    
    # Concatenate the two parts
    full_bin = first_6 + second_6
    
    # Convert binary string back to integer
    num = int(full_bin, 2)
    
    return num


def generate_starting_points(width , height ,seedValue,margin=100):
    random.seed(seedValue)
    all_points = [(x, y) for x in range(margin+10, width - (margin+10),67) for y in range(margin +100, height - (margin+10),67)]
    random.shuffle(all_points)
    return all_points