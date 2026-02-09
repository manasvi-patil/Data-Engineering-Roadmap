#converting excel into csv

import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

INPUT_XLSX = BASE_DIR / "data" / "input data" / "student_data.xlsx"
OUTPUT_CSV = BASE_DIR / "data" / "input data" / "student_data.csv"

df = pd.read_excel(INPUT_XLSX)
df.to_csv(OUTPUT_CSV, index=None, header=True, encoding='utf-8')
print(f"Successfully converted {INPUT_XLSX.name} to {OUTPUT_CSV.name}")


