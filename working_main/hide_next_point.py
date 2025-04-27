from PIL import Image ,ImageDraw
from common import message_to_binary, binary_to_message , encode_number , decode_number , generate_starting_points
from encrypt import dfs_encryption
from decrypt import dfs_decryption
from config import get_depth_limit, get_height, get_width, get_password
import random

def encrptying(start_points):
    # print(width, height)
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
        current = data_index
        data_index = dfs_encryption(start_x, start_y,False,enc_msg, pixels, visited, path, data_index)
        # print(data_index-c)
        if data_index >= len(enc_msg):
            break
        i+=1

    img.save("graph_based_hashing.png")
    
    # print("Encryption done." , end="\n\n")

def decrypting(start_points):
    img = Image.open("graph_based_hashing.png").convert("RGBA")
    pixels = img.load()
    visited = set()
    for i in start_points:
        visited.add(i)
    path = []
    final_message=""
    i=0
    start_x, start_y = start_points[0]
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
    return "The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark.The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs.The stars blinked above, silent witnesses to dreams whispered in the dark."

if __name__ == "__main__":
    img = Image.open("/Users/piyushkheria/Desktop/steganography/test.png").convert("RGBA")
    width, height = img.size
    get_width(width)
    get_height(height)
    check_point = get_password("be")
    get_depth_limit(15)
    start_points = generate_starting_points(width,height,87,50)
    encrptying(start_points)
    answer = decrypting(start_points)
    print(answer == get_message())

