import os
import json
from random import randint


def read_fixture_file(file_name: str):
    with open(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures",
            file_name,
        )
    ) as fixture_file:
        return fixture_file.read().strip()

def get_fixture_json(file_name: str):
    return json.loads(read_fixture_file(file_name))

def get_random_item(items: list):
    return items[randint(0, len(items) - 1)]
