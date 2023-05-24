import random
words = [
    "banan",
    "rower",
    "Emilia",
    "Matylda",
    "mama",
    "tata",
    "kajak",
    "bajka",
    "zdrowie",
    "miłość",
    "dobro",
    "sukienka",
    "łóżko",
    "pies",
    "kotek",
    "uwaga",
    "magia",
    "czary",
    "zabawa",
    "wieloryb",
    "lody"
]

W = 100
H = 100

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
                    coords.append((x - off, y, False))
        return coords

def check_collision(word, coords):
    # check board bounding box (FIXME)
    if coords[2]:
        if coords[1] + len(word) > H:
            return True
    else:
        if coords[0] + len(word) > W:
            return True 

    # check letter collisions
    x = coords[0]
    y = coords[1]
    dir = coords[2]
    if dir:
        for i in range(0, len(word)):
            if board[x][y+i] != "_" and board[x][y+i] != word[i]:
                return True
    else:
        for i in range(0, len(word)):
            if board[x+i][y] != "_" and board[x+i][y] != word[i]:
                return True
    
    return False

def place_word(word, coords):
    x = coords[0]
    y = coords[1]
    dir = coords[2]
    if dir:
        for i in range(0, len(word)):
            board[x][y+i] = word[i]
    else:
        for i in range(0, len(word)):
            board[x+i][y] = word[i]

def check_word(word):
    for off in range(len(word)):
        coords = get_coords(word, off)
        if len(coords) == 0:
            # no common letters, skip by default (TODO: place where no collisions)
            continue
        for coord in coords:
            collided = check_collision(word, coord)
            if not collided:
                place_word(word, coord)
                return

def print_board():
    for y in range(len(board)):
        for x in range(len(board[0])):
            print(str(board[y][x]) + " ", end='')
        print("")
    print("")

def adjust_board():
    global board
    board_trimmed = []
    maxY, minY, maxX, minX = 0, H, 0, W
    for y in range(H):
        for x in range(W): 
            if board[y][x] != '_':
                if maxY < y:
                    maxY = y
                if minY > y:
                    minY = y
                if maxX < x:
                    maxX = x
                if minX > x:
                    minX = x

    i = 0
    for y in range(minY, maxY + 1):
        board_trimmed.append([])
        for x in range(minX, maxX + 1):
            if (board[y][x] == '_'):
                board_trimmed[i].append(random.choice('AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ'))
            else:
                board_trimmed[i].append(board[y][x].upper())
        i += 1

    board.clear()
    board = board_trimmed.copy() 

for word in words:
    check_word(word)
adjust_board()
print(f"Odnajdź w gąszczu literek następujące wyrazy: {words}")
print_board()