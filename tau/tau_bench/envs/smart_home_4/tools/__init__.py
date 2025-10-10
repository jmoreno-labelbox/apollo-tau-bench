# Copyright owned by Sierra.

from .get_device_by_id_or_filter import GetDeviceByIdOrFilter
from .get_sensor_by_id_or_filter import GetSensorByIdOrFilter
from .add_device_to_database import AddDeviceToDatabase
from .add_sensor_to_database import AddSensorToDatabase
from .update_device_in_database import UpdateDeviceInDatabase
from .delete_device_from_database import DeleteDeviceFromDatabase
from .list_devices_in_database import ListDevicesInDatabase
from .manage_room_in_database import ManageRoomInDatabase
from .get_scene_by_id_or_filter import GetSceneByIdOrFilter
from .add_scene_to_database import AddSceneToDatabase
from .update_scene_in_database import UpdateSceneInDatabase
from .delete_scene_from_database import DeleteSceneFromDatabase
from .list_scenes_in_database import ListScenesInDatabase
from .get_custom_list_by_id_or_filter import GetCustomListByIdOrFilter
from .add_custom_list_to_database import AddCustomListToDatabase
from .update_custom_list_in_database import UpdateCustomListInDatabase
from .delete_custom_list_from_database import DeleteCustomListFromDatabase
from .get_reminder_by_id_or_filter import GetReminderByIdOrFilter
from .add_reminder_to_database import AddReminderToDatabase
from .update_reminder_in_database import UpdateReminderInDatabase
from .delete_reminder_from_database import DeleteReminderFromDatabase
from .manage_member_in_database import ManageMemberInDatabase

ALL_TOOLS = [
    GetDeviceByIdOrFilter,
    GetSensorByIdOrFilter,
    AddDeviceToDatabase,
    AddSensorToDatabase,
    UpdateDeviceInDatabase,
    DeleteDeviceFromDatabase,
    ListDevicesInDatabase,
    ManageRoomInDatabase,
    GetSceneByIdOrFilter,
    AddSceneToDatabase,
    UpdateSceneInDatabase,
    DeleteSceneFromDatabase,
    ListScenesInDatabase,
    GetCustomListByIdOrFilter,
    AddCustomListToDatabase,
    UpdateCustomListInDatabase,
    DeleteCustomListFromDatabase,
    GetReminderByIdOrFilter,
    AddReminderToDatabase,
    UpdateReminderInDatabase,
    DeleteReminderFromDatabase,
    ManageMemberInDatabase,
]
