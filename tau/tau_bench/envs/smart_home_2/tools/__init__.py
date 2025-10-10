# Copyright Sierra

from datetime import datetime


# Helper functions
def _find(items, item_id):
    """Find first item by id. Returns (index, item) or (None, None)."""
    for idx, item in enumerate(items):
        # Check various common ID fields
        if (item.get("id") == item_id or 
            item.get("device_id") == item_id or 
            item.get("sensor_id") == item_id or
            item.get("room_id") == item_id or
            item.get("scene_id") == item_id or
            item.get("list_id") == item_id or
            item.get("reminder_id") == item_id or
            item.get("member_id") == item_id):
            return idx, item
    return None, None


def _now_iso():
    """Return current timestamp in ISO format."""
    return datetime.now().isoformat()

from .get_entity import GetEntity
from .query_entities import QueryEntities
from .upsert_device import UpsertDevice
from .delete_device import DeleteDevice
from .modify_device_state import ModifyDeviceState
from .modify_device_state_timer import ModifyDeviceStateTimer
from .add_device_to_room import AddDeviceToRoom
from .remove_device_from_room import RemoveDeviceFromRoom
from .upsert_scene import UpsertScene
from .run_scene import RunScene
from .upsert_custom_list import UpsertCustomList
from .modify_custom_list_item import ModifyCustomListItem
from .upsert_reminder import UpsertReminder
from .delete_reminder import DeleteReminder
from .upsert_member import UpsertMember
from .modify_sensor_state import ModifySensorState

ALL_TOOLS = [
    GetEntity,
    QueryEntities,
    UpsertDevice,
    DeleteDevice,
    ModifyDeviceState,
    ModifyDeviceStateTimer,
    AddDeviceToRoom,
    RemoveDeviceFromRoom,
    UpsertScene,
    RunScene,
    UpsertCustomList,
    ModifyCustomListItem,
    UpsertReminder,
    DeleteReminder,
    UpsertMember,
    ModifySensorState,
]
