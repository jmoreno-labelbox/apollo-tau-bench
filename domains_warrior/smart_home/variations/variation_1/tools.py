import json
from typing import Any, Dict, List, Optional
from domains.dto import Tool
from datetime import datetime

def _now_iso() -> str:
    # return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    return "deterministic placeholder for current time"


# ---------------------------------------------------------------------------
# 1. List all devices
# ---------------------------------------------------------------------------

class ListDevices(Tool):
    """Return an array of all devices with optional type/location filters."""

    @staticmethod
    def invoke(data: Dict[str, Any], type: Optional[str] = None, location: Optional[str] = None) -> str:
        devices = data.get("devices", [])
        if type:
            devices = [d for d in devices if d["type"] == type]
        if location:
            devices = [d for d in devices if d["location"].lower() == location.lower()]
        return json.dumps({"devices": devices}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_devices",
                "description": "List all devices, optionally filtering by type or location.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "type": {"type": "string", "description": "Device type filter (e.g. 'light', 'curtain')."},
                        "location": {"type": "string", "description": "Location/room name filter."},
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


# ---------------------------------------------------------------------------
# 2. Get device detail by id
# ---------------------------------------------------------------------------

class GetDevice(Tool):
    """Fetch a single device record by its id."""

    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str) -> str:
        devices: List[Dict[str, Any]] = data.get("devices", [])
        dev = next((d for d in devices if d.get("id") == device_id), None)
        if not dev:
            return json.dumps({"error": f"Device '{device_id}' not found"}, indent=2)
        return json.dumps({"device": dev}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_device",
                "description": "Fetch the full record for a specific device by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "The device identifier."},
                    },
                    "required": ["device_id"],
                    "additionalProperties": False,
                },
            },
        }

# ---------------------------------------------------------------------------
# 3. Update mutable fields of a device's state (not sensors)
# ---------------------------------------------------------------------------

