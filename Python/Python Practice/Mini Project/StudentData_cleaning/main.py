#main function to run processor and mention csvs

from processor import DataProcessor
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

CONFIG_PATH = BASE_DIR / "config" / "config.json"
INPUT_CSV = BASE_DIR / "data" / "input data" / "student_data.csv"
OUTPUT_DIR = BASE_DIR / "data" / "output data" 

processor = DataProcessor(CONFIG_PATH)
processor.process_csv(INPUT_CSV)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

processor.write_csv(OUTPUT_DIR / "valid_students.csv", processor.valid_students)
processor.write_csv(OUTPUT_DIR / "invalid_students.csv", processor.invalid_students)
