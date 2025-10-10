import json
from typing import Any, Dict, List, Optional
from domains.dto import Tool

# Devices APIs
class GetDeviceByIdOrFilter(Tool):
    """Retrieve device(s) by id or filter."""
    @staticmethod
    def invoke(data: Dict[str, Any], devices: str = "", filters: Optional[Dict[str, Any]] = None) -> str:
        device_list = data.get('devices', [])
        if devices:
            result = [d for d in device_list if d.get("id") == devices]
        elif filters:
            result = [d for d in device_list if all(d.get(k) == v for k, v in filters.items())]
        else:
            return json.dumps({"error": "Either 'devices' (id) or 'filters' must be provided"}, indent=2)
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_device_by_id_or_filter",
                "description": "Retrieve device(s) by id or filter. If 'devices' is provided, returns the device with that id. If 'filters' is provided, returns all devices matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "devices": {
                            "type": "string",
                            "description": "Device id to retrieve (optional if using filters)"
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter devices (optional if using devices)",
                            "additionalProperties": True
                        }
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
class GetSensorByIdOrFilter(Tool):
    """Retrieve sensor(s) by id or filter."""
    @staticmethod
    def invoke(data: Dict[str, Any], sensor: str = "", filters: Optional[Dict[str, Any]] = None) -> str:
        sensor_list = data.get('sensors', [])
        if sensor:
            result = [d for d in sensor_list if d.get("id") == sensor]
        elif filters:
            result = [d for d in sensor_list if all(d.get(k) == v for k, v in filters.items())]
        else:
            return json.dumps({"error": "Either 'devices' (id) or 'filters' must be provided"}, indent=2)
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_sensor_by_id_or_filter",
                "description": "Retrieve device(s) by id or filter. If 'devices' is provided, returns the device with that id. If 'filters' is provided, returns all devices matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor": {
                            "type": "string",
                            "description": "Sensor id to retrieve (optional if using filters)"
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter devices (optional if using devices)",
                            "additionalProperties": True
                        }
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

class AddDeviceToDatabase(Tool):
    """Add a new device."""
    @staticmethod
    def invoke(data: Dict[str, Any], device: Optional[Dict[str, Any]] = None) -> str:
        if not device:
            return json.dumps({"error": "'device' parameter is required"}, indent=2)
        device_list = data.get('devices', [])
        if any(d["id"] == device.get("id") for d in device_list):
            return json.dumps({"error": "Device with this id already exists"}, indent=2)
        device_list.append(device)
        return json.dumps({"success": "Device added", "device": device, "devices": device_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_device_to_database",
                "description": "Add a new device. All fields must be provided in the 'device' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device": {
                            "type": "object",
                            "description": "The full device object to add (must include id, type, name, location, vendor, model, firmware_version, state_params, state, scheduled_updates)",
                            "additionalProperties": True
                        }
                    },
                    "required": ["device"],
                    "additionalProperties": False
                }
            }
        }
class AddSensorToDatabase(Tool):
    """Add a new device."""
    @staticmethod
    def invoke(data: Dict[str, Any], sensor: Optional[Dict[str, Any]] = None) -> str:
        if not sensor:
            return json.dumps({"error": "'sensor' parameter is required"}, indent=2)
        sensors_list = data.get('sensors', [])
        if any(d["id"] == sensor.get("id") for d in sensors_list):
            return json.dumps({"error": "Sensor with this id already exists"}, indent=2)
        sensors_list.append(sensor)
        return json.dumps({"success": "Sensor added", "sensor": sensor, "sensors": sensors_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_sensor_to_database",
                "description": "Add a new sensor. All fields must be provided in the 'device' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor": {
                            "type": "object",
                            "description": "The full sensor object to add (must include id, type, name, location, vendor, model, firmware_version, state_params, state, scheduled_updates)",
                            "additionalProperties": True
                        }
                    },
                    "required": ["sensor"],
                    "additionalProperties": False
                }
            }
        }
