from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:

    # Implement your code here.
    a = len(input_board)
    b = len(input_board[0])

    if x >= a or y >= b:
        return []

    output_board = input_board[:]

    def flood(x: int, y: int):
        if output_board[x][y] == old:
            output_board[x] = output_board[x][:y] + new + output_board[x][y + 1:]

            if x < a - 1: 
                flood(x + 1, y)

            if y < b - 1:
                flood(x, y + 1)

            if x > 0:
                flood(x - 1, y)

            if y > 0:
                flood(x, y - 1)

        else:
            return

    flood(x, y)

    return output_board


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)



# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....