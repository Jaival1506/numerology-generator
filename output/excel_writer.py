import pandas as pd
from utils.helpers import reduce_to_single
from io import BytesIO

def build_excel_bytes(name, columns, sequences, years):
    buffer = BytesIO()

    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        first, middle, last = [x.strip().title() for x in name.split()]

        # --- Name Analysis ---
        def create_name_df(part):
            letters = list(part)
            numbers = [(ord(c.upper()) - ord('A')) % 9 + 1 for c in letters]
            cumsum, total = [], 0
            for n in numbers:
                total += n
                cumsum.append(total)
            return pd.DataFrame({
                "Letters": letters,
                "Numbers": numbers,
                "Cumulative": cumsum
            })

        sheet = "Name Analysis"
        r = 0
        for label, part in [("FIRST NAME", first), ("MIDDLE NAME", middle), ("LAST NAME", last)]:
            df = create_name_df(part)
            pd.DataFrame({label: [part]}).to_excel(writer, sheet_name=sheet, startrow=r, index=False)
            r += 2
            df.to_excel(writer, sheet_name=sheet, startrow=r, index=False)
            r += len(df) + 3

        # --- Pythagoras Output (one column per name + gaps) ---
        col_df = pd.DataFrame({
            first: pd.Series(columns[first]),
            "": pd.Series([]),
            middle: pd.Series(columns[middle]),
            " ": pd.Series([]),
            last: pd.Series(columns[last])
        })
        col_df.to_excel(writer, sheet_name="Pythagoras Output", index=False)

        # --- Sequences (len >= 2) ---
        seq_df = pd.DataFrame({
            "Sequence": [", ".join(map(str, s)) for s in sequences if len(s) >= 2]
        })
        seq_df.to_excel(writer, sheet_name="Sequences", index=False)

        # --- Year Prediction (single digit) ---
        year_df = pd.DataFrame({
            "Year": years,
            "Digit": [reduce_to_single(y) for y in years]
        })
        year_df.to_excel(writer, sheet_name="Year Prediction", index=False)

    buffer.seek(0)
    return buffer