class UpdateDeviceInDatabase(Tool):
    """Update any field of a device."""
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str = "", updates: Optional[Dict[str, Any]] = None) -> str:
        if not device_id or not updates:
            return json.dumps({"error": "'device_id' and 'updates' parameters are required"}, indent=2)
        device_list = data.get('devices', [])
        found = False
        for d in device_list:
            if d["id"] == device_id:
                for k, v in updates.items():
                    if k in d:
                        d[k] = v
                    elif k in d.get("state", {}):
                        d["state"][k] = v
                    else:
                        d[k] = v
                found = True
                break
        if not found:
            return json.dumps({"error": "Device not found"}, indent=2)
        return json.dumps({"success": "Device updated", "device_id": device_id, "updates": updates, "devices": device_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_device_in_database",
                "description": "Update any field of a device by id. Updates can be for top-level or nested fields (e.g., state).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The id of the device to update."
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update. For nested fields like state, use the field name directly.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["device_id", "updates"],
                    "additionalProperties": False
                }
            }
        }

class DeleteDeviceFromDatabase(Tool):
    """Remove a device by id."""
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str = "") -> str:
        if not device_id:
            return json.dumps({"error": "'device_id' parameter is required"}, indent=2)
        device_list = data.get('devices', [])
        new_list = [d for d in device_list if d["id"] != device_id]
        if len(new_list) == len(device_list):
            return json.dumps({"error": "Device not found"}, indent=2)
        return json.dumps({"success": "Device deleted", "device_id": device_id, "devices": new_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_device_from_database",
                "description": "Remove a device by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The id of the device to delete."
                        }
                    },
                    "required": ["device_id"],
                    "additionalProperties": False
                }
            }
        }

class ListDevicesInDatabase(Tool):
    """List all devices, with optional filters."""
    @staticmethod
    def invoke(data: Dict[str, Any], filters: Optional[Dict[str, Any]] = None) -> str:
        device_list = data.get('devices', [])
        if filters:
            result = [d for d in device_list if all(d.get(k) == v for k, v in filters.items())]
        else:
            result = device_list
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_devices_in_database",
                "description": "List all devices, or filter by any field.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter devices (optional)",
                            "additionalProperties": True
                        }
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

# Rooms API (merged CRUD)
class ManageRoomInDatabase(Tool):
    """Unified CRUD for rooms: get, update device assignments/settings, but not add/remove rooms."""
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        action: str = "get",
        room_id: str = "",
        device_id: str = "",
        device_settings: Optional[Dict[str, Any]] = None,
        filters: Optional[Dict[str, Any]] = None
    ) -> str:
        rooms = data.get('rooms', [])
        if action == "get":
            if room_id:
                result = [r for r in rooms if r.get("id") == room_id]
            elif filters:
                result = [r for r in rooms if all(r.get(k) == v for k, v in filters.items())]
            else:
                result = rooms
            return json.dumps(result, indent=2)
        elif action == "add_device_to_database":
            if not room_id or not device_id:
                return json.dumps({"error": "'room_id' and 'device_id' are required for add_device"}, indent=2)
            found = False
            for r in rooms:
                if r["id"] == room_id:
                    if device_id not in r["devices"]:
                        r["devices"].append(device_id)
                    found = True
                    break
            if not found:
                return json.dumps({"error": "Room not found"}, indent=2)
            return json.dumps({"success": "Device added to room", "room_id": room_id, "device_id": device_id, "rooms": rooms}, indent=2)
        elif action == "remove_device":
            if not room_id or not device_id:
                return json.dumps({"error": "'room_id' and 'device_id' are required for remove_device"}, indent=2)
            found = False
            for r in rooms:
                if r["id"] == room_id:
                    if device_id in r["devices"]:
                        r["devices"].remove(device_id)
                    found = True
                    break
            if not found:
                return json.dumps({"error": "Room not found"}, indent=2)
            return json.dumps({"success": "Device removed from room", "room_id": room_id, "device_id": device_id, "rooms": rooms}, indent=2)
        elif action == "update_device_settings":
            if not room_id or not device_id or not device_settings:
                return json.dumps({"error": "'room_id', 'device_id', and 'device_settings' are required for update_device_settings"}, indent=2)
            found = False
            for r in rooms:
                if r["id"] == room_id:
                    if device_id in r["devices"]:
                        # This is a placeholder; actual device settings per room would need a schema
                        if "device_settings" not in r:
                            r["device_settings"] = {}
                        r["device_settings"][device_id] = device_settings
                        found = True
                        break
            if not found:
                return json.dumps({"error": "Room or device not found in room"}, indent=2)
            return json.dumps({"success": "Device settings updated in room", "room_id": room_id, "device_id": device_id, "device_settings": device_settings, "rooms": rooms}, indent=2)
        else:
            return json.dumps({"error": f"Unknown action: {action}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_room_in_database",
                "description": "Get room info, add/remove device to/from room, or update device-specific settings in a room. Cannot add/remove rooms themselves.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "description": "Action to perform: get, add_device, remove_device, update_device_settings"
                        },
                        "room_id": {
                            "type": "string",
                            "description": "Room id to operate on (required for all actions except get with filters)"
                        },
                        "device_id": {
                            "type": "string",
                            "description": "Device id to add/remove/update in the room (required for add_device, remove_device, update_device_settings)"
                        },
                        "device_settings": {
                            "type": "object",
                            "description": "Settings to update for the device in the room (required for update_device_settings)",
                            "additionalProperties": True
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter rooms (optional for get)",
                            "additionalProperties": True
                        }
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }

