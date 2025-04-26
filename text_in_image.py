import hashlib
import random
from PIL import Image, ImageDraw

# max word length can be 250 characters currently

def message_to_binary(message):
    return ''.join(format(ord(char), '08b') for char in message) + '11111111'

def binary_to_message(mess_convert):
    message = ""
    for i in range(0, len(mess_convert), 8):
        byte = mess_convert[i:i+8]
        if byte == '11111111':  # Optional delimiter
            break
        message += chr(int(byte, 2))
    return message

def get_neighbors(x, y):
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            neighbors.append((nx, ny))
    return neighbors

def get_seeded_neighbors(x, y):
    neighbors = get_neighbors(x, y)
    seed_input = f"{x}-{y}-{password}"
    seed = int(hashlib.sha256(seed_input.encode()).hexdigest(), 16) % (2**32)
    rng = random.Random(seed)
    rng.shuffle(neighbors)
    return neighbors

def dfs_encryption(x, y, enc_msg, depth_limit=300):
    global data_index
    if (x, y) in visited or len(path) >= depth_limit:
        return
    visited.add((x, y))
    path.append((x, y))
    for (text_x , text_y) in mini_directions:
        if data_index < len(enc_msg):
            r, g, b = pixels[x+text_x, y+text_y]
            r = (r & ~1) | int(enc_msg[data_index])
            pixels[x+text_x, y+text_y] = (r, g, b)
            data_index += 1
    for nx, ny in get_seeded_neighbors(x, y):
        if (nx, ny) not in visited:
            dfs_encryption(nx, ny, enc_msg, depth_limit)
    path.pop()

def dfs_decryption(x, y, depth_limit=300):
    global message_extraction
    if (x, y) in visited or len(path) >= depth_limit:
        return
    visited.add((x, y))
    path.append((x, y))
    for (text_x , text_y) in mini_directions:
        r, g, b = pixels[x+text_x, y+text_y]
        message_extraction += str(r & 1)
    for nx, ny in get_seeded_neighbors(x, y):
        if (nx, ny) not in visited:
            dfs_decryption(nx, ny, depth_limit)
    path.pop()

if __name__ == "__main__":
    img = Image.open("test.png")
    img = img.convert("RGB")
    (width, height) = img.size
    pixels = img.load()

    # Parameters
    password = "super_secret_key"
    directions = [(-5, -5), (-5, 0), (-5, 5),
                  (0, -5),         (0, 5),
                  (5, -5),  (5, 0), (5, 5)]
    mini_directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    # Encrypt
    visited = set()
    path = []
    data_index = 0
    message = "The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs. Each step carried a memory, a story untold, wrapped in moonlight and stitched with longing."
    depth = len(message)*4
    enc_msg = message_to_binary(message)
    start_x, start_y = 10, 10
    dfs_encryption(start_x, start_y, enc_msg=enc_msg, depth_limit=depth)
    img.save("graph_based_testing.png")
    print("encryption done")

    # Decrypt
    img = Image.open("graph_based_testing.png")
    img = img.convert("RGB")
    (width, height) = img.size
    pixels = img.load()
    visited = set()
    path = []
    message_extraction = ""
    dfs_decryption(start_x, start_y, depth_limit=depth)
    final_message = binary_to_message(message_extraction)
    print("message :", final_message)
