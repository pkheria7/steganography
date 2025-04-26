from common import mini_directions, get_seeded_neighbors

def dfs_decryption(x, y, pixels, visited, path, message_extraction):
    from config import width,height,depth_limit
    if (x, y) in visited or len(path) >= depth_limit:
        return message_extraction
    visited.add((x, y))
    path.append((x, y))

    for (text_x, text_y) in mini_directions:
        r, g, b = pixels[x + text_x, y + text_y]
        message_extraction += str(r & 1)
    for nx, ny in get_seeded_neighbors(x, y, width, height):
        if (nx, ny) not in visited:
            message_extraction = dfs_decryption(nx, ny, pixels, visited, path, message_extraction)
    path.pop()
    return message_extraction