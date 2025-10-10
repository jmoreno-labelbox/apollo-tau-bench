import json
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from domains.dto import Tool

# -------------------------------------------------------------
# Helper utilities (simple in-memory manipulation; persistence
# responsibility is delegated to the caller or outer framework)
# -------------------------------------------------------------

def _load(entity: str, data: Dict[str, Any]):
    """Return a *mutable copy* of a top-level collection list."""
    return [*data.get(entity, [])]


def _find(collection: List[Dict[str, Any]], entity_id: str):
    for idx, item in enumerate(collection):
        if item.get("id") == entity_id or item.get("reminder_id") == entity_id \
           or item.get("list_id") == entity_id or item.get("member_id") == entity_id:
            return idx, item
    return None, None

def _now_iso() -> str:
    # return datetime.now(timezone.utc).isoformat()
    return "deterministic placeholder for current time"

# -------------------------------------------------------------
# 1. GetEntity – generic read‑only fetch for any entity type
# -------------------------------------------------------------
class GetEntity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], entity_type: str, entity_id: Optional[str] = None) -> str:
        collection = data.get(entity_type)
        if collection is None:
            return json.dumps({"error": f"unknown entity_type '{entity_type}'"}, indent=2)
        if entity_id:
            _, item = _find(collection, entity_id)
            if not item:
                return json.dumps({"error": f"{entity_type} '{entity_id}' not found"}, indent=2)
        else:
            item = collection
        return json.dumps(item, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_entity",
                "description": "Fetch a single entity (device, sensor, room, scene, list, reminder, member) by id. If no id is provided, return all entities of the given type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entity_type": {
                            "type": "string",
                            "description": "One of: devices, sensors, rooms, scenes, custom_lists, reminders, members"
                        },
                        "entity_id": {
                            "type": "string",
                            "description": "ID of the entity to fetch"
                        }
                    },
                    "required": ["entity_type"],
                    "additionalProperties": False
                }
            }
        }

# -----------------------------------------------------------------
# 2. QueryEntities – filtered search across collections
# -----------------------------------------------------------------
class QueryEntities(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], entity_type: str, filters: Dict[str, Any]) -> str:
        collection = data.get(entity_type, [])
        matches: List[Dict[str, Any]] = []
        for item in collection:
            ok = True
            for k, v in filters.items():
                if item.get(k) != v:
                    ok = False
                    break
            if ok:
                matches.append(item)
        return json.dumps({"count": len(matches), "results": matches}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "query_entities",
                "description": "Return all entities of a given type that match simple equality filters (top-level keys).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entity_type": {
                            "type": "string",
                            "description": "Collection to search: devices, sensors, rooms, scenes, custom_lists, reminders, members"
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key/value pairs that must match (equality) on each entity.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["entity_type"],
                    "additionalProperties": False
                }
            }
        }

# -----------------------------------------------------------------
# 3. UpsertDevice – add *or* update a device definition
# -----------------------------------------------------------------
class UpsertDevice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device: Dict[str, Any]) -> str:
        if not device or not isinstance(device, dict):
            return json.dumps({"error": "device object required"}, indent=2)
        devices = _load("devices", data)
        idx, _old = _find(devices, device["id"])
        if idx is not None:
            devices[idx].update(device)
            action = "updated"
        else:
            devices.append(device)
            action = "added"
            data["devices"] = devices
        return json.dumps({"success": f"device {action}", "device": device}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_device",
                "description": "Create a new device or update an existing one (metadata only; state changes use modify_device_state).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "upsert_scene": {
                            "type": "object",
                            "description": "Full or partial device object following the schema in devices.json.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["device"],
                    "additionalProperties": False
                }
            }
        }

# -----------------------------------------------------------------
# 4. DeleteDevice – remove a device (also prunes from rooms)
# -----------------------------------------------------------------
class DeleteDevice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str) -> str:
        devices = _load("devices", data)
        idx, _ = _find(devices, device_id)
        if idx is None:
            return json.dumps({"error": f"device '{device_id}' not found"}, indent=2)
        removed = devices.pop(idx)
        # prune from rooms
        for room in data.get("rooms", []):
            if device_id in room.get("devices", []):
                room["devices"].remove(device_id)
        return json.dumps({"success": "device deleted", "device": removed}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_device",
                "description": "Remove a device from the home. If present in any room, it will be detached as well.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "ID of device to delete"}
                    },
                    "required": ["device_id"],
                    "additionalProperties": False
                }
            }
        }

