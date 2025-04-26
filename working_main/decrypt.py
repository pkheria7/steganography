from common import mini_directions, get_seeded_neighbors

def tobinary(num):
    if num==0 : return "00"
    elif num==1 : return "01"
    elif num==2: return "10"
    return "11"

def dfs_decryption(x, y, pixels, visited, path, message_extraction,length):
    from config import width,height,depth_limit
    if (x, y) in visited or len(path) >= depth_limit or len(message_extraction)>=length:
        return message_extraction
    visited.add((x, y))
    path.append((x, y))

    for (text_x, text_y) in mini_directions:
        r, g, b = pixels[x + text_x, y + text_y]
        message_extraction += tobinary(r&3)
    for nx, ny in get_seeded_neighbors(x, y, width, height):
        if (nx, ny) not in visited:
            message_extraction = dfs_decryption(nx, ny, pixels, visited, path, message_extraction,length)
    path.pop()
    return message_extraction