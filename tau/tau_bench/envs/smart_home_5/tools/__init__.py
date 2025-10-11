# Copyright Sierra

# Utility function (should be declared BEFORE imports to prevent circular dependencies)
from datetime import datetime

def _now_iso():
    """Return current time in ISO format."""
    return datetime.now().isoformat()


from .get_device_info import GetDeviceInfo
from .set_device_state import SetDeviceState
from .add_device import AddDevice
from .remove_device import RemoveDevice
from .get_room_info import GetRoomInfo
from .manage_room_devices import ManageRoomDevices
from .list_all_scenes import ListAllScenes
from .activate_scene import ActivateScene
from .create_scene import CreateScene
from .delete_scene import DeleteScene
from .get_reminders import GetReminders
from .add_reminder import AddReminder
from .update_reminder import UpdateReminder
from .delete_reminder import DeleteReminder
from .get_custom_list import GetCustomList
from .create_custom_list import CreateCustomList
from .manage_custom_list_items import ManageCustomListItems
from .delete_custom_list import DeleteCustomList
from .get_sensor_data import GetSensorData
from .get_member_info import GetMemberInfo


ALL_TOOLS = [
    GetDeviceInfo,
    SetDeviceState,
    AddDevice,
    RemoveDevice,
    GetRoomInfo,
    ManageRoomDevices,
    ListAllScenes,
    ActivateScene,
    CreateScene,
    DeleteScene,
    GetReminders,
    AddReminder,
    UpdateReminder,
    DeleteReminder,
    GetCustomList,
    CreateCustomList,
    ManageCustomListItems,
    DeleteCustomList,
    GetSensorData,
    GetMemberInfo,
]
