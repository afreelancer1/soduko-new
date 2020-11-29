board = [[0, 9, 0, 0, 7, 5, 0, 0, 6],
         [0, 0, 0, 0, 0, 2, 0, 7, 4],
         [0, 7, 0, 3, 0, 0, 5, 8, 0],
         [0, 0, 9, 5, 3, 0, 4, 6, 0],
         [6, 0, 0, 2, 0, 4, 0, 0, 5],
         [0, 5, 2, 0, 9, 6, 8, 0, 0],
         [0, 4, 1, 0, 0, 7, 0, 3, 0],
         [3, 6, 0, 1, 0, 0, 0, 0, 0],
         [9, 0, 0, 4, 8, 0, 0, 5, 0]]

all_no = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_empty(b):
    e = []
    for i in range(81):
        r = i // 9
        c = i % 9
        if b[r][c] == 0:
            e.append(str(r) + str(c))
    return e


empty = get_empty(board)
nlist = [[] for i in range(len(empty) + 1)]


def valid(b, r, c, n, move):
    if move + str(n) in nlist:
        return False
    if n in b[r]:
        return False
    bb = list(map(list, zip(*b)))[c]
    if n in bb:
        return False
    return True


i = 0
move = ""

while i < len(empty):
    r, c = int(empty[i][0]), int(empty[i][1])
    for n in all_no:
        if valid(board, r, c, n, move):
            board[r][c] = n
            move = move + str(n)
            i += 1
            break
        elif n == 9:
            i -= 1
            board[int(empty[i][0])][int(empty[i][1])] = 0
            nlist.append(move)
            move = move[0:-1]
            break

[print(x, sum(x)) for x in board]
print(".....................")

tboard = list(map(list, zip(*board)))

[print(x, sum(x)) for x in tboard]
