from tau_bench.types import Action, Task

TASKS = [
    # Task 1 – Generate and initiate a detailed nighttime environment.
    Task(
        annotator="0",
        user_id="res_01",
        instruction="""
        Current time is 2025-07-28 17:45. You are required to design a new scene suitable for a relaxed summer evening. Title it "Evening Breeze" with the ID "scene_evening_breeze". Upon running this scene, it should set up the living room as follows:

        Initially, activate the Living-Room ceiling light (device_id: light_lr_ceiling) and adjust its brightness to 35%. Then, set the Living-Room curtain (device_id: curtain_lr) to halfway open by positioning it at 50%, ensuring it's powered on. Proceed with configuring the Central AC (device_id: ac_home) by turning it on in cool mode, setting the temperature to 23°C, and adjusting the fan speed to "medium".

        For added comfort, generate a custom shopping list titled "Evening Essentials" (list_id: list_evening_essentials) and include the following items: one pack of scented candles and one bottle of iced tea. Additionally, ensure the Living-Room floor lamp (device_id: light_lr_floor) remains off to maintain a cozy atmosphere.

        Once the scene is crafted, initiate it immediately. After it's operational, retrieve and present the updated status of all four devices previously mentioned and review the shopping list to confirm all settings.
        """,
        actions=[
            Action(
                name="ListAllScenes",
                kwargs={}
            ),
            Action(
                name="CreateScene",
                kwargs={
                    "new_scene": {
                        "id": "scene_evening_breeze",
                        "actions": [
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 35}
                            },
                            {
                                "device_id": "curtain_lr",
                                "update": {"power": "on", "position": 50}
                            },
                            {
                                "device_id": "ac_home",
                                "update": {"power": "on", "mode": "cool", "setpoint_c": 23, "fan_speed": "medium"}
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {"power": "off"}
                            }
                        ]
                    }
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_evening_essentials",

                        "items": [
                            {"item": "Scented candles", "quantity": 1},
                            {"item": "Iced tea", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="ActivateScene",
                kwargs={"scene_id": "scene_evening_breeze"}
            ),
            Action(
                name="GetDeviceInfo",
                kwargs={"device_ids": ["light_lr_ceiling", "curtain_lr", "ac_home", "light_lr_floor"]}
            ),
            Action(
                name="GetCustomList",
                kwargs={"list_id": "list_evening_essentials"}
            ),
        ],
        outputs=[]
    ),

    # Task 2 – Set up a yearly reminder for HVAC filter replacement.
    Task(
        annotator="0",
        user_id="res_02",
        instruction="""
        You aim to establish regular upkeep for your HVAC system. Begin by inspecting the current status of your AC unit (ac_home).

        Proceed to set up an annual reminder (reminder_id: rem_hvac_filter) to change the HVAC filters. Arrange it to trigger on January 15th at 10:00 each year, employing the rrule "FREQ=YEARLY;BYMONTH=1;BYMONTHDAY=15;BYHOUR=10;BYMINUTE=0". Assign it normal priority and configure it to dispatch mobile push notifications.

        For preparation, compile a custom list named "HVAC Maintenance Supplies" (list_id: list_hvac_supplies), including: one HVAC filter and one cleaning spray.

        Prior to undertaking maintenance, ensure the AC unit (ac_home) is turned off for safety purposes. After completing these tasks, display both the reminder and the supplies list to confirm everything is accurately scheduled and arranged.
        """,
        actions=[
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["ac_home"]}),
            Action(
                name="AddReminder",
                kwargs={
                    "new_reminder": {
                        "reminder_id": "rem_hvac_filter",

                        "target": {"type": "note", "text": "Replace HVAC filter"},
                        "trigger": {"rrule": "FREQ=YEARLY;BYMONTH=1;BYMONTHDAY=15;BYHOUR=10;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",

                    }
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_hvac_supplies",

                        "items": [
                            {"item": "HVAC filter", "quantity": 1},
                            {"item": "Cleaning spray", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "ac_home",
                    "state_update": {"power": "off"}
                }
            ),
            Action(name="GetReminders", kwargs={"reminder_id": "rem_hvac_filter"}),
            Action(name="GetCustomList", kwargs={"list_id": "list_hvac_supplies"}),
        ],
        outputs=[]
    ),

    # Task 3 – Verify thermometer measurement, warm the house, and get ready for winter.
    Task(
        annotator="0",
        user_id="res_03",
        instruction="""
        Begin by checking the current reading from the Living Room Thermometer (sensor_id: sensor_lr_thermometer).

        Following this, irrespective of the temperature shown, set up the Central Heater (device_id: heater_home) with the precise settings: Switch on the power, select heat mode, and adjust the temperature setting to 22°C.

        Then, for winter readiness, assemble a custom shopping list titled "Winter Essentials" (list_id: list_winter_essentials) and include these items: one pack of radiator antifreeze and one set of thermal curtains.

        Ultimately, confirm that the AC unit (device_id: ac_home) remains turned off to prevent redundant cooling during heating. Once all steps are done, present the updated heater status and the shopping list to verify everything is correctly established.
        """,
        actions=[
            Action(
                name="GetSensorData",
                kwargs={"sensor_ids": ["sensor_lr_thermometer"]}
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "heater_home",
                    "state_update": {"power": "on", "mode": "heat", "setpoint_c": 22}
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_winter_essentials",

                        "items": [
                            {"item": "Radiator antifreeze", "quantity": 1},
                            {"item": "Thermal curtains", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "ac_home",
                    "state_update": {"power": "off"}
                }
            ),
            Action(
                name="GetDeviceInfo",
                kwargs={"device_ids": ["heater_home"]}
            ),
            Action(
                name="GetCustomList",
                kwargs={"list_id": "list_winter_essentials"}
            ),
        ],
        outputs=[]
    ),

    # Task 4 – Create a checklist for camping supplies
    Task(
        annotator="0",
        user_id="res_04",
        instruction="""
        It's necessary to create a new custom list for the camping trip you plan to take. The list specifications should be as follows:

        Initiate the list with the ID "list_camping_trip" and name it "Camping Trip Packing". Label it with "travel" and record both the created_at and updated_at timestamps as "2025-07-28T18:10:00". To start, incorporate these items into your list: one Tent, four Sleeping Bags, and two packs of Marshmallows.

        After setting up the list, include one First Aid Kit. Subsequently, add two Flashlights and one pack of Batteries to guarantee sufficient lighting for your trip. Furthermore, ensure your home heater (device_id: heater_home) is turned off before you depart for safety.

        Finally, exhibit the finalized list and the heater status to verify all items are appropriately added and the device is securely switched off.
        """,
        actions=[
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_camping_trip",
                        "name": "Camping Trip Packing",
                        "tags": ["travel"],
                        "created_at": "2025-07-28T18:10:00",
                        "updated_at": "2025-07-28T18:10:00",
                        "items": [
                            {"item": "Tent", "quantity": 1},
                            {"item": "Sleeping Bag", "quantity": 4},
                            {"item": "Marshmallows", "quantity": 2}
                        ]
                    }
                }
            ),
            Action(
                name="ManageCustomListItems",
                kwargs={
                    "list_id": "list_camping_trip",
                    "item": {"item": "First Aid Kit", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="ManageCustomListItems",
                kwargs={
                    "list_id": "list_camping_trip",
                    "item": {"item": "Flashlight", "quantity": 2},
                    "action": "add"
                }
            ),
            Action(
                name="ManageCustomListItems",
                kwargs={
                    "list_id": "list_camping_trip",
                    "item": {"item": "Batteries", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "heater_home",
                    "state_update": {"power": "off"}
                }
            ),
            Action(
                name="GetCustomList",
                kwargs={"list_id": "list_camping_trip"}
            ),
            Action(
                name="GetDeviceInfo",
                kwargs={"device_ids": ["heater_home"]}
            ),
        ],
        outputs=[]
    ),

    # Task 5 – Lower the priority of the medication reminder, disable it, and get ready for the upcoming refill.
    Task(
        annotator="0",
        user_id="res_05",
        instruction="""
        Handle the update for the Medication Reminder (reminder_id: "rem_254afa34"). Locate this reminder and execute two modifications: Firstly, alter its status to "inactive". Next, in the meta field, adjust the priority to "low".

        To assist in getting ready for your next refill, structure a personalized shopping list dubbed "Medication Supplies" (list_id: list_medication_supplies) and include one box of your medication and one bottle of water.

        Lastly, confirm that your bedroom night lamp (device_id: lamp_br_night) is switched off to ensure a tranquil environment. Once these adjustments are made, display the updated reminder, the shopping list, and the lamp state to check that everything is correctly configured.
        """,
        actions=[
            Action(
                name="GetReminders",
                kwargs={"reminder_id": "rem_254afa34"}
            ),
            Action(
                name="UpdateReminder",
                kwargs={
                    "reminder_id": "rem_254afa34",
                    "update_fields": {"status": "inactive", "meta": {"priority": "low"}}
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_medication_supplies",

                        "items": [
                            {"item": "Medication box", "quantity": 1},
                            {"item": "Water bottle", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "lamp_br_night",
                    "state_update": {"power": "off"}
                }
            ),
            Action(
                name="GetReminders",
                kwargs={"reminder_id": "rem_254afa34"}
            ),
            Action(
                name="GetCustomList",
                kwargs={"list_id": "list_medication_supplies"}
            ),
            Action(
                name="GetDeviceInfo",
                kwargs={"device_ids": ["lamp_br_night"]}
            ),
        ],
        outputs=[]
    ),

    # Task 6 – Set up the new washing machine, establish a single laundry reminder, and gather necessary supplies.
    Task(
        annotator="0",
        user_id="res_06",
        instruction="""
        Coordinate the installation of a new LG TurboWash 360 washing machine in your basement. Register it using ID "washer_bs" as a device of type "washing_machine". Label it "Basement Washing Machine" and assign its location to Basement. It's an LG TurboWash 360 model with firmware version 1.0.0. The device supports these state parameters: power, cycle, time_remaining_min, and door.

        For the initial setup, configure it to be powered off, in idle cycle mode, with 0 minutes remaining and the door closed. Establish the last update timestamp as "2025-07-28T16:30:00".

        Afterward, establish a reminder to assist you in remembering to move your laundry to the dryer. Formulate a new reminder with these specific details: designate the reminder_id as "rem_laundry" and call it "Laundry Time". The objective should be a note type with the message "Move laundry to dryer". Arrange it to go off at "2025-07-28T17:00:00". Configure it to dispatch a mobile push notification upon activation. Set the priority to "normal" in the meta field and maintain the status as "scheduled". The reminder should be recorded as created at "2025-07-28T16:30:00Z".

        To get ready for laundry, craft a personalized list titled "Laundry Supplies" (list_id: list_laundry_supplies) and add one pack of detergent and one box of dryer sheets.

        Additionally, ensure the new washing machine (device_id: washer_bs) is powered off before activating the dryer for safety. Once the reminder is created, display it, the supplies list, and the washing machine state to verify all settings are accurate.
        """,
        actions=[
            Action(
                name="AddDevice",
                kwargs={
                    "new_device": {
                        "id": "washer_bs",
                        "type": "washing_machine",
                        "location": "Basement",
                        "vendor": "LG",
                        "model": "TurboWash 360",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "cycle", "time_remaining_min", "door"],
                        "state": {
                            "power": "off",
                            "cycle": "idle",
                            "time_remaining_min": 0,
                            "door": "closed",
                        },
                        "scheduled_updates": [],
                    }
                }
            ),
            Action(
                name="AddReminder",
                kwargs={
                    "new_reminder": {
                        "reminder_id": "rem_laundry",
                        "target": {"type": "note", "text": "Move laundry to dryer"},
                        "trigger": {"datetime": "2025-07-28T16:30:00"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "scheduled",
                    }
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_laundry_supplies",

                        "items": [
                            {"item": "Detergent", "quantity": 1},
                            {"item": "Dryer sheets", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "washer_bs",
                    "state_update": {"power": "off", "cycle": "idle", "time_remaining_min": 0, "door": "closed"}
                }
            ),
            Action(
                name="GetReminders",
                kwargs={"reminder_id": "rem_laundry"}
            ),
            Action(
                name="GetCustomList",
                kwargs={"list_id": "list_laundry_supplies"}
            ),
            Action(
                name="GetDeviceInfo",
                kwargs={"device_ids": ["washer_bs"]}
            ),
        ],
        outputs=[]
    ),

    # Task 7 – Completely eliminate the bedside lamp from the East Bedroom.
    Task(
        annotator="0",
        user_id="res_07",
        instruction="""
        After unplugging the East Bedroom Bedside Lamp (device_id: lamp_be_bedside), proceed to remove it from your smart home system. Start by extracting it from the East Bedroom (room_id: "bedroom_east"), followed by completely erasing the device from the system.

        Ensure the lamp is switched off for safety prior to removal. Once the lamp is removed, devise a custom shopping list labeled "Bedroom Lamp Replacement" (list_id: list_lamp_replacement) and include one bedside lamp for potential replacement.

        Upon completing these tasks, display the East Bedroom room details and the shopping list to confirm successful lamp removal and that the replacement is accounted for.
        """,
        actions=[
            Action(
                name="GetRoomInfo",
                kwargs={"room_ids": ["bedroom_east"]}
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "lamp_be_bedside",
                    "state_update": {"power": "off"}
                }
            ),
            Action(
                name="ManageRoomDevices",
                kwargs={
                    "room_id": "bedroom_east",
                    "device_id": "lamp_be_bedside",
                    "action": "remove"
                }
            ),
            Action(
                name="RemoveDevice",
                kwargs={"device_id": "lamp_be_bedside"}
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_lamp_replacement",

                        "items": [
                            {"item": "Bedside lamp", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="GetRoomInfo",
                kwargs={"room_ids": ["bedroom_east"]}
            ),
            Action(
                name="GetCustomList",
                kwargs={"list_id": "list_lamp_replacement"}
            ),
        ],
        outputs=[]
    ),

    # Task 8 – Immediately initiate the movie time scene and gather necessary materials.
    Task(
        annotator="0",
        user_id="res_08",
        instruction="""
        Prepare to enjoy a movie! Promptly engage the existing scene with id "scene_movie_time".

        Once the scene is activated, verify and exhibit the updated statuses of these devices: the living room curtain (curtain_lr), floor light (light_lr_floor), ceiling light (light_lr_ceiling), and the AC unit (ac_home).

        To enhance the movie experience, compile a custom shopping list called "Movie Night Essentials" (list_id: list_movie_essentials) and list the following items: one pack of popcorn and two bottles of soda.

        Additionally, ensure that the kitchen dishwasher (dishwasher_kt) is turned off to prevent noise disruption during the movie. Afterwards, present the shopping list and the dishwasher state to confirm everything is ready for an ideal movie night.
        """,
        actions=[
            Action(name="ListAllScenes", kwargs={}),
            Action(name="ActivateScene", kwargs={"scene_id": "scene_movie_time"}),
            Action(
                name="GetDeviceInfo",
                kwargs={"device_ids": ["curtain_lr", "light_lr_floor", "light_lr_ceiling", "ac_home"]}
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_movie_essentials",

                        "items": [
                            {"item": "Popcorn", "quantity": 1},
                            {"item": "Soda", "quantity": 2}
                        ]
                    }
                }
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "dishwasher_kt",
                    "state_update": {"power": "off"}
                }
            ),
            Action(
                name="GetCustomList",
                kwargs={"list_id": "list_movie_essentials"}
            ),
            Action(
                name="GetDeviceInfo",
                kwargs={"device_ids": ["dishwasher_kt"]}
            ),
        ],
        outputs=[]
    ),

    # Task 9 – Utilize sensor data to pre-cool the living area and gather necessary supplies.
    Task(
        annotator="0",
        user_id="res_09",
        instruction="""
        Handle the preparations for the living room's climate. Begin by reviewing the data from both the Living Room Thermometer (sensor_lr_thermometer) and the Air-Quality Sensor (sensor_lr_air_quality).

        Once the readings have been checked, irrespective of their outcomes, proceed with these adjustments: Initially, set up the AC unit (ac_home) by switching it on, choosing cool mode with a target temperature of 20°C, and adjusting the fan speed to "high". Subsequently, completely open the Living-Room curtain (curtain_lr) by setting its position to 100 and ensure it remains powered on.

        Then, ensure the Living-Room floor lamp (light_lr_floor) is switched off to conserve energy. Additionally, assemble a custom shopping list titled "Living Room Climate Supplies" (list_id: list_lr_climate_supplies) and include the following items: one pack of air filters and one bottle of air freshener.

        Finally, exhibit the new operational states of the AC unit, the curtain, and the floor lamp, along with displaying the shopping list to verify your updates.
        """,
        actions=[
            Action(
                name="GetSensorData",
                kwargs={"sensor_ids": ["sensor_lr_thermometer", "sensor_lr_air_quality"]}
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "ac_home",
                    "state_update": {"power": "on", "mode": "cool", "setpoint_c": 20, "fan_speed": "high"}
                }
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "curtain_lr",
                    "state_update": {"power": "on", "position": 100}
                }
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "light_lr_floor",
                    "state_update": {"power": "off"}
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_lr_climate_supplies",

                        "items": [
                            {"item": "Air filters", "quantity": 1},
                            {"item": "Air freshener", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="GetDeviceInfo",
                kwargs={"device_ids": ["ac_home", "curtain_lr", "light_lr_floor"]}
            ),
            Action(
                name="GetCustomList",
                kwargs={"list_id": "list_lr_climate_supplies"}
            ),
        ],
        outputs=[]
    ),

    # Task 10 – Generate and execute a party mode scene right away.
    Task(
        annotator="0",
        user_id="res_10",
        instruction="""
        Coordinate the setup of a high-energy scene for parties. Initiate by assessing the current data from the Living Room Air-Quality Sensor (sensor_lr_air_quality) to confirm a safe environment for visitors.

        Develop a new scene labeled "Party Mode" with id "scene_party_mode" to configure your devices as follows:

        Within the living room, deactivate the ceiling light (light_lr_ceiling), adjust the floor light (light_lr_floor) to 15% brightness and turn it on, and close the curtain (curtain_lr) fully by setting its position to 0 while keeping it powered. For climate control, configure the AC (ac_home) to cool mode at 19°C with the fan speed on "high". Within the bedroom, set the ceiling light (light_br_ceiling) to full brightness with a purple hue (color settings: hue=300, saturation=80).

        To get ready for the party, put together a custom shopping list labeled "Party Essentials" (list_id: list_party_essentials) including the following items: one pack of snacks and two bottles of soda.

        Additionally, confirm the kitchen dishwasher (dishwasher_kt) is turned off to prevent noise during the gathering.

        Once the scene is created, activate it right away. Subsequently, present the current status of all five devices, the shopping list, and the dishwasher state to visualize the party setting.
        """,
        actions=[
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(name="ListAllScenes", kwargs={}),
            Action(
                name="CreateScene",
                kwargs={
                    "new_scene": {
                        "id": "scene_party_mode",
                        "actions": [
                            {"device_id": "light_lr_ceiling", "update": {"power": "off"}},
                            {"device_id": "light_lr_floor", "update": {"power": "on", "brightness": 15}},
                            {"device_id": "ac_home", "update": {"power": "on", "mode": "cool", "setpoint_c": 19, "fan_speed": "high"}},
                            {"device_id": "curtain_lr", "update": {"power": "on", "position": 0}},
                            {"device_id": "light_br_ceiling", "update": {"power": "on", "brightness": 100, "color": {"hue": 300, "saturation": 80}}}
                        ]
                    }
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_party_essentials",

                        "items": [
                            {"item": "Snacks", "quantity": 1},
                            {"item": "Soda", "quantity": 2}
                        ]
                    }
                }
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "dishwasher_kt",
                    "state_update": {"power": "off"}
                }
            ),
            Action(name="ActivateScene", kwargs={"scene_id": "scene_party_mode"}),
            Action(
                name="GetDeviceInfo",
                kwargs={"device_ids": ["light_lr_ceiling", "light_lr_floor", "ac_home", "curtain_lr", "light_br_ceiling", "dishwasher_kt"]}
            ),
            Action(
                name="GetCustomList",
                kwargs={"list_id": "list_party_essentials"}
            ),
        ],
        outputs=[]
    ),

    # Task 11 – Update the weekend shopping list and verify kitchen safety.
    Task(
        annotator="0",
        user_id="res_11",
        instruction="""
        Make adjustments to your weekend grocery list (list_id: list_groceries_weekend). Begin by checking the current status of your Kitchen Sink Leak Sensor (sensor_id: sensor_sink_leak) to confirm there are no water issues before you continue.

        After that, incorporate six Bananas into the list. Next, eliminate one entry of Olive Oil. Additionally, add two cartons of Milk and one pack of Eggs to be well-prepared for the weekend.

        For safety purposes, ensure the kitchen dishwasher (device_id: dishwasher_kt) is switched off before you head out shopping.

        Upon making these changes, show the entire updated list alongside the status of the dishwasher so you can confirm that all adjustments and safety measures have been correctly implemented.
        """,
        actions=[
            Action(
                name="GetSensorData",
                kwargs={"sensor_ids": ["sensor_sink_leak"]}
            ),
            Action(
                name="ManageCustomListItems",
                kwargs={
                    "list_id": "list_groceries_weekend",
                    "item": {"item": "Bananas", "quantity": 6},
                    "action": "add"
                }
            ),
            Action(
                name="ManageCustomListItems",
                kwargs={
                    "list_id": "list_groceries_weekend",
                    "item": {"item": "Olive Oil"},
                    "action": "remove"
                }
            ),
            Action(
                name="ManageCustomListItems",
                kwargs={
                    "list_id": "list_groceries_weekend",
                    "item": {"item": "Milk", "quantity": 2},
                    "action": "add"
                }
            ),
            Action(
                name="ManageCustomListItems",
                kwargs={
                    "list_id": "list_groceries_weekend",
                    "item": {"item": "Eggs", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "dishwasher_kt",
                    "state_update": {"power": "off"}
                }
            ),
            Action(name="GetCustomList", kwargs={"list_id": "list_groceries_weekend"}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["dishwasher_kt"]}),
        ],
        outputs=[]
    ),

    # Task 12 – Install a smart coffee maker in the kitchen, initiate brewing, and gather necessary supplies.
    Task(
        annotator="0",
        user_id="res_12",
        instruction="""
        Start by setting up a new Nespresso Vertuo Next coffee maker in your kitchen. Here are the device specifications:

        Register it under the ID "coffee_maker_kt" as a device of type "coffee_maker". Give it the name "Kitchen Coffee Maker". It's manufactured by Nespresso, model Vertuo Next, and runs firmware version 1.2.3. The supported state parameters include power, mode, and cups_remaining.

        For the initial setup, set it to powered off, in idle mode, with 0 cups remaining. Assign the last update timestamp to "2025-07-28T18:20:00".

        Prior to any alterations, verify the current reading from the Kitchen Sink Leak Sensor (sensor_id: sensor_sink_leak) to ensure there are no water issues.

        Once the device is added, register it in the kitchen (room_id: "kitchen"). Proceed to start brewing by powering it on, setting the mode to "brew", and adjusting cups_remaining to 1.

        To arrange for future coffee sessions, establish a custom shopping list named "Coffee Supplies" (list_id: list_coffee_supplies) and include the following items: one box of coffee capsules and one bottle of descaler.

        Also, ensure the kitchen dishwasher (device_id: dishwasher_kt) is turned off for safety before initiating the coffee maker.

        Lastly, present the kitchen information and the coffee supplies list to verify that all is configured appropriately.
        """,
        actions=[
            Action(
                name="GetSensorData",
                kwargs={"sensor_ids": ["sensor_sink_leak"]}
            ),
            Action(
                name="AddDevice",
                kwargs={
                    "new_device": {
                        "id": "coffee_maker_kt",
                        "type": "coffee_maker",

                        "location": "Kitchen",
                        "vendor": "Nespresso",
                        "model": "Vertuo Next",
                        "firmware_version": "1.2.3",
                        "state_params": ["power", "mode", "cups_remaining"],
                        "state": {
                            "power": "off",
                            "mode": "idle",
                            "cups_remaining": 0,

                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="ManageRoomDevices",
                kwargs={
                    "room_id": "kitchen",
                    "device_id": "coffee_maker_kt",
                    "action": "add"
                }
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "coffee_maker_kt",
                    "state_update": {"power": "on", "mode": "brew", "cups_remaining": 1}
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_coffee_supplies",

                        "items": [
                            {"item": "Coffee capsules", "quantity": 1},
                            {"item": "Descaler", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "dishwasher_kt",
                    "state_update": {"power": "off"}
                }
            ),
            Action(name="GetRoomInfo", kwargs={"room_ids": ["kitchen"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_coffee_supplies"}),
        ],
        outputs=[]
    ),

    # Task 13 – Develop and arrange an accessible environment for the grandmother's visit.
    Task(
        annotator="0",
        user_id="res_13",
        instruction="""
        Your grandmother, Linda Johnson, will be visiting next Friday at 14:00; prepare your home to accommodate her wheelchair accessibility needs. Start by checking the current reading from your Living Room Air-Quality Sensor (sensor_lr_air_quality) to ensure the environment is comfortable for her.

        Generate a new scene titled "Grandma's Welcome" with id "scene_grandma_welcome" that will adjust your home settings as follows:

        In the living room, adjust the ceiling light (light_lr_ceiling) to 85% brightness and switch it on for improved visibility. Fully open the curtain (curtain_lr) by setting its position to 100. For comfort, configure the AC (ac_home) to cool mode at 24°C with the fan speed on "low" for minimal noise. As she will not be using the East Bedroom, turn off both the ceiling light (light_be_ceiling) and bedside lamp (lamp_be_bedside). Moreover, ensure that the East Bedroom curtain (curtain_be) is closed by setting its position to 0 while keeping it powered on for privacy.

        Handle the creation of a high priority reminder (reminder_id: rem_grandma_july) that will alert you on your mobile 30 minutes before her arrival with the message "Prepare guest room for Grandma Linda - wheelchair access needed".

        To guarantee you have all necessary items for her visit, establish a custom shopping list named "Grandma Visit Essentials" (list_id: list_grandma_essentials) and include the following items: one wheelchair ramp and one bottle of water.

        Conclude by displaying both the scene details, the reminder, and the shopping list to confirm everything is set up correctly.
        """,
        actions=[
            Action(
                name="GetSensorData",
                kwargs={"sensor_ids": ["sensor_lr_air_quality"]}
            ),
            Action(
                name="CreateScene",
                kwargs={
                    "new_scene": {
                        "id": "scene_grandma_welcome",
                        "actions": [
                            {"device_id": "light_lr_ceiling", "update": {"power": "on", "brightness": 85}},
                            {"device_id": "curtain_lr", "update": {"power": "on", "position": 100}},
                            {"device_id": "ac_home", "update": {"power": "on", "mode": "cool", "setpoint_c": 24, "fan_speed": "low"}},
                            {"device_id": "light_be_ceiling", "update": {"power": "off"}},
                            {"device_id": "lamp_be_bedside", "update": {"power": "off"}},
                            {"device_id": "curtain_be", "update": {"power": "on", "position": 0}}
                        ]
                    }
                }
            ),
            Action(
                name="AddReminder",
                kwargs={
                    "new_reminder": {
                        "reminder_id": "rem_grandma_july",
                        "target": {"type": "note", "text": "Prepare guest room for Grandma Linda - wheelchair access needed"},
                        "trigger": {"datetime": "2025-07-04T13:30:00"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "high"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_grandma_essentials",

                        "items": [
                            {"item": "Wheelchair ramp", "quantity": 1},
                            {"item": "Water bottle", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="ListAllScenes",
                kwargs={}
            ),
            Action(
                name="GetReminders",
                kwargs={"reminder_id": "rem_grandma_july"}
            ),
            Action(
                name="GetCustomList",
                kwargs={"list_id": "list_grandma_essentials"}
            )
        ],
        outputs=[]
    ),

    # Task 14 – Concentrated study environment for West Bedroom
    Task(
        annotator="0",
        user_id="res_14",
        instruction="""
        The date is 2025-07-29 09:00, and you need to set up a scene that will aid in intensive studying within the West Bedroom. Designate this new scene as "Focused Study" with id "scene_focused_study_west". When engaged, the scene should set your devices as follows:

        Initially, check the current air quality data from your sensors to make sure the study area remains healthy.

        For ideal lighting, switch on the West Bedroom Desk Lamp (device_id: lamp_bw_desk) at full brightness and adjust its color temperature to 5000K. Adjust the West Bedroom Ceiling Light (device_id: light_bw_ceiling) to a softer 40% brightness and turn it on. For natural lighting, open the West Bedroom Curtain (device_id: curtain_bw) to position 100 while keeping it powered on. Then, create a comfortable atmosphere by turning on the Central AC (device_id: ac_home), setting it to cool mode at 21°C with the fan speed on "low".

        To assemble everything needed for focused study, prepare a custom shopping list called "Study Essentials" (list_id: list_study_essentials) that includes: one Desk Organizer and one pack of Highlighters.

        Additionally, ensure the Living Room Floor Lamp (device_id: light_lr_floor) is off to prevent any distractions.

        Once the scene is created, activate it promptly and display the new status of all four devices listed above, the shopping list, and the Living Room Floor Lamp's status.
        """,
        actions=[
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(name="ListAllScenes", kwargs={}),
            Action(name="GetRoomInfo", kwargs={"room_ids": ["bedroom_west"]}),
            Action(
                name="CreateScene",
                kwargs={
                    "new_scene": {
                        "id": "scene_focused_study_west",
                        "actions": [
                            {"device_id": "lamp_bw_desk", "update": {"power": "on", "brightness": 100, "color_temperature": 5000}},
                            {"device_id": "light_bw_ceiling", "update": {"power": "on", "brightness": 40}},
                            {"device_id": "curtain_bw", "update": {"power": "on", "position": 100}},
                            {"device_id": "ac_home", "update": {"power": "on", "mode": "cool", "setpoint_c": 21, "fan_speed": "low"}}
                        ]
                    }
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_study_essentials",

                        "items": [
                            {"item": "Desk Organizer", "quantity": 1},
                            {"item": "Highlighters", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "light_lr_floor",
                    "state_update": {"power": "off"}
                }
            ),
            Action(name="ActivateScene", kwargs={"scene_id": "scene_focused_study_west"}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["lamp_bw_desk", "light_bw_ceiling", "curtain_bw", "ac_home", "light_lr_floor"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_study_essentials"}),
        ],
        outputs=[]
    ),

    # Task 15 – Install a new dishwasher model and initiate a quick cycle.
    Task(
        annotator="0",
        user_id="res_15",
        instruction="""
        On 2025-07-29 at 10:15, your task is to enhance your kitchen's setup by installing a new Bosch Series 9 dishwasher. Follow these steps:

        Start by verifying your current Kitchen room settings and check the condition of the existing dishwasher (device_id: dishwasher_kt) to confirm it is powered off for safety reasons. Additionally, inspect the Kitchen Sink Leak Sensor (sensor_id: sensor_sink_leak) to ensure there are no water-related issues before proceeding.

        Next, detach the current dishwasher (device_id: dishwasher_kt) from the Kitchen (room_id: "kitchen") and completely remove it from your system.

        Proceed to install the new dishwasher with these specifications: Register it under ID "dishwasher_kt2" as a device type "dishwasher". Assign it the name "Kitchen Dishwasher (Series 9)" and place it in the Kitchen. It is a Bosch Series 9 model with firmware version 6.0.0. The device supports state parameters: power, cycle, time_remaining_min, and door.

        For the initial setup, set it up as powered off, in auto cycle mode, with 0 minutes remaining, and the door closed. Update the last update timestamp to "2025-07-29T10:15:00".

        After integrating the new dishwasher into the Kitchen, initiate a quick wash by powering it on, setting the cycle to "quick", adjusting time_remaining_min to 30, and keeping the door closed.

        To plan for future maintenance, create a new shopping list titled "Dishwasher Supplies" (list_id: list_dishwasher_supplies) and include one pack of dishwasher detergent and one bottle of rinse aid.

        Finally, present the updated Kitchen information alongside the supplies list to confirm the installation and preparation.
        """,
        actions=[
            Action(name="GetRoomInfo", kwargs={"room_ids": ["kitchen"]}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["dishwasher_kt"]}),
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_sink_leak"]}),
            Action(name="SetDeviceState", kwargs={"device_id": "dishwasher_kt", "state_update": {"power": "off"}}),
            Action(name="ManageRoomDevices", kwargs={"room_id": "kitchen", "device_id": "dishwasher_kt", "action": "remove"}),
            Action(name="RemoveDevice", kwargs={"device_id": "dishwasher_kt"}),
            Action(
                name="AddDevice",
                kwargs={
                    "new_device": {
                        "id": "dishwasher_kt2",
                        "type": "dishwasher",
                        "location": "Kitchen",
                        "vendor": "Bosch",
                        "model": "Series 9",
                        "firmware_version": "6.0.0",
                        "state_params": ["power", "cycle", "time_remaining_min", "door"],
                        "state": {
                            "power": "off",
                            "cycle": "auto",
                            "time_remaining_min": 0,
                            "door": "closed",
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(name="ManageRoomDevices", kwargs={"room_id": "kitchen", "device_id": "dishwasher_kt2", "action": "add"}),
            Action(name="SetDeviceState", kwargs={"device_id": "dishwasher_kt2", "state_update": {"power": "on", "cycle": "quick", "time_remaining_min": 30, "door": "closed"}}),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_dishwasher_supplies",

                        "items": [
                            {"item": "Dishwasher detergent", "quantity": 1},
                            {"item": "Rinse aid", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="GetRoomInfo", kwargs={"room_ids": ["kitchen"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_dishwasher_supplies"}),
        ],
        outputs=[]
    ),
    # Task 16 – Conduct a safety check for the bedroom fire drill, including a lighting alert, inventory of supplies, and a follow-up notification.
    Task(
        annotator="0",
        user_id="res_16",
        instruction="""
        At 2025-07-29 11:00, conduct a fire-drill in the Master Bedroom by following these steps sequentially:

        Initially, check the current status from the Bedroom Smoke Detector (sensor_id: sensor_bed_smoke) to confirm the absence of fire or smoke issues before moving forward.

        Then, utilize the add_device tool to install a new Dyson Pure Cool TP07 air-purifier in the Master Bedroom. Register it with ID "air_purifier_mb" as a device of type "air_purifier". Name it "Master Bedroom Air-Purifier", designate its location as Master Bedroom, vendor as Dyson, model as Pure Cool TP07, and firmware version as 1.0.1. The device can manage these state parameters: power, mode, fan_speed, and filter_life_pct. For initial configuration, set it as powered off, in auto mode, with low fan speed, and 100% filter life. Update the last update timestamp to "2025-07-29T11:00:00".

        Then, compile a custom shopping list called "Fire Drill Supplies" (list_id: list_fire_drill_supplies) and incorporate the following items: one fire blanket and one emergency flashlight.

        Subsequently, configure the bedroom lights for the drill: Power on the Master Bedroom Ceiling Light (light_br_ceiling) at maximum brightness with neutral white light (color settings: hue=0, saturation=0). Apply the same settings to the Master Bedroom Night Lamp (lamp_br_night).

        For precaution, ensure the master bedroom air-purifier (air_purifier_mb) remains powered off throughout the drill.

        To ensure proper follow-through, organize a one-time reminder with the following details: Assign the reminder_id as "rem_fire_drill_05min" and title it "Fire-Drill Follow-up". The reminder should convey the message "Confirm fire-drill completion log" and be set for 2025-07-29T11:05:00. Assign it high priority and configure it to dispatch a mobile push notification.

        Finally, show both the updated light states, the air-purifier state, the supplies list, and the newly created reminder to ensure that everything is correctly arranged.
        """,
        actions=[
            Action(
                name="AddDevice",
                kwargs={
                    "new_device": {
                        "id": "air_purifier_mb",
                        "type": "air_purifier",
                        "location": "Master Bedroom",
                        "vendor": "Dyson",
                        "model": "Pure Cool TP07",
                        "firmware_version": "1.0.1",
                        "state_params": ["power", "mode", "fan_speed", "filter_life_pct"],
                        "state": {
                            "power": "off",
                            "mode": "auto",
                            "fan_speed": "low",
                            "filter_life_pct": 100,
                        },
                        "scheduled_updates": [],
                        "last_updated": "2025-07-29T11:00:00"
                    }
                }
            ),
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_bed_smoke"]}),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_fire_drill_supplies",
                        "items": [
                            {"item": "Fire blanket", "quantity": 1},
                            {"item": "Emergency flashlight", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="SetDeviceState", kwargs={"device_id": "light_br_ceiling", "state_update": {"power": "on", "brightness": 100, "color": {"hue": 0, "saturation": 0}}}),
            Action(name="SetDeviceState", kwargs={"device_id": "lamp_br_night", "state_update": {"power": "on", "brightness": 100, "color": {"hue": 0, "saturation": 0}}}),
            Action(name="SetDeviceState", kwargs={"device_id": "air_purifier_mb", "state_update": {"power": "off"}}),
            Action(
                name="AddReminder",
                kwargs={
                    "new_reminder": {
                        "reminder_id": "rem_fire_drill_05min",
                        "target": {"type": "note", "text": "Confirm fire-drill completion log"},
                        "trigger": {"datetime": "2025-07-29T11:05:00"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "high"},
                        "status": "scheduled",
                    }
                }
            ),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["light_br_ceiling", "lamp_br_night", "air_purifier_mb"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_fire_drill_supplies"}),
            Action(name="GetReminders", kwargs={"reminder_id": "rem_fire_drill_05min"}),
        ],
        outputs=[]
    ),
    # Task 17 – Update reading list, verify lamp status, and establish daily reading notification.
    Task(
        annotator="0",
        user_id="res_17",
        instruction="""
        To enhance your reading routine and establish a cozy setting, follow these steps:

        Begin by verifying the status of your Bedroom Night Lamp (device_id: lamp_br_night) to ensure it is turned off before initiating your reading session. Then, present your current reading list (list_id: list_reading) to review its contents.

        Proceed to insert "The Pragmatic Programmer" (quantity: 1) into the list, and eliminate the existing entry for "Clean Code". Additionally, include a new item "Reading Glasses" (quantity: 1) to the list should you require them. Following these modifications, display the revised reading list to confirm the changes.

        To support your reading habit, establish a daily evening reminder with the following details: Assign the reminder_id to "rem_reading_daily" and title it "Evening Reading Time". Connect it to your reading list by setting the target type as "entity", entity_type as "list", and entity_id as "list_reading". Set it to repeat every day at 20:00 using the rrule "FREQ=DAILY;BYHOUR=20;BYMINUTE=0". Configure it with standard priority and ensure it delivers mobile push notifications. Designate it with an "active" status.

        Lastly, display the reminder to verify it is properly configured.
        """,
        actions=[
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["lamp_br_night"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_reading"}),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_reading", "item": {"item": "The Pragmatic Programmer", "quantity": 1}, "action": "add"}),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_reading", "item": {"item": "Clean Code"}, "action": "remove"}),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_reading", "item": {"item": "Reading Glasses", "quantity": 1}, "action": "add"}),
            Action(name="GetCustomList", kwargs={"list_id": "list_reading"}),
            Action(
                name="AddReminder",
                kwargs={
                    "new_reminder": {
                        "reminder_id": "rem_reading_daily",
                        "target": {"type": "entity", "entity_type": "list", "entity_id": "list_reading"},
                        "trigger": {"rrule": "FREQ=DAILY;BYHOUR=20;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(name="GetReminders", kwargs={"reminder_id": "rem_reading_daily"}),
        ],
        outputs=[]
    ),

    # Task 18 – Enable advanced nighttime security mode
    Task(
        annotator="0",
        user_id="res_18",
        instruction="""
        At 23:00 this evening, initiate the activation of enhanced security features in your home. Develop a new scene called "Enhanced Security" with id "scene_security_night" that will set up your devices as follows:

        Initially, assess and document the current state of the Hallway Motion Sensor (sensor_hall_motion) along with both door cameras (camera_front_door, camera_back_door) prior to implementing any adjustments. For surveillance purposes, enable both your Front Door Camera and Back Door Camera by adjusting their stream_online and recording settings to True. For safety, switch off both the Living-Room Ceiling Light (light_lr_ceiling) and the Master Bedroom Ceiling Light (light_br_ceiling). Also, ensure the Living-Room Floor Lamp (light_lr_floor) is powered off for conserving energy.

        To guarantee you are equipped for night-time security, assemble a custom shopping list entitled "Night Security Essentials" (list_id: list_security_essentials) and incorporate the following items: one pack of batteries for cameras and one flashlight.

        Once the scene is created, activate it at once and display the current states of both cameras, both ceiling lights, the floor lamp, and the shopping list to confirm the security arrangement.
        """,
        actions=[
            Action(name="ListAllScenes", kwargs={}),
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_hall_motion", "camera_front_door", "camera_back_door"]}),
            Action(
                name="CreateScene",
                kwargs={
                    "new_scene": {
                        "id": "scene_security_night",
                        "actions": [
                            {"device_id": "camera_front_door", "update": {"stream_online": True, "recording": True}},
                            {"device_id": "camera_back_door", "update": {"stream_online": True, "recording": True}},
                            {"device_id": "light_lr_ceiling", "update": {"power": "off"}},
                            {"device_id": "light_br_ceiling", "update": {"power": "off"}},
                            {"device_id": "light_lr_floor", "update": {"power": "off"}}
                        ]
                    }
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_security_essentials",

                        "items": [
                            {"item": "Camera batteries", "quantity": 1},
                            {"item": "Flashlight", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="ActivateScene", kwargs={"scene_id": "scene_security_night"}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["light_lr_ceiling", "light_br_ceiling", "light_lr_floor", "camera_front_door", "camera_back_door"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_security_essentials"}),
        ],
        outputs=[]
    ),

    # Task 19 – Get the house ready for a two-week trip.
    Task(
        annotator="0",
        user_id="res_19",
        instruction="""
        As you are departing for vacation on 2025-07-05, it's essential to get your house ready for your absence. Set up a new scene titled "Vacation Away" with id "scene_vacation_away" to ensure your home is both energy-efficient and secure.

        Prior to implementing any changes, verify the current reading from your Kitchen Sink Leak Sensor (sensor_id: sensor_sink_leak) to confirm there are no water issues before you leave.

        The scene should control your devices in this order: Start by turning off all the main lights in the house, including the living room ceiling and floor lights (light_lr_ceiling, light_lr_floor), all bedroom ceiling lights (light_br_ceiling, light_bw_ceiling, light_be_ceiling), as well as both the master bedroom night lamp (lamp_br_night) and west bedroom desk lamp (lamp_bw_desk). Subsequently, close all curtains in the bedrooms and living room (curtain_lr, curtain_br, curtain_bw, curtain_be) by setting their positions to 0 while ensuring they remain powered on. Lastly, deactivate the climate control by switching off both the AC (ac_home) and heater (heater_home).

        Once the scene is created, activate it right away. Then, put together a custom shopping list named "Vacation Essentials" (list_id: list_vacation_essentials) and include these items: one pack of batteries for sensors and one bottle of plant fertilizer.

        Additionally, verify that the dishwasher (dishwasher_kt) is powered off for safety before your departure.

        Lastly, arrange a reminder (rem_vacation_plants) to water the houseplants every Saturday at 09:00 during your absence, utilizing the rrule "FREQ=WEEKLY;BYDAY=SA;BYHOUR=9;BYMINUTE=0". Showcase the states of the AC, heater, living room curtain, living room ceiling light, the dishwasher, the shopping list, and the reminder details to ensure everything is properly set.
        """,
        actions=[
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_sink_leak"]}),
            Action(name="ListAllScenes", kwargs={}),
            Action(
                name="CreateScene",
                kwargs={
                    "new_scene": {
                        "id": "scene_vacation_away",
                        "actions": [
                            {"device_id": "light_lr_ceiling", "update": {"power": "off"}},
                            {"device_id": "light_lr_floor", "update": {"power": "off"}},
                            {"device_id": "light_br_ceiling", "update": {"power": "off"}},
                            {"device_id": "lamp_br_night", "update": {"power": "off"}},
                            {"device_id": "light_bw_ceiling", "update": {"power": "off"}},
                            {"device_id": "lamp_bw_desk", "update": {"power": "off"}},
                            {"device_id": "light_be_ceiling", "update": {"power": "off"}},
                            {"device_id": "curtain_lr", "update": {"power": "on", "position": 0}},
                            {"device_id": "curtain_br", "update": {"power": "on", "position": 0}},
                            {"device_id": "curtain_bw", "update": {"power": "on", "position": 0}},
                            {"device_id": "curtain_be", "update": {"power": "on", "position": 0}},
                            {"device_id": "ac_home", "update": {"power": "off"}},
                            {"device_id": "heater_home", "update": {"power": "off"}}
                        ]
                    }
                }
            ),
            Action(name="ActivateScene", kwargs={"scene_id": "scene_vacation_away"}),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_vacation_essentials",

                        "items": [
                            {"item": "Sensor batteries", "quantity": 1},
                            {"item": "Plant fertilizer", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "dishwasher_kt",
                    "state_update": {"power": "off"}
                }
            ),
            Action(
                name="AddReminder",
                kwargs={
                    "new_reminder": {
                        "reminder_id": "rem_vacation_plants",
                        "target": {"type": "note", "text": "Water houseplants"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=SA;BYHOUR=9;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["ac_home", "heater_home", "curtain_lr", "light_lr_ceiling", "dishwasher_kt"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_vacation_essentials"}),
            Action(name="GetReminders", kwargs={"reminder_id": "rem_vacation_plants"}),
        ],
        outputs=[]
    ),
    # Task 20 – Generate a garden upkeep checklist and weekly alert following the inspection of the leak sensor and verification of the outdoor faucet.
    Task(
        annotator="0",
        user_id="res_20",
        instruction="""
        You're set to regularly tend to your outdoor space.

        Establish a new custom list with these criteria: Assign the list_id "list_garden_maintenance" and label it "Garden Maintenance". Tag it with "garden". Initially, incorporate these items into your list: one Fertilizer, one Hose Nozzle, and two pairs of Gloves.

        After the list creation, introduce two additional items: Weed Killer (quantity: 1) and one pack of Plant Stakes (quantity: 1). Exhibit the complete list to confirm all items are accurately included.

        Lastly, organize a weekly reminder (reminder_id: rem_garden_weekly) that will alert you every Sunday at 08:00 to review your garden maintenance list. Use the rrule "FREQ=WEEKLY;BYDAY=SU;BYHOUR=08;BYMINUTE=0", set it up to deliver mobile push notifications, and present the reminder to verify it's appropriately scheduled.
        """,
        actions=[
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_garden_maintenance",

                        "items": [
                            {"item": "Fertilizer", "quantity": 1},
                            {"item": "Hose Nozzle", "quantity": 1},
                            {"item": "Gloves", "quantity": 2}
                        ]
                    }
                }
            ),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_garden_maintenance", "item": {"item": "Weed Killer", "quantity": 1}, "action": "add"}),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_garden_maintenance", "item": {"item": "Plant Stakes", "quantity": 1}, "action": "add"}),
            Action(name="GetCustomList", kwargs={"list_id": "list_garden_maintenance"}),
            Action(
                name="AddReminder",
                kwargs={
                    "new_reminder": {
                        "reminder_id": "rem_garden_weekly",
                        "target": {"type": "entity", "entity_type": "list", "entity_id": "list_garden_maintenance"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=SU;BYHOUR=08;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(name="GetReminders", kwargs={"reminder_id": "rem_garden_weekly"}),
        ],
        outputs=[]
    ),

    # Task 21 – Nighttime setting for kids' rooms
    Task(
        annotator="0",
        user_id="res_21",
        instruction="""
        Handle the creation of a tranquil setting for the children's bedtime tonight at 20:30. Before implementing any modifications, examine the latest readings from the West Bedroom Temperature Sensor (sensor_bw_temp) and East Bedroom Temperature Sensor (sensor_be_temp) to confirm the rooms' comfort levels.

        Develop a new scene titled "Kids Bedtime" with the id "scene_kids_bedtime" to ready both rooms for sleep.

        In the West Bedroom, turn off both light sources: the ceiling light (light_bw_ceiling) and the desk lamp (lamp_bw_desk). Proceed to draw the curtain (curtain_bw) by setting its position to 0 while ensuring it remains powered on. Likewise, in the East Bedroom, turn off the ceiling light (light_be_ceiling) and close its curtain (curtain_be) using the same settings. To foster a quiet atmosphere, adjust the AC unit (ac_home) by setting its fan speed to "low" while preserving its current power state.

        To promote energy efficiency, ensure the West Bedroom Desk Lamp (lamp_bw_desk) is turned off following the scene's activation.

        Additionally, compile a custom shopping list titled "Kids Bedtime Essentials" (list_id: list_kids_bedtime_essentials) and incorporate these items: one pack of night lights and one bottle of water.

        Once the scene is established, activate it without delay and exhibit the current status of these devices: the West Bedroom ceiling light and curtain, the East Bedroom ceiling light and curtain, the AC unit, and the desk lamp. Moreover, present the shopping list to verify all items are included.
        """,
        actions=[
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_bw_temp", "sensor_be_temp"]}),
            Action(name="ListAllScenes", kwargs={}),
            Action(name="GetRoomInfo", kwargs={"room_ids": ["bedroom_west", "bedroom_east"]}),
            Action(
                name="CreateScene",
                kwargs={
                    "new_scene": {
                        "id": "scene_kids_bedtime",
                        "actions": [
                            {"device_id": "light_bw_ceiling", "update": {"power": "off"}},
                            {"device_id": "lamp_bw_desk", "update": {"power": "off"}},
                            {"device_id": "curtain_bw", "update": {"power": "on", "position": 0}},
                            {"device_id": "light_be_ceiling", "update": {"power": "off"}},
                            {"device_id": "curtain_be", "update": {"power": "on", "position": 0}},
                            {"device_id": "ac_home", "update": {"fan_speed": "low"}}
                        ]
                    }
                }
            ),
            Action(name="ActivateScene", kwargs={"scene_id": "scene_kids_bedtime"}),
            Action(name="SetDeviceState", kwargs={"device_id": "lamp_bw_desk", "state_update": {"power": "off"}}),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_kids_bedtime_essentials",

                        "items": [
                            {"item": "Night lights", "quantity": 1},
                            {"item": "Water bottle", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["light_bw_ceiling", "curtain_bw", "light_be_ceiling", "curtain_be", "ac_home", "lamp_bw_desk"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_kids_bedtime_essentials"}),
        ],
        outputs=[]
    ),

    # Task 22 – Set up the air purifier in the master bedroom, monitor air quality, activate it, and gather necessary supplies.
    Task(
        annotator="0",
        user_id="res_22",
        instruction="""
        Manage the addition of an air-purifier to your Master Bedroom and verify the environment's health. Start by inspecting the current air quality through your Bedroom Air-Quality Sensor (sensor_id: sensor_mb_air_quality). Should this sensor be absent, set it up using these specifications: id "sensor_mb_air_quality", type "air_quality_sensor", location "Master Bedroom", vendor "Dyson", model "AQ-100", firmware_version "1.0.0", and state_params ["co2", "voc", "pm2_5"].

        Proceed to install a new Dyson Pure Cool TP07 air-purifier in the Master Bedroom. Log it with the ID "air_purifier_mb" as a device of type "air_purifier". Designate it as "Master Bedroom Air-Purifier", position its location to Master Bedroom, vendor to Dyson, model to Pure Cool TP07, and firmware version to 1.0.1. The device accommodates these state parameters: power, mode, fan_speed, and filter_life_pct. For the starting configuration, set it to powered off, in auto mode, with low fan speed, and 100% filter life.

        Following the device's addition, assign it to your Master Bedroom (room_id: "bedroom_master"). Then, switch it on, maintaining it in auto mode, yet raise the fan speed to "medium".

        To gear up for future maintenance, develop a custom shopping list called "Air-Purifier Supplies" (list_id: list_air_purifier_supplies) and include one replacement filter and one cleaning cloth.

        For safety measures, confirm the Master Bedroom Night Lamp (device_id: lamp_br_night) is turned off.

        Ultimately, display the Master Bedroom information and the supplies list to verify the installation and preparation.
        """,
        actions=[
            Action(
                name="GetSensorData",
                kwargs={"sensor_ids": ["sensor_mb_air_quality"]}
            ),
            Action(
                name="AddDevice",
                kwargs={
                    "new_device": {
                        "id": "sensor_mb_air_quality",
                        "type": "air_quality_sensor",
                        "location": "Master Bedroom",
                        "vendor": "Dyson",
                        "model": "AQ-100",
                        "firmware_version": "1.0.0",
                        "state_params": ["co2", "voc", "pm2_5"],
                        "state": {},
                        "scheduled_updates": []
                    }
                }
            ),
            Action(name="GetRoomInfo", kwargs={"room_ids": ["bedroom_master"]}),
            Action(
                name="AddDevice",
                kwargs={
                    "new_device": {
                        "id": "air_purifier_mb",
                        "type": "air_purifier",
                        "location": "Master Bedroom",
                        "vendor": "Dyson",
                        "model": "Pure Cool TP07",
                        "firmware_version": "1.0.1",
                        "state_params": ["power", "mode", "fan_speed", "filter_life_pct"],
                        "state": {
                            "power": "off",
                            "mode": "auto",
                            "fan_speed": "low",
                            "filter_life_pct": 100,
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(name="ManageRoomDevices", kwargs={"room_id": "bedroom_master", "device_id": "air_purifier_mb", "action": "add"}),
            Action(name="SetDeviceState", kwargs={"device_id": "air_purifier_mb", "state_update": {"power": "on", "mode": "auto", "fan_speed": "medium"}}),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_air_purifier_supplies",

                        "items": [
                            {"item": "Replacement filter", "quantity": 1},
                            {"item": "Cleaning cloth", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="SetDeviceState", kwargs={"device_id": "lamp_br_night", "state_update": {"power": "off"}}),
            Action(name="GetRoomInfo", kwargs={"room_ids": ["bedroom_master"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_air_purifier_supplies"}),
        ],
        outputs=[]
    ),
    # Task 23 – Stabilize climate post-thermometer reading by tweaking heater and curtains, and gather necessary supplies.
    Task(
        annotator="0",
        user_id="res_23",
        instruction="""
        It seems warm inside your home. Begin by inspecting the temperature on your Living Room Thermometer (sensor_id: sensor_lr_thermometer).

        Regardless of the temperature reading, proceed with these steps to stabilize the environment: Configure the AC unit (device_id: ac_home) by switching it on, selecting cool mode, setting the temperature to 23°C, and adjusting the fan speed to "medium". Confirm that the heater (device_id: heater_home) is off. Set the Living Room curtain (device_id: curtain_lr) to 75% open, ensuring it stays powered on.

        For energy efficiency, ensure the Living Room Floor Lamp (device_id: light_lr_floor) is switched off. Additionally, compile a custom shopping list named "Climate Balance Supplies" (list_id: list_climate_balance_supplies) and include: one pack of air filters and one bottle of water.

        Once all these modifications are completed, present the updated states for the AC unit, heater, curtain, and floor lamp, and review the shopping list to confirm your modifications.
        """,
        actions=[
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_lr_thermometer"]}),
            Action(name="SetDeviceState", kwargs={"device_id": "ac_home", "state_update": {"power": "on", "mode": "cool", "setpoint_c": 23, "fan_speed": "medium"}}),
            Action(name="SetDeviceState", kwargs={"device_id": "heater_home", "state_update": {"power": "off"}}),
            Action(name="SetDeviceState", kwargs={"device_id": "curtain_lr", "state_update": {"power": "on", "position": 75}}),
            Action(name="SetDeviceState", kwargs={"device_id": "light_lr_floor", "state_update": {"power": "off"}}),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_climate_balance_supplies",

                        "items": [
                            {"item": "Air filters", "quantity": 1},
                            {"item": "Water bottle", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["ac_home", "heater_home", "curtain_lr", "light_lr_floor"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_climate_balance_supplies"}),
        ],
        outputs=[]
    ),
    # Task 24 – Develop and execute an energy-efficient morning scene.
    Task(
        annotator="0",
        user_id="res_24",
        instruction="""
        You aim to begin your day in an energy-saving manner. Initially, verify current readings from your Living Room Air-Quality Sensor (sensor_lr_air_quality) and Master Bedroom Temperature Sensor (sensor_br_temp) to confirm environmental comfort before applying any changes. If the Master Bedroom Temperature Sensor is absent, establish it with these details: id "sensor_br_temp", type "temperature_sensor", location "Master Bedroom", vendor "Xiaomi", model "TempSense X1", firmware_version "1.0.0", and state_params ["temperature_c"].

        Then, formulate a new scene named "Eco Morning" with id "scene_eco_morning" to set your home for a lower-energy morning. Adjust your devices as follows: In the living room, activate the ceiling light (light_lr_ceiling) at 70% brightness and set the color temperature to 5000K. Within the master bedroom, activate the ceiling light (light_br_ceiling) at 60% brightness. For climate control, deactivate the central heater (heater_home), and configure the AC (ac_home) to cool mode at 24°C, fan speed set to "auto".

        To optimize energy efficiency, verify that the Living Room Floor Lamp (light_lr_floor) is switched off. Additionally, develop a custom shopping list titled "Eco Morning Essentials" (list_id: list_eco_morning_essentials) including: 1 LED bulbs and 1 Eco-friendly cleaner.

        Subsequent to scene creation, execute it right away. Proceed to include 1 Reusable kitchen towels and 1 Plant-based dish soap in the shopping list. Also, ensure the kitchen dishwasher (device_id: dishwasher_kt) is turned off for energy conservation. Before applying any device adjustments, review the present condition of the Living Room Floor Lamp (light_lr_floor) and the kitchen dishwasher (dishwasher_kt).

        Ultimately, present the updated conditions of both ceiling lights, the heater, the AC unit, the floor lamp, the dishwasher, and the shopping list to authenticate your energy-saving configuration.
        """,
        actions=[
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_lr_air_quality", "sensor_br_temp"]}),
            Action(
                name="AddDevice",
                kwargs={
                    "new_device": {
                        "id": "sensor_br_temp",
                        "type": "temperature_sensor",
                        "location": "Master Bedroom",
                        "vendor": "Xiaomi",
                        "model": "TempSense X1",
                        "firmware_version": "1.0.0",
                        "state_params": ["temperature_c"],
                        "state": {},
                        "scheduled_updates": []
                    }
                }
            ),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["light_lr_floor", "dishwasher_kt"]}),
            Action(name="ListAllScenes", kwargs={}),
            Action(
                name="CreateScene",
                kwargs={
                    "new_scene": {
                        "id": "scene_eco_morning",
                        "actions": [
                            {"device_id": "light_lr_ceiling", "update": {"power": "on", "brightness": 70, "color": {"kelvin": 5000}}},
                            {"device_id": "light_br_ceiling", "update": {"power": "on", "brightness": 60}},
                            {"device_id": "heater_home", "update": {"power": "off"}},
                            {"device_id": "ac_home", "update": {"power": "on", "mode": "cool", "setpoint_c": 24, "fan_speed": "auto"}}
                        ]
                    }
                }
            ),
            Action(name="ActivateScene", kwargs={"scene_id": "scene_eco_morning"}),
            Action(name="SetDeviceState", kwargs={"device_id": "light_lr_floor", "state_update": {"power": "off"}}),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_eco_morning_essentials",

                        "items": [
                            {"item": "LED bulbs", "quantity": 1},
                            {"item": "Eco-friendly cleaner", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_eco_morning_essentials", "item": {"item": "Reusable kitchen towels", "quantity": 1}, "action": "add"}),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_eco_morning_essentials", "item": {"item": "Plant-based dish soap", "quantity": 1}, "action": "add"}),
            Action(name="SetDeviceState", kwargs={"device_id": "dishwasher_kt", "state_update": {"power": "off"}}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["light_lr_ceiling", "light_br_ceiling", "heater_home", "ac_home", "light_lr_floor", "dishwasher_kt"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_eco_morning_essentials"}),
        ],
        outputs=[]
    ),
    # Task 25 – Verify for leaks, implement safety shut-off, prepare supplies inventory, and set a follow-up reminder.
    Task(
        annotator="0",
        user_id="res_25",
        instruction="""
        Handle a safety assessment in your kitchen. Begin by examining the current status of your Kitchen Sink Leak Sensor (sensor_id: sensor_sink_leak) to confirm there are no water-related issues.

        Then, check whether your Kitchen Dishwasher (device_id: dishwasher_kt) is switched off for safety reasons. If it is still on, switch it off.

        In preparation for any potential leak repairs, organize a new custom list labeled "Leak Repair Supplies" with id "list_leak_repair_supplies" and mark it with "maintenance". Add these items to the list: one roll of plumber's tape and one leak repair kit.

        To continue monitoring the safety inspection, set up a reminder (rem_leak_followup) to reassess the sensor in 30 minutes, precisely at 07:40. Set the reminder with high priority and configure it to deliver a mobile push notification.

        Conclude by presenting the newly established reminder and the supplies list to ensure everything is organized and ready.
        """,
        actions=[
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_sink_leak"]}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["dishwasher_kt"]}),
            Action(name="SetDeviceState", kwargs={"device_id": "dishwasher_kt", "state_update": {"power": "off"}}),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_leak_repair_supplies",

                        "items": [
                            {"item": "Plumber's tape", "quantity": 1},
                            {"item": "Leak repair kit", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="AddReminder",
                kwargs={
                    "new_reminder": {
                        "reminder_id": "rem_leak_followup",
                        "target": {"type": "note", "text": "Check kitchen leak sensor again"},
                        "trigger": {"datetime": "07:40"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "high"},
                        "status": "scheduled",
                    }
                }
            ),
            Action(name="GetReminders", kwargs={"reminder_id": "rem_leak_followup"}),
            Action(name="GetCustomList", kwargs={"list_id": "list_leak_repair_supplies"}),
        ],
        outputs=[]
    ),

    # Task 26 – Update the obsolete credit card bill reminder with a revised schedule, inventory list, and safety verification.
    Task(
        annotator="0",
        user_id="res_26",
        instruction="""
        Coordinate updates to your credit card bill reminder system and organize for monthly payments. Start by revealing your current reminder (rem_94f92a43) to check its configuration, then remove it since it is no longer relevant.

        Prior to making any adjustments, verify the current status of your Kitchen Dishwasher (device_id: dishwasher_kt) to ensure it remains powered off for safety. If it is not off, power it down.

        Proceed by establishing a new reminder with id "rem_cc_bill_new" to assist you in managing your monthly payments. Schedule it to activate on the 10th of every month at 09:00 using the rule "FREQ=MONTHLY;BYMONTHDAY=10;BYHOUR=9;BYMINUTE=0". Configure it with high priority and set it to issue mobile push notifications.

        To aid in your bill payment preparations, set up a new custom list named "Credit Card Payment Supplies" with id "list_cc_payment_supplies" and tag it with "finance". Include these items in the list: one envelope and one pen.

        Upon creating the new reminder and supplies list, present both to confirm that all configurations are correct and everything is scheduled and arranged properly.
        """,
        actions=[
            Action(name="GetReminders", kwargs={"reminder_id": "rem_94f92a43"}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["dishwasher_kt"]}),
            Action(name="SetDeviceState", kwargs={"device_id": "dishwasher_kt", "state_update": {"power": "off"}}),
            Action(name="DeleteReminder", kwargs={"reminder_id": "rem_94f92a43"}),
            Action(
                name="AddReminder",
                kwargs={
                    "new_reminder": {
                        "reminder_id": "rem_cc_bill_new",
                        "target": {"type": "note", "text": "Pay credit-card bill"},
                        "trigger": {"rrule": "FREQ=MONTHLY;BYMONTHDAY=10;BYHOUR=9;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "high"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_cc_payment_supplies",

                        "items": [
                            {"item": "Envelope", "quantity": 1},
                            {"item": "Pen", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="GetReminders", kwargs={"reminder_id": "rem_cc_bill_new"}),
            Action(name="GetCustomList", kwargs={"list_id": "list_cc_payment_supplies"}),
        ],
        outputs=[]
    ),

    # Task 27 – Set up a smart TV, enlarge the movie scene, verify the sensor, and gather materials.
    Task(
        annotator="0",
        user_id="res_27",
        instruction="""
        Enhance your movie-watching experience by incorporating a smart TV into your setup. Begin by showing the current information about your Living Room.

        Prior to implementing any changes, verify the current reading from your Living Room Air-Quality Sensor (sensor_id: sensor_lr_air_quality) to confirm the environment is suitable for movie viewing.

        Proceed to install a new Samsung QN90A TV with the following specifications: Register it under ID "tv_lr" as a device of type "tv". Designate it as "Living Room TV" and assign its location to the Living Room. It's a Samsung product, model QN90A, operating on firmware version 1.0.0. The device has the capability to handle these state parameters: power, input_source, and volume.

        During the initial setup, set it to powered off, configure the input source to "HDMI1", and adjust volume to 10. Once the device is added, link it to your Living Room (room_id: "living_room").

        Subsequently, establish a new scene named "Movie Plus" with id "scene_movie_plus" to optimize your devices for movie viewing: Switch on the TV, set its input to "HDMI1" and adjust the volume to 15, switch off the living room ceiling light (light_lr_ceiling), and close the curtain (curtain_lr) by setting its position to 0 whilst maintaining it powered on.

        To prevent distractions, ensure the Living Room Floor Lamp (device_id: light_lr_floor) is turned off before initiating the scene.

        Also, assemble a custom shopping list titled "Movie Plus Essentials" (list_id: list_movie_plus_essentials) and include the following items: one pack of popcorn and one bottle of soda.

        In conclusion, activate the scene and present the current states of the TV, ceiling light, curtain, floor lamp, and the shopping list to confirm your movie setup.
        """,
        actions=[
            Action(name="GetRoomInfo", kwargs={"room_ids": ["living_room"]}),
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(
                name="AddDevice",
                kwargs={
                    "new_device": {
                        "id": "tv_lr",
                        "type": "tv",
                        "location": "Living Room",
                        "vendor": "Samsung",
                        "model": "QN90A",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "input_source", "volume"],
                        "state": {
                            "power": "off",
                            "input_source": "HDMI1",
                            "volume": 10,
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(name="ManageRoomDevices", kwargs={"room_id": "living_room", "device_id": "tv_lr", "action": "add"}),
            Action(
                name="CreateScene",
                kwargs={
                    "new_scene": {
                        "id": "scene_movie_plus",
                        "actions": [
                            {"device_id": "tv_lr", "update": {"power": "on", "input_source": "HDMI1", "volume": 15}},
                            {"device_id": "light_lr_ceiling", "update": {"power": "off"}},
                            {"device_id": "curtain_lr", "update": {"power": "on", "position": 0}}
                        ]
                    }
                }
            ),
            Action(name="SetDeviceState", kwargs={"device_id": "light_lr_floor", "state_update": {"power": "off"}}),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_movie_plus_essentials",

                        "items": [
                            {"item": "Popcorn", "quantity": 1},
                            {"item": "Soda", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="ActivateScene", kwargs={"scene_id": "scene_movie_plus"}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["tv_lr", "light_lr_ceiling", "curtain_lr", "light_lr_floor"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_movie_plus_essentials"}),
        ],
        outputs=[]
    ),

    # Task 28 – Create a list of supplies for the birthday party and verify kitchen safety.
    Task(
        annotator="0",
        user_id="res_28",
        instruction="""
        Your son's birthday is approaching next month, and you need to organize a list of party supplies and ensure your kitchen is secure before heading out to shop. First, examine the current state of your Kitchen Dishwasher (device_id: dishwasher_kt) to ensure it is powered off for safety prior to leaving for shopping. If it's not off, power it down.

        Then, formulate a new custom list with these criteria: Assign the list_id "list_birthday_party" and title it "Birthday Party Supplies". Mark it with "party". Initially, include these items in your list: twenty Balloons, two Candles, and one Cake Mix.

        Once the list is created, perform three changes: Add three packages of Confetti, add one pack of Paper Plates, and then eliminate the Candles entry. Lastly, exhibit the complete list to confirm that all modifications have been correctly implemented.
        """,
        actions=[
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["dishwasher_kt"]}),
            Action(name="SetDeviceState", kwargs={"device_id": "dishwasher_kt", "state_update": {"power": "off"}}),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_birthday_party",

                        "items": [
                            {"item": "Balloons", "quantity": 20},
                            {"item": "Candles", "quantity": 2},
                            {"item": "Cake Mix", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_birthday_party", "item": {"item": "Confetti", "quantity": 3}, "action": "add"}),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_birthday_party", "item": {"item": "Paper Plates", "quantity": 1}, "action": "add"}),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_birthday_party", "item": {"item": "Candles"}, "action": "remove"}),
            Action(name="GetCustomList", kwargs={"list_id": "list_birthday_party"}),
        ],
        outputs=[]
    ),

    # Task 29 – Evening camera inspection, inventory checklist, and safety shutdown.
    Task(
        annotator="0",
        user_id="res_29",
        instruction="""
        You are aiming to strengthen your home's nightly security monitoring. Start by verifying the current status of your security cameras: the front door camera (camera_front_door) and the back door camera (camera_back_door) to ensure they are operational.

        Then, switch both cameras to active by setting their stream_online and recording parameters to True.

        To maintain regular security confirmations, establish a daily reminder (rem_camera_night) that will alert you to check if the cameras are recording. Schedule it to trigger every day at 22:00 using the rrule "FREQ=DAILY;BYHOUR=22;BYMINUTE=0". Set it to normal priority and configure it to send mobile push notifications.

        For future maintenance readiness, create a custom shopping list labeled "Camera Night Essentials" (list_id: list_camera_night_essentials) and include the following items: one pack of camera batteries and one lens cleaning cloth.

        To achieve energy efficiency, confirm that the Living Room Floor Lamp (device_id: light_lr_floor) is switched off during the night.

        Once these tasks are done, present the reminder, the shopping list, and the status of both cameras and the floor lamp to verify all settings are correct.
        """,
        actions=[
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["camera_front_door", "camera_back_door"]}),
            Action(name="SetDeviceState", kwargs={"device_id": "camera_front_door", "state_update": {"stream_online": True, "recording": True}}),
            Action(name="SetDeviceState", kwargs={"device_id": "camera_back_door", "state_update": {"stream_online": True, "recording": True}}),
            Action(
                name="AddReminder",
                kwargs={
                    "new_reminder": {
                        "reminder_id": "rem_camera_night",
                        "target": {"type": "note", "text": "Verify cameras recording"},
                        "trigger": {"rrule": "FREQ=DAILY;BYHOUR=22;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_camera_night_essentials",

                        "items": [
                            {"item": "Camera batteries", "quantity": 1},
                            {"item": "Lens cleaning cloth", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="SetDeviceState", kwargs={"device_id": "light_lr_floor", "state_update": {"power": "off"}}),
            Action(name="GetReminders", kwargs={"reminder_id": "rem_camera_night"}),
            Action(name="GetCustomList", kwargs={"list_id": "list_camera_night_essentials"}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["camera_front_door", "camera_back_door", "light_lr_floor"]}),
        ],
        outputs=[]
    ),

    # Task 30 – Replace bedside lamp in East Bedroom, verify device status, and gather materials.
    Task(
        annotator="0",
        user_id="res_30",
        instruction="""
        You are required to set up a new bedside lamp in your East Bedroom, replacing the outdated one. Here are the new device specifications:

        Register it under ID "lamp_be_bedside2" as a device of type "light". Designate it as "East Bedroom Bedside Lamp (New)" and assign its location to East Bedroom. It's a Govee Aura HLB-2 model operating firmware version 1.4.0. The device supports these state parameters: power, brightness, and color.

        During initial setup, configure it to be powered off, with 0% brightness, and adjust its color to a warm yellow (hue=45, saturation=80).

        Prior to adjustments, confirm the current state of the East Bedroom (room_id: "bedroom_east") to ensure device status.

        Once the device is added, register it in your East Bedroom (room_id: "bedroom_east"). Proceed to turn it on, adjust brightness to 50%, and retain the same warm yellow color settings (hue=45, saturation=80).

        To facilitate future upkeep, formulate a custom shopping list titled "Bedside Lamp Supplies" (list_id: list_bedside_lamp_supplies) and include the following items: one replacement bulb and one cleaning cloth.

        Ensure for safety that the East Bedroom ceiling light (device_id: light_be_ceiling) is powered off post installation of the new lamp.

        Conclusively, display the East Bedroom details and the supplies list to confirm the installation and preparations.
        """,
        actions=[
            Action(name="GetRoomInfo", kwargs={"room_ids": ["bedroom_east"]}),
            Action(
                name="AddDevice",
                kwargs={
                    "new_device": {
                        "id": "lamp_be_bedside2",
                        "type": "light",
                        "location": "East Bedroom",
                        "vendor": "Govee",
                        "model": "Aura HLB-2",
                        "firmware_version": "1.4.0",
                        "state_params": ["power", "brightness", "color"],
                        "state": {
                            "power": "off",
                            "brightness": 0,
                            "color": {"hue": 45, "saturation": 80},
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(name="ManageRoomDevices", kwargs={"room_id": "bedroom_east", "device_id": "lamp_be_bedside2", "action": "add"}),
            Action(name="SetDeviceState", kwargs={"device_id": "lamp_be_bedside2", "state_update": {"power": "on", "brightness": 50, "color": {"hue": 45, "saturation": 80}}}),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_bedside_lamp_supplies",

                        "items": [
                            {"item": "Replacement bulb", "quantity": 1},
                            {"item": "Cleaning cloth", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="SetDeviceState", kwargs={"device_id": "light_be_ceiling", "state_update": {"power": "off"}}),
            Action(name="GetRoomInfo", kwargs={"room_ids": ["bedroom_east"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_bedside_lamp_supplies"}),
        ],
        outputs=[]
    ),
    # Task 31 – Enhance air quality through adjustments to the purifier and AC, along with a supplies inventory and safety inspection.
    Task(
        annotator="0",
        user_id="res_31",
        instruction="""
        The air in your home feels stuffy. Initially, assess the current CO₂ and VOC levels by using your Living Room Air-Quality Sensor (sensor_lr_air_quality).

        To enhance air quality, proceed with these modifications: First, manage your Living Room Air-Purifier (device_id: air_purifier_lr) by activating it, configuring it to auto mode, and elevating the fan speed to "high". Next, modify your AC unit (device_id: ac_home) by setting its fan speed to "medium" to assist with air circulation.

        For energy conservation, ensure the Living Room Floor Lamp (device_id: light_lr_floor) remains off after executing these changes.

        Additionally, generate a shopping list titled "Air Quality Supplies" (list_id: list_air_quality_supplies) and include the following items: one replacement air filter and one bottle of air freshener.

        Upon finishing all tasks, present the updated statuses of the air purifier, AC unit, and floor lamp, and display the shopping list to confirm your adjustments.
        """,
        actions=[
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(name="SetDeviceState", kwargs={"device_id": "air_purifier_lr", "state_update": {"power": "on", "mode": "auto", "fan_speed": "high"}}),
            Action(name="SetDeviceState", kwargs={"device_id": "ac_home", "state_update": {"fan_speed": "medium"}}),
            Action(name="SetDeviceState", kwargs={"device_id": "light_lr_floor", "state_update": {"power": "off"}}),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_air_quality_supplies",

                        "items": [
                            {"item": "Replacement air filter", "quantity": 1},
                            {"item": "Air freshener", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["air_purifier_lr", "ac_home", "light_lr_floor"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_air_quality_supplies"}),
        ],
        outputs=[]
    ),

    # Task 32 – Develop and execute a "Return Home" scene, including resource and safety assessments.
    Task(
        annotator="0",
        user_id="res_32",
        instruction="""
        You're returning from vacation tonight and aim to prepare your home for your arrival. Initially, check the current data from your Living Room Air-Quality Sensor (sensor_id: sensor_lr_air_quality) to ensure the setting is comfortable.

        Establish a new scene titled "Return Home" with id "scene_return_home" that will adjust your devices as follows:

        Start by making the living room inviting: Fully draw open the curtain (curtain_lr) by adjusting its position to 100 while it remains powered on, and switch on the ceiling light (light_lr_ceiling) at 80% brightness with a warm white color temperature of 4000K. For optimal temperature, activate the heater (heater_home) in heat mode at 22°C, and ensure the AC (ac_home) is switched off. Conclude with creating ambiance in the master bedroom by lighting the night lamp (lamp_br_night) at 30% brightness with a warm orange glow (color settings: hue=30, saturation=60).

        To maintain a serene setting, ensure the Living Room Floor Lamp (device_id: light_lr_floor) is turned off before triggering the scene.

        Also, assemble a shopping list named "Return Home Essentials" (list_id: list_return_home_essentials) and include the following items: one bottle of milk and one loaf of bread.

        Following the scene's creation, activate it without delay and display the current statuses of all five mentioned devices, the floor lamp, and the shopping list to verify everything is in place for your return.
        """,
        actions=[
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(name="ListAllScenes", kwargs={}),
            Action(
                name="CreateScene",
                kwargs={
                    "new_scene": {
                        "id": "scene_return_home",
                        "actions": [
                            {"device_id": "curtain_lr", "update": {"power": "on", "position": 100}},
                            {"device_id": "light_lr_ceiling", "update": {"power": "on", "brightness": 80, "color": {"kelvin": 4000}}},
                            {"device_id": "heater_home", "update": {"power": "on", "mode": "heat", "setpoint_c": 22}},
                            {"device_id": "ac_home", "update": {"power": "off"}},
                            {"device_id": "lamp_br_night", "update": {"power": "on", "brightness": 30, "color": {"hue": 30, "saturation": 60}}}
                        ]
                    }
                }
            ),
            Action(name="SetDeviceState", kwargs={"device_id": "light_lr_floor", "state_update": {"power": "off"}}),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_return_home_essentials",

                        "items": [
                            {"item": "Milk", "quantity": 1},
                            {"item": "Bread", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="ActivateScene", kwargs={"scene_id": "scene_return_home"}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["curtain_lr", "light_lr_ceiling", "heater_home", "ac_home", "lamp_br_night", "light_lr_floor"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_return_home_essentials"}),
        ],
        outputs=[]
    ),
    # Task 33 – Configure the daily homework alert for Olivia, create a list of required supplies, and perform a device safety inspection.
    Task(
        annotator="0",
        user_id="res_33",
        instruction="""
        Assist Emma in organizing her homework routine efficiently. Begin by evaluating the current status of the Desk Lamp in Emma's room (device_id: lamp_olivia_desk) to confirm it's switched off for energy conservation before implementing any adjustments. If this device is not present, establish it with these parameters: id "lamp_olivia_desk", type "light", location "Emma's Room", vendor "Philips", model "StudyLamp X2", firmware_version "1.0.0", and state_params ["power", "brightness", "color"].

        Following that, assemble a supplies list with these details: Generate a new list entitled "Homework Supplies" with id "list_homework_supplies" and label it with "school". Initially, incorporate these items: ten Pencils, three Erasers, and two Notebooks.

        Subsequent to list creation, incorporate four Highlighters and one pack of Sticky Notes into it. Display the updated list to ensure all items are correctly included.

        For consistent homework discipline, schedule a daily reminder (reminder_id: rem_homework_daily) to alert Emma for homework completion. Set it to activate daily at 16:30, configure it with normal priority, and opt for mobile push notifications.

        Conclude by ensuring the Desk Lamp (lamp_olivia_desk) remains powered off to save energy, and exhibit both the reminder and lamp state for confirmation of proper scheduling and setup.
        """,
        actions=[
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["lamp_olivia_desk"]}),
            Action(
                name="AddDevice",
                kwargs={
                    "new_device": {
                        "id": "lamp_olivia_desk",
                        "type": "light",
                        "location": "Emma's Room",
                        "vendor": "Philips",
                        "model": "StudyLamp X2",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "brightness", "color"],
                        "state": {
                            "power": "off",
                            "brightness": 0,
                            "color": {"hue": 45, "saturation": 80},
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_homework_supplies",

                        "items": [
                            {"item": "Pencils", "quantity": 10},
                            {"item": "Erasers", "quantity": 3},
                            {"item": "Notebook", "quantity": 2}
                        ]
                    }
                }
            ),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_homework_supplies", "item": {"item": "Highlighters", "quantity": 4}, "action": "add"}),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_homework_supplies", "item": {"item": "Sticky Notes", "quantity": 1}, "action": "add"}),
            Action(name="GetCustomList", kwargs={"list_id": "list_homework_supplies"}),
            Action(
                name="AddReminder",
                kwargs={
                    "new_reminder": {
                        "reminder_id": "rem_homework_daily",
                        "target": {"type": "note", "text": "Do homework"},
                        "trigger": {"rrule": "FREQ=DAILY;BYHOUR=16;BYMINUTE=30"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(name="SetDeviceState", kwargs={"device_id": "lamp_olivia_desk", "state_update": {"power": "off"}}),
            Action(name="GetReminders", kwargs={"reminder_id": "rem_homework_daily"}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["lamp_olivia_desk"]}),
        ],
        outputs=[]
    ),

    # Task 34 – Set up washing machine in the basement, initiate a quick wash cycle, gather necessary supplies, and verify safety measures.
    Task(
        annotator="0",
        user_id="res_34",
        instruction="""
        Your task is to install a new LG TurboWash washing machine in your basement. Adhere to these device specifications:

        Enter it with ID "washer_bs" classifying it as a device of type "washing_machine". Assign it the name "Basement Washing Machine" and designate its location to Basement. It is an LG TurboWash 360 model operating on firmware version 1.0.0. The device allows these state parameters: power, cycle, time_remaining_min, and door.

        For initial configuration, set it as powered off, in an idle cycle mode, with 0 minutes remaining, and the door closed.

        Prior to proceeding with modifications, assess the existing state of the Basement Washing Machine (device_id: washer_bs) to confirm its condition.

        Post device addition, register it to your basement (room_id: "basement"). Then initiate a quick wash by activating it, adjusting the cycle to "quick", setting the remaining time to 35 minutes, and maintaining the door closed.

        To gear up for laundry tasks, devise a custom shopping list labeled "Basement Laundry Supplies" (list_id: list_basement_laundry_supplies) including one pack of detergent and one box of dryer sheets.

        For security purposes, validate that the Basement Washing Machine (device_id: washer_bs) is powered off post wash cycle completion.

        Lastly, showcase the basement information along with the supplies list to confirm the setup and arrangements.
        """,
        actions=[
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["washer_bs"]}),
            Action(
                name="AddDevice",
                kwargs={
                    "new_device": {
                        "id": "washer_bs",
                        "type": "washing_machine",
                        "location": "Basement",
                        "vendor": "LG",
                        "model": "TurboWash 360",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "cycle", "time_remaining_min", "door"],
                        "state": {
                            "power": "off",
                            "cycle": "idle",
                            "time_remaining_min": 0,
                            "door": "closed",
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(name="ManageRoomDevices", kwargs={"room_id": "basement", "device_id": "washer_bs", "action": "add"}),
            Action(name="SetDeviceState", kwargs={"device_id": "washer_bs", "state_update": {"power": "on", "cycle": "quick", "time_remaining_min": 35, "door": "closed"}}),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_basement_laundry_supplies",

                        "items": [
                            {"item": "Detergent", "quantity": 1},
                            {"item": "Dryer sheets", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="SetDeviceState", kwargs={"device_id": "washer_bs", "state_update": {"power": "off", "cycle": "idle", "time_remaining_min": 0, "door": "closed"}}),
            Action(name="GetRoomInfo", kwargs={"room_ids": ["basement"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_basement_laundry_supplies"}),
        ],
        outputs=[]
    ),

    # Task 35 – Develop a Focus Study environment for the West Bedroom using the air-quality sensor and inventory list.
    Task(
        annotator="0",
        user_id="res_35",
        instruction="""
        As it is 2025-07-30 08:30, arrange an ideal study setting. Begin by checking the current air quality data from your Living Room Air-Quality Sensor (sensor_lr_air_quality) to confirm a healthy study atmosphere.

        Subsequently, set up a new scene titled "Study Fresh" with id "scene_study_fresh" that will configure your devices like this:

        For the best lighting, activate the West Bedroom Desk Lamp (lamp_bw_desk) at 90% brightness and adjust its color temperature to 5500K. Disable the West Bedroom Ceiling Light (light_bw_ceiling) to prevent glare. For natural illumination and airflow, open the West Bedroom Curtain (curtain_bw) to 75% while maintaining power. Lastly, promote good air quality by switching on the Living Room Air-Purifier (air_purifier_lr), setting it to auto mode with a medium fan speed.

        To ensure you have everything for undistracted study, compile a custom shopping list named "Study Fresh Essentials" (list_id: list_study_fresh_essentials) including: one pack of sticky notes and one bottle of water.

        Additionally, confirm the Living Room Floor Lamp (light_lr_floor) is switched off to minimize distractions.

        After creating the scene, engage it promptly and display the current status of all four devices, the shopping list, and the status of the Living Room Floor Lamp to verify your study setup is complete.
        """,
        actions=[
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(name="ListAllScenes", kwargs={}),
            Action(name="GetRoomInfo", kwargs={"room_ids": ["bedroom_west"]}),
            Action(
                name="CreateScene",
                kwargs={
                    "new_scene": {
                        "id": "scene_study_fresh",
                        "actions": [
                            {"device_id": "lamp_bw_desk", "update": {"power": "on", "brightness": 90, "color_temperature": 5500}},
                            {"device_id": "light_bw_ceiling", "update": {"power": "off"}},
                            {"device_id": "curtain_bw", "update": {"power": "on", "position": 75}},
                            {"device_id": "air_purifier_lr", "update": {"power": "on", "mode": "auto", "fan_speed": "medium"}}
                        ]
                    }
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_study_fresh_essentials",

                        "items": [
                            {"item": "Sticky notes", "quantity": 1},
                            {"item": "Water bottle", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="SetDeviceState",
                kwargs={
                    "device_id": "light_lr_floor",
                    "state_update": {"power": "off"}
                }
            ),
            Action(name="ActivateScene", kwargs={"scene_id": "scene_study_fresh"}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["lamp_bw_desk", "light_bw_ceiling", "curtain_bw", "air_purifier_lr", "light_lr_floor"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_study_fresh_essentials"}),
        ],
        outputs=[]
    ),

    # Task 36 – Revise shopping list, include omitted items, verify kitchen safety, and establish weekly grocery reminder.
    Task(
        annotator="0",
        user_id="res_36",
        instruction="""
        It's necessary to update your shopping list and organize a regular grocery reminder. Initially, inspect the current status of your Kitchen Dishwasher (device_id: dishwasher_kt) to ensure it's turned off to maintain safety prior to making any updates. If it's on, switch it off.

        Proceed with modifying your existing shopping list (list_id: list_shopping): Insert twelve rolls of Toilet Paper, and eliminate one entry of Dog Food from the list. Moreover, include two bottles of Dish Soap and one pack of Sponges to guarantee adequate cleaning supplies.

        Following these updates, display the revised list to confirm the changes.

        To aid your grocery shopping routine, establish a weekly reminder (reminder_id: rem_weekly_groceries) that will alert you every Saturday at 09:30. Implement the rrule "FREQ=WEEKLY;BYDAY=SA;BYHOUR=9;BYMINUTE=30", set it at normal priority, and configure it to push notifications to your mobile.

        Finally, reveal the newly established reminder and the dishwasher's state to ensure everything is scheduled correctly and safe.
        """,
        actions=[
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["dishwasher_kt"]}),
            Action(name="SetDeviceState", kwargs={"device_id": "dishwasher_kt", "state_update": {"power": "off"}}),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_shopping", "item": {"item": "Toilet Paper", "quantity": 12}, "action": "add"}),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_shopping", "item": {"item": "Dog Food"}, "action": "remove"}),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_shopping", "item": {"item": "Dish Soap", "quantity": 2}, "action": "add"}),
            Action(name="ManageCustomListItems", kwargs={"list_id": "list_shopping", "item": {"item": "Sponges", "quantity": 1}, "action": "add"}),
            Action(name="GetCustomList", kwargs={"list_id": "list_shopping"}),
            Action(
                name="AddReminder",
                kwargs={
                    "new_reminder": {
                        "reminder_id": "rem_weekly_groceries",
                        "target": {"type": "entity", "entity_type": "list", "entity_id": "list_shopping"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=SA;BYHOUR=9;BYMINUTE=30"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(name="GetReminders", kwargs={"reminder_id": "rem_weekly_groceries"}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["dishwasher_kt"]}),
        ],
        outputs=[]
    ),

    # Task 37 – Update the outdated Good Night scene with a new version and gather necessary materials.
    Task(
        annotator="0",
        user_id="res_37",
        instruction="""
        Handle the upgrade for your bedtime scene by incorporating a new version, ensuring everything is set for a peaceful evening. Initially, verify the reading from your Living Room Air-Quality Sensor (sensor_id: sensor_lr_air_quality) to confirm a comfortable environment prior to adjustments.

        Designate a new scene called "Good Night Plus" with id "scene_good_night_plus" that will adjust your devices accordingly:

        In the living room, set the curtain (curtain_lr) position to 0 while it remains on, and switch off both the floor and ceiling lights (light_lr_floor and light_lr_ceiling). Create a relaxing atmosphere in the master bedroom by illuminating the night lamp (lamp_br_night) to 10% brightness with a warm tone (color settings: hue=30, saturation=40). To maintain tranquility, adjust your AC unit's (ac_home) fan speed to "low".

        Prior to activating the new scene, remove the existing scene (scene_good_night). Additionally, ensure the kitchen dishwasher (device_id: dishwasher_kt) is turned off for safety before sleeping.

        To set the scene for the night, organize a custom shopping list titled "Good Night Essentials" (list_id: list_good_night_essentials) and include the following items: one sleep mask and one bottle of water.

        After implementing your new scene, present the updated statuses of all devices, the dishwasher, and the shopping list to confirm your enhanced bedtime arrangement.
        """,
        actions=[
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["dishwasher_kt"]}),
            Action(name="SetDeviceState", kwargs={"device_id": "dishwasher_kt", "state_update": {"power": "off"}}),
            Action(name="DeleteScene", kwargs={"scene_id": "scene_good_night"}),
            Action(
                name="CreateScene",
                kwargs={
                    "new_scene": {
                        "id": "scene_good_night_plus",
                        "actions": [
                            {"device_id": "curtain_lr", "update": {"power": "on", "position": 0}},
                            {"device_id": "light_lr_floor", "update": {"power": "off"}},
                            {"device_id": "light_lr_ceiling", "update": {"power": "off"}},
                            {"device_id": "lamp_br_night", "update": {"power": "on", "brightness": 10, "color": {"hue": 30, "saturation": 40}}},
                            {"device_id": "ac_home", "update": {"fan_speed": "low"}}
                        ]
                    }
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_good_night_essentials",

                        "items": [
                            {"item": "Sleep mask", "quantity": 1},
                            {"item": "Water bottle", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="ActivateScene", kwargs={"scene_id": "scene_good_night_plus"}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["curtain_lr", "light_lr_floor", "light_lr_ceiling", "lamp_br_night", "dishwasher_kt"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_good_night_essentials"}),
        ],
        outputs=[]
    ),

    # Task 38 – Set a reminder for battery replacement, compile a list of needed supplies, and verify safety after inspecting the smoke detector.
    Task(
        annotator="0",
        user_id="res_38",
        instruction="""
        Coordinate the check of your Bedroom Smoke Detector (sensor_id: sensor_bed_smoke) and organize its battery maintenance schedule. Begin by obtaining the current reading from the smoke detector to evaluate its condition.

        Following the check, establish a one-time reminder (reminder_id: rem_smoke_battery) to change the detector's batteries. Set it for 2025-07-01T09:00:00, give it high priority, and configure it to send a mobile push notification.

        Subsequently, get ready for the battery change by forming a custom shopping list named "Smoke Detector Supplies" (list_id: list_smoke_detector_supplies) and add these items: one pack of AA batteries and one cleaning cloth.

        For safety precautions, verify that the Bedroom Night Lamp (device_id: lamp_br_night) is turned off before any maintenance begins. Check its current state before making any adjustments.

        Lastly, showcase the newly established reminder, the supply list, and the lamp status to ensure all is correctly scheduled and ready.
        """,
        actions=[
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_bed_smoke"]}),
            Action(
                name="AddReminder",
                kwargs={
                    "new_reminder": {
                        "reminder_id": "rem_smoke_battery",
                        "target": {"type": "note", "text": "Replace bedroom smoke detector battery"},
                        "trigger": {"datetime": "2025-07-01T09:00:00"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "high"},
                        "status": "scheduled",
                    }
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_smoke_detector_supplies",

                        "items": [
                            {"item": "AA batteries", "quantity": 1},
                            {"item": "Cleaning cloth", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["lamp_br_night"]}),
            Action(name="SetDeviceState", kwargs={"device_id": "lamp_br_night", "state_update": {"power": "off"}}),
            Action(name="GetReminders", kwargs={"reminder_id": "rem_smoke_battery"}),
            Action(name="GetCustomList", kwargs={"list_id": "list_smoke_detector_supplies"}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["lamp_br_night"]}),
        ],
        outputs=[]
    ),

    # Task 39 – Set up robot vacuum, initiate cleaning mode, gather materials, and verify safety measures.
    Task(
        annotator="0",
        user_id="res_39",
        instruction="""
        You've acquired a Roborock S8 robot vacuum for your home. Here are the steps to configure the device:

        Register it with ID "vacuum_lr" as a "vacuum" device. Name it "Living Room Vacuum" and assign its location to Living Room. It is a Roborock S8 model using firmware version 1.0.0. This device supports the following state parameters: power, mode, and battery_pct.

        For the initial setup, ensure it is set as powered off, in idle mode, and has 100% battery.

        Prior to making adjustments, verify the current reading from your Living Room Air-Quality Sensor (sensor_id: sensor_lr_air_quality) to confirm the environment is ideal for cleaning.

        After integrating the vacuum into your Living Room, establish a new scene named "Clean Up" with id "scene_clean_up" to initiate the cleaning process: Power on the vacuum and configure its mode to "clean", and close the living room curtain (curtain_lr) by setting its position to 0 while it remains powered on.

        To organize for future upkeep, generate a custom shopping list named "Vacuum Supplies" (list_id: list_vacuum_supplies) and include these items: one replacement filter and one cleaning brush.

        For safety purposes, ensure the Living Room Floor Lamp (device_id: light_lr_floor) is powered off before scene activation.

        Finally, activate the scene and display the current states of the vacuum, curtain, floor lamp, and the supplies list to confirm your cleaning setup.
        """,
        actions=[
            Action(name="GetSensorData", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(
                name="AddDevice",
                kwargs={
                    "new_device": {
                        "id": "vacuum_lr",
                        "type": "vacuum",
                        "location": "Living Room",
                        "vendor": "Roborock",
                        "model": "S8",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "mode", "battery_pct"],
                        "state": {
                            "power": "off",
                            "mode": "idle",
                            "battery_pct": 100,
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(name="ManageRoomDevices", kwargs={"room_id": "living_room", "device_id": "vacuum_lr", "action": "add"}),
            Action(
                name="CreateScene",
                kwargs={
                    "new_scene": {
                        "id": "scene_clean_up",
                        "actions": [
                            {"device_id": "vacuum_lr", "update": {"power": "on", "mode": "clean"}},
                            {"device_id": "curtain_lr", "update": {"power": "on", "position": 0}}
                        ]
                    }
                }
            ),
            Action(
                name="CreateCustomList",
                kwargs={
                    "new_list": {
                        "list_id": "list_vacuum_supplies",

                        "items": [
                            {"item": "Replacement filter", "quantity": 1},
                            {"item": "Cleaning brush", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="SetDeviceState", kwargs={"device_id": "light_lr_floor", "state_update": {"power": "off"}}),
            Action(name="ActivateScene", kwargs={"scene_id": "scene_clean_up"}),
            Action(name="GetDeviceInfo", kwargs={"device_ids": ["vacuum_lr", "curtain_lr", "light_lr_floor"]}),
            Action(name="GetCustomList", kwargs={"list_id": "list_vacuum_supplies"}),
        ],
        outputs=[]
    ),

    # Task 40 – Get ready for David Lee's dinner visit.
    Task(
        annotator="0",
        user_id="res_40",
        instruction="""
        You're hosting Christopher Chen for dinner this Sunday at 18:30, and aim to create a welcoming setting. Construct a new scene titled "David Dinner" with id "scene_david_dinner" that will configure your home as follows:

        In the living room, fully open the curtain (curtain_lr) by setting its position to 100 while it remains powered on, and switch on the floor lamp (light_lr_floor) at 70% brightness. For comfort, set up the AC unit (ac_home) by turning it on, selecting cool mode at 23°C, with the fan speed set to "low" for quiet operation.

        After devising the scene, arrange a reminder (rem_pickup_dinner) to assist in preparing for his arrival. Set it to alert you at 17:45 on that day to "Pick up the take-out food". Configure it with high priority and set it to dispatch mobile push notifications.

        Finally, display both the scene list and the reminder to ensure everything is correctly prepared for Michael's visit.
        """,
        actions=[
            Action(
                name="CreateScene",
                kwargs={
                    "new_scene": {
                        "id": "scene_david_dinner",
                        "name": "Michael Dinner",
                        "actions": [
                            {"device_id": "curtain_lr", "update": {"power": "on", "position": 100}},
                            {"device_id": "light_lr_floor", "update": {"power": "on", "brightness": 70}},
                            {"device_id": "ac_home", "update": {"power": "on", "mode": "cool", "setpoint_c": 23, "fan_speed": "low"}}
                        ]
                    }
                }
            ),
            Action(
                name="AddReminder",
                kwargs={
                    "new_reminder": {
                        "reminder_id": "rem_pickup_dinner",

                        "target": {"type": "note", "text": "Pick up the take-out food"},
                        "trigger": {"datetime": "2025-07-06T17:45:00"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "high"},
                        "status": "scheduled",

                    }
                }
            ),
            Action(name="ListAllScenes", kwargs={}),
            Action(name="GetReminders", kwargs={"reminder_id": "rem_pickup_dinner"}),
        ],
        outputs=[]
    ),
]
