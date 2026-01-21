import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
if __name__ == '__main__':
    task()
with open(OUTPUT_FILENAME, encoding='utf-8') as output_f:
    for line in output_f:
        print(line, end="")
