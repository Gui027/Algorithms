def contar(letra, palavra):
    count = 0
    for x in palavra:
        if x == letra:
            count += 1
    return count


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    for x in first_string:
        if contar(x, first_string) != contar(x, second_string):
            return False
    return True
