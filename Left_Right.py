from PIL import Image

# Function to hide a message in an image
def hide_message(image_path, message, directions):
    img = Image.open(image_path)
    img = img.convert("RGBA")
    
    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'  # End of message delimiter
    
    print(binary_message)
    # Hide the message in the least significant bits of the image
    data_index = 0
    pixels = img.load()
    x=0
    y=0

    for char in directions:
        r, g, b,a = pixels[x, y]
        # Modify the least significant bit of the red channel
        r = (r & ~1) | int(binary_message[data_index])
        g = (g & ~1) | int(ord(char)&1)
        pixels[x, y] = (r, g, b,a)
        if g&1 == 0:
            x+=1
        else :
            y+=1
        data_index+=1
    
    img.save("output_test.png")

# Function to retrieve a hidden message from an image
def retrieve_message(image_path, direction):
    img = Image.open(image_path)
    binary_message = ""
    pixels = img.load()
    x=0
    y=0

    for i in direction:
        r, g, b ,a= pixels[x, y]
        binary_message += str(r & 1)
        if ord(i)&1 == 0:
            x+=1
        else :
            y+=1

        
    print(binary_message)
    # Convert binary message to characters
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))
    
    return message

# Example usage
if __name__ == "__main__":
    message = "M"
    direction = "01100110"
    hide_message("test.png", message, directions=direction)  # Replace with your image path
    retrieved_message = retrieve_message("output_test.png", direction)
    print("Retrieved Message:", retrieved_message)