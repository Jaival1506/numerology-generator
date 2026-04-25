from core.name_logic import generate_pattern_column, name_to_numbers, cumulative_sum
from core.sequence_logic import get_sequences
from core.year_prediction import generate_year_sequence
from output.excel_writer import build_excel_bytes


def generate_numerology_report(first, middle, last, birth_year):

    # -------------------------
    # PROCESS EACH NAME PART
    # -------------------------
    def process_name_part(part_name):
        nums = name_to_numbers(part_name)
        cumsum = cumulative_sum(nums)

        start = cumsum[0]        # first cumulative value
        start_index = 0          # first letter index

        column = generate_pattern_column(start, nums, start_index)

        return column

    # Generate columns
    f_col = process_name_part(first)
    m_col = process_name_part(middle)
    l_col = process_name_part(last)

    # -------------------------
    # STRUCTURE FOR EXCEL
    # -------------------------
    columns = {
        first.strip().title(): f_col,
        middle.strip().title(): m_col,
        last.strip().title(): l_col
    }

    # -------------------------
    # SEQUENCES
    # -------------------------
    all_numbers = f_col + m_col + l_col
    sequences = get_sequences(all_numbers)

    # -------------------------
    # YEAR PREDICTION
    # -------------------------
    years = generate_year_sequence(birth_year, 30)

    # -------------------------
    # EXPORT (IN-MEMORY)
    # -------------------------
    return build_excel_bytes(
        name=f"{first} {middle} {last}",
        columns=columns,
        sequences=sequences,
        years=years
    )