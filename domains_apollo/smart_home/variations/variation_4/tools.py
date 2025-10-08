import json
from typing import Any

from domains.dto import Tool


#APIs for Devices
class GetDeviceByIdOrFilter(Tool):
    """Fetch device(s) using id or filters."""

    @staticmethod
    def invoke(
        data: dict[str, Any], devices: str = "", filters: dict[str, Any] | None = None
    ) -> str:
        device_list = data.get("devices", [])
        if devices:
            result = [d for d in device_list if d.get("id") == devices]
        elif filters:
            result = [
                d for d in device_list if all(d.get(k) == v for k, v in filters.items())
            ]
        else:
            payload = {"error": "Either 'devices' (id) or 'filters' must be provided"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDeviceByIdOrFilter",
                "description": "Retrieve device(s) by id or filter. If 'devices' is provided, returns the device with that id. If 'filters' is provided, returns all devices matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "devices": {
                            "type": "string",
                            "description": "Device id to retrieve (optional if using filters)",
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter devices (optional if using devices)",
                            "additionalProperties": True,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class GetSensorByIdOrFilter(Tool):
    """Fetch sensor(s) using id or filters."""

    @staticmethod
    def invoke(
        data: dict[str, Any], sensor: str = "", filters: dict[str, Any] | None = None
    ) -> str:
        sensor_list = data.get("sensors", [])
        if sensor:
            result = [d for d in sensor_list if d.get("id") == sensor]
        elif filters:
            result = [
                d for d in sensor_list if all(d.get(k) == v for k, v in filters.items())
            ]
        else:
            payload = {"error": "Either 'devices' (id) or 'filters' must be provided"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSensorByIdOrFilter",
                "description": "Retrieve device(s) by id or filter. If 'devices' is provided, returns the device with that id. If 'filters' is provided, returns all devices matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor": {
                            "type": "string",
                            "description": "Sensor id to retrieve (optional if using filters)",
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter devices (optional if using devices)",
                            "additionalProperties": True,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class AddDeviceToDatabase(Tool):
    """Introduce a new device."""

    @staticmethod
    def invoke(data: dict[str, Any], device: dict[str, Any] | None = None,
    new_device: Any = None,
    ) -> str:
        if not device:
            payload = {"error": "'device' parameter is required"}
            out = json.dumps(payload, indent=2)
            return out
        device_list = data.get("devices", [])
        if any(d["id"] == device.get("id") for d in device_list):
            payload = {"error": "Device with this id already exists"}
            out = json.dumps(payload, indent=2)
            return out
        device_list.append(device)
        payload = {"success": "Device added", "device": device, "devices": device_list}
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddDeviceToDatabase",
                "description": "Add a new device. All fields must be provided in the 'device' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device": {
                            "type": "object",
                            "description": "The full device object to add (must include id, type, name, location, vendor, model, firmware_version, state_params, state, scheduled_updates)",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["device"],
                    "additionalProperties": False,
                },
            },
        }


class AddSensorToDatabase(Tool):
    """Introduce a new device."""

    @staticmethod
    def invoke(data: dict[str, Any], sensor: dict[str, Any] | None = None) -> str:
        if not sensor:
            payload = {"error": "'sensor' parameter is required"}
            out = json.dumps(payload, indent=2)
            return out
        sensors_list = data.get("sensors", [])
        if any(d["id"] == sensor.get("id") for d in sensors_list):
            payload = {"error": "Sensor with this id already exists"}
            out = json.dumps(payload, indent=2)
            return out
        sensors_list.append(sensor)
        payload = {"success": "Sensor added", "sensor": sensor, "sensors": sensors_list}
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddSensorToDatabase",
                "description": "Add a new sensor. All fields must be provided in the 'device' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor": {
                            "type": "object",
                            "description": "The full sensor object to add (must include id, type, name, location, vendor, model, firmware_version, state_params, state, scheduled_updates)",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["sensor"],
                    "additionalProperties": False,
                },
            },
        }


