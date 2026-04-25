import pandas as pd
from utils.helpers import reduce_to_single
import datetime


def write_to_excel(name, nums, cumsum, columns, sequences, years):

    # -------------------------
    # UNIQUE FILE NAME
    # -------------------------
    filename = f"numerology_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

    with pd.ExcelWriter(filename, engine="openpyxl") as writer:

        # -------------------------
        # SPLIT NAME
        # -------------------------
        first, middle, last = name.split()

        # -------------------------
        # SHEET 1: NAME ANALYSIS
        # -------------------------
        def create_name_df(part):
            letters = list(part)
            numbers = [(ord(c.upper()) - ord('A')) % 9 + 1 for c in letters]

            cumsum = []
            total = 0
            for n in numbers:
                total += n
                cumsum.append(total)

            return pd.DataFrame({
                "Letters": letters,
                "Numbers": numbers,
                "Cumulative": cumsum
            })

        sheet_name = "Name Analysis"
        start_row = 0

        for label, part in [("FIRST NAME", first), ("MIDDLE NAME", middle), ("LAST NAME", last)]:
            df = create_name_df(part)

            pd.DataFrame({label: [part]}).to_excel(
                writer, sheet_name=sheet_name, startrow=start_row, index=False
            )
            start_row += 2

            df.to_excel(writer, sheet_name=sheet_name, startrow=start_row, index=False)
            start_row += len(df) + 3

        # -------------------------
        # SHEET 2: PYTHAGORAS OUTPUT (SINGLE COLUMN PER NAME)
        # -------------------------

        # columns dict should now be like:
        # { "Alpa": [...], "Kalpesh": [...], "Badiani": [...] }

        col_df = pd.DataFrame({
            first: pd.Series(columns[first]),
            "": pd.Series([]),  # gap
            middle: pd.Series(columns[middle]),
            " ": pd.Series([]),  # gap
            last: pd.Series(columns[last])
        })

        col_df.to_excel(writer, sheet_name="Pythagoras Output", index=False)

        # -------------------------
        # SHEET 3: SEQUENCES (ONLY LEN >= 2)
        # -------------------------
        seq_df = pd.DataFrame({
            "Sequence": [
                ", ".join(map(str, seq))
                for seq in sequences if len(seq) >= 2
            ]
        })

        seq_df.to_excel(writer, sheet_name="Sequences", index=False)

        # -------------------------
        # SHEET 4: YEAR PREDICTION
        # -------------------------
        year_df = pd.DataFrame({
            "Year": years,
            "Digit": [reduce_to_single(y) for y in years]
        })

        year_df.to_excel(writer, sheet_name="Year Prediction", index=False)

    return filename