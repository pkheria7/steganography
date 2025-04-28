# Steganography Project

## Overview
Welcome to my Steganography Project! Here, I explore hiding information inside images — from basic pixel manipulation to advanced graph-based techniques. It's been an incredible learning journey, and I’m excited to share it with you!

## Development Journey
- **`baseModel.py`**: My starting point, experimenting with linear pixel storage and directional data tweaks.
- **`just_graph.py`**: Introduction to using graph structures for navigating pixel data — a thrilling way to encode text!
- **`variableLength.py`**: Inspired by Torrent-style encryption, enabling dynamic, randomized embedding for even stronger hiding.

## Key Features
- Store up to **50,000 characters** (~8,000 words) in a **1024x1024** image — **one pixel per character**.
- Invisible encryption: `image.png` vs `output.png` show no visible difference.
- Secure decryption using a generated password.
- `visited_paths.png` visualizes pixel usage for large messages.
- **Note**: Only supports single-paragraph messages (no line breaks).

## Final Code
Find the complete, working version inside the `working_main` folder. Feel free to tweak, improve, and innovate!

## Collaboration
I'd love for you to **clone**, **build a GUI**, and **add me as a collaborator** — let's make it even better together!

## Getting Started
Install the required libraries and run:

```bash
python UI_UX.py