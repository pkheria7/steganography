from PIL import Image
from common import message_to_binary, binary_to_message, get_password
from encrypt import dfs_encryption
from decrypt import dfs_decryption
from config import get_depth_limit,get_height,get_width


if __name__ == "__main__":
    img = Image.open("/Users/piyushkheria/Desktop/steganography/test.png").convert("RGB")
    width, height = img.size
    get_width(width)
    get_height(height)
    pixels = img.load()
    message = "The stars blinked above, silent witnesses to dreams whispered in the dark. She wandered far, chasing echoes of hope and fragments of forgotten songs. Each step carried a memory, a story untold, wrapped in moonlight and stitched with longing."
    check_point = get_password("hello")
    enc_msg = message_to_binary(message)
    depth = len(message) * 4
    get_depth_limit(depth)
    visited = set()
    path = []
    data_index = 0
    start_x, start_y = 10, 10

    data_index = dfs_encryption(start_x, start_y, enc_msg, pixels,visited, path, data_index)
    img.save("graph_based_testing.png")
    print("Encryption done.")

    # Decryption
    img = Image.open("graph_based_testing.png").convert("RGB")
    width, height = img.size
    pixels = img.load()
    visited = set()
    path = []
    message_extraction = ""
    message_extraction = dfs_decryption(start_x, start_y, pixels, visited, path, message_extraction)
    final_message = binary_to_message(message_extraction)
    print("Decrypted message:", final_message)