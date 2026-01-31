import pandas as pd
import json


def save_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