# Scenes APIs
class GetSceneByIdOrFilter(Tool):
    """Retrieve scene(s) by id or filter."""
    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str = "", filters: Optional[Dict[str, Any]] = None) -> str:
        scenes = data.get('scenes', [])
        if scene_id:
            result = [s for s in scenes if s.get("id") == scene_id]
        elif filters:
            result = [s for s in scenes if all(s.get(k) == v for k, v in filters.items())]
        else:
            return json.dumps({"error": "Either 'scene_id' or 'filters' must be provided"}, indent=2)
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_scene_by_id_or_filter",
                "description": "Retrieve scene(s) by id or filter. If 'scene_id' is provided, returns the scene with that id. If 'filters' is provided, returns all scenes matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "Scene id to retrieve (optional if using filters)"
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter scenes (optional if using scene_id)",
                            "additionalProperties": True
                        }
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

class AddSceneToDatabase(Tool):
    """Add a new scene."""
    @staticmethod
    def invoke(data: Dict[str, Any], scene: Optional[Dict[str, Any]] = None, threshold: Optional[Dict[str, Any]] = None) -> str:
        if not scene:
            return json.dumps({"error": "'scene' parameter is required"}, indent=2)
        scenes = data.get('scenes', [])
        if any(s["id"] == scene.get("id") for s in scenes):
            return json.dumps({"error": "Scene with this id already exists"}, indent=2)
        if not threshold:
            scenes.append(scene)
        else:
            for sensor in data.get('sensors', []):
                if sensor.get("id") == threshold.get("sensor_id"):
                    for param, limit in threshold.items():
                        current_value = sensor['state'].get(param)
                        if (limit.get('operator') == 'gt' and current_value > limit.get('value')) or (limit.get('operator') == 'lt' and current_value < limit.get('value')):
                            scenes.append(scene)
        return json.dumps({"success": "Scene added", "scene": scene, "scenes": scenes}, indent=2)




    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_scene_to_database",
                "description": "Add a new scene. All fields must be provided in the 'scene' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene": {
                            "type": "object",
                            "description": "The full scene object to add (must include id, name, description, actions, scheduled_runs)",
                            "additionalProperties": True
                        }
                    },
                    "required": ["scene"],
                    "additionalProperties": False
                }
            }
        }

class UpdateSceneInDatabase(Tool):
    """Update any field of a scene."""
    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str = "", updates: Optional[Dict[str, Any]] = None) -> str:
        if not scene_id or not updates:
            return json.dumps({"error": "'scene_id' and 'updates' parameters are required"}, indent=2)
        scenes = data.get('scenes', [])
        found = False
        for s in scenes:
            if s["id"] == scene_id:
                for k, v in updates.items():
                    if k == "actions":
                        s["actions"] + v
                    else:
                        s[k] = v
                found = True
                break
        if not found:
            return json.dumps({"error": "Scene not found"}, indent=2)
        return json.dumps({"success": "Scene updated", "scene_id": scene_id, "updates": updates, "scenes": scenes}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_scene_in_database",
                "description": "Update any field of a scene by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The id of the scene to update."
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["scene_id", "updates"],
                    "additionalProperties": False
                }
            }
        }

