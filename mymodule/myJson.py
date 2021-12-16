import json

def load_jsonfile(path):
    with open(path, "r") as f:
        x = json.load(f)
    return x

def save_jsonfile(path, value):
    with open(path, 'w') as f:
        json.dump(value, f, indent=4, ensure_ascii=False)