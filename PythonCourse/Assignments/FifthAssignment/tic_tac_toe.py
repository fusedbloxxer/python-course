import time
import random

robot_choices = (4, 0, 2, 6, 8, 1, 3, 5, 7)
game_table = [[0 for i in range(3)] for i in range(3)]


def is_game_over(score: int) -> tuple:
    if score == 3:
        return True, "First player won."
    elif score == -3:
        return True, "Second player won."
    else:
        return False, None


def check_table():
    global game_table

    is_full = True
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(len(game_table)):
        col_sum = 0
        row_sum = 0

        for j in range(len(game_table)):
            col_sum += game_table[i][j]
            row_sum += game_table[j][i]

            if i == j:
                main_diagonal_sum += game_table[i][j]

            if i + j == len(game_table) - 1:
                secondary_diagonal_sum += game_table[i][j]

            if game_table[i][j] == 0:
                is_full = False

        if (game_result := is_game_over(col_sum))[0] or (game_result := is_game_over(row_sum))[0]:
            return game_result

    if (game_result := is_game_over(main_diagonal_sum))[0] or (game_result := is_game_over(secondary_diagonal_sum))[0]:
        return game_result

    return is_full, "It's a tie!"


def draw_sign(value: int) -> str:
    if value == 0:
        return ' '
    elif value == 1:
        return 'X'
    elif value == -1:
        return '0'
    raise ValueError


def draw_table():
    global game_table

    drawn_table = ""

    for i in range(len(game_table)):
        for j in range(len(game_table)):
            drawn_table += draw_sign(game_table[i][j])

            if j < len(game_table) - 1:
                drawn_table += '|'

        if i < len(game_table) - 1:
            drawn_table += "\n------\n"

    return drawn_table


def robot_turn():
    global game_table, robot_choices

    for choice in robot_choices:
        col = choice % len(game_table)
        row = choice // len(game_table)

        if game_table[row][col] == 0:
            game_table[row][col] = -1
            break


def is_input_valid(user_input: str) -> tuple:
    global game_table
    table_len = len(game_table)

    if not user_input.isdigit():
        return False, "You did not enter a number!"
    elif (position := int(user_input)) < 1 or position > 9:
        return False, "Number is out of bounds. Allowed range is 1-9."
    elif game_table[(position := position - 1) // table_len][position % table_len] != 0:
        return False, "Position is already occupied!"
    return True, position


round_count = -1

while (result := check_table())[0] is False:
    print(draw_table())

    if (round_count := round_count + 1) % 2 == 0:
        while not (player_choice := is_input_valid(input("Enter a position from 1-9: ")))[0]:
            print(player_choice[1])
        game_table[player_choice[1] // len(game_table)][player_choice[1] % len(game_table)] = 1
    else:
        print("Robot is thinking ", end=' ', flush=True)
        thinking_time = random.randint(1, 4) / 3

        for i in range(3):
            time.sleep(thinking_time)
            print('.', end=' ', flush=True)

        print(flush=True)
        robot_turn()

print(draw_table())
print(result[1])
