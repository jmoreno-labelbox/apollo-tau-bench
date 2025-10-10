import json
from typing import Any, Dict, List, Optional
from datetime import datetime
from domains.dto import Tool

def _now_iso() -> str:
    # return datetime.now(timezone.utc).isoformat()
    return "deterministic placeholder for current time"


class GetDeviceInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_ids: Optional[List[str]] = None) -> str:
        devices = data.get('devices', [])
        if device_ids:
            result = [d for d in devices if d.get('id') in device_ids]
        else:
            result = devices
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_device_info",
                "description": "Get information about one or more devices.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of device IDs to retrieve. If empty, all devices will be returned."
                        }
                    },
                    "additionalProperties": False
                }
            }
        }

class SetDeviceState(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str, state_update: Dict[str, Any]) -> str:
        devices = data.get('devices', [])
        device_found = False
        for device in devices:
            if device.get('id') == device_id:
                device_found = True
                device['state'].update(state_update)
                device['state']['last_updated'] = _now_iso()
                break

        if not device_found:
            # try sensors if not found in devices
            sensors = data.get('sensors', [])
            sensor_found = False
            for sensor in sensors:
                if sensor.get('id') == device_id:
                    sensor['state'].update(state_update)
                    sensor['state']['last_updated'] = _now_iso()
                    sensor_found = True
                    break
            if not sensor_found:
                return json.dumps({"error": f"Device/sensor with ID '{device_id}' not found."}, indent=2)

        return json.dumps({"success": f"State for device/sensor '{device_id}' updated."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_device_state",
                "description": "Set the state of a specific device/sensor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The ID of the device/sensor to update."
                        },
                        "state_update": {
                            "type": "object",
                            "description": "A dictionary of state parameters to update (e.g., {\"power\": \"on\", \"brightness\": 80}).",
                            "additionalProperties": True
                        }
                    },
                    "required": ["device_id", "state_update"],
                    "additionalProperties": False
                }
            }
        }

class AddDevice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_device: Dict[str, Any]) -> str:
        devices = data.get('devices', [])
        if 'id' not in new_device:
            return json.dumps({"error": "New device must have an 'id'."}, indent=2)

        if any(d.get('id') == new_device['id'] for d in devices):
            return json.dumps({"error": f"Device with ID '{new_device['id']}' already exists."}, indent=2)

        devices.append(new_device)
        return json.dumps({"success": f"Device '{new_device.get('name', new_device['id'])}' added."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_device",
                "description": "Add a new device to the smart home system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "new_device": {
                            "type": "object",
                            "description": "A dictionary representing the new device.",
                            "properties": {
                                "id": {"type": "string"},
                                "type": {"type": "string"},
                                "name": {"type": "string"},
                                "location": {"type": "string"}
                            },
                            "required": ["id", "type", "name"],
                            "additionalProperties": True
                        }
                    },
                    "required": ["new_device"],
                    "additionalProperties": False
                }
            }
        }

class RemoveDevice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str) -> str:
        devices = data.get('devices', [])
        initial_len = len(devices)
        devices[:] = [d for d in devices if d.get('id') != device_id]

        if len(devices) == initial_len:
            return json.dumps({"error": f"Device with ID '{device_id}' not found."}, indent=2)

        # Also remove from rooms
        rooms = data.get('rooms', [])
        for room in rooms:
            if device_id in room.get('devices', []):
                room['devices'].remove(device_id)

        return json.dumps({"success": f"Device '{device_id}' removed."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_device",
                "description": "Remove a device from the smart home system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The ID of the device to remove."
                        }
                    },
                    "required": ["device_id"],
                    "additionalProperties": False
                }
            }
        }

class GetRoomInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], room_ids: Optional[List[str]] = None) -> str:
        rooms = data.get('rooms', [])
        if room_ids:
            result = [r for r in rooms if r.get('id') in room_ids]
        else:
            result = rooms
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_room_info",
                "description": "Get information about one or more rooms.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of room IDs to retrieve. If empty, all rooms will be returned."
                        }
                    },
                    "additionalProperties": False
                }
            }
        }

