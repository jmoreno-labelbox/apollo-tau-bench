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
    #return datetime.now(timezone.utc).isoformat()
    return "deterministic placeholder for current time"

#-------------------------------------------------------------
#Utility functions for basic in-memory handling and persistence
#the caller or external framework takes on the responsibility)
#-------------------------------------------------------------


def _load(entity: str, data: dict[str, Any]):
    """Provide a *modifiable copy* of a top-level collection list."""
    pass
    return [*data.get(entity, {}).values()]


def _find(collection: list[dict[str, Any]], entity_id: str):
    pass
    for idx, item in enumerate(collection):
        if (
            item.get("id") == entity_id
            or item.get("reminder_id") == entity_id
            or item.get("list_id") == entity_id
            or item.get("member_id") == entity_id
        ):
            return idx, item
    return None, None


#-------------------------------------------------------------
#1. GetEntity – a general read-only retrieval for any type of entity
#-------------------------------------------------------------
class GetEntity(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], entity_type: str, entity_id: str | None = None
    ) -> str:
        collection = data.get(entity_type)
        if collection is None:
            payload = {"error": f"unknown entity_type '{entity_type}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if entity_id:
            _, item = _find(collection, entity_id)
            if not item:
                payload = {"error": f"{entity_type} '{entity_id}' not found"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        else:
            item = collection
        payload = item
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEntity",
                "description": "Fetch a single entity (device, sensor, room, scene, list, reminder, member) by id. If no id is provided, return all entities of the given type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entity_type": {
                            "type": "string",
                            "description": "One of: devices, sensors, rooms, scenes, custom_lists, reminders, members",
                        },
                        "entity_id": {
                            "type": "string",
                            "description": "ID of the entity to fetch",
                        },
                    },
                    "required": ["entity_type"],
                    "additionalProperties": False,
                },
            },
        }


#-----------------------------------------------------------------
#2. QueryEntities – a filtered search through various collections
#-----------------------------------------------------------------
class QueryEntities(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], entity_type: str, filters: dict[str, Any]) -> str:
        collection = data.get(entity_type, {}).values()
        matches: list[dict[str, Any]] = []
        for item in collection:
            ok = True
            for k, v in filters.items():
                if item.get(k) != v:
                    ok = False
                    break
            if ok:
                matches.append(item)
        payload = {"count": len(matches), "results": matches}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "QueryEntities",
                "description": "Return all entities of a given type that match simple equality filters (top-level keys).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entity_type": {
                            "type": "string",
                            "description": "Collection to search: devices, sensors, rooms, scenes, custom_lists, reminders, members",
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key/value pairs that must match (equality) on each entity.",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["entity_type"],
                    "additionalProperties": False,
                },
            },
        }


#-----------------------------------------------------------------
#3. UpsertDevice – either add or modify a device definition
#-----------------------------------------------------------------
class UpsertDevice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], device: dict[str, Any]) -> str:
        if not device or not isinstance(device, dict):
            payload = {"error": "device object required"}
            out = json.dumps(payload, indent=2)
            return out
        devices = _load("devices", data)
        idx, _old = _find(devices, device["id"])
        if idx is not None:
            devices[idx].update(device)
            action = "updated"
        else:
            data["devices"][device_id] = device
            action = "added"
            data["devices"] = devices
        payload = {"success": f"device {action}", "device": device}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertDevice",
                "description": "Create a new device or update an existing one (metadata only; state changes use modify_device_state).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "UpsertScene": {
                            "type": "object",
                            "description": "Full or partial device object following the schema in devices.json.",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["device"],
                    "additionalProperties": False,
                },
            },
        }


