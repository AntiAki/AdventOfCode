def create_bingo_boards(filename):
    f = open(filename)
    bingo_boards = []
    puzzle_numbers = f.readline().strip("\n").split(",")
    f.readline()

    bingo_board = []
    for row in f:
        row = row.strip("\n").split(" ")
        if row != [""]:
            bingo_board.append([[a, False] for a in row if a != ""])
        else:
            if bingo_board:
                bingo_boards.append(bingo_board)
                bingo_board = []

    return bingo_boards, puzzle_numbers


def display_board(bingo_board):
    for row in bingo_board:
        print(row)
    print("")


def display_boards(bingo_boards):
    for bingo_board in bingo_boards:
        display_board(bingo_board)


def check_board(bingo_board):
    columns = []
    for row in bingo_board:
        played_numbers_row = [block[1] for block in row]
        if all(played_numbers_row):
            return True
        for i, block in enumerate(row):
            try:
                columns[i].append(block[1])
            except IndexError:
                columns.append([block[1]])

    for column in columns:
        if all(column):
            return True


def mark_board(bingo_board, number):
    for row in bingo_board:
        for block in row:
            block_value = block[0]
            if block_value == number:
                block[1] = True
                return check_board(bingo_board)


def mark_boards(bingo_boards, puzzle_numbers):
    for nth, number in enumerate(puzzle_numbers):
        for i, bingo_board in enumerate(bingo_boards):
            if mark_board(bingo_board, number):
                print("board number: ", i, "wins at number", nth)
                return bingo_board, number, nth
        # display_boards(bingo_boards)


def calculate_answer(winning_board, last_number):
    sum_of_false_numbers = 0
    for row in winning_board:
        sum_of_false_numbers += sum([int(block[0]) for block in row if not block[1]])

    print("Final sum:", sum_of_false_numbers * int(last_number))


def get_last_winner(bingo_boards, win_order):
    sorted_win_order = sorted(win_order, key=lambda x: (x[1], x[0]), reverse=True)
    print(sorted_win_order)
    last_played_number = sorted_win_order[0][2]
    last_winner = bingo_boards[sorted_win_order[0][0]]
    display_board(last_winner)
    calculate_answer(last_winner, last_played_number)


def play_bingo():
    bingo_boards, puzzle_numbers = create_bingo_boards("inputs/adventofcode4.txt")
    winning_board, last_number, nth = mark_boards(bingo_boards, puzzle_numbers)
    display_board(winning_board)
    calculate_answer(winning_board, last_number)

    return bingo_boards, puzzle_numbers, nth

    # display_boards(bingo_boards)


# Creates new boards and starts finding the nth puzzle number for each board
# After all boards have won
def play_bingo_last_wins():
    bingo_boards, puzzle_numbers = create_bingo_boards("inputs/adventofcode4.txt")
    win_order = []
    for b, bingo_board in enumerate(bingo_boards):
        for n, number in enumerate(puzzle_numbers):
            if mark_board(bingo_board, number):
                # (board_index, index of last played number, last_played number)
                win_order.append((b, n, number))
                break

    get_last_winner(bingo_boards, win_order)


# Continues where first part left of just because it felt cool :D
def play_bingo_last_wins_alt(bingo_boards, puzzle_numbers, nth):
    win_order = []
    for b, bingo_board in enumerate(bingo_boards):
        for n, number in enumerate(puzzle_numbers[nth:]):
            if mark_board(bingo_board, number):
                # (board_index, index of last played number, last_played number)
                win_order.append((b, n + nth, number))
                break

    get_last_winner(bingo_boards, win_order)


if __name__ == '__main__':
    boards, numbers, number_index = play_bingo()
    play_bingo_last_wins_alt(bingo_boards=boards, puzzle_numbers=numbers, nth=number_index)
    play_bingo_last_wins()
