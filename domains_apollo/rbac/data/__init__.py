import json
import os
from typing import Any, Dict

FOLDER_PATH = os.path.dirname(__file__)

JSON_EXTENSION = '.json'

def load_data() -> Dict[str, Any]:

    data = {}
    for root, dirs, files in os.walk(FOLDER_PATH):
        for fname in files:
            if fname.endswith(JSON_EXTENSION):
                with open(os.path.join(FOLDER_PATH, fname)) as f:
                    data[os.path.splitext(fname)[0]] = json.load(f)

    return data