class ManageRoomDevices(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], room_id: str, device_id: str, action: str) -> str:
        rooms = data.get('rooms', [])
        room_found = False
        for room in rooms:
            if room.get('id') == room_id:
                room_found = True
                if action == 'add':
                    if device_id not in room.get('devices', []):
                        room.setdefault('devices', []).append(device_id)
                        return json.dumps({"success": f"Device '{device_id}' added to room '{room_id}'."}, indent=2)
                    else:
                        return json.dumps({"error": f"Device '{device_id}' already in room '{room_id}'."}, indent=2)
                elif action == 'remove':
                    if device_id in room.get('devices', []):
                        room['devices'].remove(device_id)
                        return json.dumps({"success": f"Device '{device_id}' removed from room '{room_id}'."}, indent=2)
                    else:
                        return json.dumps({"error": f"Device '{device_id}' not found in room '{room_id}'."}, indent=2)
                else:
                    return json.dumps({"error": "Invalid action. Use 'add' or 'remove'."}, indent=2)

        if not room_found:
            return json.dumps({"error": f"Room with ID '{room_id}' not found."}, indent=2)
        return json.dumps({"error": "An unexpected error occurred."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_room_devices",
                "description": "Add or remove a device from a room.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {
                            "type": "string",
                            "description": "The ID of the room to modify."
                        },
                        "device_id": {
                            "type": "string",
                            "description": "The ID of the device to add or remove."
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "remove"],
                            "description": "The action to perform."
                        }
                    },
                    "required": ["room_id", "device_id", "action"],
                    "additionalProperties": False
                }
            }
        }

class ListAllScenes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        scenes = data.get('scenes', [])
        scene_info = [{"id": s.get("id"), "name": s.get("name"), "description": s.get("description")} for s in scenes]
        return json.dumps(scene_info, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_all_scenes",
                "description": "List all available scenes."
            }
        }

class ActivateScene(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str) -> str:
        scenes = data.get('scenes', [])
        devices = data.get('devices', [])
        scene_found = False
        for scene in scenes:
            if scene.get('id') == scene_id:
                scene_found = True
                for action in scene.get('actions', []):
                    device_id = action.get('device_id')
                    update = action.get('update')
                    for device in devices:
                        if device.get('id') == device_id:
                            device['state'].update(update)
                            device['state']['last_updated'] = _now_iso()
                break

        if not scene_found:
            return json.dumps({"error": f"Scene with ID '{scene_id}' not found."}, indent=2)

        return json.dumps({"success": f"Scene '{scene_id}' activated."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "activate_scene",
                "description": "Activate a specific scene, applying its actions to devices.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The ID of the scene to activate."
                        }
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False
                }
            }
        }

class CreateScene(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_scene: Dict[str, Any]) -> str:
        scenes = data.get('scenes', [])
        if 'id' not in new_scene:
            return json.dumps({"error": "New scene must have an 'id'."}, indent=2)
        if any(s.get('id') == new_scene['id'] for s in scenes):
            return json.dumps({"error": f"Scene with ID '{new_scene['id']}' already exists."}, indent=2)

        scenes.append(new_scene)
        return json.dumps({"success": f"Scene '{new_scene.get('name', new_scene['id'])}' created."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_scene",
                "description": "Create a new scene.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "new_scene": {
                            "type": "object",
                            "description": "A dictionary representing the new scene.",
                             "properties": {
                                "id": {"type": "string"},
                                "name": {"type": "string"},
                                "description": {"type": "string"},
                                "actions": {"type": "array", "items": {"type": "object"}}
                            },
                            "required": ["id", "name", "actions"],
                            "additionalProperties": True
                        }
                    },
                    "required": ["new_scene"],
                    "additionalProperties": False
                }
            }
        }

