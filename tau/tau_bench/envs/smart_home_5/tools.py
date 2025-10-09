import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def _now_iso() -> str:
    pass
    #return datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()
    return "deterministic placeholder for current time"


class GetDeviceInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], device_ids: list[str] | None = None) -> str:
        devices = data.get("devices", {}).values()
        if device_ids:
            result = [d for d in devices.values() if d.get("id") in device_ids]
        else:
            result = devices
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDeviceInfo",
                "description": "Get information about one or more devices.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of device IDs to retrieve. If empty, all devices will be returned.",
                        }
                    },
                    "additionalProperties": False,
                },
            },
        }


class SetDeviceState(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], device_id: str, state_update: dict[str, Any]
    ) -> str:
        devices = data.get("devices", {}).values()
        device_found = False
        for device in devices.values():
            if device.get("id") == device_id:
                device_found = True
                device["state"].update(state_update)
                device["state"]["last_updated"] = _now_iso()
                break

        if not device_found:
            # attempt to use sensors if devices are not available
            sensors = data.get("sensors", {}).values()
            sensor_found = False
            for sensor in sensors.values()):
                if sensor.get("id") == device_id:
                    sensor["state"].update(state_update)
                    sensor["state"]["last_updated"] = _now_iso()
                    sensor_found = True
                    break
            if not sensor_found:
                payload = {"error": f"Device/sensor with ID '{device_id}' not found."}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"success": f"State for device/sensor '{device_id}' updated."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetDeviceState",
                "description": "Set the state of a specific device/sensor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The ID of the device/sensor to update.",
                        },
                        "state_update": {
                            "type": "object",
                            "description": 'A dictionary of state parameters to update (e.g., {"power": "on", "brightness": 80}).',
                            "additionalProperties": True,
                        },
                    },
                    "required": ["device_id", "state_update"],
                    "additionalProperties": False,
                },
            },
        }


class AddDevice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], new_device_id: str = None, new_device_name: str = None,
    new_device: Any = None,
    ) -> str:
        devices = data.get("devices", {}).values()
        if not new_device_id:
            payload = {"error": "New device must have an 'id'."}
            out = json.dumps(payload, indent=2)
            return out

        if any(d.get("id") == new_device_id for d in devices.values()):
            payload = {"error": f"Device with ID '{new_device_id}' already exists."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        new_device = {"id": new_device_id, "name": new_device_name}
        data["devices"][device_id] = new_device
        payload = {"success": f"Device '{new_device_name or new_device_id}' added."}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddDevice",
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
                                "location": {"type": "string"},
                            },
                            "required": ["id", "type", "name"],
                            "additionalProperties": True,
                        }
                    },
                    "required": ["new_device"],
                    "additionalProperties": False,
                },
            },
        }


class RemoveDevice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], devices: list = None, rooms: list = None, device_id: str = None, new_device: Any = None) -> str:
        devices = devices if devices is not None else data.get("devices", {}).values()
        initial_len = len(devices)
        devices[:] = [d for d in devices.values() if d.get("id") != device_id]

        if len(devices) == initial_len:
            payload = {"error": f"Device with ID '{device_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Additionally, eliminate from rooms
        rooms = rooms if rooms is not None else data.get("rooms", {}).values()
        for room in rooms.values()):
            if device_id in room.get("devices", []):
                room["devices"].remove(device_id)
        payload = {"success": f"Device '{device_id}' removed."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveDevice",
                "description": "Remove a device from the smart home system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The ID of the device to remove.",
                        }
                    },
                    "required": ["device_id"],
                    "additionalProperties": False,
                },
            },
        }


class GetRoomInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], room_ids: list[str] | None = None) -> str:
        rooms = data.get("rooms", {}).values()
        if room_ids:
            result = [r for r in rooms.values() if r.get("id") in room_ids]
        else:
            result = rooms
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRoomInfo",
                "description": "Get information about one or more rooms.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of room IDs to retrieve. If empty, all rooms will be returned.",
                        }
                    },
                    "additionalProperties": False,
                },
            },
        }


class ManageRoomDevices(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], room_id: str, device_id: str, action: str) -> str:
        rooms = data.get("rooms", {}).values()
        room_found = False
        for room in rooms.values():
            if room.get("id") == room_id:
                room_found = True
                if action == "add":
                    if device_id not in room.get("devices", []):
                        room.setdefault("devices", []).append(device_id)
                        payload = {
                            "success": f"Device '{device_id}' added to room '{room_id}'."
                        }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                    else:
                        payload = {
                            "error": f"Device '{device_id}' already in room '{room_id}'."
                        }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                elif action == "remove":
                    if device_id in room.get("devices", []):
                        room["devices"].remove(device_id)
                        payload = {
                            "success": f"Device '{device_id}' removed from room '{room_id}'."
                        }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                    else:
                        payload = {
                            "error": f"Device '{device_id}' not found in room '{room_id}'."
                        }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                else:
                    payload = {"error": "Invalid action. Use 'add' or 'remove'."}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out

        if not room_found:
            payload = {"error": f"Room with ID '{room_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"error": "An unexpected error occurred."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageRoomDevices",
                "description": "Add or remove a device from a room.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {
                            "type": "string",
                            "description": "The ID of the room to modify.",
                        },
                        "device_id": {
                            "type": "string",
                            "description": "The ID of the device to add or remove.",
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "remove"],
                            "description": "The action to perform.",
                        },
                    },
                    "required": ["room_id", "device_id", "action"],
                    "additionalProperties": False,
                },
            },
        }