# ---------------------------------------------------------------------
# 5. ModifyDeviceState – edit device.state or schedule future update
# ---------------------------------------------------------------------
class ModifyDeviceState(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str, update: Dict[str, Any], schedule_at: Optional[str] = None, rrule: Optional[str] = None, timestamp: Optional[str] = None) -> str:

        devices = data.get("devices", [])
        idx, device = _find(devices, device_id)
        if not device:
            return json.dumps({"error": f"device '{device_id}' not found"}, indent=2)
        allowed = set(device.get("state_params", []))
        if any(k not in allowed for k in update):
            return json.dumps({"error": "one or more params not allowed for this device"}, indent=2)

        if schedule_at:
            device.setdefault("scheduled_updates", []).append({
                "timestamp": schedule_at,
                "update": update,
                **({"rrule": rrule} if rrule else {})
            })
            return json.dumps({"success": "scheduled", "scheduled_update": device["scheduled_updates"][-1]}, indent=2)
        else:
            device_state = device.get("state", {})
            device_state.update(update)
            device_state["last_updated"] = timestamp or _now_iso()
            return json.dumps({"success": "state updated"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_device_state",
                "description": "Update the live state of a device, or schedule a future state change.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "Target device id"},
                        "update": {
                            "type": "object",
                            "description": "Subset of allowed state params and their new values.",
                            "additionalProperties": True
                        },
                        "schedule_at": {
                            "type": "string",
                            "description": "Optional ISO8601 timestamp for when to apply the update"
                        },
                        "rrule": {
                            "type": "string",
                            "description": "Optional recurrence rule (RFC5545) if schedule_at is provided"
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "Override the 'last_updated' timestamp when updating immediately"
                        }
                    },
                    "required": ["device_id", "update"],
                    "additionalProperties": False
                }
            }
        }
# ---------------------------------------------------------------------
# 5.1 ModifyDeviceState – edit device.state or schedule future update, then schedule a power off
# ---------------------------------------------------------------------
class ModifyDeviceStateTimer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], device_id: str, schedule_end: str, update: Dict[str, Any], schedule_at: Optional[str] = None,  rrule: Optional[str] = None, timestamp: Optional[str] = None) -> str:

        devices = data.get("devices", [])
        idx, device = _find(devices, device_id)
        if not schedule_end:
            return json.dumps({"error": f"end time is required"}, indent=2)
        if not device:
            return json.dumps({"error": f"device '{device_id}' not found"}, indent=2)
        allowed = set(device.get("state_params", []))
        if any(k not in allowed for k in update):
            return json.dumps({"error": "one or more params not allowed for this device"}, indent=2)

        if schedule_at:
            device.setdefault("scheduled_updates", []).append({
                "timestamp": schedule_at,
                "update": update,
                **({"rrule": rrule} if rrule else {})
            })
            ModifyDeviceState.invoke(data, device_id, {"power": "off"}, schedule_end, rrule, timestamp)
            return json.dumps({"success": "scheduled", "scheduled_update": device["scheduled_updates"][-1]}, indent=2)
        else:
            device_state = device.get("state", {})
            device_state.update(update)
            device_state["last_updated"] = timestamp or _now_iso()
            ModifyDeviceState.invoke(data, device_id, {"power": "off"}, schedule_end, rrule, timestamp)
            return json.dumps({"success": "state updated"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_device_state_timer",
                "description": "Update the live state of a device, or schedule a future state change, then schedule the device to power off.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {"type": "string", "description": "Target device id"},
                        "schedule_at": {
                            "type": "string",
                            "description": "ISO8601 timestamp for when to apply the power off"
                        },
                        "update": {
                            "type": "object",
                            "description": "Subset of allowed state params and their new values.",
                            "additionalProperties": True
                        },
                        "schedule_at": {
                            "type": "string",
                            "description": "Optional ISO8601 timestamp for when to apply the update"
                        },
                        "rrule": {
                            "type": "string",
                            "description": "Optional recurrence rule (RFC5545) if schedule_at is provided"
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "Override the 'last_updated' timestamp when updating immediately"
                        }
                    },
                    "required": ["device_id", "update", "schedule_end"],
                    "additionalProperties": False
                }
            }
        }
# ----------------------------------------------------------
# 6. AddDeviceToRoom – attach device to a room
# ----------------------------------------------------------
class AddDeviceToRoom(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], room_id: str, device_id: str) -> str:
        rooms = data.get("rooms", [])
        _, room = _find(rooms, room_id)
        if not room:
            return json.dumps({"error": f"room '{room_id}' not found"}, indent=2)
        # verify device exists
        if not _find(data.get("devices", []), device_id)[1]:
            return json.dumps({"error": f"device '{device_id}' not found"}, indent=2)
        if device_id in room.get("devices", []):
            return json.dumps({"warning": "device already in room"}, indent=2)
        room.setdefault("devices", []).append(device_id)
        return json.dumps({"success": f"device '{device_id}' added to room '{room_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_device_to_room",
                "description": "Associate an existing device with a room (physical placement).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {"type": "string", "description": "Room id"},
                        "device_id": {"type": "string", "description": "Device id"}
                    },
                    "required": ["room_id", "device_id"],
                    "additionalProperties": False
                }
            }
        }

