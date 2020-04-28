# TestCase: "0 10 0010 000.001 .0 .10 0. 1. +0 -0 +10 -10 , , +.01 +01. -.01 -01. -.07 7"

# General patterns: [+-]{0,1}[0-9]{0,}\.{0,1}[0-9]{0,1}

# Note: min length is 1


def is_num_seq(sequence: str, sep: str = "") -> bool:
    if len(sequence) == 0:
        return False

    index = 0
    dot = False
    first = True
    result = True
    length = len(sequence)

    while index < length:

        if sequence[index] in sep:
            first = True
            dot = False
            index += 1
            continue

        if first:
            if sequence[index] in "-+":
                if index + 1 >= length:
                    result = False
                    break
                elif sequence[index + 1] == '.':
                    if index + 2 >= length or not sequence[index + 2].isdigit():
                        result = False
                        break
                elif not sequence[index + 1].isdigit():
                    result = False
                    break
            elif sequence[index] == '.':
                if index + 1 >= length:
                    result = False
                    break
                else:
                    dot = True
            elif not sequence[index].isdigit():
                result = False
                break
        else:
            if sequence[index] == '.':
                if dot:
                    result = False
                    break
                else:
                    dot = True
            elif not sequence[index].isdigit():
                result = False
                break

        first = False
        index += 1

    return result


def to_float(number: str) -> float:
    if number.isdigit():
        return float(number)
    elif not is_num_seq(number):
        return None
    else:
        if '+' in number:
            number = float(number.split('+')[1])
        elif '-' in number:
            number = -1 * float(number.split('-')[1])
        else:
            number = float(number)
        return number
