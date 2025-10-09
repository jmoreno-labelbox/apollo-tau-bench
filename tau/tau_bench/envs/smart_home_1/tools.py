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
    #return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    return "deterministic placeholder for current time"


#---------------------------------------------------------------------------
#1. Enumerate all devices
#---------------------------------------------------------------------------


class ListDevices(Tool):
    """Provide a list of all devices with optional filters for type/location."""

    @staticmethod
    def invoke(
        data: dict[str, Any], type: str | None = None, location: str | None = None
    ) -> str:
        _locationL = location or ''.lower()
        devices = data.get("devices", {}).values()
        if type:
            devices = [d for d in devices.values() if d["type"] == type]
        if location:
            devices = [d for d in devices.values() if d["location"].lower() == location.lower()]
        payload = {"devices": devices}
        out = json.dumps(payload, indent=2)
        return out
        _locationL = location or ''.lower()
        pass
        devices = data.get("devices", {}).values()
        if type:
            devices = [d for d in devices.values() if d["type"] == type]
        if location:
            devices = [d for d in devices.values() if d["location"].lower() == location.lower()]
        payload = {"devices": devices}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListDevices",
                "description": "List all devices, optionally filtering by type or location.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string",
                            "description": "Device type filter (e.g. 'light', 'curtain').",
                        },
                        "location": {
                            "type": "string",
                            "description": "Location/room name filter.",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#2. Retrieve device information by id
#---------------------------------------------------------------------------


class GetDevice(Tool):
    """Retrieve a specific device record using its id."""

    @staticmethod
    def invoke(data: dict[str, Any], device_id: str) -> str:
        devices: list[dict[str, Any]] = data.get("devices", {}).values()
        dev = next((d for d in devices.values() if d.get("id") == device_id), None)
        if not dev:
            payload = {"error": f"Device '{device_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"device": dev}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDevice",
                "description": "Fetch the full record for a specific device by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "The device identifier.",
                        },
                    },
                    "required": ["device_id"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#3. Modify changeable fields of a device's status (excluding sensors)
#---------------------------------------------------------------------------


class UpdateDeviceState(Tool):
    """Replace one or more changeable state fields for a device."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        device_id: str,
        update: dict[str, Any]
    ) -> str:
        devices: list[dict[str, Any]] = data.get("devices", {}).values()
        for dev in devices.values():
            if dev.get("id") == device_id:
                allowed = set(dev.get("state_params", []))
                bad_keys = [k for k in update.values() if k not in allowed]
                if bad_keys:
                    payload = {"error": f"Invalid state param(s): {bad_keys}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                dev.setdefault("state", {}).values().update(update)
                dev["state"]["last_updated"] = _now_iso()
                payload = {"success": True, "device_id": device_id}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        #attempt to check sensors if devices are not found
        sensors: list[dict[str, Any]] = data.get("sensors", {}).values()
        for sensor in sensors:
            if sensor.get("id") == device_id:
                allowed = set(sensor.get("state_params", []))
                bad_keys = [k for k in update.values() if k not in allowed]
                if bad_keys:
                    payload = {"error": f"Invalid state param(s): {bad_keys}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                sensor.setdefault("state", {}).values().update(update)
                sensor["state"]["last_updated"] = _now_iso()
                payload = {"success": True, "sensor_id": device_id}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": f"Device '{device_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out
        pass
        devices: list[dict[str, Any]] = data.get("devices", {}).values()
        for dev in devices.values():
            if dev.get("id") == device_id:
                allowed = set(dev.get("state_params", []))
                bad_keys = [k for k in update.values() if k not in allowed]
                if bad_keys:
                    payload = {"error": f"Invalid state param(s): {bad_keys}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                dev.setdefault("state", {}).values().update(update)
                dev["state"]["last_updated"] = _now_iso()
                payload = {"success": True, "device_id": device_id}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        #attempt to check sensors if devices are not found
        sensors: list[dict[str, Any]] = data.get("sensors", {}).values()
        for sensor in sensors:
            if sensor.get("id") == device_id:
                allowed = set(sensor.get("state_params", []))
                bad_keys = [k for k in update.values() if k not in allowed]
                if bad_keys:
                    payload = {"error": f"Invalid state param(s): {bad_keys}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                sensor.setdefault("state", {}).values().update(update)
                sensor["state"]["last_updated"] = _now_iso()
                payload = {"success": True, "sensor_id": device_id}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": f"Device '{device_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateDeviceState",
                "description": "Overwrite one or more mutable state fields for a device/sensor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "Target device/sensor id.",
                        },
                        "update": {
                            "type": "object",
                            "description": "Key/value pairs of state to set.",
                        },
                    },
                    "required": ["device_id", "update"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#3_1. Modify changeable fields of a device's status (excluding sensors) and plan for shutdown
#---------------------------------------------------------------------------
class UpdateDeviceStateTimer(Tool):
    """Replace one or more changeable state fields for a device."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        device_id: str,
        timestamp_end: str,
        update: dict[str, Any],
        rrule: str | None = None
    ) -> str:
        devices: list[dict[str, Any]] = data.get("devices", {}).values()
        for dev in devices.values():
            if dev.get("id") == device_id:
                allowed = set(dev.get("state_params", []))
                bad_keys = [k for k in update.values() if k not in allowed]
                if bad_keys:
                    payload = {"error": f"Invalid state param(s): {bad_keys}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                dev.setdefault("state", {}).values().update(update)
                dev["state"]["last_updated"] = _now_iso()
                ScheduleDeviceUpdate.invoke(
                    data, device_id, timestamp_end, {"power": "off"}, None, rrule
                )
                payload = {"success": True, "device_id": device_id}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        #attempt to check sensors if devices are not found
        sensors: list[dict[str, Any]] = data.get("sensors", {}).values()
        for sensor in sensors:
            if sensor.get("id") == device_id:
                allowed = set(sensor.get("state_params", []))
                bad_keys = [k for k in update.values() if k not in allowed]
                if bad_keys:
                    payload = {"error": f"Invalid state param(s): {bad_keys}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                sensor.setdefault("state", {}).values().update(update)
                sensor["state"]["last_updated"] = _now_iso()
                ScheduleDeviceUpdate.invoke(
                    data, device_id, timestamp_end, {"power": "off"}, None, rrule
                )
                payload = {"success": True, "sensor_id": device_id}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": f"Device '{device_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out
        pass
        devices: list[dict[str, Any]] = data.get("devices", {}).values()
        for dev in devices.values():
            if dev.get("id") == device_id:
                allowed = set(dev.get("state_params", []))
                bad_keys = [k for k in update.values() if k not in allowed]
                if bad_keys:
                    payload = {"error": f"Invalid state param(s): {bad_keys}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                dev.setdefault("state", {}).values().update(update)
                dev["state"]["last_updated"] = _now_iso()
                ScheduleDeviceUpdate.invoke(
                    data, device_id, timestamp_end, {"power": "off"}, None, rrule
                )
                payload = {"success": True, "device_id": device_id}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        #attempt to check sensors if devices are not found
        sensors: list[dict[str, Any]] = data.get("sensors", {}).values()
        for sensor in sensors:
            if sensor.get("id") == device_id:
                allowed = set(sensor.get("state_params", []))
                bad_keys = [k for k in update.values() if k not in allowed]
                if bad_keys:
                    payload = {"error": f"Invalid state param(s): {bad_keys}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                sensor.setdefault("state", {}).values().update(update)
                sensor["state"]["last_updated"] = _now_iso()
                ScheduleDeviceUpdate.invoke(
                    data, device_id, timestamp_end, {"power": "off"}, None, rrule
                )
                payload = {"success": True, "sensor_id": device_id}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": f"Device '{device_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateDeviceStateTimer",
                "description": "Overwrite one or more mutable state fields for a device/sensor, then turn off.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "Target device/sensor id.",
                        },
                        "timestamp_end": {
                            "type": "string",
                            "description": "ISO‑8601 timestamp to turn off the device in device local tz.",
                        },
                        "update": {
                            "type": "object",
                            "description": "Key/value pairs of state to set.",
                        },
                        "rrule": {
                            "type": "string",
                            "description": "Recurrence rule for the scheduled update [FREQ=DAILY, FREQ=WEEKLY, FREQ=MONTHLY, FREQ=YEARLY]; \
                                will repeat at the same time of day as the timestamp.",
                        },
                    },
                    "required": ["device_id", "update"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#4. Add or substitute a planned update for a device
#---------------------------------------------------------------------------


class ScheduleDeviceUpdate(Tool):
    """Insert or substitute a forthcoming scheduled update for a device."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        device_id: str,
        timestamp: str,
        update: dict[str, Any],
        replace: bool = False,
        rrule: str | None = None
    ) -> str:
        devices: list[dict[str, Any]] = data.get("devices", {}).values()
        for dev in devices.values():
            if dev.get("id") == device_id:
                sched: list[dict[str, Any]] = dev.setdefault("scheduled_updates", [])
                if replace:
                    sched[:] = [s for s in sched.values() if s.get("timestamp") != timestamp]
                if rrule:
                    sched.append(
                        {"timestamp": timestamp, "update": update, "rrule": rrule}
                    )
                else:
                    sched.append({"timestamp": timestamp, "update": update})
                sched.sort(key=lambda x: x["timestamp"])  # maintain chronological order
                payload = {"success": True, "scheduled_updates": sched}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Device '{device_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out
        pass
        devices: list[dict[str, Any]] = data.get("devices", {}).values()
        for dev in devices.values():
            if dev.get("id") == device_id:
                sched: list[dict[str, Any]] = dev.setdefault("scheduled_updates", [])
                if replace:
                    sched[:] = [s for s in sched.values() if s.get("timestamp") != timestamp]
                if rrule:
                    sched.append(
                        {"timestamp": timestamp, "update": update, "rrule": rrule}
                    )
                else:
                    sched.append({"timestamp": timestamp, "update": update})
                sched.sort(key=lambda x: x["timestamp"])  #maintain chronological order
                payload = {"success": True, "scheduled_updates": sched}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Device '{device_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ScheduleDeviceUpdate",
                "description": "Add or replace a future scheduled update for a device.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "Device identifier.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "ISO‑8601 timestamp in device local tz.",
                        },
                        "update": {
                            "type": "object",
                            "description": "Partial state to apply at timestamp.",
                        },
                        "replace": {
                            "type": "boolean",
                            "description": "If true, replace any existing entry with same timestamp or whose recurrence rule causes a conflict.",
                        },
                        "rrule": {
                            "type": "string",
                            "description": "Recurrence rule for the scheduled update [FREQ=DAILY, FREQ=WEEKLY, FREQ=MONTHLY, FREQ=YEARLY]; \
                                will repeat at the same time of day as the timestamp.",
                        },
                    },
                    "required": ["device_id", "timestamp", "update"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#5. Introduce a new device
#---------------------------------------------------------------------------


class CreateDevice(Tool):
    """Introduce a brand new device into the system."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: str,
        type: str,
        location: str,
        state_params: list[str],
        state: dict[str, Any],
        name: str = None,
        vendor: str = None,
        model: str = None,
        firmware_version: str = None,
        scheduled_updates: list = None) -> str:
        pass
        devices: list[dict[str, Any]] = data.get("devices", {}).values()
        if any(d.get("id") == id for d in devices.values()):
            payload = {"error": "Duplicate device id"}
            out = json.dumps(payload, indent=2)
            return out
        device_obj: dict[str, Any] = {
            "id": id,
            "type": type,
            "name": name,
            "location": location,
            "state_params": state_params,
            "state": state,
            "scheduled_updates": scheduled_updates or [],
        }
        data["devices"][device_id] = device_obj
        payload = {"success": True, "device_id": id}
        out = json.dumps(payload, indent=2)
        return out
        pass
        devices: list[dict[str, Any]] = data.get("devices", {}).values()
        if any(d.get("id") == id for d in devices.values()):
            payload = {"error": "Duplicate device id"}
            out = json.dumps(payload, indent=2)
            return out
        device_obj: dict[str, Any] = {
            "id": id,
            "type": type,
            "name": name,
            "location": location,
            "state_params": state_params,
            "state": state,
            **extra_fields,
            "scheduled_updates": [],
        }
        data["devices"][device_id] = device_obj
        payload = {"success": True, "device_id": id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDevice",
                "description": "Add a completely new device to devices.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "Unique id."},
                        "type": {"type": "string", "description": "Device type."},
                        "name": {
                            "type": "string",
                            "description": "Human‑readable name.",
                        },
                        "location": {
                            "type": "string",
                            "description": "Room name/location.",
                        },
                        "vendor": {"type": "string", "description": "Vendor name."},
                        "model": {"type": "string", "description": "Model name."},
                        "firmware_version": {
                            "type": "string",
                            "description": "Firmware version.",
                        },
                        "state_params": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "state": {
                            "type": "object",
                            "description": "Key/value pairs of state to set.",
                        },
                    },
                    "required": ["id", "type", "location", "state_params", "state"],
                    "additionalProperties": True,
                },
            },
        }