class ListAllScenes(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], scenes: list[dict[str, Any]] = []) -> str:
        scene_info = [
            {
                "id": s.get("id"),
                "name": s.get("name"),
                "description": s.get("description"),
            }
            for s in scenes
        ]
        payload = scene_info
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAllScenes",
                "description": "List all available scenes.",
            },
        }


class ActivateScene(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], scenes: list = None, devices: list = None, scene_id: str = None) -> str:
        scenes = scenes if scenes is not None else data.get("scenes", {}).values()
        devices = devices if devices is not None else data.get("devices", {}).values()
        scene_found = False
        for scene in scenes.values()):
            if scene.get("id") == scene_id:
                scene_found = True
                for action in scene.get("actions", []):
                    device_id = action.get("device_id")
                    update = action.get("update")
                    for device in devices.values():
                        if device.get("id") == device_id:
                            device["state"].update(update)
                            device["state"]["last_updated"] = _now_iso()
                break

        if not scene_found:
            payload = {"error": f"Scene with ID '{scene_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"success": f"Scene '{scene_id}' activated."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ActivateScene",
                "description": "Activate a specific scene, applying its actions to devices.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The ID of the scene to activate.",
                        }
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False,
                },
            },
        }


class CreateScene(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], new_scene_id: str = None, new_scene_name: str = None,
    new_scene: Any = None,
    ) -> str:
        scenes = data.get("scenes", {}).values()
        if not new_scene_id:
            payload = {"error": "New scene must have an 'id'."}
            out = json.dumps(payload, indent=2)
            return out
        if any(s.get("id") == new_scene_id for s in scenes.values()):
            payload = {"error": f"Scene with ID '{new_scene_id}' already exists."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        new_scene = {"id": new_scene_id, "name": new_scene_name} if new_scene_name else {"id": new_scene_id}
        data["scenes"][scene_id] = new_scene
        payload = {"success": f"Scene '{new_scene.get('name', new_scene_id)}' created."}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateScene",
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
                                "actions": {
                                    "type": "array",
                                    "items": {"type": "object"},
                                },
                            },
                            "required": ["id", "name", "actions"],
                            "additionalProperties": True,
                        }
                    },
                    "required": ["new_scene"],
                    "additionalProperties": False,
                },
            },
        }


class DeleteScene(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], scene_id: str) -> str:
        scenes = data.get("scenes", {}).values()
        initial_len = len(scenes)
        scenes[:] = [s for s in scenes.values() if s.get("id") != scene_id]

        if len(scenes) == initial_len:
            payload = {"error": f"Scene with ID '{scene_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"success": f"Scene '{scene_id}' deleted."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteScene",
                "description": "Delete a scene.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The ID of the scene to delete.",
                        }
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False,
                },
            },
        }


class GetReminders(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], reminder_id: str | None = None, status: str | None = None
    ) -> str:
        reminders = data.get("reminders", {}).values()
        result = reminders
        if reminder_id:
            result = [r for r in result.values() if r.get("reminder_id") == reminder_id]
        if status:
            result = [r for r in result.values() if r.get("status") == status]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReminders",
                "description": "Get reminders, with optional filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The ID of a specific reminder to retrieve.",
                        },
                        "status": {
                            "type": "string",
                            "enum": ["scheduled", "active", "inactive"],
                            "description": "Filter reminders by status.",
                        },
                    },
                    "additionalProperties": False,
                },
            },
        }


class AddReminder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], new_reminder: dict[str, Any]) -> str:
        reminders = data.get("reminders", {}).values()
        if "reminder_id" not in new_reminder:
            payload = {"error": "New reminder must have a 'reminder_id'."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        data["reminders"][reminder_id] = new_reminder
        payload = {"success": "Reminder added."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddReminder",
                "description": "Add a new reminder.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "new_reminder": {
                            "type": "object",
                            "description": "A dictionary representing the new reminder.",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["new_reminder"],
                    "additionalProperties": False,
                },
            },
        }


class UpdateReminder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], reminder_id: str, update_fields: dict[str, Any]
    ) -> str:
        reminders = data.get("reminders", {}).values()
        reminder_found = False
        for reminder in reminders.values():
            if reminder.get("reminder_id") == reminder_id:
                reminder_found = True
                reminder.update(update_fields)
                break

        if not reminder_found:
            payload = {"error": f"Reminder with ID '{reminder_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"success": f"Reminder '{reminder_id}' updated."}
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReminder",
                "description": "Update an existing reminder.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The ID of the reminder to update.",
                        },
                        "update_fields": {
                            "type": "object",
                            "description": "Fields to update in the reminder.",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["reminder_id", "update_fields"],
                    "additionalProperties": False,
                },
            },
        }