# ------------------------------------------------------------------
# 7. RemoveDeviceFromRoom – detach a device from a room
# ------------------------------------------------------------------
class RemoveDeviceFromRoom(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], room_id: str, device_id: str) -> str:
        _, room = _find(data.get("rooms", []), room_id)
        if not room:
            return json.dumps({"error": f"room '{room_id}' not found"}, indent=2)
        if device_id not in room.get("devices", []):
            return json.dumps({"error": f"device '{device_id}' not in room"}, indent=2)
        room["devices"].remove(device_id)
        return json.dumps({"success": f"device '{device_id}' removed from room '{room_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_device_from_room",
                "description": "Detach a device from a room without deleting the device itself.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {"type": "string", "description": "Room id"},
                        "device_id": {"type": "string", "description": "Device id"}
                    },
                    "required": ["room_id", "device_id"],
                    "additionalProperties": False
                }
            }
        }

# --------------------------------------------------------------
# 8. UpsertScene – create or modify a scene definition
# --------------------------------------------------------------
class UpsertScene(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], scene: Dict[str, Any]) -> str:
        if not scene:
            return json.dumps({"error": "scene object required"}, indent=2)
        scenes = _load("scenes", data)
        idx, _ = _find(scenes, scene["id"])
        if idx is not None:
            scenes[idx].update(scene)
            msg = "updated"
        else:
            scenes.append(scene)
            msg = "added"
            data["scenes"] = scenes
        return json.dumps({"success": f"scene {msg}", "scene": scene}, indent=2)

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
                        "scene": {
                            "type": "object",
                            "description": "Full or partial scene object.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["scene"],
                    "additionalProperties": False
                }
            }
        }

# --------------------------------------------------------
# 9. RunScene – execute a scene immediately (simulation)
# --------------------------------------------------------
class RunScene(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str) -> str:
        _, scene = _find(data.get("scenes", []), scene_id)
        if not scene:
            return json.dumps({"error": f"scene '{scene_id}' not found"}, indent=2)
        results = []
        for act in scene.get("actions", []):
            res = ModifyDeviceState.invoke(data, device_id=act["device_id"], update=act["update"])
            results.append(json.loads(res))
        return json.dumps({"success": f"scene '{scene_id}' executed", "results": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "run_scene",
                "description": "Execute the actions of a scene immediately.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {"type": "string", "description": "Scene id to run"}
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False
                }
            }
        }

# -----------------------------------------------------------------
# 10. UpsertCustomList – create or update a custom list entity
# -----------------------------------------------------------------
class UpsertCustomList(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], custom_list: Dict[str, Any]) -> str:
        if not custom_list:
            return json.dumps({"error": "custom_list object required"}, indent=2)
        lists = _load("custom_lists", data)
        idx, _ = _find(lists, custom_list["list_id"])
        if idx is not None:
            lists[idx].update(custom_list)
            msg = "updated"
        else:
            lists.append(custom_list)
            msg = "added"
            data["custom_lists"] = lists
        return json.dumps({"success": f"list {msg}", "list": custom_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_custom_list",
                "description": "Create a new custom list or update an existing one (metadata & tags, not line-items).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "custom_list": {
                            "type": "object",
                            "description": "Full or partial custom list object.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["custom_list"],
                    "additionalProperties": False
                }
            }
        }

# ---------------------------------------------------------------------
# 11. ModifyCustomListItem – add/update/remove an item in a list
# ---------------------------------------------------------------------
class ModifyCustomListItem(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: str, item: Dict[str, Any], action: str = "add") -> str:
        lists = data.get("custom_lists", [])
        _, lst = _find(lists, list_id)
        if not lst:
            return json.dumps({"error": f"list '{list_id}' not found"}, indent=2)
        items = lst.setdefault("items", [])
        # locate existing item by name
        idx = next((i for i, it in enumerate(items) if it["item"] == item.get("item")), None)
        if action == "add":
            if idx is not None:
                return json.dumps({"error": "item already exists"}, indent=2)
            items.append(item)
        elif action == "update":
            if idx is None:
                return json.dumps({"error": "item not found"}, indent=2)
            items[idx].update(item)
        elif action == "remove":
            if idx is None:
                return json.dumps({"error": "item not found"}, indent=2)
            items.pop(idx)
        else:
            return json.dumps({"error": "invalid action"}, indent=2)
        return json.dumps({"success": f"item {action}ed", "items": items}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_custom_list_item",
                "description": "Add, update, or remove a single item in a custom list by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "string", "description": "Target list id"},
                        "item": {
                            "type": "object",
                            "description": "Item object with 'item' (name) and optional 'quantity'.",
                            "additionalProperties": True
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "update", "remove"],
                            "description": "Operation to perform"
                        }
                    },
                    "required": ["list_id", "item", "action"],
                    "additionalProperties": False
                }
            }
        }