class UpdateDeviceInDatabase(Tool):
    """Modify any attribute of a device."""

    @staticmethod
    def invoke(
        data: dict[str, Any], device_id: str = "", updates: dict[str, Any] | None = None
    ) -> str:
        if not device_id or not updates:
            payload = {"error": "'device_id' and 'updates' parameters are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        device_list = data.get("devices", [])
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
            payload = {"error": "Device not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {
                "success": "Device updated",
                "device_id": device_id,
                "updates": updates,
                "devices": device_list,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateDeviceInDatabase",
                "description": "Update any field of a device by id. Updates can be for top-level or nested fields (e.g., state).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The id of the device to update.",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update. For nested fields like state, use the field name directly.",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["device_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }


class DeleteDeviceFromDatabase(Tool):
    """Delete a device using its id."""

    @staticmethod
    def invoke(data: dict[str, Any], device_id: str = "") -> str:
        if not device_id:
            payload = {"error": "'device_id' parameter is required"}
            out = json.dumps(payload, indent=2)
            return out
        device_list = data.get("devices", [])
        new_list = [d for d in device_list if d["id"] != device_id]
        if len(new_list) == len(device_list):
            payload = {"error": "Device not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"success": "Device deleted", "device_id": device_id, "devices": new_list}
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteDeviceFromDatabase",
                "description": "Remove a device by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The id of the device to delete.",
                        }
                    },
                    "required": ["device_id"],
                    "additionalProperties": False,
                },
            },
        }


class ListDevicesInDatabase(Tool):
    """Display all devices, with optional filtering."""

    @staticmethod
    def invoke(data: dict[str, Any], filters: dict[str, Any] | None = None) -> str:
        device_list = data.get("devices", [])
        if filters:
            result = [
                d for d in device_list if all(d.get(k) == v for k, v in filters.items())
            ]
        else:
            result = device_list
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listDevicesInDatabase",
                "description": "List all devices, or filter by any field.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter devices (optional)",
                            "additionalProperties": True,
                        }
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


#Rooms API (consolidated CRUD)
class ManageRoomInDatabase(Tool):
    """Consolidated CRUD for rooms: retrieve and modify device assignments/settings, but cannot add or remove rooms."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        action: str = "get",
        room_id: str = "",
        device_id: str = "",
        device_settings: dict[str, Any] | None = None,
        filters: dict[str, Any] | None = None
    ) -> str:
        rooms = data.get("rooms", [])
        if action == "get":
            if room_id:
                result = [r for r in rooms if r.get("id") == room_id]
            elif filters:
                result = [
                    r for r in rooms if all(r.get(k) == v for k, v in filters.items())
                ]
            else:
                result = rooms
            payload = result
            out = json.dumps(payload, indent=2)
            return out
        elif action == "AddDeviceToDatabase":
            if not room_id or not device_id:
                payload = {"error": "'room_id' and 'device_id' are required for add_device"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            found = False
            for r in rooms:
                if r["id"] == room_id:
                    if device_id not in r["devices"]:
                        r["devices"].append(device_id)
                    found = True
                    break
            if not found:
                payload = {"error": "Room not found"}
                out = json.dumps(payload, indent=2)
                return out
            payload = {
                    "success": "Device added to room",
                    "room_id": room_id,
                    "device_id": device_id,
                    "rooms": rooms,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        elif action == "remove_device":
            if not room_id or not device_id:
                payload = {
                        "error": "'room_id' and 'device_id' are required for remove_device"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            found = False
            for r in rooms:
                if r["id"] == room_id:
                    if device_id in r["devices"]:
                        r["devices"].remove(device_id)
                    found = True
                    break
            if not found:
                payload = {"error": "Room not found"}
                out = json.dumps(payload, indent=2)
                return out
            payload = {
                    "success": "Device removed from room",
                    "room_id": room_id,
                    "device_id": device_id,
                    "rooms": rooms,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        elif action == "update_device_settings":
            if not room_id or not device_id or not device_settings:
                payload = {
                        "error": "'room_id', 'device_id', and 'device_settings' are required for update_device_settings"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            found = False
            for r in rooms:
                if r["id"] == room_id:
                    if device_id in r["devices"]:
                        # This serves as a placeholder; real device configurations for each room will require a schema
                        if "device_settings" not in r:
                            r["device_settings"] = {}
                        r["device_settings"][device_id] = device_settings
                        found = True
                        break
            if not found:
                payload = {"error": "Room or device not found in room"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            payload = {
                    "success": "Device settings updated in room",
                    "room_id": room_id,
                    "device_id": device_id,
                    "device_settings": device_settings,
                    "rooms": rooms,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {"error": f"Unknown action: {action}"}
            out = json.dumps(payload, indent=2)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageRoomInDatabase",
                "description": "Get room info, add/remove device to/from room, or update device-specific settings in a room. Cannot add/remove rooms themselves.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "description": "Action to perform: get, add_device, remove_device, update_device_settings",
                        },
                        "room_id": {
                            "type": "string",
                            "description": "Room id to operate on (required for all actions except get with filters)",
                        },
                        "device_id": {
                            "type": "string",
                            "description": "Device id to add/remove/update in the room (required for add_device, remove_device, update_device_settings)",
                        },
                        "device_settings": {
                            "type": "object",
                            "description": "Settings to update for the device in the room (required for update_device_settings)",
                            "additionalProperties": True,
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter rooms (optional for get)",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }


#APIs for Scenes
class GetSceneByIdOrFilter(Tool):
    """Fetch scene(s) using id or filters."""

    @staticmethod
    def invoke(
        data: dict[str, Any], scene_id: str = "", filters: dict[str, Any] | None = None
    ) -> str:
        scenes = data.get("scenes", [])
        if scene_id:
            result = [s for s in scenes if s.get("id") == scene_id]
        elif filters:
            result = [
                s for s in scenes if all(s.get(k) == v for k, v in filters.items())
            ]
        else:
            payload = {"error": "Either 'scene_id' or 'filters' must be provided"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSceneByIdOrFilter",
                "description": "Retrieve scene(s) by id or filter. If 'scene_id' is provided, returns the scene with that id. If 'filters' is provided, returns all scenes matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "Scene id to retrieve (optional if using filters)",
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter scenes (optional if using scene_id)",
                            "additionalProperties": True,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class AddSceneToDatabase(Tool):
    """Introduce a new scene."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        scene: dict[str, Any] | None = None,
        threshold: dict[str, Any] | None = None,
    ) -> str:
        if not scene:
            payload = {"error": "'scene' parameter is required"}
            out = json.dumps(payload, indent=2)
            return out
        scenes = data.get("scenes", [])
        if any(s["id"] == scene.get("id") for s in scenes):
            payload = {"error": "Scene with this id already exists"}
            out = json.dumps(payload, indent=2)
            return out
        if not threshold:
            scenes.append(scene)
        else:
            for sensor in data.get("sensors", []):
                if sensor.get("id") == threshold.get("sensor_id"):
                    for param, limit in threshold.items():
                        current_value = sensor["state"].get(param)
                        if (
                            limit.get("operator") == "gt"
                            and current_value > limit.get("value")
                        ) or (
                            limit.get("operator") == "lt"
                            and current_value < limit.get("value")
                        ):
                            scenes.append(scene)
        payload = {"success": "Scene added", "scene": scene, "scenes": scenes}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddSceneToDatabase",
                "description": "Add a new scene. All fields must be provided in the 'scene' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene": {
                            "type": "object",
                            "description": "The full scene object to add (must include id, name, description, actions, scheduled_runs)",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["scene"],
                    "additionalProperties": False,
                },
            },
        }


