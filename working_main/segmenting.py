from PIL import Image ,ImageDraw
from common import message_to_binary, binary_to_message
from encrypt import dfs_encryption
from decrypt import dfs_decryption
from config import get_depth_limit, get_height, get_width, get_password
import random

def get_message():
    return "The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs."

def divide_message(message, packet_length):
    return [message[i:i + packet_length] for i in range(0, len(message), packet_length)]

def generate_starting_points():
    random.seed(17892703)
    all_points = [(x, y) for x in range(100, 900) for y in range(120, 1400)]
    random.shuffle(all_points)
    return all_points

if __name__ == "__main__":
    img = Image.open("/Users/piyushkheria/Desktop/steganography/test.png").convert("RGBA")
    width, height = img.size
    print(width, height)
    get_width(width)
    get_height(height)
    pixels = img.load()

    message = get_message()
    packet_length = 100  # Divide into packets
    packets = divide_message(message, packet_length)
    check_point = get_password("hello")
    depth = packet_length
    get_depth_limit(depth)

    start_points = generate_starting_points()

    visited = set()
    path = []
    additonal = 0
    for i in range (len(packets)):
        data_index = 0
        enc_msg = message_to_binary(packets[i])
        start_x, start_y = start_points[i+additonal]
        while (start_x,start_y) in visited:
            additonal += 1
            start_x, start_y = start_points[i+additonal]
        data_index = dfs_encryption(start_x, start_y, enc_msg, pixels, visited, path, data_index)
        # print(data_index)
        data_index = 0

    img.save("graph_based_hashing.png")
    
    print("Encryption done." , end="\n\n")

    # Decryption
    img = Image.open("graph_based_hashing.png").convert("RGBA")
    width, height = img.size
    pixels = img.load()
    visited = set()
    path = []
    final_message=""
    additonal=0
    for i in range(len(packets)):
        start_x, start_y = start_points[i+additonal]
        while (start_x,start_y) in visited:
            additonal += 1
            start_x, start_y = start_points[i+additonal]
        message_extraction = ""
        message_extraction = dfs_decryption(start_x, start_y, pixels, visited, path, message_extraction,8*(packet_length+1))
        final_message += binary_to_message(message_extraction)
    print(message == final_message)
    print(len(message))
    # print(final_message)

    canvas = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(canvas)

    for (vx, vy) in visited:
        draw.point((vx, vy), fill="blue")
    # Save or show the resulting image
    canvas.save("visited_paths.png")
