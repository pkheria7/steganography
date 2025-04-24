from PIL import Image

# Function to hide a message in an image
def hide_message(image_path, message, directions):
    img = Image.open(image_path)
    img = img.convert("RGBA")
    
    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'  # End of message delimiter
    
    # Hide the message in the least significant bits of the image
    data_index = 0
    pixels = img.load()
    for y in range(img.height):
        for x in range(img.width):
            if data_index < len(binary_message):
                r, g, b,a = pixels[x, y]
                # Modify the least significant bit of the red channel
                r = (r & ~1) | int(binary_message[data_index])
                pixels[x, y] = (r, g, b,a)
                print(f"Changing pixel at ({x}, {y}) to: ({r}, {g}, {b}, {a})")  # Print changed pixel info
                data_index += 1
            else:
                break
    
    img.save("output_test.png")

# Function to retrieve a hidden message from an image
def retrieve_message(image_path):
    img = Image.open(image_path)
    binary_message = ""
    
    pixels = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b ,a= pixels[x, y]
            binary_message += str(r & 1)  # Get the least significant bit of the red channel
    
    # Convert binary message to characters
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '11111111':  # Check for end of message delimiter
            break
        message += chr(int(byte, 2))
    
    return message

# Example usage
if __name__ == "__main__":
    message = "My"
    direction = "01100110"
    binary_message = ''.join(str(ord(char) & 1)for char in direction)
    print(binary_message)
    hide_message("test.png", message, directions=direction)  # Replace with your image path
    retrieved_message = retrieve_message("output_test.png")
    print("Retrieved Message:", retrieved_message)
#hello 