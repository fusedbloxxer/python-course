import random

# The Hangman Game
#   _ _
#  |   |
#  |  _O_
#  |  /|\
#  |   |
#  |  / \
# _|_
#
# def string_mapper(string: str) -> list:
#     return [[(0, c) for c in line] for line in string.split('\n')]


hangman = [
    [(7, ' '), (7, ' '), (7, '_'), (7, ' '), (7, '_')],
    [(7, ' '), (7, '|'), (7, ' '), (7, ' '), (7, ' '), (0, '|')],
    [(7, ' '), (7, '|'), (7, ' '), (6, ' '), (0, '_'), (6, 'O'), (0, '_')],
    [(7, ' '), (7, '|'), (7, ' '), (5, ' '), (5, '/'), (3, '|'), (4, '\\')],
    [(7, ' '), (7, '|'), (7, ' '), (3, ' '), (3, ' '), (3, '|')],
    [(7, ' '), (7, '|'), (7, ' '), (2, ' '), (2, '/'), (1, ' '), (1, '\\')],
    [(7, '_'), (7, '|'), (7, '_')]
]


def add_hints(guesses: dict) -> int:
    total_guesses = len(guesses)

    if total_guesses <= 3:
        hints = random.sample(list(guesses), k=random.randint(0, total_guesses // 2))
    elif total_guesses <= 6:
        hints = random.sample(list(guesses), k=random.randint(20 * total_guesses // 100, 40 * total_guesses // 100))
    else:
        hints = random.sample(list(guesses), k=random.randint(25 * total_guesses // 100, 45 * total_guesses // 100))

    for hint in hints:
        guesses[hint] = True

    return len(hints)


def draw_hangman(lives_left: int) -> None:
    if lives_left < 8:
        for row in hangman:
            for cell in row:
                print(cell[1] if cell[0] >= lives_left else ' ', end='')
            print()
    print(f"Lives left: {lives_left}")


def fetch_unique_words(filename: str) -> list:
    with open(filename, newline='') as word_reader:
        found_words = word_reader.read().replace('\r\n', ' ').upper().split(' ')
        return list({word for word in found_words if word.isalpha()})


def draw_hidden_word(word: str, guesses: dict) -> None:
    for character in word:
        print(character if guesses.get(character, False) is True else '_', end='')
    print()


if len(words := fetch_unique_words('words.txt')) == 0:
    print('No words were found.')
    exit()

score_count = {'NORMAL': {'wins': 0, 'losses': 0}, 'HINTS': {'wins': 0, 'losses': 0}}

while (play := input("Play Hangman? [normal/hints/exit]: ").upper()) in ['NORMAL', 'HINTS', '']:
    total_lives = 8
    correct_guesses = 0
    random_word = random.choice(words)
    guessed_unique_letters = dict(zip(list(random_word), [False] * len(random_word)))

    if play == 'HINTS':
        correct_guesses += add_hints(guessed_unique_letters)
    elif play == '':
        play = 'NORMAL'

    while total_lives != 0 and correct_guesses != len(guessed_unique_letters):

        draw_hangman(total_lives)
        draw_hidden_word(random_word, guessed_unique_letters)

        letter = input("Guess a letter: ").upper()

        if not letter.isalpha() or len(letter) != 1:
            print('Invalid input. Enter a single letter.')
            continue

        if letter not in guessed_unique_letters:
            total_lives = total_lives - 1
            continue

        if guessed_unique_letters[letter] is True:
            print('You already entered this letter!')
            continue

        guessed_unique_letters[letter] = True
        correct_guesses += 1

    if total_lives == 0:
        draw_hangman(total_lives)
        score_count[play]['losses'] += 1
        print(f'Game Over... The word was {random_word}.')
    else:
        score_count[play]['wins'] += 1
        print(f'Congratulations, you won! You guessed the word {random_word}.')

    for mode in score_count.items():
        print(f'Results for {mode[0].lower()} mode:')
        for result in mode[1].items():
            print(f'{result[0]}: {result[1]}')
