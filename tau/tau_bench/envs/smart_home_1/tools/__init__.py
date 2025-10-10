# Copyright Sierra Corporation

from .list_devices import ListDevices
from .get_device import GetDevice
from .update_device_state import UpdateDeviceState
from .update_device_state_timer import UpdateDeviceStateTimer
from .schedule_device_update import ScheduleDeviceUpdate
from .create_device import CreateDevice
from .delete_device import DeleteDevice
from .add_device_to_room import AddDeviceToRoom
from .remove_device_from_room import RemoveDeviceFromRoom
from .list_rooms import ListRooms
from .list_scenes import ListScenes
from .upsert_scene import UpsertScene
from .delete_scene import DeleteScene
from .schedule_scene_run import ScheduleSceneRun
from .list_members import ListMembers
from .upsert_member import UpsertMember
from .delete_member import DeleteMember
from .list_sensor_names_ids import ListSensorNamesIds
from .get_sensor_state import GetSensorState
from .manage_custom_list import ManageCustomList
from .manage_list_items import ManageListItems
from .manage_reminders import ManageReminders
from .schedule_device_timer_update import ScheduleDeviceTimerUpdate

ALL_TOOLS = [
    ListDevices,
    GetDevice,
    UpdateDeviceState,
    UpdateDeviceStateTimer,
    ScheduleDeviceUpdate,
    CreateDevice,
    DeleteDevice,
    AddDeviceToRoom,
    RemoveDeviceFromRoom,
    ListRooms,
    ListScenes,
    UpsertScene,
    DeleteScene,
    ScheduleSceneRun,
    ListMembers,
    UpsertMember,
    DeleteMember,
    ListSensorNamesIds,
    GetSensorState,
    ManageCustomList,
    ManageListItems,
    ManageReminders,
    ScheduleDeviceTimerUpdate,
]