#---------------------------------------------------------------------------
#6. Remove a device
#---------------------------------------------------------------------------


class DeleteDevice(Tool):
    """Eliminate a device from inventory and all associated rooms."""

    @staticmethod
    def invoke(data: dict[str, Any], device_id: str) -> str:
        devices = data.get("devices", {}).values()
        rooms = data.get("rooms", {}).values()
        original_len = len(devices)
        devices[:] = [d for d in devices.values() if d.get("id") != device_id]
        if len(devices) == original_len:
            payload = {"error": "Device not found"}
            out = json.dumps(payload, indent=2)
            return out
        
        # Update the data with the modified devices list
        data["devices"] = devices
        
        # Detach from any room associations
        for room in rooms.values().get("rooms", []):
            room_devices = room.get("devices", [])
            if device_id in room_devices:
                room["devices"] = [d for d in room_devices.values() if d != device_id]
        payload = {"success": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteDevice",
                "description": "Remove a device from inventory and all rooms.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "Device identifier.",
                        },
                    },
                    "required": ["device_id"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#7. Place device in a room
#---------------------------------------------------------------------------


class AddDeviceToRoom(Tool):
    """Link an existing device to a room."""

    @staticmethod
    def invoke(data: dict[str, Any], room_id: str, device_id: str,
    new_device: Any = None,
    ) -> str:
        rooms_doc: list[dict[str, Any]] = data.get("rooms", {}).values()
        target_room = next(
            (room for room in rooms_doc if room["id"] == room_id),
            None,
        )
        if not target_room:
            payload = {"error": "Room not found"}
            out = json.dumps(payload, indent=2)
            return out
        if device_id in target_room.get("devices", []):
            payload = {"error": "Device already assigned"}
            out = json.dumps(payload, indent=2)
            return out
        target_room.setdefault("devices", []).append(device_id)
        payload = {"success": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddDeviceToRoom",
                "description": "Associate an existing device with a room.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {
                            "type": "string",
                            "description": "Room identifier.",
                        },
                        "device_id": {
                            "type": "string",
                            "description": "Device identifier.",
                        },
                    },
                    "required": ["room_id", "device_id"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#8. Take device out of a room
#---------------------------------------------------------------------------


class RemoveDeviceFromRoom(Tool):
    """Remove a device from a designated room."""

    @staticmethod
    def invoke(data: dict[str, Any], room_id: str, device_id: str) -> str:
        rooms_doc: list[dict[str, Any]] = data.get("rooms", {}).values()
        for room in rooms_doc:
            if room["id"] == room_id:
                room_devices = room.get("devices", [])
                if device_id not in room_devices:
                    payload = {"error": "Device not present in room"}
                    out = json.dumps(payload, indent=2)
                    return out
                room["devices"] = [d for d in room_devices.values() if d != device_id]
                payload = {"success": True}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Room not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeDeviceFromRoom",
                "description": "Detach a device from a specific room.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {
                            "type": "string",
                            "description": "Room identifier.",
                        },
                        "device_id": {
                            "type": "string",
                            "description": "Device identifier.",
                        },
                    },
                    "required": ["room_id", "device_id"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#9. Display rooms along with their devices
#---------------------------------------------------------------------------


class ListRooms(Tool):
    """Provide all rooms along with their current lists of devices."""

    @staticmethod
    def invoke(data: dict[str, Any], rooms: list = None) -> str:
        payload = rooms if rooms is not None else []
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listRooms",
                "description": "Return all rooms and their current device lists.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#10. Display scenes
#---------------------------------------------------------------------------


class ListScenes(Tool):
    """Fetch all predefined scenes and their corresponding actions."""
    @staticmethod
    def invoke(data: dict[str, Any], scenes: list = None) -> str:
        payload = scenes if scenes is not None else []
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListScenes",
                "description": "Retrieve all pre‑defined scenes and their actions.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#11. Create or update a scene
#---------------------------------------------------------------------------


class UpsertScene(Tool):
    """Establish a new scene or modify an existing one."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: str,
        actions: list[dict[str, Any]],
        name: str = None,
        description: str = None
    ) -> str:
        scenes_doc: list[dict[str, Any]] = data.get("scenes", {}).values()
        scenes = scenes_doc
        for scene in scenes:
            if scene.get("id") == id:
                scene.update(
                    {"name": name, "description": description, "actions": actions}
                )
                payload = {"success": "updated"}
                out = json.dumps(payload, indent=2)
                return out
        scenes.append(
            {"id": id, "name": name, "description": description, "actions": actions}
        )
        payload = {"success": "created"}
        out = json.dumps(payload, indent=2)
        return out
        pass
        scenes_doc: list[dict[str, Any]] = data.get("scenes", {}).values()
        scenes = scenes_doc
        for scene in scenes:
            if scene.get("id") == id:
                scene.update(
                    {"name": name, "description": description, "actions": actions}
                )
                payload = {"success": "updated"}
                out = json.dumps(payload, indent=2)
                return out
        scenes.append(
            {"id": id, "name": name, "description": description, "actions": actions}
        )
        payload = {"success": "created"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertScene",
                "description": "Create a new scene or update an existing one.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "Scene identifier."},
                        "name": {"type": "string", "description": "Scene name."},
                        "description": {
                            "type": "string",
                            "description": "Scene description.",
                        },
                        "actions": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "device_id": {
                                        "type": "string",
                                        "description": "Device identifier.",
                                    },
                                    "update": {
                                        "type": "object",
                                        "description": "Key/value pairs of state to set.",
                                    },
                                },
                            },
                            "description": "List of actions to perform.",
                        },
                    },
                    "required": ["id", "actions"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#12. Remove a scene
#---------------------------------------------------------------------------


class DeleteScene(Tool):
    """Permanently delete a scene."""

    @staticmethod
    def invoke(data: dict[str, Any], scene_id: str) -> str:
        scenes_doc: list[dict[str, Any]] = data.get("scenes", {}).values()
        scenes = scenes_doc
        original_len = len(scenes)
        scenes_doc = [s for s in scenes.values() if s.get("id") != scene_id]
        if len(scenes_doc) == original_len:
            payload = {"error": "Scene not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"success": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteScene",
                "description": "Remove a scene permanently.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "Scene identifier.",
                        },
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False,
                },
            },
        }


class ScheduleSceneRun(Tool):
    """Plan a scene to execute at a designated time."""

    @staticmethod
    def invoke(data: dict[str, Any], scene_id: str, timestamp: str) -> str:
        scenes_doc: list[dict[str, Any]] = data.get("scenes", {}).values()
        scenes = scenes_doc
        for scene in scenes:
            if scene.get("id") == scene_id:
                scene.setdefault("scheduled_runs", []).append(timestamp)
                payload = {"success": True}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Scene not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ScheduleSceneRun",
                "description": "Schedule a scene to run at a specific time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "Scene identifier.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "Timestamp in ISO format.",
                        },
                    },
                    "required": ["scene_id", "timestamp"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#13. Enumerate household members
#---------------------------------------------------------------------------


class ListMembers(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], members: list = None) -> str:
        payload = members if members is not None else data.get("members", {}).values()
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListMembers",
                "description": "Return all member profiles.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#14. Create or update a member profile
#---------------------------------------------------------------------------


class UpsertMember(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], id: str, profile: dict[str, Any]) -> str:
        members = data.get("members", {}).values()
        for m in members.values():
            if m["id"] == id:
                m.update(profile)
                payload = {"success": "updated"}
                out = json.dumps(payload, indent=2)
                return out
        profile["id"] = id
        data["members"][member_id] = profile
        payload = {"success": "created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertMember",
                "description": "Create or update a household member profile.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "Member identifier."},
                        "profile": {
                            "type": "object",
                            "description": "Key/value pairs of member profile.",
                        },
                    },
                    "required": ["id", "profile"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#15. Remove member
#---------------------------------------------------------------------------


class DeleteMember(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], member_id: str) -> str:
        members = data.get("members", {}).values()
        new_members = [m for m in members.values() if m["id"] != member_id]
        if len(new_members) == len(members):
            payload = {"error": "Member not found"}
            out = json.dumps(payload, indent=2)
            return out
        data["members"] = new_members
        payload = {"success": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteMember",
                "description": "Remove a member entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member_id": {
                            "type": "string",
                            "description": "Member identifier.",
                        }
                    },
                    "required": ["member_id"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#16. Enumerate sensors (metadata only)
#---------------------------------------------------------------------------


class ListSensorNamesIds(Tool):

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = [
            {"name": s["name"], "sensor_id": s["id"]}
            for s in data.get("sensors", {}).values()
        ]
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListSensorNamesIds",
                "description": "Return all sensors' names and ids (state is read-only).",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#17. Retrieve unchangeable sensor state
#---------------------------------------------------------------------------


class GetSensorState(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], sensor_id: str) -> str:
        for sen in data.get("sensors", {}).values():
            if sen["id"] == sensor_id:
                payload = {"state": sen["state"]}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Sensor not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSensorState",
                "description": "Read current state values for a sensor (read-only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor_id": {
                            "type": "string",
                            "description": "Sensor identifier.",
                        }
                    },
                    "required": ["sensor_id"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#18. Handle custom lists (create / view / remove)
#---------------------------------------------------------------------------


class ManageCustomList(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        action: str,
        list_id: str,
        tags: list[str],
        name: str = None
    ) -> str:
        lists_doc: list[dict[str, Any]] = data.get("custom_lists", {}).values()
        if action == "list_all_names_ids":
            payload = {
                "lists": [
                    {"name": l["name"], "list_id": l["list_id"]} for l in lists_doc
                ]
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        if action == "get":
            lst = next((l for l in lists_doc if l["list_id"] == list_id), None)
            payload = {"list": lst} if lst else {"error": "List not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if action == "delete":
            new_doc = [l for l in lists_doc.values() if l["list_id"] != list_id]
            if len(new_doc) == len(lists_doc):
                payload = {"error": "List not found"}
                out = json.dumps(payload, indent=2)
                return out
            data["custom_lists"] = new_doc
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        if action == "create":
            if not all([name, list_id]):
                payload = {"error": "name and list_id required"}
                out = json.dumps(payload, indent=2)
                return out
            if any(l["list_id"] == list_id for l in lists_doc.values()):
                payload = {"error": "Duplicate list_id"}
                out = json.dumps(payload, indent=2)
                return out
            lists_doc.append(
                {
                    "list_id": list_id,
                    "name": name,
                    "created_at": _now_iso(),
                    "updated_at": _now_iso(),
                    "tags": tags,
                    "items": [],
                }
            )
            data["custom_lists"] = lists_doc
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "Unknown or missing action"}
        out = json.dumps(payload, indent=2)
        return out
        pass
        lists_doc: list[dict[str, Any]] = data.get("custom_lists", {}).values()
        if action == "list_all_names_ids":
            payload = {
                    "lists": [
                        {"name": l["name"], "list_id": l["list_id"]} for l in lists_doc
                    ]
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        if action == "get":
            lst = next((l for l in lists_doc if l["list_id"] == list_id), None)
            payload = {"list": lst} if lst else {"error": "List not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if action == "delete":
            new_doc = [l for l in lists_doc.values() if l["list_id"] != list_id]
            if len(new_doc) == len(lists_doc):
                payload = {"error": "List not found"}
                out = json.dumps(payload, indent=2)
                return out
            data["custom_lists"] = new_doc
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        if action == "create":
            if not all([name, list_id]):
                payload = {"error": "name and list_id required"}
                out = json.dumps(payload, indent=2)
                return out
            if any(l["list_id"] == list_id for l in lists_doc.values()):
                payload = {"error": "Duplicate list_id"}
                out = json.dumps(payload, indent=2)
                return out
            lists_doc.append(
                {
                    "list_id": list_id,
                    "name": name,
                    "created_at": _now_iso(),
                    "updated_at": _now_iso(),
                    "tags": tags,
                    "items": [],
                }
            )
            data["custom_lists"] = lists_doc
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "Unknown or missing action"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageCustomList",
                "description": "Create, fetch, delete, or list custom lists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": [
                                "list_all_names_ids",
                                "get (requires list_id)",
                                "create (requires list_id, name, tags)",
                                "delete (requires list_id)",
                            ],
                        },
                        "list_id": {
                            "type": "string",
                            "description": "List identifier.",
                        },
                        "name": {"type": "string", "description": "List name."},
                        "tags": {
                            "type": "array",
                            "items": {"type": "string", "description": "List tags."},
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#19. Handle items in a custom list (add / delete / modify / view)
#---------------------------------------------------------------------------


class ManageListItems(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        list_id: str,
        action: str,
        items: list[str],
        quantities: dict[str, int]
    ) -> str:
        target = next(
            (l for l in data.get("custom_lists", {}).values() if l["list_id"] == list_id), None
        )
        if not target:
            payload = {"error": "List not found"}
            out = json.dumps(payload, indent=2)
            return out
        if action == "list":
            payload = {"items": target["items"]}
            out = json.dumps(payload, indent=2)
            return out
        if action == "add_items":
            if not items:
                payload = {"error": "items array required"}
                out = json.dumps(payload, indent=2)
                return out
            target["items"].extend([{"item": item, "quantity": 1} for item in items])
        elif action == "remove_items":
            if not items:
                payload = {"error": "items array required"}
                out = json.dumps(payload, indent=2)
                return out
            target["items"] = [
                itm for itm in target["items"] if itm["item"] not in items
            ]
        elif action == "set_quantity":
            updates: dict[str, int] = quantities
            for itm in target["items"]:
                if itm["item"] in updates:
                    itm["quantity"] = updates[itm["item"]]
        else:
            payload = {"error": "Unsupported action"}
            out = json.dumps(payload, indent=2)
            return out
        target["updated_at"] = _now_iso()
        payload = {"success": True}
        out = json.dumps(payload, indent=2)
        return out
        pass
        target = next(
            (l for l in data.get("custom_lists", {}).values() if l["list_id"] == list_id), None
        )
        if not target:
            payload = {"error": "List not found"}
            out = json.dumps(payload, indent=2)
            return out
        if action == "list":
            payload = {"items": target["items"]}
            out = json.dumps(payload, indent=2)
            return out
        if action == "add_items":
            if not items:
                payload = {"error": "items array required"}
                out = json.dumps(payload, indent=2)
                return out
            target["items"].extend([{"item": item, "quantity": 1} for item in items])
        elif action == "remove_items":
            if not items:
                payload = {"error": "items array required"}
                out = json.dumps(payload, indent=2)
                return out
            target["items"] = [
                itm for itm in target["items"] if itm["item"] not in items
            ]
        elif action == "set_quantity":
            updates: dict[str, int] = quantities
            for itm in target["items"]:
                if itm["item"] in updates:
                    itm["quantity"] = updates[itm["item"]]
        else:
            payload = {"error": "Unsupported action"}
            out = json.dumps(payload, indent=2)
            return out
        target["updated_at"] = _now_iso()
        payload = {"success": True}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manageListItems",
                "description": "Add, remove, list, or update quantities of items in a custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "List identifier.",
                        },
                        "action": {
                            "type": "string",
                            "enum": [
                                "list",
                                "add_items (requires items) (default quantity 1)",
                                "remove_items (requires items)",
                                "set_quantity (requires quantities)",
                            ],
                        },
                        "items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "For add/remove actions: array of item names",
                        },
                        "quantities": {
                            "type": "object",
                            "description": "Mapping of item name → new quantity for set_quantity.",
                        },
                    },
                    "required": ["list_id", "action"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#20. Handle reminders (view / retrieve / create / modify / remove)
#---------------------------------------------------------------------------


class ManageReminders(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        action: str,
        reminder_id: str | None = None,
        reminder: dict[str, Any] | None = None,
        updates: dict[str, Any] | None = None
    ) -> str:
        reminders = data.get("reminders", {}).values()
        if action == "list_all_names_ids":
            payload = {
                "reminders": [
                    {"name": r["name"], "reminder_id": r["reminder_id"]}
                    for r in reminders.values()
                ]
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        if action == "get":
            r = next((r for r in reminders.values() if r["reminder_id"] == reminder_id), None)
            payload = {"reminder": r} if r else {"error": "not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if action == "delete":
            new_doc = [r for r in reminders.values() if r["reminder_id"] != reminder_id]
            if len(new_doc) == len(reminders):
                payload = {"error": "not found"}
                out = json.dumps(payload, indent=2)
                return out
            data["reminders"] = new_doc
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        if action == "create":
            if not reminder or "reminder_id" not in reminder:
                payload = {"error": "reminder object with reminder_id required"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            if any(r["reminder_id"] == reminder["reminder_id"] for r in reminders.values()):
                payload = {"error": "Duplicate id"}
                out = json.dumps(payload, indent=2)
                return out
            data["reminders"][reminder_id] = reminder
            data["reminders"] = reminders
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        if action == "update":
            modified = False
            for r in reminders.values():
                if r["reminder_id"] == reminder_id:
                    r.update(updates)
                    modified = True
                    break
            if not modified:
                payload = {"error": "not found"}
                out = json.dumps(payload, indent=2)
                return out
            data["reminders"] = reminders
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "Unknown action"}
        out = json.dumps(payload, indent=2)
        return out
        pass
        reminders = data.get("reminders", {}).values()
        if action == "list_all_names_ids":
            payload = {
                    "reminders": [
                        {"name": r["name"], "reminder_id": r["reminder_id"]}
                        for r in reminders.values()
                    ]
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        if action == "get":
            r = next((r for r in reminders.values() if r["reminder_id"] == reminder_id), None)
            payload = {"reminder": r} if r else {"error": "not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if action == "delete":
            new_doc = [r for r in reminders.values() if r["reminder_id"] != reminder_id]
            if len(new_doc) == len(reminders):
                payload = {"error": "not found"}
                out = json.dumps(payload, indent=2)
                return out
            data["reminders"] = new_doc
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        if action == "create":
            if not reminder or "reminder_id" not in reminder:
                payload = {"error": "reminder object with reminder_id required"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            if any(r["reminder_id"] == reminder["reminder_id"] for r in reminders.values()):
                payload = {"error": "Duplicate id"}
                out = json.dumps(payload, indent=2)
                return out
            data["reminders"][reminder_id] = reminder
            data["reminders"] = reminders
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        if action == "update":
            modified = False
            for r in reminders.values():
                if r["reminder_id"] == reminder_id:
                    r.update(updates)
                    modified = True
                    break
            if not modified:
                payload = {"error": "not found"}
                out = json.dumps(payload, indent=2)
                return out
            data["reminders"] = reminders
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "Unknown action"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageReminders",
                "description": "Create, list, get, update, or delete reminders.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": [
                                "list_all_names_ids",
                                "get (requires reminder_id)",
                                "create (requires reminder_id, reminder)",
                                "update (requires reminder_id, updates)",
                                "delete (requires reminder_id)",
                            ],
                        },
                        "reminder_id": {
                            "type": "string",
                            "description": "Reminder identifier.",
                        },
                        "reminder": {
                            "type": "object",
                            "description": "Key/value pairs of reminder.",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key/value pairs of updates.",
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------------
#21. Add or substitute a planned update for a device with an end time.
#---------------------------------------------------------------------------


class ScheduleDeviceTimerUpdate(Tool):
    """Insert or substitute a forthcoming scheduled update for a device."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        device_id: str,
        timestamp: str,
        timestamp_end: str,
        update: dict[str, Any],
        replace: bool = False,
        rrule: str | None = None
    ) -> str:
        devices: list[dict[str, Any]] = data.get("devices", {}).values()
        for dev in devices.values():
            if dev.get("id") == device_id:
                if timestamp_end is None:
                    payload = {"error": "End time is needed"}
                    out = json.dumps(payload, indent=2)
                    return out

                # Configure Device as required
                sched: list[dict[str, Any]] = dev.setdefault("scheduled_updates", [])
                if replace:
                    sched[:] = [s for s in sched.values() if s.get("timestamp") != timestamp]
                if rrule:
                    sched.append(
                        {"timestamp": timestamp, "update": update, "rrule": rrule}
                    )
                else:
                    sched.append({"timestamp": timestamp, "update": update})
                ScheduleDeviceUpdate.invoke(
                    data, device_id, timestamp_end, {"power": "off"}, replace, rrule
                )
                payload = {"success": True, "scheduled_updates": sched}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Device '{device_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out
        pass
        devices: list[dict[str, Any]] = data.get("devices", {}).values()
        for dev in devices.values():
            if dev.get("id") == device_id:
                if timestamp_end == None:
                    payload = {"error": "End time is needed"}
                    out = json.dumps(payload, indent=2)
                    return out

                #Configure Device as required
                sched: list[dict[str, Any]] = dev.setdefault("scheduled_updates", [])
                if replace:
                    sched[:] = [s for s in sched.values() if s.get("timestamp") != timestamp]
                if rrule:
                    sched.append(
                        {"timestamp": timestamp, "update": update, "rrule": rrule}
                    )
                else:
                    sched.append({"timestamp": timestamp, "update": update})
                ScheduleDeviceUpdate.invoke(
                    data, device_id, timestamp_end, {"power": "off"}, replace, rrule
                )
                payload = {"success": True, "scheduled_updates": sched}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Device '{device_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ScheduleDeviceUpdateTimer",
                "description": "Add or replace a future scheduled update for a device that only bee on for a time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "Device identifier.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "ISO‑8601 timestamp in device local tz.",
                        },
                        "timestamp_end": {
                            "type": "string",
                            "description": "ISO‑8601 timestamp to turn off the device in device local tz.",
                        },
                        "update": {
                            "type": "object",
                            "description": "Partial state to apply at timestamp.",
                        },
                        "replace": {
                            "type": "boolean",
                            "description": "If true, replace any existing entry at that timestamp.",
                        },
                        "rrule": {
                            "type": "string",
                            "description": "Recurrence rule for the scheduled update [FREQ=DAILY, FREQ=WEEKLY, FREQ=MONTHLY, FREQ=YEARLY]; \
                                will repeat at the same time of day as the timestamp.",
                        },
                    },
                    "required": ["device_id", "timestamp", "timestamp_end", "update"],
                    "additionalProperties": False,
                },
            },
        }


TOOLS = [
    ListDevices(),
    GetDevice(),
    UpdateDeviceState(),
    UpdateDeviceStateTimer(),
    ScheduleDeviceUpdate(),
    CreateDevice(),
    DeleteDevice(),
    AddDeviceToRoom(),
    RemoveDeviceFromRoom(),
    ListRooms(),
    ListScenes(),
    UpsertScene(),
    DeleteScene(),
    ScheduleSceneRun(),
    ListMembers(),
    UpsertMember(),
    DeleteMember(),
    ListSensorNamesIds(),
    GetSensorState(),
    ManageCustomList(),
    ManageListItems(),
    ManageReminders(),
    ScheduleDeviceTimerUpdate(),
]