class UpdateDeviceState(Tool):
    """Overwrite one or more mutable state fields for a device."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        device_id: str,
        update: Dict[str, Any],
    ) -> str:
        devices: List[Dict[str, Any]] = data.get("devices", [])
        for dev in devices:
            if dev.get("id") == device_id:
                allowed = set(dev.get("state_params", []))
                bad_keys = [k for k in update if k not in allowed]
                if bad_keys:
                    return json.dumps({"error": f"Invalid state param(s): {bad_keys}"}, indent=2)
                dev.setdefault("state", {}).update(update)
                dev["state"]["last_updated"] = _now_iso()
                return json.dumps(
                    {"success": True, "device_id": device_id},
                    indent=2,
                )
        # try sensors if not found in devices
        sensors: List[Dict[str, Any]] = data.get("sensors", [])
        for sensor in sensors:
            if sensor.get("id") == device_id:
                allowed = set(sensor.get("state_params", []))
                bad_keys = [k for k in update if k not in allowed]
                if bad_keys:
                    return json.dumps({"error": f"Invalid state param(s): {bad_keys}"}, indent=2)
                sensor.setdefault("state", {}).update(update)
                sensor["state"]["last_updated"] = _now_iso()
                return json.dumps(
                    {"success": True, "sensor_id": device_id},
                    indent=2,
                )
        return json.dumps({"error": f"Device '{device_id}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_device_state",
                "description": "Overwrite one or more mutable state fields for a device/sensor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "Target device/sensor id."},
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

# ---------------------------------------------------------------------------
# 3_1. Update mutable fields of a device's state (not sensors) and schedule turn off
# ---------------------------------------------------------------------------
class UpdateDeviceStateTimer(Tool):
    """Overwrite one or more mutable state fields for a device."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        device_id: str,
        timestamp_end: str,
        update: Dict[str, Any],
        rrule: Optional[str] = None
    ) -> str:
        devices: List[Dict[str, Any]] = data.get("devices", [])
        for dev in devices:
            if dev.get("id") == device_id:
                allowed = set(dev.get("state_params", []))
                bad_keys = [k for k in update if k not in allowed]
                if bad_keys:
                    return json.dumps({"error": f"Invalid state param(s): {bad_keys}"}, indent=2)
                dev.setdefault("state", {}).update(update)
                dev["state"]["last_updated"] = _now_iso()
                ScheduleDeviceUpdate.invoke(data, device_id, timestamp_end, {"power": "off"}, None, rrule)
                return json.dumps(
                    {"success": True, "device_id": device_id},
                    indent=2,
                )
        # try sensors if not found in devices
        sensors: List[Dict[str, Any]] = data.get("sensors", [])
        for sensor in sensors:
            if sensor.get("id") == device_id:
                allowed = set(sensor.get("state_params", []))
                bad_keys = [k for k in update if k not in allowed]
                if bad_keys:
                    return json.dumps({"error": f"Invalid state param(s): {bad_keys}"}, indent=2)
                sensor.setdefault("state", {}).update(update)
                sensor["state"]["last_updated"] = _now_iso()
                ScheduleDeviceUpdate.invoke(data, device_id, timestamp_end, {"power": "off"}, None, rrule)
                return json.dumps(
                    {"success": True, "sensor_id": device_id},
                    indent=2,
                )

        return json.dumps({"error": f"Device '{device_id}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_device_state_timer",
                "description": "Overwrite one or more mutable state fields for a device/sensor, then turn off.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "Target device/sensor id."},
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

# ---------------------------------------------------------------------------
# 4. Append or replace a scheduled update for a device
# ---------------------------------------------------------------------------

class ScheduleDeviceUpdate(Tool):
    """Add or replace a future scheduled update for a device."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        device_id: str,
        timestamp: str,
        update: Dict[str, Any],
        replace: bool = False,
        rrule: Optional[str] = None,
    ) -> str:
        devices: List[Dict[str, Any]] = data.get("devices", [])
        for dev in devices:
            if dev.get("id") == device_id:
                sched: List[Dict[str, Any]] = dev.setdefault("scheduled_updates", [])
                if replace:
                    sched[:] = [s for s in sched if s.get("timestamp") != timestamp]
                if rrule:
                    sched.append({"timestamp": timestamp, "update": update, "rrule": rrule})
                else:
                    sched.append({"timestamp": timestamp, "update": update})
                sched.sort(key=lambda x: x["timestamp"])  # keep chronologically ordered
                return json.dumps({"success": True, "scheduled_updates": sched}, indent=2)
        return json.dumps({"error": f"Device '{device_id}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_device_update",
                "description": "Add or replace a future scheduled update for a device.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "Device identifier."},
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

# ---------------------------------------------------------------------------
# 5. Create a new device
# ---------------------------------------------------------------------------

class CreateDevice(Tool):
    """Add a completely new device to the system."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        id: str,
        type: str,
        location: str,
        state_params: List[str],
        state: Dict[str, Any],
        name: str = None,
        **extra_fields: Any,
    ) -> str:
        devices: List[Dict[str, Any]] = data.get("devices", [])
        if any(d.get("id") == id for d in devices):
            return json.dumps({"error": "Duplicate device id"}, indent=2)
        device_obj: Dict[str, Any] = {
            "id": id,
            "type": type,
            "name": name,
            "location": location,
            "state_params": state_params,
            "state": state,
            **extra_fields,
            "scheduled_updates": [],
        }
        devices.append(device_obj)
        return json.dumps({"success": True, "device_id": id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_device",
                "description": "Add a completely new device to devices.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "Unique id."},
                        "type": {"type": "string", "description": "Device type."},
                        "name": {"type": "string", "description": "Human‑readable name."},
                        "location": {"type": "string", "description": "Room name/location."},
                        "vendor": {"type": "string", "description": "Vendor name."},
                        "model": {"type": "string", "description": "Model name."},
                        "firmware_version": {"type": "string", "description": "Firmware version."},
                        "state_params": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "state": {"type": "object", "description": "Key/value pairs of state to set."},
                    },
                    "required": ["id", "type", "location", "state_params", "state"],
                    "additionalProperties": True,
                },
            },
        }

# ---------------------------------------------------------------------------
# 6. Delete a device
# ---------------------------------------------------------------------------

