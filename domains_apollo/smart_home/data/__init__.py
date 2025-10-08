import json
import os
from typing import Any, Dict

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> Dict[str, Any]:
    with open(os.path.join(FOLDER_PATH, "devices.json")) as f:
        devices_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "custom_lists.json")) as f:
        custom_lists_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "reminders.json")) as f:
        reminders_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "rooms.json")) as f:
        rooms_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "members.json")) as f:
        members_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "sensors.json")) as f:
        sensors_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "scenes.json")) as f:
        scenes_data = json.load(f)
    return {
        "devices": devices_data,
        "custom_lists": custom_lists_data,
        "reminders": reminders_data,
        "rooms": rooms_data,
        "members": members_data,
        "sensors": sensors_data,
        "scenes": scenes_data
    }