#-----------------------------------------------------------------
#4. DeleteDevice – eliminate a device (also removes from rooms)
#-----------------------------------------------------------------
class DeleteDevice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], device_id: str, rooms: list[dict[str, Any]] = None) -> str:
        devices = _load("devices", data)
        idx, _ = _find(devices, device_id)
        if idx is None:
            payload = {"error": f"device '{device_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        removed = devices.pop(idx)
        # remove from rooms
        for room in (rooms or []):
            if device_id in room.get("devices", []):
                room["devices"].remove(device_id)
        payload = {"success": "device deleted", "device": removed}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteDevice",
                "description": "Remove a device from the home. If present in any room, it will be detached as well.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "ID of device to delete",
                        }
                    },
                    "required": ["device_id"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------
#5. ModifyDeviceState – change device.state or plan a future update
#---------------------------------------------------------------------
class ModifyDeviceState(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        device_id: str,
        update: dict[str, Any],
        schedule_at: str | None = None,
        rrule: str | None = None,
        timestamp: str | None = None,
    ) -> str:
        devices = data.get("devices", {}).values()
        idx, device = _find(devices, device_id)
        if not device:
            payload = {"error": f"device '{device_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        allowed = set(device.get("state_params", []))
        if any(k not in allowed for k in update.values()):
            payload = {"error": "one or more params not allowed for this device"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if schedule_at:
            device.setdefault("scheduled_updates", []).append(
                {
                    "timestamp": schedule_at,
                    "update": update,
                    **({"rrule": rrule} if rrule else {}),
                }
            )
            payload = {
                    "success": "scheduled",
                    "scheduled_update": device["scheduled_updates"][-1],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            device_state = device.get("state", {}).values()
            device_state.update(update)
            device_state["last_updated"] = timestamp or _now_iso()
            payload = {"success": "state updated"}
            out = json.dumps(payload, indent=2)
            return out

        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ModifyDeviceState",
                "description": "Update the live state of a device, or schedule a future state change.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "Target device id",
                        },
                        "update": {
                            "type": "object",
                            "description": "Subset of allowed state params and their new values.",
                            "additionalProperties": True,
                        },
                        "schedule_at": {
                            "type": "string",
                            "description": "Optional ISO8601 timestamp for when to apply the update",
                        },
                        "rrule": {
                            "type": "string",
                            "description": "Optional recurrence rule (RFC5545) if schedule_at is provided",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "Override the 'last_updated' timestamp when updating immediately",
                        },
                    },
                    "required": ["device_id", "update"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------
#5.1 ModifyDeviceState – adjust device.state or plan a future update, followed by scheduling a power off
#---------------------------------------------------------------------
class ModifyDeviceStateTimer(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        device_id: str,
        schedule_end: str,
        update: dict[str, Any],
        schedule_at: str | None = None,
        rrule: str | None = None,
        timestamp: str | None = None,
    ) -> str:
        devices = data.get("devices", {}).values()
        idx, device = _find(devices, device_id)
        if not schedule_end:
            payload = {"error": "end time is required"}
            out = json.dumps(payload, indent=2)
            return out
        if not device:
            payload = {"error": f"device '{device_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        allowed = set(device.get("state_params", []))
        if any(k not in allowed for k in update.values()):
            payload = {"error": "one or more params not allowed for this device"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if schedule_at:
            device.setdefault("scheduled_updates", []).append(
                {
                    "timestamp": schedule_at,
                    "update": update,
                    **({"rrule": rrule} if rrule else {}),
                }
            )
            ModifyDeviceState.invoke(
                data, device_id, {"power": "off"}, schedule_end, rrule, timestamp
            )
            payload = {
                    "success": "scheduled",
                    "scheduled_update": device["scheduled_updates"][-1],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            device_state = device.get("state", {}).values()
            device_state.update(update)
            device_state["last_updated"] = timestamp or _now_iso()
            ModifyDeviceState.invoke(
                data, device_id, {"power": "off"}, schedule_end, rrule, timestamp
            )
            payload = {"success": "state updated"}
            out = json.dumps(payload, indent=2)
            return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ModifyDeviceStateTimer",
                "description": "Update the live state of a device, or schedule a future state change, then schedule the device to power off.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "device_id": {
                            "type": "string",
                            "description": "Target device id",
                        },
                        "schedule_at": {
                            "type": "string",
                            "description": "ISO8601 timestamp for when to apply the power off",
                        },
                        "update": {
                            "type": "object",
                            "description": "Subset of allowed state params and their new values.",
                            "additionalProperties": True,
                        },
                        "schedule_at": {
                            "type": "string",
                            "description": "Optional ISO8601 timestamp for when to apply the update",
                        },
                        "rrule": {
                            "type": "string",
                            "description": "Optional recurrence rule (RFC5545) if schedule_at is provided",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "Override the 'last_updated' timestamp when updating immediately",
                        },
                    },
                    "required": ["device_id", "update", "schedule_end"],
                    "additionalProperties": False,
                },
            },
        }


#----------------------------------------------------------
#6. AddDeviceToRoom – connect a device to a room
#----------------------------------------------------------
class AddDeviceToRoom(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], room_id: str, device_id: str,
    new_device: Any = None,
    ) -> str:
        rooms = data.get("rooms", {}).values()
        _, room = _find(rooms, room_id)
        if not room:
            payload = {"error": f"room '{room_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        # check if the device is present
        if not _find(data.get("devices", {}).values()), device_id)[1]:
            payload = {"error": f"device '{device_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        if device_id in room.get("devices", []):
            payload = {"warning": "device already in room"}
            out = json.dumps(payload, indent=2)
            return out
        room.setdefault("devices", []).append(device_id)
        payload = {"success": f"device '{device_id}' added to room '{room_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddDeviceToRoom",
                "description": "Associate an existing device with a room (physical placement).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {"type": "string", "description": "Room id"},
                        "device_id": {"type": "string", "description": "Device id"},
                    },
                    "required": ["room_id", "device_id"],
                    "additionalProperties": False,
                },
            },
        }


