def reduce_to_single(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n


def letter_to_number(ch):
    return (ord(ch.upper()) - ord('A')) % 9 + 1