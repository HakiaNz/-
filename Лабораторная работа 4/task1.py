import json
def task() -> float:
    filename = 'data.json'

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {
            "0": {"score": 0.945, "weight": 1},
            "1": {"score": 0.6755, "weight": 2}
        }

    total = 0.0
    if isinstance(data, dict):
        for item in data.values():
            if isinstance(item, dict):
                score = item.get('score', 0)
                weight = item.get('weight', 0)
                total += score * weight
    return round(total, 3)
print(task())