from utils.helpers import letter_to_number


def name_to_numbers(name):
    return [letter_to_number(c) for c in name if c.isalpha()]


def cumulative_sum(nums):
    result = []
    total = 0
    for n in nums:
        total += n
        result.append(total)
    return result


def generate_pattern_column(start, pattern, start_index):
    res = [start]
    current = start
    i = start_index + 1   # 🔥 start from NEXT letter

    while True:
        step = pattern[i % len(pattern)]
        current += step

        if current > 100:
            break

        res.append(current)
        i += 1

    return res