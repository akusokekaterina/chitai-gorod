import json
import random
import string
from typing import Dict, Any


def generate_random_phone():
    return f"+79{''.join(random.choices(string.digits, k=9))}"


def generate_random_code():
    return ''.join(random.choices(string.digits, k=6))


def read_json_file(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json_file(file_path: str, data: Dict[str, Any]):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