class UpdateSceneInDatabase(Tool):
    """Modify any attribute of a scene."""

    @staticmethod
    def invoke(
        data: dict[str, Any], scene_id: str = "", updates: dict[str, Any] | None = None
    ) -> str:
        if not scene_id or not updates:
            payload = {"error": "'scene_id' and 'updates' parameters are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        scenes = data.get("scenes", [])
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
            payload = {"error": "Scene not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {
                "success": "Scene updated",
                "scene_id": scene_id,
                "updates": updates,
                "scenes": scenes,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSceneInDatabase",
                "description": "Update any field of a scene by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The id of the scene to update.",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update.",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["scene_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }


class DeleteSceneFromDatabase(Tool):
    """Delete a scene using its id."""

    @staticmethod
    def invoke(data: dict[str, Any], scene_id: str = "") -> str:
        if not scene_id:
            payload = {"error": "'scene_id' parameter is required"}
            out = json.dumps(payload, indent=2)
            return out
        scenes = data.get("scenes", [])
        new_list = [s for s in scenes if s["id"] != scene_id]
        if len(new_list) == len(scenes):
            payload = {"error": "Scene not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"success": "Scene deleted", "scene_id": scene_id, "scenes": new_list}
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteSceneFromDatabase",
                "description": "Remove a scene by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The id of the scene to delete.",
                        }
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False,
                },
            },
        }


class ListScenesInDatabase(Tool):
    """Display all scenes, with optional filtering."""

    @staticmethod
    def invoke(data: dict[str, Any], filters: dict[str, Any] | None = None) -> str:
        scenes = data.get("scenes", [])
        if filters:
            result = [
                s for s in scenes if all(s.get(k) == v for k, v in filters.items())
            ]
        else:
            result = scenes
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listScenesInDatabase",
                "description": "List all scenes, or filter by any field.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter scenes (optional)",
                            "additionalProperties": True,
                        }
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