class DeleteSceneFromDatabase(Tool):
    """Remove a scene by id."""
    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str = "") -> str:
        if not scene_id:
            return json.dumps({"error": "'scene_id' parameter is required"}, indent=2)
        scenes = data.get('scenes', [])
        new_list = [s for s in scenes if s["id"] != scene_id]
        if len(new_list) == len(scenes):
            return json.dumps({"error": "Scene not found"}, indent=2)
        return json.dumps({"success": "Scene deleted", "scene_id": scene_id, "scenes": new_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_scene_from_database",
                "description": "Remove a scene by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The id of the scene to delete."
                        }
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False
                }
            }
        }

class ListScenesInDatabase(Tool):
    """List all scenes, with optional filters."""
    @staticmethod
    def invoke(data: Dict[str, Any], filters: Optional[Dict[str, Any]] = None) -> str:
        scenes = data.get('scenes', [])
        if filters:
            result = [s for s in scenes if all(s.get(k) == v for k, v in filters.items())]
        else:
            result = scenes
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_scenes_in_database",
                "description": "List all scenes, or filter by any field.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter scenes (optional)",
                            "additionalProperties": True
                        }
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

# Custom Lists APIs
class GetCustomListByIdOrFilter(Tool):
    """Retrieve a custom list by name/id."""
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: str = "", name: str = "", filters: Optional[Dict[str, Any]] = None) -> str:
        custom_lists = data.get('custom_lists', [])
        if list_id:
            result = [l for l in custom_lists if l.get("list_id") == list_id]
        elif name:
            result = [l for l in custom_lists if l.get("name") == name]
        elif filters:
            result = [l for l in custom_lists if all(l.get(k) == v for k, v in filters.items())]
        else:
            return json.dumps({"error": "Either 'list_id', 'name', or 'filters' must be provided"}, indent=2)
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_custom_list_by_filter_or_id",
                "description": "Retrieve a custom list by list_id, name, or filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "Custom list id to retrieve (optional if using name or filters)"
                        },
                        "name": {
                            "type": "string",
                            "description": "Custom list name to retrieve (optional if using list_id or filters)"
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter custom lists (optional if using list_id or name)",
                            "additionalProperties": True
                        }
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

class AddCustomListToDatabase(Tool):
    """Add a new custom list."""
    @staticmethod
    def invoke(data: Dict[str, Any], custom_list: Optional[Dict[str, Any]] = None) -> str:
        if not custom_list:
            return json.dumps({"error": "'custom_list' parameter is required"}, indent=2)
        custom_lists = data.get('custom_lists', [])
        if any(l["list_id"] == custom_list.get("list_id") for l in custom_lists):
            return json.dumps({"error": "Custom list with this id already exists"}, indent=2)
        custom_lists.append(custom_list)
        return json.dumps({"success": "Custom list added", "custom_list": custom_list, "custom_lists": custom_lists}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_custom_list_to_database",
                "description": "Add a new custom list. All fields must be provided in the 'custom_list' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "custom_list": {
                            "type": "object",
                            "description": "The full custom list object to add (must include list_id, name, created_at, updated_at, tags, items)",
                            "additionalProperties": True
                        }
                    },
                    "required": ["custom_list"],
                    "additionalProperties": False
                }
            }
        }

class UpdateCustomListInDatabase(Tool):
    """Update items in a custom list."""
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: str = "", updates: Optional[Dict[str, Any]] = None) -> str:
        if not list_id or not updates:
            return json.dumps({"error": "'list_id' and 'updates' parameters are required"}, indent=2)
        custom_lists = data.get('custom_lists', [])
        found = False
        for l in custom_lists:
            if l["list_id"] == list_id:
                for k, v in updates.items():
                    l[k] = v
                found = True
                break
        if not found:
            return json.dumps({"error": "Custom list not found"}, indent=2)
        return json.dumps({"success": "Custom list updated", "list_id": list_id, "updates": updates, "custom_lists": custom_lists}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_custom_list_in_database",
                "description": "Update any field of a custom list by list_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The id of the custom list to update."
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["list_id", "updates"],
                    "additionalProperties": False
                }
            }
        }

