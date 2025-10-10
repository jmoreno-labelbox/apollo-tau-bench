from domains.dto import Task, Action

TASKS = [
    # Task 1 – Create and activate a complex evening scene
    Task(
        annotator="0",
        user_id="res_01",
        instruction="""
        The time is 2025-07-28 17:45. You need to create a new scene for a relaxed summer evening. Name it "Evening Breeze" with the ID "scene_evening_breeze". When you run this scene, it should prepare the living room by doing the following:

        First, turn on the Living-Room ceiling light (device_id: light_lr_ceiling) and set its brightness to 35%. Next, adjust the Living-Room curtain (device_id: curtain_lr) to be halfway open by setting its position to 50% while ensuring it remains powered on. Then, configure the Central AC (device_id: ac_home) by turning it on in cool mode, setting the temperature to 23°C, and adjusting the fan speed to "medium".

        To make the evening more comfortable, create a custom shopping list named "Evening Essentials" (list_id: list_evening_essentials) and add the following items: one pack of scented candles and one bottle of iced tea. Also, make sure the Living-Room floor lamp (device_id: light_lr_floor) is turned off for a cozy ambiance.

        After you've created the scene, activate it right away. Once it's running, return the new states of all four devices mentioned above and display the shopping list to verify everything is set.
        """,
        actions=[
            Action(
                name="list_all_scenes",
                kwargs={}
            ),
            Action(
                name="create_scene",
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
                name="create_custom_list",
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
                name="activate_scene",
                kwargs={"scene_id": "scene_evening_breeze"}
            ),
            Action(
                name="get_device_info",
                kwargs={"device_ids": ["light_lr_ceiling", "curtain_lr", "ac_home", "light_lr_floor"]}
            ),
            Action(
                name="get_custom_list",
                kwargs={"list_id": "list_evening_essentials"}
            ),
        ],
        outputs=[]
    ),

    # Task 2 – Schedule annual HVAC filter replacement reminder
    Task(
        annotator="0",
        user_id="res_02",
        instruction="""
        You want to ensure regular maintenance of your HVAC system. Start by checking the current information about your AC unit (ac_home) to assess its status.

        Next, create an annual reminder (reminder_id: rem_hvac_filter) to replace the HVAC filters. Schedule it to trigger on January 15th at 10:00 each year using the rrule "FREQ=YEARLY;BYMONTH=1;BYMONTHDAY=15;BYHOUR=10;BYMINUTE=0". Configure it with normal priority and set it to send mobile push notifications.

        To help with preparation, create a custom list named "HVAC Maintenance Supplies" (list_id: list_hvac_supplies) and add the following items: one HVAC filter and one cleaning spray.

        Finally, before maintenance, make sure the AC unit (ac_home) is powered off for safety. After completing these steps, display both the reminder and the supplies list to verify everything is properly scheduled and prepared.
        """,
        actions=[
            Action(name="get_device_info", kwargs={"device_ids": ["ac_home"]}),
            Action(
                name="add_reminder",
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
                name="create_custom_list",
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
                name="set_device_state",
                kwargs={
                    "device_id": "ac_home",
                    "state_update": {"power": "off"}
                }
            ),
            Action(name="get_reminders", kwargs={"reminder_id": "rem_hvac_filter"}),
            Action(name="get_custom_list", kwargs={"list_id": "list_hvac_supplies"}),
        ],
        outputs=[]
    ),

    # Task 3 – Check thermometer reading, heat the house, and prepare for winter
    Task(
        annotator="0",
        user_id="res_03",
        instruction="""
        First, check the current temperature reading from the Living Room Thermometer (sensor_id: sensor_lr_thermometer).

        After checking the reading, regardless of what temperature it shows, configure the Central Heater (device_id: heater_home) with the following exact settings: Turn the power on, set it to heat mode, and adjust the temperature setpoint to 22°C.

        Next, for winter preparation, create a custom shopping list named "Winter Essentials" (list_id: list_winter_essentials) and add the following items: one pack of radiator antifreeze and one set of thermal curtains.

        Finally, ensure the AC unit (device_id: ac_home) is powered off to avoid unnecessary cooling while heating is active. After completing these steps, display the updated heater state and the shopping list to verify everything is set.
        """,
        actions=[
            Action(
                name="get_sensor_data",
                kwargs={"sensor_ids": ["sensor_lr_thermometer"]}
            ),
            Action(
                name="set_device_state",
                kwargs={
                    "device_id": "heater_home",
                    "state_update": {"power": "on", "mode": "heat", "setpoint_c": 22}
                }
            ),
            Action(
                name="create_custom_list",
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
                name="set_device_state",
                kwargs={
                    "device_id": "ac_home",
                    "state_update": {"power": "off"}
                }
            ),
            Action(
                name="get_device_info",
                kwargs={"device_ids": ["heater_home"]}
            ),
            Action(
                name="get_custom_list",
                kwargs={"list_id": "list_winter_essentials"}
            ),
        ],
        outputs=[]
    ),

    # Task 4 – Build a packing list for a camping trip
    Task(
        annotator="0",
        user_id="res_04",
        instruction="""
        You need to create a new custom list for your upcoming camping trip. The list should have the following specifications:

        Set up the list with the ID "list_camping_trip" and name it "Camping Trip Packing". Tag it with "travel" and set both the created_at and updated_at timestamps to "2025-07-28T18:10:00". Initially, add these items to your list: one Tent, four Sleeping Bags, and two packs of Marshmallows.

        Once you've created the list, add one First Aid Kit to it. Next, add two Flashlights and one pack of Batteries to ensure you have enough lighting for the trip. Also, make sure your home heater (device_id: heater_home) is powered off before leaving for safety.

        Then, show the final version of your list and the heater state to verify all items are properly included and the device is safely turned off.
        """,
        actions=[
            Action(
                name="create_custom_list",
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
                name="manage_custom_list_items",
                kwargs={
                    "list_id": "list_camping_trip",
                    "item": {"item": "First Aid Kit", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="manage_custom_list_items",
                kwargs={
                    "list_id": "list_camping_trip",
                    "item": {"item": "Flashlight", "quantity": 2},
                    "action": "add"
                }
            ),
            Action(
                name="manage_custom_list_items",
                kwargs={
                    "list_id": "list_camping_trip",
                    "item": {"item": "Batteries", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="set_device_state",
                kwargs={
                    "device_id": "heater_home",
                    "state_update": {"power": "off"}
                }
            ),
            Action(
                name="get_custom_list",
                kwargs={"list_id": "list_camping_trip"}
            ),
            Action(
                name="get_device_info",
                kwargs={"device_ids": ["heater_home"]}
            ),
        ],
        outputs=[]
    ),

    # Task 5 – Downgrade medication reminder priority and deactivate it, plus prepare for next refill
    Task(
        annotator="0",
        user_id="res_05",
        instruction="""
        You need to modify the Medication Reminder (reminder_id: "rem_254afa34"). Find this reminder and make two changes to it: First, change its status to "inactive". Then, in the meta field, set the priority to "low".

        To help you prepare for your next refill, create a custom shopping list named "Medication Supplies" (list_id: list_medication_supplies) and add one box of your medication and one bottle of water.

        Finally, make sure your bedroom night lamp (device_id: lamp_br_night) is powered off for a restful environment. After making these changes, display the updated reminder, the shopping list, and the lamp state to verify everything is set correctly.
        """,
        actions=[
            Action(
                name="get_reminders",
                kwargs={"reminder_id": "rem_254afa34"}
            ),
            Action(
                name="update_reminder",
                kwargs={
                    "reminder_id": "rem_254afa34",
                    "update_fields": {"status": "inactive", "meta": {"priority": "low"}}
                }
            ),
            Action(
                name="create_custom_list",
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
                name="set_device_state",
                kwargs={
                    "device_id": "lamp_br_night",
                    "state_update": {"power": "off"}
                }
            ),
            Action(
                name="get_reminders",
                kwargs={"reminder_id": "rem_254afa34"}
            ),
            Action(
                name="get_custom_list",
                kwargs={"list_id": "list_medication_supplies"}
            ),
            Action(
                name="get_device_info",
                kwargs={"device_ids": ["lamp_br_night"]}
            ),
        ],
        outputs=[]
    ),

    # Task 6 – Install new washing machine, create a one-off laundry reminder, and prepare supplies
    Task(
        annotator="0",
        user_id="res_06",
        instruction="""
        You need to install a new LG TurboWash 360 washing machine in your basement. Register it with ID "washer_bs" as a device of type "washing_machine". Name it "Basement Washing Machine" and set its location to Basement. It's an LG TurboWash 360 model running firmware version 1.0.0. The device supports these state parameters: power, cycle, time_remaining_min, and door.

        For the initial setup, configure it as powered off, in idle cycle mode, with 0 minutes remaining and the door closed. Set the last update timestamp to "2025-07-28T16:30:00".

        Next, set up a reminder to help you remember to move your laundry to the dryer. Create a new reminder with these specific details: Set the reminder_id to "rem_laundry" and name it "Laundry Time". The target should be a note type with the text "Move laundry to dryer". Schedule it to trigger at "2025-07-28T17:00:00". Configure it to send a mobile push notification when triggered. Set the priority to "normal" in the meta field and keep the status as "scheduled". The reminder should be marked as created at "2025-07-28T16:30:00Z".

        To prepare for laundry, create a custom list named "Laundry Supplies" (list_id: list_laundry_supplies) and add one pack of detergent and one box of dryer sheets.

        Also, make sure the new washing machine (device_id: washer_bs) is powered off before starting the dryer for safety. After creating the reminder, display it, the supplies list, and the washing machine state to verify all settings are correct.
        """,
        actions=[
            Action(
                name="add_device",
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
                name="add_reminder",
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
                name="create_custom_list",
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
                name="set_device_state",
                kwargs={
                    "device_id": "washer_bs",
                    "state_update": {"power": "off", "cycle": "idle", "time_remaining_min": 0, "door": "closed"}
                }
            ),
            Action(
                name="get_reminders",
                kwargs={"reminder_id": "rem_laundry"}
            ),
            Action(
                name="get_custom_list",
                kwargs={"list_id": "list_laundry_supplies"}
            ),
            Action(
                name="get_device_info",
                kwargs={"device_ids": ["washer_bs"]}
            ),
        ],
        outputs=[]
    ),

    # Task 7 – Remove bedside lamp from East Bedroom entirely
    Task(
        annotator="0",
        user_id="res_07",
        instruction="""
        You've unplugged the East Bedroom Bedside Lamp (device_id: lamp_be_bedside) and now need to remove it from your smart home system. First, remove it from the East Bedroom (room_id: "bedroom_east"), then completely delete the device from the system.

        Before removal, make sure the lamp is powered off for safety. After removing the lamp, create a custom shopping list named "Bedroom Lamp Replacement" (list_id: list_lamp_replacement) and add one bedside lamp to it in case you need a replacement.

        After completing all steps, display the East Bedroom room information and the shopping list to confirm that the lamp has been successfully removed and the replacement is noted.
        """,
        actions=[
            Action(
                name="get_room_info",
                kwargs={"room_ids": ["bedroom_east"]}
            ),
            Action(
                name="set_device_state",
                kwargs={
                    "device_id": "lamp_be_bedside",
                    "state_update": {"power": "off"}
                }
            ),
            Action(
                name="manage_room_devices",
                kwargs={
                    "room_id": "bedroom_east",
                    "device_id": "lamp_be_bedside",
                    "action": "remove"
                }
            ),
            Action(
                name="remove_device",
                kwargs={"device_id": "lamp_be_bedside"}
            ),
            Action(
                name="create_custom_list",
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
                name="get_room_info",
                kwargs={"room_ids": ["bedroom_east"]}
            ),
            Action(
                name="get_custom_list",
                kwargs={"list_id": "list_lamp_replacement"}
            ),
        ],
        outputs=[]
    ),

    # Task 8 – Start movie time scene right away and prepare supplies
    Task(
        annotator="0",
        user_id="res_08",
        instruction="""
        It's time to watch a movie! You need to immediately activate the existing scene with id "scene_movie_time".

        After activating the scene, check and display the updated states of these devices: the living room curtain (curtain_lr), floor light (light_lr_floor), ceiling light (light_lr_ceiling), and the AC unit (ac_home).

        To make the movie experience even better, create a custom shopping list named "Movie Night Essentials" (list_id: list_movie_essentials) and add the following items: one pack of popcorn and two bottles of soda.

        Also, make sure the kitchen dishwasher (dishwasher_kt) is powered off to avoid noise during the movie. Then, display the shopping list and the dishwasher state to verify everything is set for a perfect movie night.
        """,
        actions=[
            Action(name="list_all_scenes", kwargs={}),
            Action(name="activate_scene", kwargs={"scene_id": "scene_movie_time"}),
            Action(
                name="get_device_info",
                kwargs={"device_ids": ["curtain_lr", "light_lr_floor", "light_lr_ceiling", "ac_home"]}
            ),
            Action(
                name="create_custom_list",
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
                name="set_device_state",
                kwargs={
                    "device_id": "dishwasher_kt",
                    "state_update": {"power": "off"}
                }
            ),
            Action(
                name="get_custom_list",
                kwargs={"list_id": "list_movie_essentials"}
            ),
            Action(
                name="get_device_info",
                kwargs={"device_ids": ["dishwasher_kt"]}
            ),
        ],
        outputs=[]
    ),

    # Task 9 – Use sensor readings to pre-cool the living room and prepare supplies
    Task(
        annotator="0",
        user_id="res_09",
        instruction="""
        You need to prepare the living room's climate. Start by checking the readings from both the Living Room Thermometer (sensor_lr_thermometer) and the Air-Quality Sensor (sensor_lr_air_quality).

        After checking the readings, regardless of what they show, make the following adjustments: First, configure the AC unit (ac_home) by turning it on, setting it to cool mode with a temperature of 20°C, and setting the fan speed to "high". Then, fully open the Living-Room curtain (curtain_lr) by setting its position to 100 while keeping it powered on.

        Next, make sure the Living-Room floor lamp (light_lr_floor) is powered off for energy efficiency. Also, create a custom shopping list named "Living Room Climate Supplies" (list_id: list_lr_climate_supplies) and add the following items: one pack of air filters and one bottle of air freshener.

        Finally, display the new states of both the AC unit, the curtain, and the floor lamp, and show the shopping list to confirm your changes.
        """,
        actions=[
            Action(
                name="get_sensor_data",
                kwargs={"sensor_ids": ["sensor_lr_thermometer", "sensor_lr_air_quality"]}
            ),
            Action(
                name="set_device_state",
                kwargs={
                    "device_id": "ac_home",
                    "state_update": {"power": "on", "mode": "cool", "setpoint_c": 20, "fan_speed": "high"}
                }
            ),
            Action(
                name="set_device_state",
                kwargs={
                    "device_id": "curtain_lr",
                    "state_update": {"power": "on", "position": 100}
                }
            ),
            Action(
                name="set_device_state",
                kwargs={
                    "device_id": "light_lr_floor",
                    "state_update": {"power": "off"}
                }
            ),
            Action(
                name="create_custom_list",
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
                name="get_device_info",
                kwargs={"device_ids": ["ac_home", "curtain_lr", "light_lr_floor"]}
            ),
            Action(
                name="get_custom_list",
                kwargs={"list_id": "list_lr_climate_supplies"}
            ),
        ],
        outputs=[]
    ),

    # Task 10 – Create and immediately run a party mode scene
    Task(
        annotator="0",
        user_id="res_10",
        instruction="""
        You need to create a high-energy scene for parties. Start by checking the current reading from the Living Room Air-Quality Sensor (sensor_lr_air_quality) to ensure the environment is safe for guests.

        Create a new scene named "Party Mode" with id "scene_party_mode" that configures your devices in the following way:

        For the living room, turn off the ceiling light (light_lr_ceiling), set the floor light (light_lr_floor) to 15% brightness and turn it on, and close the curtain (curtain_lr) completely by setting its position to 0 while keeping it powered on. For climate control, set the AC (ac_home) to cool mode at 19°C with the fan speed on "high". In the bedroom, configure the ceiling light (light_br_ceiling) to be on at full brightness with a purple tint (color settings: hue=300, saturation=80).

        To prepare for the party, create a custom shopping list named "Party Essentials" (list_id: list_party_essentials) and add the following items: one pack of snacks and two bottles of soda.

        Also, make sure the dishwasher in the kitchen (dishwasher_kt) is powered off to avoid noise during the party.

        After creating the scene, activate it immediately. Then display the current states of all five devices, the shopping list, and the dishwasher state to see how the party atmosphere looks.
        """,
        actions=[
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(name="list_all_scenes", kwargs={}),
            Action(
                name="create_scene",
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
                name="create_custom_list",
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
                name="set_device_state",
                kwargs={
                    "device_id": "dishwasher_kt",
                    "state_update": {"power": "off"}
                }
            ),
            Action(name="activate_scene", kwargs={"scene_id": "scene_party_mode"}),
            Action(
                name="get_device_info",
                kwargs={"device_ids": ["light_lr_ceiling", "light_lr_floor", "ac_home", "curtain_lr", "light_br_ceiling", "dishwasher_kt"]}
            ),
            Action(
                name="get_custom_list",
                kwargs={"list_id": "list_party_essentials"}
            ),
        ],
        outputs=[]
    ),

    # Task 11 – Modify weekend grocery list and check kitchen safety
    Task(
        annotator="0",
        user_id="res_11",
        instruction="""
        You need to make some changes to your weekend grocery list (list_id: list_groceries_weekend). First, check the current reading from your Kitchen Sink Leak Sensor (sensor_id: sensor_sink_leak) to ensure there are no water issues before proceeding.

        Next, add six Bananas to the list. Then, remove one entry of Olive Oil from it. Also, add two cartons of Milk and one pack of Eggs to the grocery list to ensure you have enough for the weekend.

        For safety, make sure the kitchen dishwasher (device_id: dishwasher_kt) is powered off before you leave for shopping.

        After making these changes, display the complete updated list and the dishwasher state so you can verify that all modifications and safety checks were applied correctly.
        """,
        actions=[
            Action(
                name="get_sensor_data",
                kwargs={"sensor_ids": ["sensor_sink_leak"]}
            ),
            Action(
                name="manage_custom_list_items",
                kwargs={
                    "list_id": "list_groceries_weekend",
                    "item": {"item": "Bananas", "quantity": 6},
                    "action": "add"
                }
            ),
            Action(
                name="manage_custom_list_items",
                kwargs={
                    "list_id": "list_groceries_weekend",
                    "item": {"item": "Olive Oil"},
                    "action": "remove"
                }
            ),
            Action(
                name="manage_custom_list_items",
                kwargs={
                    "list_id": "list_groceries_weekend",
                    "item": {"item": "Milk", "quantity": 2},
                    "action": "add"
                }
            ),
            Action(
                name="manage_custom_list_items",
                kwargs={
                    "list_id": "list_groceries_weekend",
                    "item": {"item": "Eggs", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="set_device_state",
                kwargs={
                    "device_id": "dishwasher_kt",
                    "state_update": {"power": "off"}
                }
            ),
            Action(name="get_custom_list", kwargs={"list_id": "list_groceries_weekend"}),
            Action(name="get_device_info", kwargs={"device_ids": ["dishwasher_kt"]}),
        ],
        outputs=[]
    ),

    # Task 12 – Add a smart coffee maker in the kitchen, start brewing, and prepare supplies
    Task(
        annotator="0",
        user_id="res_12",
        instruction="""
        You need to set up a new Nespresso Vertuo Next coffee maker in your kitchen. Here are the device specifications:

        Register it with the ID "coffee_maker_kt" as a device of type "coffee_maker". Name it "Kitchen Coffee Maker". It's manufactured by Nespresso, model Vertuo Next, running firmware version 1.2.3. The device supports these state parameters: power, mode, and cups_remaining.

        For the initial setup, configure it as powered off, in idle mode, with 0 cups remaining. Set the last update timestamp to "2025-07-28T18:20:00".

        Before making any changes, check the current reading from the Kitchen Sink Leak Sensor (sensor_id: sensor_sink_leak) to ensure there are no water issues.

        After adding the device, register it to the kitchen (room_id: "kitchen"). Then start brewing by turning the power on, setting the mode to "brew", and setting cups_remaining to 1.

        To prepare for future coffee sessions, create a custom shopping list named "Coffee Supplies" (list_id: list_coffee_supplies) and add the following items: one box of coffee capsules and one bottle of descaler.

        Also, make sure the kitchen dishwasher (device_id: dishwasher_kt) is powered off for safety before starting the coffee maker.

        Finally, display the kitchen information and the coffee supplies list to confirm everything is set up correctly.
        """,
        actions=[
            Action(
                name="get_sensor_data",
                kwargs={"sensor_ids": ["sensor_sink_leak"]}
            ),
            Action(
                name="add_device",
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
                name="manage_room_devices",
                kwargs={
                    "room_id": "kitchen",
                    "device_id": "coffee_maker_kt",
                    "action": "add"
                }
            ),
            Action(
                name="set_device_state",
                kwargs={
                    "device_id": "coffee_maker_kt",
                    "state_update": {"power": "on", "mode": "brew", "cups_remaining": 1}
                }
            ),
            Action(
                name="create_custom_list",
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
                name="set_device_state",
                kwargs={
                    "device_id": "dishwasher_kt",
                    "state_update": {"power": "off"}
                }
            ),
            Action(name="get_room_info", kwargs={"room_ids": ["kitchen"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_coffee_supplies"}),
        ],
        outputs=[]
    ),

    # Task 13 – Create and schedule an accessible scene for grandmother's visit
    Task(
        annotator="0",
        user_id="res_13",
        instruction="""
        Your grandmother, Linda Johnson, is visiting next Friday at 14:00, and you need to prepare the house for her wheelchair accessibility needs. First, check the current reading from your Living Room Air-Quality Sensor (sensor_lr_air_quality) to ensure the environment is comfortable for her.

        Create a new scene named "Grandma's Welcome" with id "scene_grandma_welcome" that will configure your home as follows:

        In the living room, set the ceiling light (light_lr_ceiling) to 85% brightness and turn it on for better visibility. Open the curtain (curtain_lr) completely by setting its position to 100. For her comfort, set the AC (ac_home) to cool mode at 24°C with the fan speed on "low" to keep things quiet. Since she won't be using the East Bedroom, turn off both the ceiling light (light_be_ceiling) and bedside lamp (lamp_be_bedside). Also, make sure the East Bedroom curtain (curtain_be) is closed for privacy by setting its position to 0 while keeping it powered on.

        Create a high priority reminder (reminder_id: rem_grandma_july) that will notify you on your mobile 30 minutes before her arrival with the message "Prepare guest room for Grandma Linda - wheelchair access needed".

        To ensure you have everything needed for her visit, create a custom shopping list named "Grandma Visit Essentials" (list_id: list_grandma_essentials) and add the following items: one wheelchair ramp and one bottle of water.

        Finally, display both the scene details, the reminder, and the shopping list to verify everything is set up correctly.
        """,
        actions=[
            Action(
                name="get_sensor_data",
                kwargs={"sensor_ids": ["sensor_lr_air_quality"]}
            ),
            Action(
                name="create_scene",
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
                name="add_reminder",
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
                name="create_custom_list",
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
                name="list_all_scenes",
                kwargs={}
            ),
            Action(
                name="get_reminders",
                kwargs={"reminder_id": "rem_grandma_july"}
            ),
            Action(
                name="get_custom_list",
                kwargs={"list_id": "list_grandma_essentials"}
            )
        ],
        outputs=[]
    ),

    # Task 14 – Focused study scene for West Bedroom
    Task(
        annotator="0",
        user_id="res_14",
        instruction="""
        The time is 2025-07-29 09:00, and you need to create a scene that will help with intensive studying in the West Bedroom. Name this new scene "Focused Study" with id "scene_focused_study_west". When activated, the scene should configure your devices as follows:

        First, check the current air quality data from your sensors to ensure a healthy study space.

        For optimal lighting, turn on the West Bedroom Desk Lamp (device_id: lamp_bw_desk) at full brightness and set its color temperature to 5000K. Set the West Bedroom Ceiling Light (device_id: light_bw_ceiling) to a dimmer 40% brightness and turn it on. For natural light, fully open the West Bedroom Curtain (device_id: curtain_bw) by setting its position to 100 while keeping it powered on. Finally, create a comfortable temperature by turning on the Central AC (device_id: ac_home), setting it to cool mode at 21°C with the fan speed on "low".

        To ensure you have everything needed for focused study, create a custom shopping list named "Study Essentials" (list_id: list_study_essentials) and add the following items: one Desk Organizer and one pack of Highlighters.

        Also, make sure the Living Room Floor Lamp (device_id: light_lr_floor) is powered off to avoid distractions.

        After creating the scene, activate it immediately and display the new states of all four devices mentioned above, the shopping list, and the state of the Living Room Floor Lamp.
        """,
        actions=[
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(name="list_all_scenes", kwargs={}),
            Action(name="get_room_info", kwargs={"room_ids": ["bedroom_west"]}),
            Action(
                name="create_scene",
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
                name="create_custom_list",
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
                name="set_device_state",
                kwargs={
                    "device_id": "light_lr_floor",
                    "state_update": {"power": "off"}
                }
            ),
            Action(name="activate_scene", kwargs={"scene_id": "scene_focused_study_west"}),
            Action(name="get_device_info", kwargs={"device_ids": ["lamp_bw_desk", "light_bw_ceiling", "curtain_bw", "ac_home", "light_lr_floor"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_study_essentials"}),
        ],
        outputs=[]
    ),

    # Task 15 – Replace the existing dishwasher with a new model and start a quick cycle
    Task(
        annotator="0",
        user_id="res_15",
        instruction="""
        It's 2025-07-29 10:15, and you need to upgrade your kitchen's dishwasher to a new Bosch Series 9 unit. Here's what you need to do:

        First, check your current Kitchen room information and the state of the existing dishwasher (device_id: dishwasher_kt) to ensure it's powered off for safety. Also, check the Kitchen Sink Leak Sensor (sensor_id: sensor_sink_leak) to make sure there are no water issues before proceeding.

        Then, remove the existing dishwasher (device_id: dishwasher_kt) from the Kitchen (room_id: "kitchen") and delete it from your system entirely.

        Now, set up the new dishwasher with these specifications: Register it with ID "dishwasher_kt2" as a device of type "dishwasher". Name it "Kitchen Dishwasher (Series 9)" and set its location to Kitchen. It's a Bosch Series 9 model running firmware version 6.0.0. The device supports these state parameters: power, cycle, time_remaining_min, and door.

        For the initial setup, configure it as powered off, in auto cycle mode, with 0 minutes remaining and the door closed. Set the last update timestamp to "2025-07-29T10:15:00".

        After adding the new dishwasher to the Kitchen, start a quick wash by turning it on, setting the cycle to "quick", setting time_remaining_min to 30, and keeping the door closed.

        To prepare for future maintenance, create a custom shopping list named "Dishwasher Supplies" (list_id: list_dishwasher_supplies) and add one pack of dishwasher detergent and one bottle of rinse aid.

        Finally, display the updated Kitchen information and the supplies list to verify the installation and preparation.
        """,
        actions=[
            Action(name="get_room_info", kwargs={"room_ids": ["kitchen"]}),
            Action(name="get_device_info", kwargs={"device_ids": ["dishwasher_kt"]}),
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_sink_leak"]}),
            Action(name="set_device_state", kwargs={"device_id": "dishwasher_kt", "state_update": {"power": "off"}}),
            Action(name="manage_room_devices", kwargs={"room_id": "kitchen", "device_id": "dishwasher_kt", "action": "remove"}),
            Action(name="remove_device", kwargs={"device_id": "dishwasher_kt"}),
            Action(
                name="add_device",
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
            Action(name="manage_room_devices", kwargs={"room_id": "kitchen", "device_id": "dishwasher_kt2", "action": "add"}),
            Action(name="set_device_state", kwargs={"device_id": "dishwasher_kt2", "state_update": {"power": "on", "cycle": "quick", "time_remaining_min": 30, "door": "closed"}}),
            Action(
                name="create_custom_list",
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
            Action(name="get_room_info", kwargs={"room_ids": ["kitchen"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_dishwasher_supplies"}),
        ],
        outputs=[]
    ),
    # Task 16 – Bedroom fire-drill safety check with lighting alert, supplies list, and follow-up reminder
    Task(
        annotator="0",
        user_id="res_16",
        instruction="""
        At 2025-07-29 11:00, you need to run a fire-drill in the Master Bedroom. Here's what you need to do in sequence:

        First, check the current reading from the Bedroom Smoke Detector (sensor_id: sensor_bed_smoke) to ensure there are no fire or smoke issues before proceeding.

        Next, install a new Dyson Pure Cool TP07 air-purifier in the Master Bedroom using the add_device tool. Register it with ID "air_purifier_mb" as a device of type "air_purifier". Name it "Master Bedroom Air-Purifier", set its location to Master Bedroom, vendor to Dyson, model to Pure Cool TP07, and firmware version to 1.0.1. The device supports these state parameters: power, mode, fan_speed, and filter_life_pct. For the initial setup, configure it as powered off, in auto mode, with low fan speed, and 100% filter life. Set the last update timestamp to "2025-07-29T11:00:00".

        Then, create a custom shopping list named "Fire Drill Supplies" (list_id: list_fire_drill_supplies) and add the following items: one fire blanket and one emergency flashlight.

        Next, set up the bedroom lights for the drill: Turn on the Master Bedroom Ceiling Light (light_br_ceiling) at full brightness with neutral white light (color settings: hue=0, saturation=0). Do the same for the Master Bedroom Night Lamp (lamp_br_night).

        For safety, make sure the master bedroom air-purifier (air_purifier_mb) is powered off during the drill.

        To ensure proper follow-up, create a one-time reminder with these specifications: Set the reminder_id to "rem_fire_drill_05min" and name it "Fire-Drill Follow-up". The reminder should display the message "Confirm fire-drill completion log" and be scheduled for 2025-07-29T11:05:00. Configure it with high priority and set it to send a mobile push notification.

        Finally, display both the updated light states, the air-purifier state, the supplies list, and the new reminder to verify everything is set correctly.
        """,
        actions=[
            Action(
                name="add_device",
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
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_bed_smoke"]}),
            Action(
                name="create_custom_list",
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
            Action(name="set_device_state", kwargs={"device_id": "light_br_ceiling", "state_update": {"power": "on", "brightness": 100, "color": {"hue": 0, "saturation": 0}}}),
            Action(name="set_device_state", kwargs={"device_id": "lamp_br_night", "state_update": {"power": "on", "brightness": 100, "color": {"hue": 0, "saturation": 0}}}),
            Action(name="set_device_state", kwargs={"device_id": "air_purifier_mb", "state_update": {"power": "off"}}),
            Action(
                name="add_reminder",
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
            Action(name="get_device_info", kwargs={"device_ids": ["light_br_ceiling", "lamp_br_night", "air_purifier_mb"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_fire_drill_supplies"}),
            Action(name="get_reminders", kwargs={"reminder_id": "rem_fire_drill_05min"}),
        ],
        outputs=[]
    ),
    # Task 17 – Expand reading list, check lamp state, and set daily reading reminder
    Task(
        annotator="0",
        user_id="res_17",
        instruction="""
        You want to improve your reading routine and ensure a comfortable environment. Here's what you need to do:

        First, check the current state of your Bedroom Night Lamp (device_id: lamp_br_night) to make sure it's off before starting your reading session. Then, display your current reading list (list_id: list_reading) to see what's on it.

        Next, add "The Pragmatic Programmer" (quantity: 1) to the list, and remove the existing entry for "Clean Code". Also, add a new item "Reading Glasses" (quantity: 1) to the list in case you need them. After making these changes, display the updated reading list to verify the modifications.

        To help maintain your reading habit, create a daily evening reminder with these specifications: Set the reminder_id to "rem_reading_daily" and name it "Evening Reading Time". Link it to your reading list by setting the target type to "entity", entity_type to "list", and entity_id to "list_reading". Schedule it to repeat daily at 20:00 using the rrule "FREQ=DAILY;BYHOUR=20;BYMINUTE=0". Configure it with normal priority and set it to send mobile push notifications. Mark it with an "active" status.

        Finally, display the reminder to confirm it's set up correctly.
        """,
        actions=[
            Action(name="get_device_info", kwargs={"device_ids": ["lamp_br_night"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_reading"}),
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_reading", "item": {"item": "The Pragmatic Programmer", "quantity": 1}, "action": "add"}),
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_reading", "item": {"item": "Clean Code"}, "action": "remove"}),
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_reading", "item": {"item": "Reading Glasses", "quantity": 1}, "action": "add"}),
            Action(name="get_custom_list", kwargs={"list_id": "list_reading"}),
            Action(
                name="add_reminder",
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
            Action(name="get_reminders", kwargs={"reminder_id": "rem_reading_daily"}),
        ],
        outputs=[]
    ),

    # Task 18 – Activate enhanced night-time security mode
    Task(
        annotator="0",
        user_id="res_18",
        instruction="""
        At 23:00 tonight, you want to enable enhanced security features in your home. Create a new scene named "Enhanced Security" with id "scene_security_night" that will configure your devices as follows:

        First, check and log the current state of the Hallway Motion Sensor (sensor_hall_motion) and both door cameras (camera_front_door, camera_back_door) before making any changes. For surveillance, activate both your Front Door Camera and Back Door Camera by setting their stream_online and recording parameters to True. For safety, turn off both the Living-Room Ceiling Light (light_lr_ceiling) and the Master Bedroom Ceiling Light (light_br_ceiling). Also, make sure the Living-Room Floor Lamp (light_lr_floor) is powered off for energy efficiency.

        To ensure you have everything needed for night-time security, create a custom shopping list named "Night Security Essentials" (list_id: list_security_essentials) and add the following items: one pack of batteries for cameras and one flashlight.

        After creating the scene, activate it immediately and display the updated states of both cameras, both ceiling lights, the floor lamp, and the shopping list to verify the security setup.
        """,
        actions=[
            Action(name="list_all_scenes", kwargs={}),
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_hall_motion", "camera_front_door", "camera_back_door"]}),
            Action(
                name="create_scene",
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
                name="create_custom_list",
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
            Action(name="activate_scene", kwargs={"scene_id": "scene_security_night"}),
            Action(name="get_device_info", kwargs={"device_ids": ["light_lr_ceiling", "light_br_ceiling", "light_lr_floor", "camera_front_door", "camera_back_door"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_security_essentials"}),
        ],
        outputs=[]
    ),

    # Task 19 – Prepare the house for a two-week vacation
    Task(
        annotator="0",
        user_id="res_19",
        instruction="""
        You're leaving for vacation on 2025-07-05 and need to prepare your house for your absence. Create a new scene named "Vacation Away" with id "scene_vacation_away" that will put your home in an energy-efficient and secure state.

        Before making any changes, check the current reading from your Kitchen Sink Leak Sensor (sensor_id: sensor_sink_leak) to ensure there are no water issues before leaving.

        The scene should manage your devices as follows: First, turn off all the main lights in the house: the living room ceiling and floor lights (light_lr_ceiling, light_lr_floor), all bedroom ceiling lights (light_br_ceiling, light_bw_ceiling, light_be_ceiling), and both the master bedroom night lamp (lamp_br_night) and west bedroom desk lamp (lamp_bw_desk). Next, close all curtains in the bedrooms and living room (curtain_lr, curtain_br, curtain_bw, curtain_be) by setting their positions to 0 while keeping them powered on. Finally, shut down the climate control by turning off both the AC (ac_home) and heater (heater_home).

        After creating the scene, activate it immediately. Then, create a custom shopping list named "Vacation Essentials" (list_id: list_vacation_essentials) and add the following items: one pack of batteries for sensors and one bottle of plant fertilizer.

        Also, make sure the dishwasher (dishwasher_kt) is powered off for safety before leaving.

        Finally, create a reminder (rem_vacation_plants) to water the houseplants every Saturday at 09:00 while you're away, using the rrule "FREQ=WEEKLY;BYDAY=SA;BYHOUR=9;BYMINUTE=0". Display the states of the AC, heater, living room curtain, living room ceiling light, the dishwasher, the shopping list, and the reminder details to verify everything is set correctly.
        """,
        actions=[
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_sink_leak"]}),
            Action(name="list_all_scenes", kwargs={}),
            Action(
                name="create_scene",
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
            Action(name="activate_scene", kwargs={"scene_id": "scene_vacation_away"}),
            Action(
                name="create_custom_list",
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
                name="set_device_state",
                kwargs={
                    "device_id": "dishwasher_kt",
                    "state_update": {"power": "off"}
                }
            ),
            Action(
                name="add_reminder",
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
            Action(name="get_device_info", kwargs={"device_ids": ["ac_home", "heater_home", "curtain_lr", "light_lr_ceiling", "dishwasher_kt"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_vacation_essentials"}),
            Action(name="get_reminders", kwargs={"reminder_id": "rem_vacation_plants"}),
        ],
        outputs=[]
    ),
    # Task 20 – Create a garden-maintenance list and weekly reminder, after inspecting leak sensor and checking outdoor faucet
    Task(
        annotator="0",
        user_id="res_20",
        instruction="""
        You're planning to maintain your outdoor space regularly.

        Create a new custom list with these specifications: Set the list_id to "list_garden_maintenance" and name it "Garden Maintenance". Tag it with "garden". Initially, add these items to your list: one Fertilizer, one Hose Nozzle, and two pairs of Gloves.

        After creating the list, add two more items: Weed Killer (quantity: 1) and one pack of Plant Stakes (quantity: 1). Display the complete list to verify all items are included correctly.

        Finally, set up a weekly reminder (reminder_id: rem_garden_weekly) that will notify you every Sunday at 08:00 to check your garden maintenance list. Use the rrule "FREQ=WEEKLY;BYDAY=SU;BYHOUR=08;BYMINUTE=0", configure it to send mobile push notifications, and display the reminder to confirm it's properly scheduled.
        """,
        actions=[
            Action(
                name="create_custom_list",
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
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_garden_maintenance", "item": {"item": "Weed Killer", "quantity": 1}, "action": "add"}),
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_garden_maintenance", "item": {"item": "Plant Stakes", "quantity": 1}, "action": "add"}),
            Action(name="get_custom_list", kwargs={"list_id": "list_garden_maintenance"}),
            Action(
                name="add_reminder",
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
            Action(name="get_reminders", kwargs={"reminder_id": "rem_garden_weekly"}),
        ],
        outputs=[]
    ),

    # Task 21 – Bedtime scene for children's bedrooms
    Task(
        annotator="0",
        user_id="res_21",
        instruction="""
        You need to create a calming environment for the children's bedtime tonight at 20:30. Before making any changes, check the current readings from the West Bedroom Temperature Sensor (sensor_bw_temp) and East Bedroom Temperature Sensor (sensor_be_temp) to ensure the rooms are comfortable.

        Create a new scene named "Kids Bedtime" with id "scene_kids_bedtime" that will prepare both bedrooms for sleep.

        In the West Bedroom, turn off both lights: the ceiling light (light_bw_ceiling) and the desk lamp (lamp_bw_desk). Then close the curtain (curtain_bw) by setting its position to 0 while keeping it powered on. Similarly in the East Bedroom, turn off the ceiling light (light_be_ceiling) and close its curtain (curtain_be) with the same settings. To create a quiet environment, adjust the AC unit (ac_home) by setting its fan speed to "low" while maintaining its current power state.

        To ensure energy efficiency, make sure the West Bedroom Desk Lamp (lamp_bw_desk) is powered off after the scene is activated.

        Also, create a custom shopping list named "Kids Bedtime Essentials" (list_id: list_kids_bedtime_essentials) and add the following items: one pack of night lights and one bottle of water.

        After creating the scene, activate it immediately and display the current states of these devices: the West Bedroom ceiling light and curtain, the East Bedroom ceiling light and curtain, the AC unit, and the desk lamp. Also, display the shopping list to verify all items are included.
        """,
        actions=[
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_bw_temp", "sensor_be_temp"]}),
            Action(name="list_all_scenes", kwargs={}),
            Action(name="get_room_info", kwargs={"room_ids": ["bedroom_west", "bedroom_east"]}),
            Action(
                name="create_scene",
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
            Action(name="activate_scene", kwargs={"scene_id": "scene_kids_bedtime"}),
            Action(name="set_device_state", kwargs={"device_id": "lamp_bw_desk", "state_update": {"power": "off"}}),
            Action(
                name="create_custom_list",
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
            Action(name="get_device_info", kwargs={"device_ids": ["light_bw_ceiling", "curtain_bw", "light_be_ceiling", "curtain_be", "ac_home", "lamp_bw_desk"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_kids_bedtime_essentials"}),
        ],
        outputs=[]
    ),

    # Task 22 – Install master bedroom air-purifier, check air quality, start it, and prepare supplies
    Task(
        annotator="0",
        user_id="res_22",
        instruction="""
        You want to add an air-purifier to your Master Bedroom and ensure the environment is healthy. First, check the current air quality using your Bedroom Air-Quality Sensor (sensor_id: sensor_mb_air_quality). If this sensor does not exist, create it with these parameters: id "sensor_mb_air_quality", type "air_quality_sensor", location "Master Bedroom", vendor "Dyson", model "AQ-100", firmware_version "1.0.0", and state_params ["co2", "voc", "pm2_5"].

        Next, install a new Dyson Pure Cool TP07 air-purifier in your Master Bedroom. Register it with the ID "air_purifier_mb" as a device of type "air_purifier". Name it "Master Bedroom Air-Purifier", set its location to Master Bedroom, vendor to Dyson, model to Pure Cool TP07, and firmware version to 1.0.1. The device supports these state parameters: power, mode, fan_speed, and filter_life_pct. For the initial setup, configure it as powered off, in auto mode, with low fan speed, and 100% filter life.

        After adding the device, register it to your Master Bedroom (room_id: "bedroom_master"). Then turn it on, keep it in auto mode, but increase the fan speed to "medium".

        To prepare for future maintenance, create a custom shopping list named "Air-Purifier Supplies" (list_id: list_air_purifier_supplies) and add one replacement filter and one cleaning cloth.

        For safety, make sure the Master Bedroom Night Lamp (device_id: lamp_br_night) is powered off.

        Finally, display the Master Bedroom information and the supplies list to verify the installation and preparation.
        """,
        actions=[
            Action(
                name="get_sensor_data",
                kwargs={"sensor_ids": ["sensor_mb_air_quality"]}
            ),
            Action(
                name="add_device",
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
            Action(name="get_room_info", kwargs={"room_ids": ["bedroom_master"]}),
            Action(
                name="add_device",
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
            Action(name="manage_room_devices", kwargs={"room_id": "bedroom_master", "device_id": "air_purifier_mb", "action": "add"}),
            Action(name="set_device_state", kwargs={"device_id": "air_purifier_mb", "state_update": {"power": "on", "mode": "auto", "fan_speed": "medium"}}),
            Action(
                name="create_custom_list",
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
            Action(name="set_device_state", kwargs={"device_id": "lamp_br_night", "state_update": {"power": "off"}}),
            Action(name="get_room_info", kwargs={"room_ids": ["bedroom_master"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_air_purifier_supplies"}),
        ],
        outputs=[]
    ),
    # Task 23 – Balance climate after reading thermometer, adjust heater and curtains, and prepare supplies
    Task(
        annotator="0",
        user_id="res_23",
        instruction="""
        You notice it's getting warm inside your home. First, check the current temperature reading from your Living Room Thermometer (sensor_id: sensor_lr_thermometer).

        Regardless of what the reading shows, make the following adjustments to balance the climate: Start by configuring the AC unit (device_id: ac_home) - turn it on, set it to cool mode with a temperature of 23°C, and set the fan speed to "medium". Then, make sure the heater (device_id: heater_home) is turned off. Adjust the Living Room curtain (device_id: curtain_lr) by setting its position to 75% open while keeping it powered on.

        To ensure energy efficiency, make sure the Living Room Floor Lamp (device_id: light_lr_floor) is powered off. Also, create a custom shopping list named "Climate Balance Supplies" (list_id: list_climate_balance_supplies) and add the following items: one pack of air filters and one bottle of water.

        After making all these changes, display the updated states of the AC unit, heater, curtain, and floor lamp, and show the shopping list to verify your adjustments.
        """,
        actions=[
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_lr_thermometer"]}),
            Action(name="set_device_state", kwargs={"device_id": "ac_home", "state_update": {"power": "on", "mode": "cool", "setpoint_c": 23, "fan_speed": "medium"}}),
            Action(name="set_device_state", kwargs={"device_id": "heater_home", "state_update": {"power": "off"}}),
            Action(name="set_device_state", kwargs={"device_id": "curtain_lr", "state_update": {"power": "on", "position": 75}}),
            Action(name="set_device_state", kwargs={"device_id": "light_lr_floor", "state_update": {"power": "off"}}),
            Action(
                name="create_custom_list",
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
            Action(name="get_device_info", kwargs={"device_ids": ["ac_home", "heater_home", "curtain_lr", "light_lr_floor"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_climate_balance_supplies"}),
        ],
        outputs=[]
    ),
    # Task 24 – Create and run an eco-morning energy-savvy scene
    Task(
        annotator="0",
        user_id="res_24",
        instruction="""
        You want to start your day in an energy-efficient way. First, check the current readings from your Living Room Air-Quality Sensor (sensor_lr_air_quality) and Master Bedroom Temperature Sensor (sensor_br_temp) to ensure the environment is comfortable before making any changes. If the Master Bedroom Temperature Sensor does not exist, create it with these parameters: id "sensor_br_temp", type "temperature_sensor", location "Master Bedroom", vendor "Xiaomi", model "TempSense X1", firmware_version "1.0.0", and state_params ["temperature_c"].

        Next, create a new scene named "Eco Morning" with id "scene_eco_morning" that will prepare your home for a low-energy morning. Configure your devices as follows: In the living room, turn on the ceiling light (light_lr_ceiling) at 70% brightness and set its color temperature to 5000K. In the master bedroom, turn on the ceiling light (light_br_ceiling) at 60% brightness. For climate control, turn off the central heater (heater_home) completely, and set the AC (ac_home) to cool mode at 24°C with the fan speed on "auto".

        To ensure energy efficiency, make sure the Living Room Floor Lamp (light_lr_floor) is powered off. Also, create a custom shopping list named "Eco Morning Essentials" (list_id: list_eco_morning_essentials) and add the following items: 1 LED bulbs and 1 Eco-friendly cleaner.

        After creating the scene, activate it immediately. Then, add 1 Reusable kitchen towels and 1 Plant-based dish soap to the shopping list. Also, make sure the kitchen dishwasher (device_id: dishwasher_kt) is powered off for energy savings. Before making any device changes, check the current state of the Living Room Floor Lamp (light_lr_floor) and the kitchen dishwasher (dishwasher_kt).

        Finally, display the new states of both ceiling lights, the heater, the AC unit, the floor lamp, the dishwasher, and the shopping list to verify your energy-efficient setup.
        """,
        actions=[
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_lr_air_quality", "sensor_br_temp"]}),
            Action(
                name="add_device",
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
            Action(name="get_device_info", kwargs={"device_ids": ["light_lr_floor", "dishwasher_kt"]}),
            Action(name="list_all_scenes", kwargs={}),
            Action(
                name="create_scene",
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
            Action(name="activate_scene", kwargs={"scene_id": "scene_eco_morning"}),
            Action(name="set_device_state", kwargs={"device_id": "light_lr_floor", "state_update": {"power": "off"}}),
            Action(
                name="create_custom_list",
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
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_eco_morning_essentials", "item": {"item": "Reusable kitchen towels", "quantity": 1}, "action": "add"}),
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_eco_morning_essentials", "item": {"item": "Plant-based dish soap", "quantity": 1}, "action": "add"}),
            Action(name="set_device_state", kwargs={"device_id": "dishwasher_kt", "state_update": {"power": "off"}}),
            Action(name="get_device_info", kwargs={"device_ids": ["light_lr_ceiling", "light_br_ceiling", "heater_home", "ac_home", "light_lr_floor", "dishwasher_kt"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_eco_morning_essentials"}),
        ],
        outputs=[]
    ),
    # Task 25 – Leak check, safety shut-off, supplies list, and follow-up reminder
    Task(
        annotator="0",
        user_id="res_25",
        instruction="""
        You need to perform a kitchen safety check. First, check the current reading from your Kitchen Sink Leak Sensor (sensor_id: sensor_sink_leak) to ensure there are no water issues.

        Next, check the current state of your Kitchen Dishwasher (device_id: dishwasher_kt) to make sure it's powered off for safety. If it's not off, turn it off.

        To prepare for any potential leak repairs, create a new custom list named "Leak Repair Supplies" with id "list_leak_repair_supplies" and tag it with "maintenance". Add these items to the list: one roll of plumber's tape and one leak repair kit.

        To follow up on this safety check, create a reminder (rem_leak_followup) to inspect the sensor again in 30 minutes, scheduled at exactly 07:40. Configure the reminder with high priority and set it to send a mobile push notification.

        Finally, display the newly created reminder and the supplies list to verify everything is scheduled and prepared.
        """,
        actions=[
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_sink_leak"]}),
            Action(name="get_device_info", kwargs={"device_ids": ["dishwasher_kt"]}),
            Action(name="set_device_state", kwargs={"device_id": "dishwasher_kt", "state_update": {"power": "off"}}),
            Action(
                name="create_custom_list",
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
                name="add_reminder",
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
            Action(name="get_reminders", kwargs={"reminder_id": "rem_leak_followup"}),
            Action(name="get_custom_list", kwargs={"list_id": "list_leak_repair_supplies"}),
        ],
        outputs=[]
    ),

    # Task 26 – Replace outdated credit-card bill reminder with a new schedule, supplies list, and safety check
    Task(
        annotator="0",
        user_id="res_26",
        instruction="""
        You need to update your credit card bill reminder system and prepare for monthly payments. First, display your current reminder (rem_94f92a43) to review its settings, then delete it as it's outdated.

        Before making any changes, check the current state of your Kitchen Dishwasher (device_id: dishwasher_kt) to ensure it's powered off for safety. If it's not off, turn it off.

        Next, create a new reminder with id "rem_cc_bill_new" that will help you stay on top of your monthly payments. Schedule it to trigger on the 10th of every month at 09:00 using the rrule "FREQ=MONTHLY;BYMONTHDAY=10;BYHOUR=9;BYMINUTE=0". Configure it with high priority and set it to send mobile push notifications.

        To help you prepare for bill payments, create a new custom list named "Credit Card Payment Supplies" with id "list_cc_payment_supplies" and tag it with "finance". Add these items to the list: one envelope and one pen.

        After creating the new reminder and supplies list, display both to verify all settings are correct and everything is properly scheduled and prepared.
        """,
        actions=[
            Action(name="get_reminders", kwargs={"reminder_id": "rem_94f92a43"}),
            Action(name="get_device_info", kwargs={"device_ids": ["dishwasher_kt"]}),
            Action(name="set_device_state", kwargs={"device_id": "dishwasher_kt", "state_update": {"power": "off"}}),
            Action(name="delete_reminder", kwargs={"reminder_id": "rem_94f92a43"}),
            Action(
                name="add_reminder",
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
                name="create_custom_list",
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
            Action(name="get_reminders", kwargs={"reminder_id": "rem_cc_bill_new"}),
            Action(name="get_custom_list", kwargs={"list_id": "list_cc_payment_supplies"}),
        ],
        outputs=[]
    ),

    # Task 27 – Install a smart TV, expand movie scene, check sensor, and prepare supplies
    Task(
        annotator="0",
        user_id="res_27",
        instruction="""
        You want to enhance your movie-watching experience by adding a smart TV to your setup. Start by displaying your current Living Room information.

        Before making any changes, check the current reading from your Living Room Air-Quality Sensor (sensor_id: sensor_lr_air_quality) to ensure the environment is comfortable for watching a movie.

        Then, install a new Samsung QN90A TV with these specifications: Register it with ID "tv_lr" as a device of type "tv". Name it "Living Room TV" and set its location to Living Room. It's manufactured by Samsung, model QN90A, running firmware version 1.0.0. The device supports these state parameters: power, input_source, and volume.

        For the initial setup, configure it as powered off, with input source set to "HDMI1" and volume at 10. After adding the device, register it to your Living Room (room_id: "living_room").

        Next, create a new scene named "Movie Plus" with id "scene_movie_plus" that will configure your devices for optimal movie viewing: Turn on the TV and set its input to "HDMI1" with volume at 15, turn off the living room ceiling light (light_lr_ceiling), and close the curtain (curtain_lr) by setting its position to 0 while keeping it powered on.

        To avoid distractions, make sure the Living Room Floor Lamp (device_id: light_lr_floor) is powered off before activating the scene.

        Also, create a custom shopping list named "Movie Plus Essentials" (list_id: list_movie_plus_essentials) and add the following items: one pack of popcorn and one bottle of soda.

        Finally, activate the scene and display the current states of the TV, ceiling light, curtain, floor lamp, and the shopping list to verify your movie setup.
        """,
        actions=[
            Action(name="get_room_info", kwargs={"room_ids": ["living_room"]}),
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(
                name="add_device",
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
            Action(name="manage_room_devices", kwargs={"room_id": "living_room", "device_id": "tv_lr", "action": "add"}),
            Action(
                name="create_scene",
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
            Action(name="set_device_state", kwargs={"device_id": "light_lr_floor", "state_update": {"power": "off"}}),
            Action(
                name="create_custom_list",
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
            Action(name="activate_scene", kwargs={"scene_id": "scene_movie_plus"}),
            Action(name="get_device_info", kwargs={"device_ids": ["tv_lr", "light_lr_ceiling", "curtain_lr", "light_lr_floor"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_movie_plus_essentials"}),
        ],
        outputs=[]
    ),

    # Task 28 – Build a birthday-party supplies list and check kitchen safety
    Task(
        annotator="0",
        user_id="res_28",
        instruction="""
        Your son's birthday is coming up next month, and you need to prepare a list of party supplies and ensure your kitchen is safe before shopping. First, check the current state of your Kitchen Dishwasher (device_id: dishwasher_kt) to make sure it's powered off for safety before you leave for shopping. If it's not off, turn it off.

        Next, create a new custom list with these specifications: Set the list_id to "list_birthday_party" and name it "Birthday Party Supplies". Tag it with "party". Initially, add these items to your list: twenty Balloons, two Candles, and one Cake Mix.

        After creating the list, make three modifications: Add three packages of Confetti, add one pack of Paper Plates, and then remove the Candles entry. Finally, display the complete list to verify all changes were applied correctly.
        """,
        actions=[
            Action(name="get_device_info", kwargs={"device_ids": ["dishwasher_kt"]}),
            Action(name="set_device_state", kwargs={"device_id": "dishwasher_kt", "state_update": {"power": "off"}}),
            Action(
                name="create_custom_list",
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
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_birthday_party", "item": {"item": "Confetti", "quantity": 3}, "action": "add"}),
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_birthday_party", "item": {"item": "Paper Plates", "quantity": 1}, "action": "add"}),
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_birthday_party", "item": {"item": "Candles"}, "action": "remove"}),
            Action(name="get_custom_list", kwargs={"list_id": "list_birthday_party"}),
        ],
        outputs=[]
    ),

    # Task 29 – Nightly camera check, supplies list, and safety shut-off
    Task(
        annotator="0",
        user_id="res_29",
        instruction="""
        You want to enhance your home's nightly security monitoring. First, check the current state of both your security cameras: the front door camera (camera_front_door) and the back door camera (camera_back_door) to ensure they are ready for use.

        Next, activate both cameras by setting their stream_online and recording parameters to True.

        To ensure consistent security checks, create a daily reminder (rem_camera_night) that will notify you to verify the cameras are recording. Schedule it to trigger every day at 22:00 using the rrule "FREQ=DAILY;BYHOUR=22;BYMINUTE=0". Configure it with normal priority and set it to send mobile push notifications.

        To prepare for future maintenance, create a custom shopping list named "Camera Night Essentials" (list_id: list_camera_night_essentials) and add the following items: one pack of camera batteries and one lens cleaning cloth.

        For energy efficiency, make sure the Living Room Floor Lamp (device_id: light_lr_floor) is powered off during the night.

        After completing these steps, display the reminder, the shopping list, and the states of both cameras and the floor lamp to verify everything is set up correctly.
        """,
        actions=[
            Action(name="get_device_info", kwargs={"device_ids": ["camera_front_door", "camera_back_door"]}),
            Action(name="set_device_state", kwargs={"device_id": "camera_front_door", "state_update": {"stream_online": True, "recording": True}}),
            Action(name="set_device_state", kwargs={"device_id": "camera_back_door", "state_update": {"stream_online": True, "recording": True}}),
            Action(
                name="add_reminder",
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
                name="create_custom_list",
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
            Action(name="set_device_state", kwargs={"device_id": "light_lr_floor", "state_update": {"power": "off"}}),
            Action(name="get_reminders", kwargs={"reminder_id": "rem_camera_night"}),
            Action(name="get_custom_list", kwargs={"list_id": "list_camera_night_essentials"}),
            Action(name="get_device_info", kwargs={"device_ids": ["camera_front_door", "camera_back_door", "light_lr_floor"]}),
        ],
        outputs=[]
    ),

    # Task 30 – Install replacement bedside lamp in East Bedroom, check device state, and prepare supplies
    Task(
        annotator="0",
        user_id="res_30",
        instruction="""
        You need to install a new bedside lamp in your East Bedroom to replace the old one. Here are the specifications for the new device:

        Register it with ID "lamp_be_bedside2" as a device of type "light". Name it "East Bedroom Bedside Lamp (New)" and set its location to East Bedroom. It's a Govee Aura HLB-2 model running firmware version 1.4.0. The device supports these state parameters: power, brightness, and color.

        For the initial setup, configure it as powered off, with 0% brightness, and set its color to a warm yellow (hue=45, saturation=80).

        Before making any changes, check the current state of the East Bedroom (room_id: "bedroom_east") to verify device status.

        After adding the device, register it to your East Bedroom (room_id: "bedroom_east"). Then turn it on, set its brightness to 50%, and maintain the same warm yellow color settings (hue=45, saturation=80).

        To prepare for future maintenance, create a custom shopping list named "Bedside Lamp Supplies" (list_id: list_bedside_lamp_supplies) and add the following items: one replacement bulb and one cleaning cloth.

        For safety, make sure the East Bedroom ceiling light (device_id: light_be_ceiling) is powered off after installing the new lamp.

        Finally, display the East Bedroom information and the supplies list to verify the installation and preparation.
        """,
        actions=[
            Action(name="get_room_info", kwargs={"room_ids": ["bedroom_east"]}),
            Action(
                name="add_device",
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
            Action(name="manage_room_devices", kwargs={"room_id": "bedroom_east", "device_id": "lamp_be_bedside2", "action": "add"}),
            Action(name="set_device_state", kwargs={"device_id": "lamp_be_bedside2", "state_update": {"power": "on", "brightness": 50, "color": {"hue": 45, "saturation": 80}}}),
            Action(
                name="create_custom_list",
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
            Action(name="set_device_state", kwargs={"device_id": "light_be_ceiling", "state_update": {"power": "off"}}),
            Action(name="get_room_info", kwargs={"room_ids": ["bedroom_east"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_bedside_lamp_supplies"}),
        ],
        outputs=[]
    ),
    # Task 31 – Improve air quality with purifier and AC adjustments, plus supplies list and safety check
    Task(
        annotator="0",
        user_id="res_31",
        instruction="""
        You notice the air in your home feels stuffy. First, check the current CO₂ and VOC levels using your Living Room Air-Quality Sensor (sensor_lr_air_quality).

        To improve the air quality, make these adjustments: First, configure your Living Room Air-Purifier (device_id: air_purifier_lr) by turning it on, setting it to auto mode, and increasing its fan speed to "high". Then, adjust your AC unit (device_id: ac_home) by setting its fan speed to "medium" to help with air circulation.

        For energy efficiency, make sure the Living Room Floor Lamp (device_id: light_lr_floor) is powered off after making these changes.

        Also, create a custom shopping list named "Air Quality Supplies" (list_id: list_air_quality_supplies) and add the following items: one replacement air filter and one bottle of air freshener.

        After completing all steps, display the updated states of both the air purifier, AC unit, and floor lamp, and show the shopping list to verify your adjustments.
        """,
        actions=[
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(name="set_device_state", kwargs={"device_id": "air_purifier_lr", "state_update": {"power": "on", "mode": "auto", "fan_speed": "high"}}),
            Action(name="set_device_state", kwargs={"device_id": "ac_home", "state_update": {"fan_speed": "medium"}}),
            Action(name="set_device_state", kwargs={"device_id": "light_lr_floor", "state_update": {"power": "off"}}),
            Action(
                name="create_custom_list",
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
            Action(name="get_device_info", kwargs={"device_ids": ["air_purifier_lr", "ac_home", "light_lr_floor"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_air_quality_supplies"}),
        ],
        outputs=[]
    ),

    # Task 32 – Create a "Return Home" scene and run it, plus supplies and safety checks
    Task(
        annotator="0",
        user_id="res_32",
        instruction="""
        You're returning from vacation tonight and want to prepare your home for your arrival. Before making any changes, check the current reading from your Living Room Air-Quality Sensor (sensor_id: sensor_lr_air_quality) to ensure the environment is comfortable.

        Create a new scene named "Return Home" with id "scene_return_home" that will configure your devices as follows:

        Start by making the living room welcoming: Fully open the curtain (curtain_lr) by setting its position to 100 while keeping it powered on, and turn on the ceiling light (light_lr_ceiling) at 80% brightness with a warm white color temperature of 4000K. For comfortable temperature, turn on the heater (heater_home) in heat mode at 22°C, and make sure the AC (ac_home) is turned off. Finally, create some ambiance in the master bedroom by turning on the night lamp (lamp_br_night) at 30% brightness with a warm orange glow (color settings: hue=30, saturation=60).

        To ensure a restful environment, make sure the Living Room Floor Lamp (device_id: light_lr_floor) is powered off before activating the scene.

        Also, create a custom shopping list named "Return Home Essentials" (list_id: list_return_home_essentials) and add the following items: one bottle of milk and one loaf of bread.

        After creating the scene, activate it immediately and display the current states of all five devices mentioned above, the floor lamp, and the shopping list to verify everything is ready for your return.
        """,
        actions=[
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(name="list_all_scenes", kwargs={}),
            Action(
                name="create_scene",
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
            Action(name="set_device_state", kwargs={"device_id": "light_lr_floor", "state_update": {"power": "off"}}),
            Action(
                name="create_custom_list",
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
            Action(name="activate_scene", kwargs={"scene_id": "scene_return_home"}),
            Action(name="get_device_info", kwargs={"device_ids": ["curtain_lr", "light_lr_ceiling", "heater_home", "ac_home", "lamp_br_night", "light_lr_floor"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_return_home_essentials"}),
        ],
        outputs=[]
    ),
    # Task 33 – Set up Olivia's daily homework reminder, supplies list, and device safety check
    Task(
        annotator="0",
        user_id="res_33",
        instruction="""
        You want to help Olivia stay organized with her homework routine. Start by checking the current state of the Desk Lamp in Olivia's room (device_id: lamp_olivia_desk) to ensure it's powered off for energy savings before making any changes. If this device does not exist, create it with these parameters: id "lamp_olivia_desk", type "light", location "Olivia's Room", vendor "Philips", model "StudyLamp X2", firmware_version "1.0.0", and state_params ["power", "brightness", "color"].

        Next, create a supplies list with these specifications: Create a new list named "Homework Supplies" with id "list_homework_supplies" and tag it with "school". Initially, add these items to the list: ten Pencils, three Erasers, and two Notebooks.

        After creating the list, add four Highlighters and one pack of Sticky Notes to it. Display the updated list to verify all items are included correctly.

        To help maintain the homework routine, create a daily reminder (reminder_id: rem_homework_daily) that will notify Olivia to do her homework. Schedule it to trigger every day at 16:30, configure it with normal priority, and set it to send mobile push notifications.

        Finally, make sure the Desk Lamp (lamp_olivia_desk) is powered off for energy efficiency, and display both the reminder and the lamp state to confirm everything is properly scheduled and set up.
        """,
        actions=[
            Action(name="get_device_info", kwargs={"device_ids": ["lamp_olivia_desk"]}),
            Action(
                name="add_device",
                kwargs={
                    "new_device": {
                        "id": "lamp_olivia_desk",
                        "type": "light",
                        "location": "Olivia's Room",
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
                name="create_custom_list",
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
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_homework_supplies", "item": {"item": "Highlighters", "quantity": 4}, "action": "add"}),
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_homework_supplies", "item": {"item": "Sticky Notes", "quantity": 1}, "action": "add"}),
            Action(name="get_custom_list", kwargs={"list_id": "list_homework_supplies"}),
            Action(
                name="add_reminder",
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
            Action(name="set_device_state", kwargs={"device_id": "lamp_olivia_desk", "state_update": {"power": "off"}}),
            Action(name="get_reminders", kwargs={"reminder_id": "rem_homework_daily"}),
            Action(name="get_device_info", kwargs={"device_ids": ["lamp_olivia_desk"]}),
        ],
        outputs=[]
    ),

    # Task 34 – Install washing machine in Basement, start a quick wash, prepare supplies, and ensure safety
    Task(
        annotator="0",
        user_id="res_34",
        instruction="""
        You need to set up a new LG TurboWash washing machine in your basement. Here are the specifications for the device:

        Register it with ID "washer_bs" as a device of type "washing_machine". Name it "Basement Washing Machine" and set its location to Basement. It's an LG TurboWash 360 model running firmware version 1.0.0. The device supports these state parameters: power, cycle, time_remaining_min, and door.

        For the initial setup, configure it as powered off, in idle cycle mode, with 0 minutes remaining and the door closed.

        Before making any changes, check the current state of the Basement Washing Machine (device_id: washer_bs) to verify its status.

        After adding the device, register it to your basement (room_id: "basement"). Then start a quick wash by turning it on, setting the cycle to "quick", setting the remaining time to 35 minutes, and keeping the door closed.

        To prepare for laundry, create a custom shopping list named "Basement Laundry Supplies" (list_id: list_basement_laundry_supplies) and add one pack of detergent and one box of dryer sheets.

        For safety, make sure the Basement Washing Machine (device_id: washer_bs) is powered off after the wash is complete.

        Finally, display the basement information and the supplies list to verify the installation and preparation.
        """,
        actions=[
            Action(name="get_device_info", kwargs={"device_ids": ["washer_bs"]}),
            Action(
                name="add_device",
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
            Action(name="manage_room_devices", kwargs={"room_id": "basement", "device_id": "washer_bs", "action": "add"}),
            Action(name="set_device_state", kwargs={"device_id": "washer_bs", "state_update": {"power": "on", "cycle": "quick", "time_remaining_min": 35, "door": "closed"}}),
            Action(
                name="create_custom_list",
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
            Action(name="set_device_state", kwargs={"device_id": "washer_bs", "state_update": {"power": "off", "cycle": "idle", "time_remaining_min": 0, "door": "closed"}}),
            Action(name="get_room_info", kwargs={"room_ids": ["basement"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_basement_laundry_supplies"}),
        ],
        outputs=[]
    ),

    # Task 35 – Create a Focus Study scene for West Bedroom leveraging air-quality sensor and supplies list
    Task(
        annotator="0",
        user_id="res_35",
        instruction="""
        The time is 2025-07-30 08:30, and you want to create an optimal study environment. First, check the current air quality data from your Living Room Air-Quality Sensor (sensor_lr_air_quality) to ensure a healthy study space.

        Then, create a new scene named "Study Fresh" with id "scene_study_fresh" that will configure your devices as follows:

        For optimal lighting, turn on the West Bedroom Desk Lamp (lamp_bw_desk) at 90% brightness and set its color temperature to 5500K. Turn off the West Bedroom Ceiling Light (light_bw_ceiling) to avoid glare. For natural light and ventilation, open the West Bedroom Curtain (curtain_bw) to 75% while keeping it powered on. Finally, ensure good air quality by turning on the Living Room Air-Purifier (air_purifier_lr), setting it to auto mode with medium fan speed.

        To make sure you have everything needed for focused study, create a custom shopping list named "Study Fresh Essentials" (list_id: list_study_fresh_essentials) and add the following items: one pack of sticky notes and one bottle of water.

        Also, make sure the Living Room Floor Lamp (light_lr_floor) is powered off to avoid distractions.

        After creating the scene, activate it immediately and display the current states of all four devices, the shopping list, and the state of the Living Room Floor Lamp to verify your study environment is properly set up.
        """,
        actions=[
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(name="list_all_scenes", kwargs={}),
            Action(name="get_room_info", kwargs={"room_ids": ["bedroom_west"]}),
            Action(
                name="create_scene",
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
                name="create_custom_list",
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
                name="set_device_state",
                kwargs={
                    "device_id": "light_lr_floor",
                    "state_update": {"power": "off"}
                }
            ),
            Action(name="activate_scene", kwargs={"scene_id": "scene_study_fresh"}),
            Action(name="get_device_info", kwargs={"device_ids": ["lamp_bw_desk", "light_bw_ceiling", "curtain_bw", "air_purifier_lr", "light_lr_floor"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_study_fresh_essentials"}),
        ],
        outputs=[]
    ),

    # Task 36 – Update shopping list, add missing items, check kitchen safety, and set weekly grocery reminder
    Task(
        annotator="0",
        user_id="res_36",
        instruction="""
        You need to update your shopping list and set up a regular reminder for groceries. First, check the current state of your Kitchen Dishwasher (device_id: dishwasher_kt) to ensure it's powered off for safety before making any changes. If it's not off, turn it off.

        Next, make some changes to your existing shopping list (list_id: list_shopping): Add twelve rolls of Toilet Paper, and remove one entry of Dog Food from the list. Also, add two bottles of Dish Soap and one pack of Sponges to ensure you have enough cleaning supplies.

        After making these changes, display the updated list to verify the modifications.

        To help you stay on top of your grocery shopping, create a weekly reminder (reminder_id: rem_weekly_groceries) that will notify you every Saturday at 09:30. Use the rrule "FREQ=WEEKLY;BYDAY=SA;BYHOUR=9;BYMINUTE=30", configure it with normal priority, and set it to send mobile push notifications.

        Finally, display the newly created reminder and the state of the dishwasher to confirm everything is properly scheduled and safe.
        """,
        actions=[
            Action(name="get_device_info", kwargs={"device_ids": ["dishwasher_kt"]}),
            Action(name="set_device_state", kwargs={"device_id": "dishwasher_kt", "state_update": {"power": "off"}}),
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_shopping", "item": {"item": "Toilet Paper", "quantity": 12}, "action": "add"}),
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_shopping", "item": {"item": "Dog Food"}, "action": "remove"}),
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_shopping", "item": {"item": "Dish Soap", "quantity": 2}, "action": "add"}),
            Action(name="manage_custom_list_items", kwargs={"list_id": "list_shopping", "item": {"item": "Sponges", "quantity": 1}, "action": "add"}),
            Action(name="get_custom_list", kwargs={"list_id": "list_shopping"}),
            Action(
                name="add_reminder",
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
            Action(name="get_reminders", kwargs={"reminder_id": "rem_weekly_groceries"}),
            Action(name="get_device_info", kwargs={"device_ids": ["dishwasher_kt"]}),
        ],
        outputs=[]
    ),

    # Task 37 – Replace old Good Night scene with an upgraded version and prepare supplies
    Task(
        annotator="0",
        user_id="res_37",
        instruction="""
        You want to upgrade your bedtime scene with a new version and ensure everything is ready for a restful night. First, check the current reading from your Living Room Air-Quality Sensor (sensor_id: sensor_lr_air_quality) to ensure the environment is comfortable before making any changes.

        Create a new scene named "Good Night Plus" with id "scene_good_night_plus" that will configure your devices as follows:

        In the living room, close the curtain (curtain_lr) by setting its position to 0 while keeping it powered on, and turn off both the floor and ceiling lights (light_lr_floor and light_lr_ceiling). Create a gentle ambiance in the master bedroom by turning on the night lamp (lamp_br_night) at 10% brightness with a warm glow (color settings: hue=30, saturation=40). For quiet comfort, set your AC unit's (ac_home) fan speed to "low".

        Before activating the new scene, delete the original scene (scene_good_night). Also, make sure the kitchen dishwasher (device_id: dishwasher_kt) is powered off for safety before bedtime.

        To prepare for the night, create a custom shopping list named "Good Night Essentials" (list_id: list_good_night_essentials) and add the following items: one sleep mask and one bottle of water.

        After activating your new scene, display the updated states of all four devices, the dishwasher, and the shopping list to verify your improved bedtime setup.
        """,
        actions=[
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(name="get_device_info", kwargs={"device_ids": ["dishwasher_kt"]}),
            Action(name="set_device_state", kwargs={"device_id": "dishwasher_kt", "state_update": {"power": "off"}}),
            Action(name="delete_scene", kwargs={"scene_id": "scene_good_night"}),
            Action(
                name="create_scene",
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
                name="create_custom_list",
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
            Action(name="activate_scene", kwargs={"scene_id": "scene_good_night_plus"}),
            Action(name="get_device_info", kwargs={"device_ids": ["curtain_lr", "light_lr_floor", "light_lr_ceiling", "lamp_br_night", "dishwasher_kt"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_good_night_essentials"}),
        ],
        outputs=[]
    ),

    # Task 38 – Schedule battery-replacement reminder, prepare supplies list, and ensure safety after checking smoke detector
    Task(
        annotator="0",
        user_id="res_38",
        instruction="""
        You need to check your Bedroom Smoke Detector (sensor_id: sensor_bed_smoke) and schedule its battery maintenance. First, retrieve the current reading from the smoke detector to assess its status.

        After checking the reading, create a one-time reminder (reminder_id: rem_smoke_battery) to replace the detector's batteries. Schedule it for 2025-07-01T09:00:00, configure it with high priority, and set it to send a mobile push notification.

        Next, prepare for the battery replacement by creating a custom shopping list named "Smoke Detector Supplies" (list_id: list_smoke_detector_supplies) and add the following items: one pack of AA batteries and one cleaning cloth.

        For safety, make sure the Bedroom Night Lamp (device_id: lamp_br_night) is powered off before starting any maintenance. Before making this change, check its current state.

        Finally, display the newly created reminder, the supplies list, and the lamp state to verify everything is properly scheduled and prepared.
        """,
        actions=[
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_bed_smoke"]}),
            Action(
                name="add_reminder",
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
                name="create_custom_list",
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
            Action(name="get_device_info", kwargs={"device_ids": ["lamp_br_night"]}),
            Action(name="set_device_state", kwargs={"device_id": "lamp_br_night", "state_update": {"power": "off"}}),
            Action(name="get_reminders", kwargs={"reminder_id": "rem_smoke_battery"}),
            Action(name="get_custom_list", kwargs={"list_id": "list_smoke_detector_supplies"}),
            Action(name="get_device_info", kwargs={"device_ids": ["lamp_br_night"]}),
        ],
        outputs=[]
    ),

    # Task 39 – Install robot vacuum, run clean-up scene, prepare supplies, and check safety
    Task(
        annotator="0",
        user_id="res_39",
        instruction="""
        You've purchased a new Roborock S8 robot vacuum for your home. Here are the specifications for setting up the device:

        Register it with ID "vacuum_lr" as a device of type "vacuum". Name it "Living Room Vacuum" and set its location to Living Room. It's a Roborock S8 model running firmware version 1.0.0. The device supports these state parameters: power, mode, and battery_pct.

        For the initial setup, configure it as powered off, in idle mode, with 100% battery.

        Before making any changes, check the current reading from your Living Room Air-Quality Sensor (sensor_id: sensor_lr_air_quality) to ensure the environment is suitable for cleaning.

        After adding the vacuum to your Living Room, create a new scene named "Clean Up" with id "scene_clean_up" that will start the cleaning process: Turn on the vacuum and set its mode to "clean", and close the living room curtain (curtain_lr) by setting its position to 0 while keeping it powered on.

        To prepare for future maintenance, create a custom shopping list named "Vacuum Supplies" (list_id: list_vacuum_supplies) and add the following items: one replacement filter and one cleaning brush.

        For safety, make sure the Living Room Floor Lamp (device_id: light_lr_floor) is powered off before activating the scene.

        Finally, activate the scene and display the current states of both the vacuum, curtain, floor lamp, and the supplies list to verify your cleaning setup.
        """,
        actions=[
            Action(name="get_sensor_data", kwargs={"sensor_ids": ["sensor_lr_air_quality"]}),
            Action(
                name="add_device",
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
            Action(name="manage_room_devices", kwargs={"room_id": "living_room", "device_id": "vacuum_lr", "action": "add"}),
            Action(
                name="create_scene",
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
                name="create_custom_list",
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
            Action(name="set_device_state", kwargs={"device_id": "light_lr_floor", "state_update": {"power": "off"}}),
            Action(name="activate_scene", kwargs={"scene_id": "scene_clean_up"}),
            Action(name="get_device_info", kwargs={"device_ids": ["vacuum_lr", "curtain_lr", "light_lr_floor"]}),
            Action(name="get_custom_list", kwargs={"list_id": "list_vacuum_supplies"}),
        ],
        outputs=[]
    ),

    # Task 40 – Prepare for David Lee's dinner visit
    Task(
        annotator="0",
        user_id="res_40",
        instruction="""
        You're expecting David Lee for dinner this Sunday at 18:30, and you want to create a welcoming atmosphere. Create a new scene named "David Dinner" with id "scene_david_dinner" that will configure your home as follows:

        In the living room, fully open the curtain (curtain_lr) by setting its position to 100 while keeping it powered on, and turn on the floor lamp (light_lr_floor) at 70% brightness. For comfort, configure the AC unit (ac_home) by turning it on, setting it to cool mode at 23°C, with the fan speed on "low" for quiet operation.

        After creating the scene, schedule a reminder (rem_pickup_dinner) to help you prepare for his arrival. Set it to notify you at 17:45 that day to "Pick up the take-out food". Configure it with high priority and set it to send mobile push notifications.

        Finally, display both the scene list and the reminder to verify everything is properly set up for David's visit.
        """,
        actions=[
            Action(
                name="create_scene",
                kwargs={
                    "new_scene": {
                        "id": "scene_david_dinner",
                        "name": "David Dinner",
                        "actions": [
                            {"device_id": "curtain_lr", "update": {"power": "on", "position": 100}},
                            {"device_id": "light_lr_floor", "update": {"power": "on", "brightness": 70}},
                            {"device_id": "ac_home", "update": {"power": "on", "mode": "cool", "setpoint_c": 23, "fan_speed": "low"}}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder",
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
            Action(name="list_all_scenes", kwargs={}),
            Action(name="get_reminders", kwargs={"reminder_id": "rem_pickup_dinner"}),
        ],
        outputs=[]
    ),
]