class DeleteScene(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str) -> str:
        scenes = data.get('scenes', [])
        initial_len = len(scenes)
        scenes[:] = [s for s in scenes if s.get('id') != scene_id]

        if len(scenes) == initial_len:
            return json.dumps({"error": f"Scene with ID '{scene_id}' not found."}, indent=2)

        return json.dumps({"success": f"Scene '{scene_id}' deleted."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_scene",
                "description": "Delete a scene.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The ID of the scene to delete."
                        }
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False
                }
            }
        }

class GetReminders(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reminder_id: Optional[str] = None, status: Optional[str] = None) -> str:
        reminders = data.get('reminders', [])
        result = reminders
        if reminder_id:
            result = [r for r in result if r.get('reminder_id') == reminder_id]
        if status:
            result = [r for r in result if r.get('status') == status]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_reminders",
                "description": "Get reminders, with optional filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The ID of a specific reminder to retrieve."
                        },
                        "status": {
                            "type": "string",
                            "enum": ["scheduled", "active", "inactive"],
                            "description": "Filter reminders by status."
                        }
                    },
                    "additionalProperties": False
                }
            }
        }

class AddReminder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_reminder: Dict[str, Any]) -> str:
        reminders = data.get('reminders', [])
        if 'reminder_id' not in new_reminder:
            return json.dumps({"error": "New reminder must have a 'reminder_id'."}, indent=2)

        reminders.append(new_reminder)
        return json.dumps({"success": "Reminder added."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_reminder",
                "description": "Add a new reminder.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "new_reminder": {
                            "type": "object",
                            "description": "A dictionary representing the new reminder.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["new_reminder"],
                    "additionalProperties": False
                }
            }
        }

class UpdateReminder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reminder_id: str, update_fields: Dict[str, Any]) -> str:
        reminders = data.get('reminders', [])
        reminder_found = False
        for reminder in reminders:
            if reminder.get('reminder_id') == reminder_id:
                reminder_found = True
                reminder.update(update_fields)
                break

        if not reminder_found:
            return json.dumps({"error": f"Reminder with ID '{reminder_id}' not found."}, indent=2)

        return json.dumps({"success": f"Reminder '{reminder_id}' updated."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_reminder",
                "description": "Update an existing reminder.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The ID of the reminder to update."
                        },
                        "update_fields": {
                            "type": "object",
                            "description": "Fields to update in the reminder.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["reminder_id", "update_fields"],
                    "additionalProperties": False
                }
            }
        }

class DeleteReminder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reminder_id: str) -> str:
        reminders = data.get('reminders', [])
        initial_len = len(reminders)
        reminders[:] = [r for r in reminders if r.get('reminder_id') != reminder_id]

        if len(reminders) == initial_len:
            return json.dumps({"error": f"Reminder with ID '{reminder_id}' not found."}, indent=2)

        return json.dumps({"success": f"Reminder '{reminder_id}' deleted."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_reminder",
                "description": "Delete a reminder.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The ID of the reminder to delete."
                        }
                    },
                    "required": ["reminder_id"],
                    "additionalProperties": False
                }
            }
        }

class GetCustomList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: Optional[str] = None, list_name: Optional[str] = None) -> str:
        custom_lists = data.get('custom_lists', [])
        if not list_id and not list_name:
            return json.dumps(custom_lists, indent=2)

        result = []
        for l in custom_lists:
            if list_id and l.get('list_id') == list_id:
                result.append(l)
            elif list_name and l.get('name') == list_name:
                result.append(l)

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_custom_list",
                "description": "Get one or more custom lists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The ID of the list to retrieve."
                        },
                        "list_name": {
                            "type": "string",
                            "description": "The name of the list to retrieve."
                        }
                    },
                    "additionalProperties": False
                }
            }
        }

