import hashlib
import random
from PIL import Image, ImageDraw
# Load image
img = Image.open("test.png")
(height , width) = img.size
pixel = img.load()

# Create a draw object
draw = ImageDraw.Draw(img)

# Parameters
password = "super_secret_key"
visited = set()
path = []

# 8-connected movement (up/down/left/right + diagonals)
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

def get_neighbors(x, y):
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < height and 0 <= ny < width:
            neighbors.append((nx, ny))
    return neighbors

# Shuffle neighbors deterministically based on password and pixel position
def get_seeded_neighbors(x, y):
    neighbors = get_neighbors(x, y)
    seed_input = f"{x}-{y}-{password}"
    seed = int(hashlib.sha256(seed_input.encode()).hexdigest(), 16)
    rng = random.Random(seed)
    rng.shuffle(neighbors)
    print("neighbours are : ", neighbors)
    return neighbors
count = 0
# DFS traversal using password-based neighbor ordering
def dfs(x, y, depth_limit=10):
    if (x, y) in visited or len(path) >= depth_limit:
        return
    visited.add((x, y))
    path.append((x, y))

    for nx, ny in get_seeded_neighbors(x, y):
        global count

        if (nx, ny) not in visited:
            dfs(nx, ny, depth_limit)
        print(f"I have completed from {x,y} : {nx , ny} , {count}")
        count +=1

# Starting point
start_x, start_y = 10, 10  # example; you can set based on metadata
dfs(start_x, start_y)

# View the path
# print("Traversal Path:")
# for i, (x, y) in enumerate(path):
#     print(f"{i+1:03}: ({x}, {y}) -> Pixel: {pixel[x, y]}")

# After the DFS traversal
# Draw the path on the image
for i, (x, y) in enumerate(path):
    draw.point((y, x), fill=(255, 0, 0))  # Draw a red point for each pixel in the path

# Save or show the modified image
img.show()  # To display the image
# img.save("output_path.png")  # To save the image with the path drawn