#------------------------------------------------------------------
#7. RemoveDeviceFromRoom – disconnect a device from a room
#------------------------------------------------------------------
class RemoveDeviceFromRoom(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], room_id: str, device_id: str) -> str:
        _, room = _find(data.get("rooms", {}).values()), room_id)
        if not room:
            payload = {"error": f"room '{room_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        if device_id not in room.get("devices", []):
            payload = {"error": f"device '{device_id}' not in room"}
            out = json.dumps(payload, indent=2)
            return out
        room["devices"].remove(device_id)
        payload = {"success": f"device '{device_id}' removed from room '{room_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeDeviceFromRoom",
                "description": "Detach a device from a room without deleting the device itself.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "room_id": {"type": "string", "description": "Room id"},
                        "device_id": {"type": "string", "description": "Device id"},
                    },
                    "required": ["room_id", "device_id"],
                    "additionalProperties": False,
                },
            },
        }


#--------------------------------------------------------------
#8. UpsertScene – establish or alter a scene definition
#--------------------------------------------------------------
class UpsertScene(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], scene: dict[str, Any]) -> str:
        if not scene:
            payload = {"error": "scene object required"}
            out = json.dumps(payload, indent=2)
            return out
        scenes = _load("scenes", data)
        idx, _ = _find(scenes, scene["id"])
        if idx is not None:
            scenes[idx].update(scene)
            msg = "updated"
        else:
            scenes.append(scene)
            msg = "added"
            data["scenes"] = scenes
        payload = {"success": f"scene {msg}", "scene": scene}
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
                        "scene": {
                            "type": "object",
                            "description": "Full or partial scene object.",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["scene"],
                    "additionalProperties": False,
                },
            },
        }


#--------------------------------------------------------
#9. RunScene – trigger a scene right away (simulation)
#--------------------------------------------------------
class RunScene(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], scene_id: str) -> str:
        _, scene = _find(data.get("scenes", {}).values()), scene_id)
        if not scene:
            payload = {"error": f"scene '{scene_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        results = []
        for act in scene.get("actions", []):
            res = ModifyDeviceState.invoke(
                data, device_id=act["device_id"], update=act["update"]
            )
            results.append(json.loads(res))
        payload = {"success": f"scene '{scene_id}' executed", "results": results}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RunScene",
                "description": "Execute the actions of a scene immediately.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {"type": "string", "description": "Scene id to run"}
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False,
                },
            },
        }


#-----------------------------------------------------------------
#10. UpsertCustomList – generate or modify a custom list entity
#-----------------------------------------------------------------
class UpsertCustomList(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], custom_list: dict[str, Any]) -> str:
        if not custom_list:
            payload = {"error": "custom_list object required"}
            out = json.dumps(payload, indent=2)
            return out
        lists = _load("custom_lists", data)
        idx, _ = _find(lists, custom_list["list_id"])
        if idx is not None:
            lists[idx].update(custom_list)
            msg = "updated"
        else:
            data["custom_lists"][custom_list["custom_list_id"]] = custom_list
            msg = "added"
            data["custom_lists"] = lists
        payload = {"success": f"list {msg}", "list": custom_list}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertCustomList",
                "description": "Create a new custom list or update an existing one (metadata & tags, not line-items).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "custom_list": {
                            "type": "object",
                            "description": "Full or partial custom list object.",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["custom_list"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------------------
#11. ModifyCustomListItem – add, update, or delete an item in a list
#---------------------------------------------------------------------
class ModifyCustomListItem(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], list_id: str, item: dict[str, Any], action: str = "add"
    ) -> str:
        lists = data.get("custom_lists", {}).values()
        _, lst = _find(lists, list_id)
        if not lst:
            payload = {"error": f"list '{list_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        items = lst.setdefault("items", [])
        # find an existing item using its name
        idx = next(
            (i for i, it in enumerate(items) if it["item"] == item.get("item")), None
        )
        if action == "add":
            if idx is not None:
                payload = {"error": "item already exists"}
                out = json.dumps(payload, indent=2)
                return out
            items.append(item)
        elif action == "update":
            if idx is None:
                payload = {"error": "item not found"}
                out = json.dumps(payload, indent=2)
                return out
            items[idx].update(item)
        elif action == "remove":
            if idx is None:
                payload = {"error": "item not found"}
                out = json.dumps(payload, indent=2)
                return out
            items.pop(idx)
        else:
            payload = {"error": "invalid action"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"success": f"item {action}ed", "items": items}
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ModifyCustomListItem",
                "description": "Add, update, or remove a single item in a custom list by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "string", "description": "Target list id"},
                        "item": {
                            "type": "object",
                            "description": "Item object with 'item' (name) and optional 'quantity'.",
                            "additionalProperties": True,
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "update", "remove"],
                            "description": "Operation to perform",
                        },
                    },
                    "required": ["list_id", "item", "action"],
                    "additionalProperties": False,
                },
            },
        }