class DeleteDevice(Tool):
    """Remove a device from inventory and all rooms."""

    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str) -> str:
        devices: List[Dict[str, Any]] = data.get("devices", [])
        original_len = len(devices)
        devices[:] = [d for d in devices if d.get("id") != device_id]
        if len(devices) == original_len:
            return json.dumps({"error": "Device not found"}, indent=2)
        # Remove from any room mapping
        rooms_doc: Dict[str, Any] = data.get("rooms", {})
        for room in rooms_doc.get("rooms", []):
            room_devices = room.get("devices", [])
            if device_id in room_devices:
                room["devices"] = [d for d in room_devices if d != device_id]
        return json.dumps({"success": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_device",
                "description": "Remove a device from inventory and all rooms.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "Device identifier."},
                    },
                    "required": ["device_id"],
                    "additionalProperties": False,
                },
            },
        }

# ---------------------------------------------------------------------------
# 7. Add device to room
# ---------------------------------------------------------------------------

class AddDeviceToRoom(Tool):
    """Associate an existing device with a room."""

    @staticmethod
    def invoke(data: Dict[str, Any], room_id: str, device_id: str) -> str:
        rooms_doc: List[Dict[str, Any]] = data.get("rooms", [])
        target_room = next(
            (room for room in rooms_doc if room["id"] == room_id),
            None,
        )
        if not target_room:
            return json.dumps({"error": "Room not found"}, indent=2)
        if device_id in target_room.get("devices", []):
            return json.dumps({"error": "Device already assigned"}, indent=2)
        target_room.setdefault("devices", []).append(device_id)
        return json.dumps({"success": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_device_to_room",
                "description": "Associate an existing device with a room.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {"type": "string", "description": "Room identifier."},
                        "device_id": {"type": "string", "description": "Device identifier."},
                    },
                    "required": ["room_id", "device_id"],
                    "additionalProperties": False,
                },
            },
        }

# ---------------------------------------------------------------------------
# 8. Remove device from room
# ---------------------------------------------------------------------------

class RemoveDeviceFromRoom(Tool):
    """Detach a device from a specific room."""

    @staticmethod
    def invoke(data: Dict[str, Any], room_id: str, device_id: str) -> str:
        rooms_doc: List[Dict[str, Any]] = data.get("rooms", [])
        for room in rooms_doc:
            if room["id"] == room_id:
                room_devices = room.get("devices", [])
                if device_id not in room_devices:
                    return json.dumps({"error": "Device not present in room"}, indent=2)
                room["devices"] = [d for d in room_devices if d != device_id]
                return json.dumps({"success": True}, indent=2)
        return json.dumps({"error": "Room not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_device_from_room",
                "description": "Detach a device from a specific room.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {"type": "string", "description": "Room identifier."},
                        "device_id": {"type": "string", "description": "Device identifier."},
                    },
                    "required": ["room_id", "device_id"],
                    "additionalProperties": False,
                },
            },
        }

# ---------------------------------------------------------------------------
# 9. List rooms with their devices
# ---------------------------------------------------------------------------

class ListRooms(Tool):
    """Return all rooms and their current device lists."""

    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:  # no extra args
        return json.dumps(data.get("rooms", []), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_rooms",
                "description": "Return all rooms and their current device lists.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }

# ---------------------------------------------------------------------------
# 10. List scenes
# ---------------------------------------------------------------------------

class ListScenes(Tool):
    """Retrieve all pre‑defined scenes and their actions."""

    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        return json.dumps(data.get("scenes", []), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_scenes",
                "description": "Retrieve all pre‑defined scenes and their actions.",
                "parameters": {"type": "object", "properties": {}, "required": [], "additionalProperties": False},
            },
        }

# ---------------------------------------------------------------------------
# 11. Upsert (create/update) a scene
# ---------------------------------------------------------------------------

