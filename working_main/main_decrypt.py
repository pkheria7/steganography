from common import get_seeded_neighbors

def tobinary(num):
    if num==0 : return "00"
    elif num==1 : return "01"
    elif num==2: return "10"
    return "11"

def get_info(x,y,pixels):
    r, g, b ,a = pixels[x,y]
    message = ""
    message += tobinary(r&3)
    message += tobinary(g&3)
    message += tobinary(b&3)
    message += tobinary(a&3)
    return message

def dfs_decryption(x, y, isStart,pixels, visited, path, message_extraction):
    from config import width,height,depth_limit
    if ((x, y) in visited and isStart) or len(path) >= depth_limit:
        return message_extraction
    visited.add((x, y))
    path.append((x, y))
    message_extraction += get_info(x,y,pixels)
    for nx, ny in get_seeded_neighbors(x, y, width, height):
        if (nx, ny) not in visited:
            message_extraction = dfs_decryption(nx, ny, True,pixels, visited, path, message_extraction)
    path.pop()
    return message_extraction