#--------------------------------------------------------------
#12. UpsertReminder – establish or modify a reminder object
#--------------------------------------------------------------
class UpsertReminder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], reminder: dict[str, Any]) -> str:
        if not reminder:
            payload = {"error": "reminder object required"}
            out = json.dumps(payload, indent=2)
            return out
        reminders = _load("reminders", data)
        idx, _ = _find(reminders, reminder["reminder_id"])
        if idx is not None:
            reminders[idx].update(reminder)
            msg = "updated"
        else:
            reminders.append(reminder)
            msg = "added"
            data["reminders"] = reminders
        payload = {"success": f"reminder {msg}", "reminder": reminder}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertReminder",
                "description": "Create a new reminder or update an existing one.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder": {
                            "type": "object",
                            "description": "Full or partial reminder object.",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["reminder"],
                    "additionalProperties": False,
                },
            },
        }


#---------------------------------------------------------
#13. DeleteReminder – eliminate a reminder
#---------------------------------------------------------
class DeleteReminder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], reminder_id: str) -> str:
        reminders = _load("reminders", data)
        idx, rem = _find(reminders, reminder_id)
        if idx is None:
            payload = {"error": "reminder not found"}
            out = json.dumps(payload, indent=2)
            return out
        reminders.pop(idx)
        data["reminders"] = reminders
        payload = {"success": "reminder deleted", "reminder": rem}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteReminder",
                "description": "Delete a reminder by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {"type": "string", "description": "Reminder id"}
                    },
                    "required": ["reminder_id"],
                    "additionalProperties": False,
                },
            },
        }


#--------------------------------------------------------------
#14. UpsertMember – create or modify data for a household member
#--------------------------------------------------------------
class UpsertMember(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], member: dict[str, Any]) -> str:
        if not member:
            payload = {"error": "member object required"}
            out = json.dumps(payload, indent=2)
            return out
        members = _load("members", data)
        idx, _ = _find(members, member["id"])
        if idx is not None:
            members[idx].update(member)
            msg = "updated"
        else:
            members.append(member)
            msg = "added"
            data["members"] = members
        payload = {"success": f"member {msg}", "member": member}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertMember",
                "description": "Create or update a household member record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "member": {
                            "type": "object",
                            "description": "Full or partial member object.",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["member"],
                    "additionalProperties": False,
                },
            },
        }


#--------------------------------------------------------------
#15. ModifySensorState – change the state of a sensor
#--------------------------------------------------------------
class ModifySensorState(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sensor_id: str, update: dict[str, Any]) -> str:
        sensors = data.get("sensors", {}).values()
        _, sensor = _find(sensors, sensor_id)
        if not sensor:
            payload = {"error": f"sensor '{sensor_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        allowed = set(sensor.get("state_params", []))
        if any(k not in allowed for k in update.values()):
            payload = {"error": "one or more params not allowed for this sensor"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        sensor_state = sensor.get("state", {}).values()
        sensor_state.update(update)
        sensor_state["last_updated"] = _now_iso()
        payload = {"success": "state updated", "state": sensor_state}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ModifySensorState",
                "description": "Update the live state of a sensor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor_id": {
                            "type": "string",
                            "description": "Target sensor id",
                        },
                        "update": {
                            "type": "object",
                            "description": "Subset of allowed state params and their new values.",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["sensor_id", "update"],
                    "additionalProperties": False,
                },
            },
        }


#--------------------------------------------------------------
#--------------- END OF 15 TOOL DEFINITIONS -------------------
#--------------------------------------------------------------

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