class DeleteCustomListFromDatabase(Tool):
    """Remove a custom list by name/id."""
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: str = "") -> str:
        if not list_id:
            return json.dumps({"error": "'list_id' parameter is required"}, indent=2)
        custom_lists = data.get('custom_lists', [])
        new_list = [l for l in custom_lists if l["list_id"] != list_id]
        if len(new_list) == len(custom_lists):
            return json.dumps({"error": "Custom list not found"}, indent=2)
        return json.dumps({"success": "Custom list deleted", "list_id": list_id, "custom_lists": new_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_custom_list_from_database",
                "description": "Remove a custom list by list_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The id of the custom list to delete."
                        }
                    },
                    "required": ["list_id"],
                    "additionalProperties": False
                }
            }
        }

# Reminders APIs
class GetReminderByIdOrFilter(Tool):
    """Retrieve reminder(s) by id or filter."""
    @staticmethod
    def invoke(data: Dict[str, Any], reminder_id: str = "", filters: Optional[Dict[str, Any]] = None) -> str:
        reminders = data.get('reminders', [])
        if reminder_id:
            result = [r for r in reminders if r.get("reminder_id") == reminder_id]
        elif filters:
            result = [r for r in reminders if all(r.get(k) == v for k, v in filters.items())]
        else:
            return json.dumps({"error": "Either 'reminder_id' or 'filters' must be provided"}, indent=2)
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_reminder_by_id_or_filter",
                "description": "Retrieve reminder(s) by id or filter. If 'reminder_id' is provided, returns the reminder with that id. If 'filters' is provided, returns all reminders matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "Reminder id to retrieve (optional if using filters)"
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter reminders (optional if using reminder_id)",
                            "additionalProperties": True
                        }
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

class AddReminderToDatabase(Tool):
    """Add a new reminder."""
    @staticmethod
    def invoke(data: Dict[str, Any], reminder: Optional[Dict[str, Any]] = None, threshold: Dict[str, Any] = None) -> str:
        if not reminder:
            return json.dumps({"error": "'reminder' parameter is required"}, indent=2)
        reminders = data.get('reminders', [])
        if any(r["reminder_id"] == reminder.get("reminder_id") for r in reminders):
            return json.dumps({"error": "Reminder with this id already exists"}, indent=2)
        reminders.append(reminder)
        return json.dumps({"success": "Reminder added", "reminder": reminder, "reminders": reminders}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_reminder_to_database",
                "description": "Add a new reminder. All fields must be provided in the 'reminder' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder": {
                            "type": "object",
                            "description": "The full reminder object to add (must include reminder_id, name, target, trigger, actions, meta, status, created_at, etc.)",
                            "additionalProperties": True
                        }
                    },
                    "required": ["reminder"],
                    "additionalProperties": False
                }
            }
        }

class UpdateReminderInDatabase(Tool):
    """Update any field of a reminder."""
    @staticmethod
    def invoke(data: Dict[str, Any], reminder_id: str = "", updates: Optional[Dict[str, Any]] = None) -> str:
        if not reminder_id or not updates:
            return json.dumps({"error": "'reminder_id' and 'updates' parameters are required"}, indent=2)
        reminders = data.get('reminders', [])
        found = False
        for r in reminders:
            if r["reminder_id"] == reminder_id:
                for k, v in updates.items():
                    r[k] = v
                found = True
                break
        if not found:
            return json.dumps({"error": "Reminder not found"}, indent=2)
        return json.dumps({"success": "Reminder updated", "reminder_id": reminder_id, "updates": updates, "reminders": reminders}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_reminder_in_database",
                "description": "Update any field of a reminder by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The id of the reminder to update."
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["reminder_id", "updates"],
                    "additionalProperties": False
                }
            }
        }