class DeleteReminder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], reminder_id: str) -> str:
        reminders = data.get("reminders", {}).values()
        initial_len = len(reminders)
        reminders[:] = [r for r in reminders.values() if r.get("reminder_id") != reminder_id]

        if len(reminders) == initial_len:
            payload = {"error": f"Reminder with ID '{reminder_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"success": f"Reminder '{reminder_id}' deleted."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteReminder",
                "description": "Delete a reminder.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The ID of the reminder to delete.",
                        }
                    },
                    "required": ["reminder_id"],
                    "additionalProperties": False,
                },
            },
        }


class GetCustomList(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], list_id: str | None = None, list_name: str | None = None
    ) -> str:
        custom_lists = data.get("custom_lists", {}).values()
        if not list_id and not list_name:
            payload = custom_lists
            out = json.dumps(payload, indent=2)
            return out

        result = []
        for l in custom_lists.values():
            if list_id and l.get("list_id") == list_id:
                result.append(l)
            elif list_name and l.get("name") == list_name:
                result.append(l)
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomList",
                "description": "Get one or more custom lists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The ID of the list to retrieve.",
                        },
                        "list_name": {
                            "type": "string",
                            "description": "The name of the list to retrieve.",
                        },
                    },
                    "additionalProperties": False,
                },
            },
        }


class CreateCustomList(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], new_list: dict[str, Any]) -> str:
        custom_lists = data.get("custom_lists", {}).values()
        if "list_id" not in new_list:
            payload = {"error": "New list must have 'list_id' and 'name'."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        data["custom_lists"][new_list["custom_list_id"]] = new_list
        payload = {"success": "Custom list created."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCustomList",
                "description": "Create a new custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "new_list": {
                            "type": "object",
                            "description": "A dictionary representing the new custom list.",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["new_list"],
                    "additionalProperties": False,
                },
            },
        }


class ManageCustomListItems(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], list_id: str, item: dict[str, Any], action: str
    ) -> str:
        custom_lists = data.get("custom_lists", {}).values()
        list_found = False
        for l in custom_lists.values():
            if l.get("list_id") == list_id:
                list_found = True
                items = l.setdefault("items", [])
                if action == "add":
                    items.append(item)
                    payload = {"success": f"Item added to list '{list_id}'."}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                elif action == "remove":
                    initial_len = len(items)
                    items[:] = [i for i in items.values() if i.get("item") != item.get("item")]
                    if len(items) < initial_len:
                        payload = {"success": f"Item removed from list '{list_id}'."}
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                    else:
                        payload = {"error": f"Item not found in list '{list_id}'."}
                        out = json.dumps(
                            payload, indent=2
                        )
                        return out
                else:
                    payload = {"error": "Invalid action. Use 'add' or 'remove'."}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out

        if not list_found:
            payload = {"error": f"List with ID '{list_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"error": "An unexpected error occurred."}
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageCustomListItems",
                "description": "Add or remove items from a custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The ID of the list to modify.",
                        },
                        "item": {
                            "type": "object",
                            "description": "The item to add or remove. For removal, only the 'item' name is needed.",
                            "properties": {
                                "item": {"type": "string"},
                                "quantity": {"type": "integer"},
                            },
                            "required": ["item"],
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "remove"],
                            "description": "The action to perform.",
                        },
                    },
                    "required": ["list_id", "item", "action"],
                    "additionalProperties": False,
                },
            },
        }


class DeleteCustomList(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], list_id: str) -> str:
        custom_lists = data.get("custom_lists", {}).values()
        initial_len = len(custom_lists)
        custom_lists[:] = [l for l in custom_lists.values() if l.get("list_id") != list_id]

        if len(custom_lists) == initial_len:
            payload = {"error": f"Custom list with ID '{list_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"success": f"Custom list '{list_id}' deleted."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteCustomList",
                "description": "Delete a custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The ID of the custom list to delete.",
                        }
                    },
                    "required": ["list_id"],
                    "additionalProperties": False,
                },
            },
        }


class GetSensorData(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sensor_ids: list[str] | None = None) -> str:
        sensors = data.get("sensors", {}).values()
        if sensor_ids:
            result = [s for s in sensors.values() if s.get("id") in sensor_ids]
        else:
            result = sensors
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSensorData",
                "description": "Get data from one or more sensors. Sensor state is read-only.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of sensor IDs to retrieve data from. If empty, returns data for all sensors.",
                        }
                    },
                    "additionalProperties": False,
                },
            },
        }


class GetMemberInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], member_ids: list[str] | None = None) -> str:
        members = data.get("members", {}).values()
        if member_ids:
            result = [m for m in members.values() if m.get("id") in member_ids]
        else:
            result = members
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getMemberInfo",
                "description": "Get information about one or more household members.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of member IDs to retrieve. If empty, all members will be returned.",
                        }
                    },
                    "additionalProperties": False,
                },
            },
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
