# ============================================================
# Knapsack Problem
# Rekursif + Backtracking
# ============================================================

def knapsack_recursive(
    items,
    target,
    index,
    current_combination,
    current_sum,
    solutions
):

    # Jika tepat target
    if current_sum == target:
        solutions.append(current_combination.copy())
        return

    # Jika melebihi target atau item habis
    if current_sum > target or index >= len(items):
        return

    # =====================================================
    # PILIH ITEM
    # =====================================================

    current_combination.append(items[index])

    knapsack_recursive(
        items,
        target,
        index + 1,
        current_combination,
        current_sum + items[index],
        solutions
    )

    # Backtracking
    current_combination.pop()

    # =====================================================
    # TIDAK PILIH ITEM
    # =====================================================

    knapsack_recursive(
        items,
        target,
        index + 1,
        current_combination,
        current_sum,
        solutions
    )


def main():

    items = [2, 5, 6, 9, 12, 14, 20]

    try:
        target = int(input("Masukkan target berat: "))

        if target <= 0:
            print("Target harus lebih besar dari 0")
            return

        solutions = []

        knapsack_recursive(
            items,
            target,
            0,
            [],
            0,
            solutions
        )

        print("\nDaftar Barang:", items)
        print("Target:", target)

        if len(solutions) > 0:

            print("\nSolusi ditemukan:\n")

            for i, solution in enumerate(solutions, start=1):
                print(
                    f"Solusi {i}: "
                    f"{solution} "
                    f"=> Total = {sum(solution)}"
                )

        else:
            print("Tidak ada kombinasi yang cocok.")

    except ValueError:
        print("Input harus berupa angka.")


if __name__ == "__main__":
    main()