class CreateCustomList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_list: Dict[str, Any]) -> str:
        custom_lists = data.get('custom_lists', [])
        if 'list_id' not in new_list:
            return json.dumps({"error": "New list must have 'list_id' and 'name'."}, indent=2)

        custom_lists.append(new_list)
        return json.dumps({"success": "Custom list created."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_custom_list",
                "description": "Create a new custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "new_list": {
                            "type": "object",
                            "description": "A dictionary representing the new custom list.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["new_list"],
                    "additionalProperties": False
                }
            }
        }

class ManageCustomListItems(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: str, item: Dict[str, Any], action: str) -> str:
        custom_lists = data.get('custom_lists', [])
        list_found = False
        for l in custom_lists:
            if l.get('list_id') == list_id:
                list_found = True
                items = l.setdefault('items', [])
                if action == 'add':
                    items.append(item)
                    return json.dumps({"success": f"Item added to list '{list_id}'."}, indent=2)
                elif action == 'remove':
                    initial_len = len(items)
                    items[:] = [i for i in items if i.get('item') != item.get('item')]
                    if len(items) < initial_len:
                        return json.dumps({"success": f"Item removed from list '{list_id}'."}, indent=2)
                    else:
                        return json.dumps({"error": f"Item not found in list '{list_id}'."}, indent=2)
                else:
                    return json.dumps({"error": "Invalid action. Use 'add' or 'remove'."}, indent=2)

        if not list_found:
            return json.dumps({"error": f"List with ID '{list_id}' not found."}, indent=2)
        return json.dumps({"error": "An unexpected error occurred."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_custom_list_items",
                "description": "Add or remove items from a custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The ID of the list to modify."
                        },
                        "item": {
                            "type": "object",
                            "description": "The item to add or remove. For removal, only the 'item' name is needed.",
                             "properties": {
                                "item": {"type": "string"},
                                "quantity": {"type": "integer"}
                            },
                            "required": ["item"]
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "remove"],
                            "description": "The action to perform."
                        }
                    },
                    "required": ["list_id", "item", "action"],
                    "additionalProperties": False
                }
            }
        }

class DeleteCustomList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: str) -> str:
        custom_lists = data.get('custom_lists', [])
        initial_len = len(custom_lists)
        custom_lists[:] = [l for l in custom_lists if l.get('list_id') != list_id]

        if len(custom_lists) == initial_len:
            return json.dumps({"error": f"Custom list with ID '{list_id}' not found."}, indent=2)

        return json.dumps({"success": f"Custom list '{list_id}' deleted."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_custom_list",
                "description": "Delete a custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The ID of the custom list to delete."
                        }
                    },
                    "required": ["list_id"],
                    "additionalProperties": False
                }
            }
        }

class GetSensorData(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sensor_ids: Optional[List[str]] = None) -> str:
        sensors = data.get('sensors', [])
        if sensor_ids:
            result = [s for s in sensors if s.get('id') in sensor_ids]
        else:
            result = sensors
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_sensor_data",
                "description": "Get data from one or more sensors. Sensor state is read-only.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of sensor IDs to retrieve data from. If empty, returns data for all sensors."
                        }
                    },
                    "additionalProperties": False
                }
            }
        }

class GetMemberInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], member_ids: Optional[List[str]] = None) -> str:
        members = data.get('members', [])
        if member_ids:
            result = [m for m in members if m.get('id') in member_ids]
        else:
            result = members
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_member_info",
                "description": "Get information about one or more household members.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of member IDs to retrieve. If empty, all members will be returned."
                        }
                    },
                    "additionalProperties": False
                }
            }
        }

TOOLS = [
    GetDeviceInfo(),
    SetDeviceState(),
    AddDevice(),
    RemoveDevice(),
    GetRoomInfo(),
    ManageRoomDevices(),
    ListAllScenes(),
    ActivateScene(),
    CreateScene(),
    DeleteScene(),
    GetReminders(),
    AddReminder(),
    UpdateReminder(),
    DeleteReminder(),
    GetCustomList(),
    CreateCustomList(),
    ManageCustomListItems(),
    DeleteCustomList(),
    GetSensorData(),
    GetMemberInfo(),
]