# --------------------------------------------------------------
# 12. UpsertReminder – create or update a reminder object
# --------------------------------------------------------------
class UpsertReminder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reminder: Dict[str, Any]) -> str:
        if not reminder:
            return json.dumps({"error": "reminder object required"}, indent=2)
        reminders = _load("reminders", data)
        idx, _ = _find(reminders, reminder["reminder_id"])
        if idx is not None:
            reminders[idx].update(reminder)
            msg = "updated"
        else:
            reminders.append(reminder)
            msg = "added"
            data["reminders"] = reminders
        return json.dumps({"success": f"reminder {msg}", "reminder": reminder}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_reminder",
                "description": "Create a new reminder or update an existing one.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder": {
                            "type": "object",
                            "description": "Full or partial reminder object.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["reminder"],
                    "additionalProperties": False
                }
            }
        }

# ---------------------------------------------------------
# 13. DeleteReminder – remove a reminder
# ---------------------------------------------------------
class DeleteReminder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reminder_id: str) -> str:
        reminders = _load("reminders", data)
        idx, rem = _find(reminders, reminder_id)
        if idx is None:
            return json.dumps({"error": "reminder not found"}, indent=2)
        reminders.pop(idx)
        data["reminders"] = reminders
        return json.dumps({"success": "reminder deleted", "reminder": rem}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_reminder",
                "description": "Delete a reminder by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {"type": "string", "description": "Reminder id"}
                    },
                    "required": ["reminder_id"],
                    "additionalProperties": False
                }
            }
        }

# --------------------------------------------------------------
# 14. UpsertMember – create/update household member data
# --------------------------------------------------------------
class UpsertMember(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], member: Dict[str, Any]) -> str:
        if not member:
            return json.dumps({"error": "member object required"}, indent=2)
        members = _load("members", data)
        idx, _ = _find(members, member["id"])
        if idx is not None:
            members[idx].update(member)
            msg = "updated"
        else:
            members.append(member)
            msg = "added"
            data["members"] = members
        return json.dumps({"success": f"member {msg}", "member": member}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_member",
                "description": "Create or update a household member record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member": {
                            "type": "object",
                            "description": "Full or partial member object.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["member"],
                    "additionalProperties": False
                }
            }
        }

# --------------------------------------------------------------
# 15. ModifySensorState – update a sensor's state
# --------------------------------------------------------------
class ModifySensorState(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sensor_id: str, update: Dict[str, Any]) -> str:
        sensors = data.get("sensors", [])
        _, sensor = _find(sensors, sensor_id)
        if not sensor:
            return json.dumps({"error": f"sensor '{sensor_id}' not found"}, indent=2)
        allowed = set(sensor.get("state_params", []))
        if any(k not in allowed for k in update):
            return json.dumps({"error": "one or more params not allowed for this sensor"}, indent=2)
        sensor_state = sensor.get("state", {})
        sensor_state.update(update)
        sensor_state["last_updated"] = _now_iso()
        return json.dumps({"success": "state updated", "state": sensor_state}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_sensor_state",
                "description": "Update the live state of a sensor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor_id": {"type": "string", "description": "Target sensor id"},
                        "update": {
                            "type": "object",
                            "description": "Subset of allowed state params and their new values.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["sensor_id", "update"],
                    "additionalProperties": False
                }
            }
        }

# --------------------------------------------------------------
# --------------- END OF 15 TOOL DEFINITIONS -------------------
# --------------------------------------------------------------

TOOLS = [
    GetEntity(),
    QueryEntities(),
    UpsertDevice(),
    DeleteDevice(),
    ModifyDeviceState(),
    ModifyDeviceStateTimer(),
    AddDeviceToRoom(),
    RemoveDeviceFromRoom(),
    UpsertScene(),
    RunScene(),
    UpsertCustomList(),
    ModifyCustomListItem(),
    UpsertReminder(),
    DeleteReminder(),
    UpsertMember(),
    ModifySensorState(),
]
