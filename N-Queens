# ============================================================
# N-Queens Problem
# Rekursif + Backtracking
# ============================================================

def print_board(board):
    n = len(board)

    print("\nSolusi ditemukan:\n")

    for row in board:
        for cell in row:
            if cell == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def is_safe(board, row, col, n):

    # Cek sisi kiri
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Cek diagonal kiri atas
    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Cek diagonal kiri bawah
    i = row
    j = col

    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, n):

    # Semua ratu berhasil ditempatkan
    if col >= n:
        return True

    for row in range(n):

        if is_safe(board, row, col, n):

            # Tempatkan ratu
            board[row][col] = 1

            # Rekursi ke kolom berikutnya
            if solve_n_queens(board, col + 1, n):
                return True

            # Backtracking
            board[row][col] = 0

    return False


def main():

    try:
        n = int(input("Masukkan ukuran papan N: "))

        if n <= 0:
            print("N harus lebih besar dari 0")
            return

        board = [[0 for _ in range(n)] for _ in range(n)]

        if solve_n_queens(board, 0, n):
            print_board(board)
        else:
            print("Tidak ada solusi.")

    except ValueError:
        print("Input harus berupa angka.")


if __name__ == "__main__":
    main()
