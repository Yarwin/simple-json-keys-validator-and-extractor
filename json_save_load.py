import json
import io


def save_to_json(results, file_path):

    with io.open(file_path, 'w', encoding='utf8') as f:
        json.dump(results, f, sort_keys=True, indent=4, ensure_ascii=False)


def load_from_json(file_path):

    with io.open(file_path, 'r', encoding="utf8") as f:
        return json.load(f)