#APIs for Custom Lists
class GetCustomListByIdOrFilter(Tool):
    """Fetch a custom list using name or id."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        list_id: str = "",
        name: str = "",
        filters: dict[str, Any] | None = None
    ) -> str:
        custom_lists = data.get("custom_lists", [])
        if list_id:
            result = [l for l in custom_lists if l.get("list_id") == list_id]
        elif name:
            result = [l for l in custom_lists if l.get("name") == name]
        elif filters:
            result = [
                l
                for l in custom_lists
                if all(l.get(k) == v for k, v in filters.items())
            ]
        else:
            payload = {"error": "Either 'list_id', 'name', or 'filters' must be provided"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCustomListByFilterOrId",
                "description": "Retrieve a custom list by list_id, name, or filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "Custom list id to retrieve (optional if using name or filters)",
                        },
                        "name": {
                            "type": "string",
                            "description": "Custom list name to retrieve (optional if using list_id or filters)",
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter custom lists (optional if using list_id or name)",
                            "additionalProperties": True,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class AddCustomListToDatabase(Tool):
    """Introduce a new custom list."""

    @staticmethod
    def invoke(data: dict[str, Any], custom_list: dict[str, Any] | None = None) -> str:
        if not custom_list:
            payload = {"error": "'custom_list' parameter is required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        custom_lists = data.get("custom_lists", [])
        if any(l["list_id"] == custom_list.get("list_id") for l in custom_lists):
            payload = {"error": "Custom list with this id already exists"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        custom_lists.append(custom_list)
        payload = {
                "success": "Custom list added",
                "custom_list": custom_list,
                "custom_lists": custom_lists,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddCustomListToDatabase",
                "description": "Add a new custom list. All fields must be provided in the 'custom_list' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "custom_list": {
                            "type": "object",
                            "description": "The full custom list object to add (must include list_id, name, created_at, updated_at, tags, items)",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["custom_list"],
                    "additionalProperties": False,
                },
            },
        }


class UpdateCustomListInDatabase(Tool):
    """Modify items within a custom list."""

    @staticmethod
    def invoke(
        data: dict[str, Any], list_id: str = "", updates: dict[str, Any] | None = None
    ) -> str:
        if not list_id or not updates:
            payload = {"error": "'list_id' and 'updates' parameters are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        custom_lists = data.get("custom_lists", [])
        found = False
        for l in custom_lists:
            if l["list_id"] == list_id:
                for k, v in updates.items():
                    l[k] = v
                found = True
                break
        if not found:
            payload = {"error": "Custom list not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {
                "success": "Custom list updated",
                "list_id": list_id,
                "updates": updates,
                "custom_lists": custom_lists,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomListInDatabase",
                "description": "Update any field of a custom list by list_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The id of the custom list to update.",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update.",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["list_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }


class DeleteCustomListFromDatabase(Tool):
    """Delete a custom list using name or id."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: str = "") -> str:
        if not list_id:
            payload = {"error": "'list_id' parameter is required"}
            out = json.dumps(payload, indent=2)
            return out
        custom_lists = data.get("custom_lists", [])
        new_list = [l for l in custom_lists if l["list_id"] != list_id]
        if len(new_list) == len(custom_lists):
            payload = {"error": "Custom list not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {
                "success": "Custom list deleted",
                "list_id": list_id,
                "custom_lists": new_list,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteCustomListFromDatabase",
                "description": "Remove a custom list by list_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The id of the custom list to delete.",
                        }
                    },
                    "required": ["list_id"],
                    "additionalProperties": False,
                },
            },
        }


#APIs for Reminders
class GetReminderByIdOrFilter(Tool):
    """Fetch reminder(s) using id or filters."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reminder_id: str = "",
        filters: dict[str, Any] | None = None
    ) -> str:
        reminders = data.get("reminders", [])
        if reminder_id:
            result = [r for r in reminders if r.get("reminder_id") == reminder_id]
        elif filters:
            result = [
                r for r in reminders if all(r.get(k) == v for k, v in filters.items())
            ]
        else:
            payload = {"error": "Either 'reminder_id' or 'filters' must be provided"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getReminderByIdOrFilter",
                "description": "Retrieve reminder(s) by id or filter. If 'reminder_id' is provided, returns the reminder with that id. If 'filters' is provided, returns all reminders matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "Reminder id to retrieve (optional if using filters)",
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter reminders (optional if using reminder_id)",
                            "additionalProperties": True,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class AddReminderToDatabase(Tool):
    """Introduce a new reminder."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reminder: dict[str, Any] | None = None,
        threshold: dict[str, Any] = None,
    ) -> str:
        if not reminder:
            payload = {"error": "'reminder' parameter is required"}
            out = json.dumps(payload, indent=2)
            return out
        reminders = data.get("reminders", [])
        if any(r["reminder_id"] == reminder.get("reminder_id") for r in reminders):
            payload = {"error": "Reminder with this id already exists"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        reminders.append(reminder)
        payload = {"success": "Reminder added", "reminder": reminder, "reminders": reminders}
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddReminderToDatabase",
                "description": "Add a new reminder. All fields must be provided in the 'reminder' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder": {
                            "type": "object",
                            "description": "The full reminder object to add (must include reminder_id, name, target, trigger, actions, meta, status, created_at, etc.)",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["reminder"],
                    "additionalProperties": False,
                },
            },
        }


