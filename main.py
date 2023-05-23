import numpy

words = [
    "dupa",
    "gorandrzej",
    "kierwo",
    "patol",
    "megatron",
    "morwa",
    "estikopat",
    "widmo",
    "meta",
    "malakser"
]

W = 20
H = 20

board = []
init = False

for y in range(H):
    board.append([])
    for x in range(W):
        board[y].append("_")

def get_coords(word, off):
    global init
    if not init:
        size = len(word)
        x = int((W - size) / 2)
        y = int(H / 2)
        init = True
        return [(x, y, False)]
    else:
        coords = []
        for y in range(H):
            for x in range(W):
                if board[x][y] == word[off]:
                    coords.append((x, y - off, True))
                    coords.append((x, y, False))
        return coords

def check_collision(word, coords, off):
    # check board bounding box (FIXME)
    if coords[2]:
        if coords[0] - off + len(word) > W:
            return True
    else:
        if coords[1] - off + len(word) > H:
            return True 
    # TODO: check letter collisions
    return False

def place_word(word, x, y, dir):
    if dir:
        for i in range(0, len(word)):
            board[x][y+i] = word[i]
    else:
        for i in range(0, len(word)):
            board[x+i][y] = word[i]

def check_word(word):
    print(word)
    for off in range(len(word)):
        coords = get_coords(word, off)
        if len(coords) == 0:
            # no common letters, skip by default (TODO: place where no collisions)
            continue
        for coord in coords:
            collided = check_collision(word, coord, off)
            if not collided:
                print(coord)
                place_word(word, coord[0], coord[1], coord[2])
                return

def print_board():
    for y in range(H):
        for x in range(W):
            print(str(board[x][y]) + " ", end='')
        print("")

for word in words:
    check_word(word)
    print_board()