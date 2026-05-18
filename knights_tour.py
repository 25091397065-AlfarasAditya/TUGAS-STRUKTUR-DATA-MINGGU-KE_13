# ============================================================
# Knight's Tour
# Rekursif + Backtracking
# ============================================================

N = 8

# Gerakan legal kuda
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]


def print_board(board):

    print("\nSolusi Knight's Tour:\n")

    for row in board:
        for value in row:
            print(f"{value:2}", end=" ")
        print()


def is_safe(x, y, board):

    return (
        0 <= x < N and
        0 <= y < N and
        board[x][y] == -1
    )


def solve_knight_tour(board, x, y, move_count):

    # Semua kotak sudah dikunjungi
    if move_count == N * N:
        return True

    # Coba semua kemungkinan gerakan
    for k in range(8):

        next_x = x + move_x[k]
        next_y = y + move_y[k]

        if is_safe(next_x, next_y, board):

            board[next_x][next_y] = move_count

            if solve_knight_tour(
                board,
                next_x,
                next_y,
                move_count + 1
            ):
                return True

            # Backtracking
            board[next_x][next_y] = -1

    return False


def main():

    try:
        start_x = int(input("Masukkan posisi awal X (0-7): "))
        start_y = int(input("Masukkan posisi awal Y (0-7): "))

        if not (0 <= start_x < N and 0 <= start_y < N):
            print("Posisi harus antara 0 sampai 7")
            return

        board = [[-1 for _ in range(N)] for _ in range(N)]

        # Posisi awal
        board[start_x][start_y] = 0

        if solve_knight_tour(board, start_x, start_y, 1):
            print_board(board)
        else:
            print("Tidak ada solusi.")

    except ValueError:
        print("Input harus berupa angka.")


if __name__ == "__main__":
    main()
