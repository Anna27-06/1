print("Игра в крестики-нолики")
matrix = [[i, "-", "-", "-"] for i in range(3)]
def game(board, rows=3, cols=4):
    for i in range(rows):
        for j in range(cols):
            print(board[i][j], end=" ")
        print()
print()
print(" ", 1, 2, 3)
game(matrix)
print()
print("Первый ход за 'крестики'")
first_move = "x"

def winner(board):
    for rows in board:
        if rows[1] == rows[2] == rows[3] and rows[1] != "-":
            return rows[1]
    for cols in range(1,4):
        if board[0][cols] == board[1][cols] == board[2][cols] and board[0][cols] != "-":
            return board[0][cols]
    if board[0][1] == board[1][2] == board[2][3] and board[0][1] != "-":
        return board[0][1]
    if board[0][3] == board[1][2] == board[2][1] and board[0][3] != "-":
        return board[0][3]
    return None


def start_game(gamer):
    global matrix
    count = 0
    while True:
        if gamer == "x":
            b = int(input(f"Введите координату по горизонтали от 1 до 3х: "))
            a = int(input(f"Введите координату по вертикали от 0 до 2х: "))
            if (a<0 or a>2) or (b<1 or b>3):
                print('Введите другие значения!')
            else:
                if matrix[a][b] == "-":
                    matrix[a][b] = "x"
                    print(" ", 1, 2, 3)
                    game(matrix)
                    gamer = "o"
                else:
                    print('Позиция занята, выберите другие координаты!')
        elif gamer == "o":
            b = int(input(f"Введите координату по горизонтали от 1 до 3х: "))
            a = int(input(f"Введите координату по вертикали от 0 до 2х: "))
            if (a<0 or a>2) or (b<1 or b>3):
                print('Введите другие значения!')
            else:
                if matrix[a][b] == "-":
                    matrix[a][b] = "o"
                    print(" ", 1, 2, 3)
                    game(matrix)
                    gamer = "x"
                else:
                    print('Позиция занята, выберите другие координаты!')
        winner(matrix)
        if winner(matrix) == "x":
            print("Победа за 'крестиками'")
            break
        elif winner(matrix) == "o":
            print("Победа за 'ноликами'")
            break


start_game(first_move)





