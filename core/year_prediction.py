from utils.helpers import reduce_to_single


def generate_year_sequence(start_year, count=30):
    years = [start_year]
    current = start_year

    for _ in range(count - 1):
        digit_sum = reduce_to_single(current)
        next_year = current + digit_sum
        years.append(next_year)
        current = next_year

    return years