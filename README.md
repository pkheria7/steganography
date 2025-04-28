# Steganography Project

## Overview
Welcome to my Steganography Project! This journey has been an exciting exploration of hiding information within images, utilizing various techniques from basic pixel manipulation to more complex graph-based methods. Each step has been a learning experience, and I invite you to join me on this adventure!

## Development Journey

### @baseModel.py
I started with `baseModel.py`, where I learned the fundamentals of pixel manipulation and how to store information in a linear manner. It was a fascinating beginning, but I quickly realized that there was so much more to explore! I experimented with different combinations and directional data, and I encourage you to do the same. Think creatively and see what you can come up with!

### @just_graph.py
Next, I delved into `just_graph.py`, which showcases how graphs work in Python. This module opened my eyes to the power of graph structures in navigating and manipulating pixel data. Imagine putting texts into a graph with fixed lengths—it's a thrilling concept that I hope you'll explore further!

### @variableLength.py
Then came `variableLength.py`, where I learned to store information in a non-linear, variable-length way. This approach is reminiscent of pure Torrent-style encryption, allowing for a more dynamic and randomized method of embedding data into images. The possibilities are endless, and I can't wait to see how you might innovate in this area!

## Key Features
- The maximum message that can be stored in a regular 1024x1024 image is approximately 50,000 characters, which is about 8,000 words. Each pixel can contain one character.
- The `image.png` is the original image used for embedding the message.
- The `output.png` is the resulting image after encryption. As you can see, there is no visible difference, yet a significant amount of information is stored within the image.
- This hidden information can only be unraveled using the password generated at the end of the encryption process.
- The `visited_paths.png` is a canvas that shows the locations of the pixels used when I attempted to embed 50,000 characters.
- **Drawback**: The message must be a single paragraph; changing paragraphs is not supported.

## Final Code Logic
The `working_main` folder contains the final code logic and the working model of my project. Feel free to dive in, tweak the code, and make it your own! This is where the magic happens, and I hope you find it as exhilarating as I did.

## Collaboration
I would love for you to clone this repository and create a GUI for the entire project. Let's make it user-friendly and accessible to everyone! And of course, don't forget to add me as a collaborator—*wink emoji*.

## Conclusion
This project represents not just a technical achievement but a significant learning experience in the field of steganography. From basic image manipulation to advanced graph-based methods, each module contributes to a deeper understanding of how information can be concealed within digital images. I look forward to seeing how you can enhance this project and explore new techniques in the future!

## Getting Started
To run the application, ensure you have the necessary libraries installed and execute the following command:

```bash
python UI_UX.py
```

## Acknowledgments
A heartfelt thank you to everyone who has supported me on this journey. Your encouragement and insights have been invaluable. Let's continue to learn and grow together!