class DeleteReminderFromDatabase(Tool):
    """Remove a reminder by id."""
    @staticmethod
    def invoke(data: Dict[str, Any], reminder_id: str = "") -> str:
        if not reminder_id:
            return json.dumps({"error": "'reminder_id' parameter is required"}, indent=2)
        reminders = data.get('reminders', [])
        new_list = [r for r in reminders if r["reminder_id"] != reminder_id]
        if len(new_list) == len(reminders):
            return json.dumps({"error": "Reminder not found"}, indent=2)
        return json.dumps({"success": "Reminder deleted", "reminder_id": reminder_id, "reminders": new_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_reminder_from_database",
                "description": "Remove a reminder by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The id of the reminder to delete."
                        }
                    },
                    "required": ["reminder_id"],
                    "additionalProperties": False
                }
            }
        }

# Members API (merged CRUD)
class ManageMemberInDatabase(Tool):
    """Unified CRUD for members: get, add, update, delete."""
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        action: str = "get",
        member_id: str = "",
        member: Optional[Dict[str, Any]] = None,
        updates: Optional[Dict[str, Any]] = None,
        filters: Optional[Dict[str, Any]] = None
    ) -> str:
        members = data.get('members', [])
        if action == "get":
            if member_id:
                result = [m for m in members if m.get("id") == member_id]
            elif filters:
                result = [m for m in members if all(m.get(k) == v for k, v in filters.items())]
            else:
                result = members
            return json.dumps(result, indent=2)
        elif action == "add":
            if not member:
                return json.dumps({"error": "'member' parameter is required for add"}, indent=2)
            if any(m["id"] == member.get("id") for m in members):
                return json.dumps({"error": "Member with this id already exists"}, indent=2)
            members.append(member)
            return json.dumps({"success": "Member added", "member": member, "members": members}, indent=2)
        elif action == "update":
            if not member_id or not updates:
                return json.dumps({"error": "'member_id' and 'updates' parameters are required for update"}, indent=2)
            found = False
            for m in members:
                if m["id"] == member_id:
                    for k, v in updates.items():
                        m[k] = v
                    found = True
                    break
            if not found:
                return json.dumps({"error": "Member not found"}, indent=2)
            return json.dumps({"success": "Member updated", "member_id": member_id, "updates": updates, "members": members}, indent=2)
        elif action == "delete":
            if not member_id:
                return json.dumps({"error": "'member_id' parameter is required for delete"}, indent=2)
            new_list = [m for m in members if m["id"] != member_id]
            if len(new_list) == len(members):
                return json.dumps({"error": "Member not found"}, indent=2)
            return json.dumps({"success": "Member deleted", "member_id": member_id, "members": new_list}, indent=2)
        else:
            return json.dumps({"error": f"Unknown action: {action}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_member_in_database",
                "description": "Get member info, add, update, or delete a member.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "description": "Action to perform: get, add, update, delete"
                        },
                        "member_id": {
                            "type": "string",
                            "description": "Member id to operate on (required for get, update, delete)"
                        },
                        "member": {
                            "type": "object",
                            "description": "The full member object to add (required for add)",
                            "additionalProperties": True
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update (required for update)",
                            "additionalProperties": True
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter members (optional for get)",
                            "additionalProperties": True
                        }
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }

TOOLS = [
    GetDeviceByIdOrFilter(),
    AddDeviceToDatabase(),
    GetSensorByIdOrFilter(),
    AddSensorToDatabase(),
    UpdateDeviceInDatabase(),
    DeleteDeviceFromDatabase(),
    ListDevicesInDatabase(),
    ManageRoomInDatabase(),
    GetSceneByIdOrFilter(),
    AddSceneToDatabase(),
    UpdateSceneInDatabase(),
    DeleteSceneFromDatabase(),
    ListScenesInDatabase(),
    GetCustomListByIdOrFilter(),
    AddCustomListToDatabase(),
    UpdateCustomListInDatabase(),
    DeleteCustomListFromDatabase(),
    GetReminderByIdOrFilter(),
    AddReminderToDatabase(),
    UpdateReminderInDatabase(),
    DeleteReminderFromDatabase(),
    ManageMemberInDatabase(),
]
