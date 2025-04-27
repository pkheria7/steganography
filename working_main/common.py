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
    for i in range(0, len(mess_convert), 8):
        byte = mess_convert[i:i+8]
        if byte == '11111111':
            break
        message += chr(int(byte, 2))
    return message

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