from common import mini_directions, get_seeded_neighbors

def dfs_encryption(x, y, enc_msg, pixels, visited, path, data_index):
    from config import width,height,depth_limit
    if (x, y) in visited or len(path) >= depth_limit:
        return data_index
    visited.add((x, y))
    path.append((x, y))
    for (text_x, text_y) in mini_directions:
        if data_index < len(enc_msg):
            r, g, b = pixels[x + text_x, y + text_y]
            r = (r & ~1) | int(enc_msg[data_index])
            pixels[x + text_x, y + text_y] = (r, g, b)
            data_index += 1
    for nx, ny in get_seeded_neighbors(x, y, width, height):
        if (nx, ny) not in visited:
            data_index = dfs_encryption(nx, ny, enc_msg, pixels, visited, path, data_index)
    path.pop()
    return data_index