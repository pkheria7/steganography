import hashlib
import random
from PIL import Image, ImageDraw

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
    return neighbors
# DFS traversal using password-based neighbor ordering
def dfs(x, y, depth_limit=10):
    if (x, y) in visited or len(path) >= depth_limit:
        return
    visited.add((x, y))
    path.append((x, y))

    draw.point((y, x), fill=(255, 0, 0))
    print(f"Visited Pixel {len(path)}: ({x}, {y})")
    for nx, ny in get_seeded_neighbors(x, y):
        if (nx, ny) not in visited:
            dfs(nx, ny, depth_limit)
    path.pop()
            




if __name__ == "__main__" :
    img = Image.open("test.png")
    (height , width) = img.size
    pixel = img.load()

    # Parameters
    password = "super_secret_key"
    visited = set()
    path = []

    # 8-connected movement (up/down/left/right + diagonals)
    directions = [(-7, -7), (-7, 0), (-7, 7),
              (0, -7),          (0, 7),
              (7, -7),  (7, 0), (7, 7)]
    
    # Starting point
    draw = ImageDraw.Draw(img)

    start_x, start_y = 10, 10  # example; you can set based on metadata
    dfs(start_x, start_y)
    draw.point((10, 10), fill=(255, 0, 230))
    img.show()