class UpdateReminderInDatabase(Tool):
    """Modify any attribute of a reminder."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reminder_id: str = "",
        updates: dict[str, Any] | None = None,
    ) -> str:
        if not reminder_id or not updates:
            payload = {"error": "'reminder_id' and 'updates' parameters are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        reminders = data.get("reminders", [])
        found = False
        for r in reminders:
            if r["reminder_id"] == reminder_id:
                for k, v in updates.items():
                    r[k] = v
                found = True
                break
        if not found:
            payload = {"error": "Reminder not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {
                "success": "Reminder updated",
                "reminder_id": reminder_id,
                "updates": updates,
                "reminders": reminders,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateReminderInDatabase",
                "description": "Update any field of a reminder by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The id of the reminder to update.",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update.",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["reminder_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }


class DeleteReminderFromDatabase(Tool):
    """Delete a reminder using its id."""

    @staticmethod
    def invoke(data: dict[str, Any], reminder_id: str = "") -> str:
        if not reminder_id:
            payload = {"error": "'reminder_id' parameter is required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        reminders = data.get("reminders", [])
        new_list = [r for r in reminders if r["reminder_id"] != reminder_id]
        if len(new_list) == len(reminders):
            payload = {"error": "Reminder not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {
                "success": "Reminder deleted",
                "reminder_id": reminder_id,
                "reminders": new_list,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteReminderFromDatabase",
                "description": "Remove a reminder by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The id of the reminder to delete.",
                        }
                    },
                    "required": ["reminder_id"],
                    "additionalProperties": False,
                },
            },
        }


#Members API (integrated CRUD)
class ManageMemberInDatabase(Tool):
    """Consolidated CRUD for members: retrieve, add, modify, and delete."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        action: str = "get",
        member_id: str = "",
        member: dict[str, Any] | None = None,
        updates: dict[str, Any] | None = None,
        filters: dict[str, Any] | None = None
    ) -> str:
        members = data.get("members", [])
        if action == "get":
            if member_id:
                result = [m for m in members if m.get("id") == member_id]
            elif filters:
                result = [
                    m for m in members if all(m.get(k) == v for k, v in filters.items())
                ]
            else:
                result = members
            payload = result
            out = json.dumps(payload, indent=2)
            return out
        elif action == "add":
            if not member:
                payload = {"error": "'member' parameter is required for add"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            if any(m["id"] == member.get("id") for m in members):
                payload = {"error": "Member with this id already exists"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            members.append(member)
            payload = {"success": "Member added", "member": member, "members": members}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        elif action == "update":
            if not member_id or not updates:
                payload = {
                        "error": "'member_id' and 'updates' parameters are required for update"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            found = False
            for m in members:
                if m["id"] == member_id:
                    for k, v in updates.items():
                        m[k] = v
                    found = True
                    break
            if not found:
                payload = {"error": "Member not found"}
                out = json.dumps(payload, indent=2)
                return out
            payload = {
                    "success": "Member updated",
                    "member_id": member_id,
                    "updates": updates,
                    "members": members,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        elif action == "delete":
            if not member_id:
                payload = {"error": "'member_id' parameter is required for delete"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            new_list = [m for m in members if m["id"] != member_id]
            if len(new_list) == len(members):
                payload = {"error": "Member not found"}
                out = json.dumps(payload, indent=2)
                return out
            payload = {
                    "success": "Member deleted",
                    "member_id": member_id,
                    "members": new_list,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {"error": f"Unknown action: {action}"}
            out = json.dumps(payload, indent=2)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageMemberInDatabase",
                "description": "Get member info, add, update, or delete a member.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "description": "Action to perform: get, add, update, delete",
                        },
                        "member_id": {
                            "type": "string",
                            "description": "Member id to operate on (required for get, update, delete)",
                        },
                        "member": {
                            "type": "object",
                            "description": "The full member object to add (required for add)",
                            "additionalProperties": True,
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update (required for update)",
                            "additionalProperties": True,
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter members (optional for get)",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
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