class UpsertScene(Tool):
    """Create a new scene or update an existing one."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        id: str,
        actions: List[Dict[str, Any]],
        name: str = None,
        description: str = None,
    ) -> str:
        scenes_doc: List[Dict[str, Any]] = data.get("scenes", [])
        scenes = scenes_doc
        for scene in scenes:
            if scene.get("id") == id:
                scene.update({"name": name, "description": description, "actions": actions})
                return json.dumps({"success": "updated"}, indent=2)
        scenes.append({"id": id, "name": name, "description": description, "actions": actions})
        return json.dumps({"success": "created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_scene",
                "description": "Create a new scene or update an existing one.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "Scene identifier."},
                        "name": {"type": "string", "description": "Scene name."},
                        "description": {"type": "string", "description": "Scene description."},
                        "actions": {"type": "array", "items": {"type": "object", "properties": {
                            "device_id": {"type": "string", "description": "Device identifier."},
                            "update": {"type": "object", "description": "Key/value pairs of state to set."},
                        }}, "description": "List of actions to perform."},
                    },
                    "required": ["id", "actions"],
                    "additionalProperties": False,
                },
            },
        }

# ---------------------------------------------------------------------------
# 12. Delete a scene
# ---------------------------------------------------------------------------

class DeleteScene(Tool):
    """Remove a scene permanently."""

    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str) -> str:
        scenes_doc: List[Dict[str, Any]] = data.get("scenes", [])
        scenes = scenes_doc
        original_len = len(scenes)
        scenes_doc = [s for s in scenes if s.get("id") != scene_id]
        if len(scenes_doc) == original_len:
            return json.dumps({"error": "Scene not found"}, indent=2)
        return json.dumps({"success": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_scene",
                "description": "Remove a scene permanently.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {"type": "string", "description": "Scene identifier."},
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False,
                },
            },
        }

class ScheduleSceneRun(Tool):
    """Schedule a scene to run at a specific time."""

    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str, timestamp: str) -> str:
        scenes_doc: List[Dict[str, Any]] = data.get("scenes", [])
        scenes = scenes_doc
        for scene in scenes:
            if scene.get("id") == scene_id:
                scene.setdefault("scheduled_runs", []).append(timestamp)
                return json.dumps({"success": True}, indent=2)
        return json.dumps({"error": "Scene not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_scene_run",
                "description": "Schedule a scene to run at a specific time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {"type": "string", "description": "Scene identifier."},
                        "timestamp": {"type": "string", "description": "Timestamp in ISO format."},
                    },
                    "required": ["scene_id", "timestamp"],
                    "additionalProperties": False,
                },
            },
        }

# ---------------------------------------------------------------------------
# 13. List household members
# ---------------------------------------------------------------------------

class ListMembers(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        return json.dumps(data.get("members", []), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_members",
                "description": "Return all member profiles.",
                "parameters": {"type": "object", "properties": {}, "required": [], "additionalProperties": False},
            },
        }


# ---------------------------------------------------------------------------
# 14. Upsert (create/update) member profile
# ---------------------------------------------------------------------------

class UpsertMember(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], id: str, profile: Dict[str, Any]) -> str:
        members = data.get("members", [])
        for m in members:
            if m["id"] == id:
                m.update(profile)
                return json.dumps({"success": "updated"}, indent=2)
        profile["id"] = id
        members.append(profile)
        return json.dumps({"success": "created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_member",
                "description": "Create or update a household member profile.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "Member identifier."},
                        "profile": {"type": "object", "description": "Key/value pairs of member profile."},
                    },
                    "required": ["id", "profile"],
                    "additionalProperties": False,
                },
            },
        }


# ---------------------------------------------------------------------------
# 15. Delete member
# ---------------------------------------------------------------------------

class DeleteMember(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], member_id: str) -> str:
        members = data.get("members", [])
        new_members = [m for m in members if m["id"] != member_id]
        if len(new_members) == len(members):
            return json.dumps({"error": "Member not found"}, indent=2)
        data["members"] = new_members
        return json.dumps({"success": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_member",
                "description": "Remove a member entry.",
                "parameters": {
                    "type": "object",
                    "properties": {"member_id": {"type": "string", "description": "Member identifier."}},
                    "required": ["member_id"],
                    "additionalProperties": False,
                },
            },
        }


# ---------------------------------------------------------------------------
# 16. List sensors (metadata only)
# ---------------------------------------------------------------------------

class ListSensorNamesIds(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        return json.dumps([{"name": s["name"], "sensor_id": s["id"]} for s in data.get("sensors", [])], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_sensor_names_ids",
                "description": "Return all sensors' names and ids (state is read-only).",
                "parameters": {"type": "object", "properties": {}, "required": [], "additionalProperties": False},
            },
        }


# ---------------------------------------------------------------------------
# 17. Get immutable sensor state
# ---------------------------------------------------------------------------

class GetSensorState(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], sensor_id: str) -> str:
        for sen in data.get("sensors", []):
            if sen["id"] == sensor_id:
                return json.dumps({"state": sen["state"]}, indent=2)
        return json.dumps({"error": "Sensor not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_sensor_state",
                "description": "Read current state values for a sensor (read-only).",
                "parameters": {
                    "type": "object",
                    "properties": {"sensor_id": {"type": "string", "description": "Sensor identifier."}},
                    "required": ["sensor_id"],
                    "additionalProperties": False,
                },
            },
        }


# ---------------------------------------------------------------------------
# 18. Manage custom lists (create / list / delete)
# ---------------------------------------------------------------------------

class ManageCustomList(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], action: str, list_id: str,  tags: List[str], name: str = None) -> str:
        lists_doc: List[Dict[str, Any]] = data.get("custom_lists", [])
        if action == "list_all_names_ids":
            return json.dumps({"lists": [{"name": l["name"], "list_id": l["list_id"]} for l in lists_doc]}, indent=2)
        if action == "get":
            lst = next((l for l in lists_doc if l["list_id"] == list_id), None)
            return json.dumps({"list": lst} if lst else {"error": "List not found"}, indent=2)
        if action == "delete":
            new_doc = [l for l in lists_doc if l["list_id"] != list_id]
            if len(new_doc) == len(lists_doc):
                return json.dumps({"error": "List not found"}, indent=2)
            data["custom_lists"] = new_doc
            return json.dumps({"success": True}, indent=2)
        if action == "create":
            if not all([name, list_id]):
                return json.dumps({"error": "name and list_id required"}, indent=2)
            if any(l["list_id"] == list_id for l in lists_doc):
                return json.dumps({"error": "Duplicate list_id"}, indent=2)
            lists_doc.append({
                "list_id": list_id,
                "name": name,
                "created_at": _now_iso(),
                "updated_at": _now_iso(),
                "tags": tags,
                "items": [],
            })
            data["custom_lists"] = lists_doc
            return json.dumps({"success": True}, indent=2)
        return json.dumps({"error": "Unknown or missing action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_custom_list",
                "description": "Create, fetch, delete, or list custom lists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["list_all_names_ids", "get (requires list_id)", "create (requires list_id, name, tags)", "delete (requires list_id)"]},
                        "list_id": {"type": "string", "description": "List identifier."},
                        "name": {"type": "string", "description": "List name."},
                        "tags": {"type": "array", "items": {"type": "string", "description": "List tags."}},
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }


# ---------------------------------------------------------------------------
# 19. Manage items in a custom list (add / remove / update / list)
# ---------------------------------------------------------------------------

class ManageListItems(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], list_id: str, action: str, items: List[str], quantities: Dict[str, int]) -> str:
        target = next((l for l in data.get("custom_lists", []) if l["list_id"] == list_id), None)
        if not target:
            return json.dumps({"error": "List not found"}, indent=2)
        if action == "list":
            return json.dumps({"items": target["items"]}, indent=2)
        if action == "add_items":
            if not items:
                return json.dumps({"error": "items array required"}, indent=2)
            target["items"].extend([{"item": item, "quantity": 1} for item in items])
        elif action == "remove_items":
            if not items:
                return json.dumps({"error": "items array required"}, indent=2)
            target["items"] = [itm for itm in target["items"] if itm["item"] not in items]
        elif action == "set_quantity":
            updates: Dict[str, int] = quantities
            for itm in target["items"]:
                if itm["item"] in updates:
                    itm["quantity"] = updates[itm["item"]]
        else:
            return json.dumps({"error": "Unsupported action"}, indent=2)
        target["updated_at"] = _now_iso()
        return json.dumps({"success": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_list_items",
                "description": "Add, remove, list, or update quantities of items in a custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "string", "description": "List identifier."},
                        "action": {"type": "string", "enum": ["list", "add_items (requires items) (default quantity 1)", "remove_items (requires items)", "set_quantity (requires quantities)"]},
                        "items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "For add/remove actions: array of item names",
                        },
                        "quantities": {"type": "object", "description": "Mapping of item name → new quantity for set_quantity."},
                    },
                    "required": ["list_id", "action"],
                    "additionalProperties": False,
                },
            },
        }


# ---------------------------------------------------------------------------
# 20. Manage reminders (list / get / create / update / delete)
# ---------------------------------------------------------------------------

class ManageReminders(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], action: str, reminder_id: Optional[str] = None, reminder: Optional[Dict[str, Any]] = None, updates: Optional[Dict[str, Any]] = None) -> str:
        reminders = data.get("reminders", [])
        if action == "list_all_names_ids":
            return json.dumps({"reminders": [{"name": r["name"], "reminder_id": r["reminder_id"]} for r in reminders]}, indent=2)
        if action == "get":
            r = next((r for r in reminders if r["reminder_id"] == reminder_id), None)
            return json.dumps({"reminder": r} if r else {"error": "not found"}, indent=2)
        if action == "delete":
            new_doc = [r for r in reminders if r["reminder_id"] != reminder_id]
            if len(new_doc) == len(reminders):
                return json.dumps({"error": "not found"}, indent=2)
            data["reminders"] = new_doc
            return json.dumps({"success": True}, indent=2)
        if action == "create":
            if not reminder or "reminder_id" not in reminder:
                return json.dumps({"error": "reminder object with reminder_id required"}, indent=2)
            if any(r["reminder_id"] == reminder["reminder_id"] for r in reminders):
                return json.dumps({"error": "Duplicate id"}, indent=2)
            reminders.append(reminder)
            data["reminders"] = reminders
            return json.dumps({"success": True}, indent=2)
        if action == "update":
            modified = False
            for r in reminders:
                if r["reminder_id"] == reminder_id:
                    r.update(updates)
                    modified = True
                    break
            if not modified:
                return json.dumps({"error": "not found"}, indent=2)
            data["reminders"] = reminders
            return json.dumps({"success": True}, indent=2)
        return json.dumps({"error": "Unknown action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_reminders",
                "description": "Create, list, get, update, or delete reminders.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["list_all_names_ids", "get (requires reminder_id)", "create (requires reminder_id, reminder)", "update (requires reminder_id, updates)", "delete (requires reminder_id)"]},
                        "reminder_id": {"type": "string", "description": "Reminder identifier."},
                        "reminder": {"type": "object", "description": "Key/value pairs of reminder."},
                        "updates": {"type": "object", "description": "Key/value pairs of updates."},
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
# ---------------------------------------------------------------------------
# 21. Append or replace a scheduled update for a device with a time to end.
# ---------------------------------------------------------------------------

class ScheduleDeviceTimerUpdate(Tool):
    """Add or replace a future scheduled update for a device."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        device_id: str,
        timestamp: str,
        timestamp_end:str,
        update: Dict[str, Any],
        replace: bool = False,
        rrule: Optional[str] = None,
    ) -> str:
        devices: List[Dict[str, Any]] = data.get("devices", [])
        for dev in devices:
            if dev.get("id") == device_id:
                if timestamp_end == None:
                    return json.dumps({"error": "End time is needed"}, indent=2)

                # Set Device as its needed
                sched: List[Dict[str, Any]] = dev.setdefault("scheduled_updates", [])
                if replace:
                    sched[:] = [s for s in sched if s.get("timestamp") != timestamp]
                if rrule:
                    sched.append({"timestamp": timestamp, "update": update, "rrule": rrule})
                else:
                    sched.append({"timestamp": timestamp, "update": update})
                ScheduleDeviceUpdate.invoke(data, device_id, timestamp_end, {"power": "off"}, replace, rrule)
                return json.dumps({"success": True, "scheduled_updates": sched}, indent=2)


        return json.dumps({"error": f"Device '{device_id}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_device_update_timer",
                "description": "Add or replace a future scheduled update for a device that only bee on for a time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "Device identifier."},
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
    ScheduleDeviceTimerUpdate()
]
