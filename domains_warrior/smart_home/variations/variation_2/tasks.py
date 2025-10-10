from domains.dto import Task, Action
TASKS = [
    Task(
        annotator="0",
        user_id="res_01",
        instruction="""
        The current time is 2025-07-25 07:30. You want to perform a few tasks.
        1. You want to know the current temperature from the living-room thermometer.
        2. If the temperature is above 22 degrees Celsius, you want to schedule the central AC to turn on at 13:00 today. The AC settings should be: power=on, mode=cool, setpoint_c=22, and fan_speed=auto.
        3. At the same time, 13:00, you want to also close the living-room curtain by setting its power=on and position=0.
        4. You also want to set up a daily routine: every day at 19:00, you want to dim the ceiling light to power=on and brightness=30, and turn the floor lamp off.
        5. Lastly, you want to create a one-shot reminder called "Close windows before AC starts". It should trigger a mobile_push notification at 2025-07-25T12:55:00 with "normal" priority.
        """,
        actions=[
            Action(name="get_entity", kwargs={"entity_type": "sensors"}),
            Action(
                name="get_entity",
                kwargs={"entity_type": "sensors", "entity_id": "sensor_lr_thermometer"}
            ),
            Action(name="get_entity", kwargs={"entity_type": "devices"}),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "ac_home",
                    "update": {"power": "on", "mode": "cool",
                               "setpoint_c": 22, "fan_speed": "auto"},
                    "schedule_at": "2025-07-25T13:00:00"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "curtain_lr",
                    "update": {"power": "on", "position": 0},
                    "schedule_at": "2025-07-25T13:00:00"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "light_lr_ceiling",
                    "update": {"power": "on", "brightness": 30},
                    "schedule_at": "2025-07-25T19:00:00",
                    "rrule": "FREQ=DAILY"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "light_lr_floor",
                    "update": {"power": "off"},
                    "schedule_at": "2025-07-25T19:00:00",
                    "rrule": "FREQ=DAILY"
                }
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_close_windows",
                        "target": {"type": "note", "text": "Close windows before AC starts"},
                        "trigger": {"datetime": "2025-07-25T12:55:00"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "scheduled",
                        "meta": {"priority": "normal"}
                    }
                }
            )
        ],
        outputs=['"temperature_c": 22.3']
    ),
    Task(
        annotator="0",
        user_id="res_02",
        instruction="""
        It's 10am on 2025-07-26. You want to prepare for family movie night.
        First, you want to create a custom list called "Friday Movie Night Snacks" with id "list_movie_snacks", and it should be tagged with "shopping" and "movie".
        Then, you want to add 2 portions of popcorn, 6 sodas, and 5 chocolates to that list.
        You also need to modify the existing "Movie Time" scene. For this scene, you want the floor lamp brightness to be 15, the AC fan_speed to be "low", and the setpoint_c to be 23. Other existing configurations should be overwritten.
        Finally, you want to add a scheduled run for this scene at 2025-07-27T20:00:00; remove existing scheduled runs if any.
        """,
        actions=[
            Action(
                name="query_entities",
                kwargs={"entity_type": "custom_lists", "filters": {"name": "Friday Movie Night Snacks"}}
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_movie_snacks",
                        "tags": ["shopping", "movie"],
                        "items": []
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_movie_snacks",
                        "item": {"item": "Popcorn", "quantity": 2},
                        "action": "add"}
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_movie_snacks",
                        "item": {"item": "Soda", "quantity": 6},
                        "action": "add"}
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_movie_snacks",
                        "item": {"item": "Chocolate", "quantity": 5},
                        "action": "add"}
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "scenes"}
            ),
            Action(
                name="upsert_scene",
                kwargs={
                    "scene": {
                        "id": "scene_movie_time",
                        "actions": [
                            {"device_id": "light_lr_floor",
                             "update": {"power": "on", "brightness": 15}},
                            {"device_id": "ac_home",
                             "update": {"power": "on", "fan_speed": "low", "setpoint_c": 23}}
                        ],
                        "scheduled_runs": ["2025-07-27T20:00:00"]
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_03",
        instruction="""
        Today is 2025-07-26 at 10:00:00
        You want to install a new smart air-purifier in the East Bedroom.
        The air-purifier is from vendor "Coway", model "AP-1512HH", firmware version "1.0.0" and you want to give it the id "purifier_be".
        Its adjustable parameters are power, mode, and fan_speed.
        You want its default state to be power=off, mode=auto, and fan_speed=1.
        The purifier currently has blank scheduled_updates list.
        You want to add the purifier to the "bedroom_east" room.
        You also want to schedule it to turn on daily at 22:00 with fan_speed=3, and turn it off daily at 06:00.
        Next, you want to create a custom list called "Air-Filter Replacements" with id "list_air_filters" and add one "Purifier Filter Type X" to it.
        Finally, you want to set up a reminder to "Replace purifier filter" that sends a mobile_push notification on the 1st of every month at 09:00.
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "rooms", "entity_id": "bedroom_east"}
            ),
            Action(
                name="upsert_device",
                kwargs={
                    "device": {
                        "id": "purifier_be",
                        "type": "air_purifier",

                        "location": "East Bedroom",
                        "vendor": "Coway",
                        "model": "AP-1512HH",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "mode", "fan_speed"],
                        "state": {
                            "power": "off",
                            "mode": "auto",
                            "fan_speed": 1,

                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="add_device_to_room",
                kwargs={"room_id": "bedroom_east", "device_id": "purifier_be"}
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "purifier_be",
                    "update": {"power": "on", "mode": "auto", "fan_speed": 3},
                    "schedule_at": "2025-07-26T22:00:00",
                    "rrule": "FREQ=DAILY"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "purifier_be",
                    "update": {"power": "off"},
                    "schedule_at": "2025-07-27T06:00:00",
                    "rrule": "FREQ=DAILY"
                }
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_air_filters",
                        "items": []
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_air_filters",
                        "item": {"item": "Purifier Filter Type X", "quantity": 1},
                        "action": "add"}
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_purifier_filter",

                        "target": {"type": "note", "text": "Replace purifier filter"},
                        "trigger": {"rrule": "FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active",
                        "meta": {"priority": "normal"}
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_04",
        instruction="""
        You want to build an "After-School Study" scene.
        This scene should:
          • Turn the West-Bedroom desk lamp on with brightness 60 and color_temperature 5000.
          • Keep the West-Bedroom ceiling light on, but dim its brightness to 40.
          • Open the living-room curtain to position 100.
          • With description "Prep lighting & curtains for homework time".
        You want to schedule this scene to run every weekday at 16:00, starting from 2025-07-25.
        You also need to add a reminder for "Olivia, start your homework" that triggers a mobile_push every weekday at 16:10.
        Finally, you want to add "Review math homework" (quantity 1) to the todo list.
        Set description as "Prep lighting & curtains for homework time".
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "devices"}
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "custom_lists"}
            ),
            Action(
                name="upsert_scene",
                kwargs={
                    "scene": {
                        "id": "scene_after_school_study",
                        "description": "Prep lighting & curtains for homework time",
                        "actions": [
                            {"device_id": "lamp_bw_desk",
                             "update": {"power": "on", "brightness": 60,
                                        "color_temperature": 5000}},
                            {"device_id": "light_bw_ceiling",
                             "update": {"power": "on", "brightness": 40}},
                            {"device_id": "curtain_lr",
                             "update": {"power": "on", "position": 100}}
                        ],
                        "scheduled_runs": ["2025-07-25T16:00:00"],
                        "meta": {"rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"}
                    }
                }
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_olivia_homework",
                        "target": {"type": "note", "text": "Olivia, start your homework"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=16;BYMINUTE=10"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active"
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_todo",
                        "item": {"item": "Review math homework", "quantity": 1},
                        "action": "add"}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_05",
        instruction="""
        You want to check the kitchen sink leak sensor.
        If its battery_level is below 95, you want to add two "CR123A batteries" to the shopping list.
        In the same condition, you want to also create a weekly reminder for every Monday at 09:00 called "Check leak-sensor battery".
        Separately, you want to schedule the dishwasher to run a self-clean cycle tonight (2025-07-26) at 23:00. The settings should be power=on and cycle=self_clean.
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "sensors"}
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "custom_lists"}
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_shopping",
                        "item": {"item": "CR123A batteries", "quantity": 2},
                        "action": "add"}
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_sink_battery",

                        "target": {"type": "note", "text": "Check leak-sensor battery"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active"
                    }
                }
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "devices"}
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "dishwasher_kt",
                    "update": {"power": "on", "cycle": "self_clean"},
                    "schedule_at": "2025-07-26T23:00:00"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_06",
        instruction="""
        You want to create a "Weekday Morning" scene with id "scene_weekday_morning".
        This scene should do the following:
          • Open the living room and bedroom curtains to position 100.
          • Turn on the living room ceiling light to brightness 70 and kelvin 4000.
          • Turn the heater off and turn the AC on with setpoint_c=24.
        You want to schedule the first run for 2025-07-26T07:00:00 and make it a recurring event from Monday to Friday.
        You also need to add a reminder to "Pack kids' lunches" via mobile_push at 07:15 on weekdays.
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "devices"}
            ),
            Action(
                name="upsert_scene",
                kwargs={
                    "scene": {
                        "id": "scene_weekday_morning",
                        "actions": [
                            {"device_id": "curtain_lr",
                             "update": {"power": "on", "position": 100}},
                            {"device_id": "curtain_br",
                             "update": {"power": "on", "position": 100}},
                            {"device_id": "light_lr_ceiling",
                             "update": {"power": "on", "brightness": 70,
                                        "color": {"kelvin": 4000}}},
                            {"device_id": "heater_home",
                             "update": {"power": "off"}},
                            {"device_id": "ac_home",
                             "update": {"power": "on", "setpoint_c": 24}}
                        ],
                        "scheduled_runs": ["2025-07-26T07:00:00"],
                        "meta": {"rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"}
                    }
                }
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_pack_lunch",

                        "target": {"type": "note", "text": "Pack kids' lunches"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=7;BYMINUTE=15"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active"
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_07",
        instruction="""
        You are leaving for a holiday on 2025-08-10 at 08:00 and you want to set up your home.
        • You want to schedule the living-room ceiling & floor lights, all bedroom ceiling lights, and the bedroom night light to turn off at 08:00 on 2025-08-10.
        • You also want to schedule the heater and AC to power off at the same time.
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "devices"}
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "light_lr_ceiling",
                    "update": {"power": "off"},
                    "schedule_at": "2025-08-10T08:00:00"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "light_lr_floor",
                    "update": {"power": "off"},
                    "schedule_at": "2025-08-10T08:00:00"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "light_br_ceiling",
                    "update": {"power": "off"},
                    "schedule_at": "2025-08-10T08:00:00"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "light_bw_ceiling",
                    "update": {"power": "off"},
                    "schedule_at": "2025-08-10T08:00:00"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "light_be_ceiling",
                    "update": {"power": "off"},
                    "schedule_at": "2025-08-10T08:00:00"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "lamp_br_night",
                    "update": {"power": "off"},
                    "schedule_at": "2025-08-10T08:00:00"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "heater_home",
                    "update": {"power": "off"},
                    "schedule_at": "2025-08-10T08:00:00"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "ac_home",
                    "update": {"power": "off"},
                    "schedule_at": "2025-08-10T08:00:00"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_08",
        instruction="""
        Today is 2025-07-25 at 11:00:00
        Robert and Linda are arriving on 2025-07-26 at 14:00. You want to prepare for their visit.
        Starting from 2025-07-26, you want to schedule the following:
        • In the West Bedroom, you want to schedule the ceiling light to turn off at 22:30 daily.
        • You want to schedule the heater to a setpoint_c of 22 at 22:00 daily.
        You want to create a custom list called "Guest Comfort" (id list_guest_comfort) tagged "guest" and add "Extra Pillows"x4 and "Lavender Room Spray"x1 to it.
        You also need to make a reminder with id "rem_pickup_grandparents" for "Pick up grandparents at SFO" for 2025-07-26T13:30 via mobile_push.
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "devices"}
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "light_bw_ceiling",
                    "update": {"power": "off"},
                    "schedule_at": "2025-07-26T22:30:00",
                    "rrule": "FREQ=DAILY"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "heater_home",
                    "update": {"power": "on", "mode": "heat", "setpoint_c": 22},
                    "schedule_at": "2025-07-26T22:00:00",
                    "rrule": "FREQ=DAILY"
                }
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_guest_comfort",
                        "name": "Guest Comfort",
                        "tags": ["guest"],
                        "items": []
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_guest_comfort",
                        "item": {"item": "Extra Pillows", "quantity": 4},
                        "action": "add"}
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_guest_comfort",
                        "item": {"item": "Lavender Room Spray", "quantity": 1},
                        "action": "add"}
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_pickup_grandparents",
                        "target": {"type": "note", "text": "Pick up grandparents at SFO"},
                        "trigger": {"datetime": "2025-07-26T13:30:00"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_09",
        instruction="""
        Today is 2025-07-25 at 11:30
        You want to add a new smart dog feeder with id "feeder_dog" in the Kitchen.
        • The vendor is PetTech, model is "FeedMaster 2" with firmware version 1.0.0, and its state_params are power and portion_g.
        • You want the default state to be power=off and portion_g=0.
        • The feeder currently has blank scheduled_updates list.
        • You want to attach it to the kitchen room.
        • You want to schedule daily feedings at 07:00 and 18:00 with power=on and portion_g=120.
        • You also want to create or extend the custom list "Pet Supplies" (id list_pet_supplies) tagged "pet" and add "Dog Food"x5.
        • Finally, you want to add a reminder to "Buy dog food" recurring monthly on the 25th at 18:00.
        """,
        actions=[
            Action(
                name="upsert_device",
                kwargs={
                    "device": {
                        "id": "feeder_dog",
                        "type": "feeder",

                        "location": "Kitchen",
                        "vendor": "PetTech",
                        "model": "FeedMaster 2",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "portion_g"],
                        "state": {
                            "power": "off",
                            "portion_g": 0
                        }
                    }
                }
            ),
            Action(
                name="add_device_to_room",
                kwargs={"room_id": "kitchen", "device_id": "feeder_dog"}
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "feeder_dog",
                    "update": {"power": "on", "portion_g": 120},
                    "schedule_at": "2025-07-26T07:00:00",
                    "rrule": "FREQ=DAILY"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "feeder_dog",
                    "update": {"power": "on", "portion_g": 120},
                    "schedule_at": "2025-07-25T18:00:00",
                    "rrule": "FREQ=DAILY"
                }
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_pet_supplies",

                        "tags": ["pet"],
                        "items": []
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_pet_supplies",
                        "item": {"item": "Dog Food", "quantity": 5},
                        "action": "add"}
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_buy_dog_food",

                        "target": {"type": "note", "text": "Buy dog food"},
                        "trigger": {"rrule": "FREQ=MONTHLY;BYMONTHDAY=25;BYHOUR=18;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active"
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_10",
        instruction="""
        You want to set up monthly dishwasher maintenance.
        • You need a reminder on the first Monday of each month at 10:00 to "Run dishwasher cleaning cycle".
        • You also want to schedule the dishwasher to power=on with cycle=self_clean at 10:05 based on the same rule.
        • You want to ensure "Descaling tablets"x1 is on your shopping list.
        • You need a reminder to "Refill the descaling tablets into the dishwasher" next day after the cleaning, first Tuesday of the month
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "devices"}
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_dishwasher_clean",

                        "target": {"type": "note", "text": "Run dishwasher cleaning cycle"},
                        "trigger": {"rrule": "FREQ=MONTHLY;BYDAY=MO;BYSETPOS=1;BYHOUR=10;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active"
                    }
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "dishwasher_kt",
                    "update": {"power": "on", "cycle": "self_clean"},
                    "schedule_at": "2025-08-04T10:05:00",
                    "rrule": "FREQ=MONTHLY;BYDAY=MO;BYSETPOS=1"
                }
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "custom_lists"}
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_shopping",
                        "item": {"item": "Descaling tablets", "quantity": 1},
                        "action": "add"}
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_dishwasher_refill",
                        "target": {"type": "note", "text": "Refill the descaling tablets into the dishwasher"},
                        "trigger": {"rrule": "FREQ=MONTHLY;BYDAY=TU;BYSETPOS=1;BYHOUR=10;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active"
                    }
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_11",
        instruction="""
        You want to verify the bedroom smoke detector battery.
        • You want to read the bedroom smoke detector's state. If the battery_level is less than 95, you want to add "9 V batteries"x2 to the shopping list.
        • You want to create a "Fire Alert" scene, that is an "Emergency red lighting", where the bedroom night light & living room floor light are set to power=on, brightness=100, and color hue=0.
        • You want to schedule no automatic run for this scene, making it for manual trigger only.
        • You want to make a yearly reminder on Jan 1 at 09:00 to "Replace smoke-detector battery".
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "sensors"}
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_shopping",
                        "item": {"item": "9 V batteries", "quantity": 2},
                        "action": "add"}
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "devices"}
            ),
            Action(
                name="upsert_scene",
                kwargs={
                    "scene": {
                        "id": "scene_fire_alert",
                        "actions": [
                            {"device_id": "lamp_br_night",
                             "update": {"power": "on", "brightness": 100,
                                        "color": {"hue": 0}}},
                            {"device_id": "light_lr_floor",
                             "update": {"power": "on", "brightness": 100,
                                        "color": {"hue": 0}}}
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_replace_smoke_battery",

                        "target": {"type": "note", "text": "Replace smoke-detector battery"},
                        "trigger": {"rrule": "FREQ=YEARLY;BYMONTH=1;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active"
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_12",
        instruction="""
        You want to strengthen your front-door security.
        • You want to immediately ensure the camera_front_door has stream_online=true and recording=true.
        • You want to create a reminder to "Review security footage" with id "rem_review_footage" daily at 21:00 via mobile_push.
        • You also need to start a custom list called "Security Logs" (id list_security_logs) and add "Review finished"x0 as a placeholder.
        """,
        actions=[
            Action(
                name="modify_sensor_state",
                kwargs={
                    "sensor_id": "camera_front_door",
                    "update": {"stream_online": True, "recording": True}
                }
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_review_footage",

                        "target": {"type": "note", "text": "Review security footage"},
                        "trigger": {"rrule": "FREQ=DAILY;BYHOUR=21;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active"
                    }
                }
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_security_logs",

                        "items": []
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_security_logs",
                        "item": {"item": "Review finished", "quantity": 0},
                        "action": "add"}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_13",
        instruction="""
        You want to add a household member, Liam Chen (id liam_chen, male, born 2003-02-11, relation Cousin), who will be staying in the East Bedroom.
        • You want to create a packing list for him called "Liam Packing" (id list_liam_pack).
        • To this list, you want to add "Towels"x2 and "Extra Blanket"x1.
        """,
        actions=[
            Action(
                name="upsert_member",
                kwargs={
                    "member": {
                        "id": "liam_chen",
                        "first_name": "Liam",
                        "last_name": "Chen",
                        "relation": "Cousin",
                        "birthdate": "2003-02-11",
                        "sex": "male",
                        "residence": {"lives_in_house": True, "room_id": "bedroom_east"}
                    }
                }
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_liam_pack",

                        "items": []
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_liam_pack",
                        "item": {"item": "Towels", "quantity": 2},
                        "action": "add"}
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_liam_pack",
                        "item": {"item": "Extra Blanket", "quantity": 1},
                        "action": "add"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_14",
        instruction="""
        You want to add a soil-moisture sensor (id sensor_garden_moisture, vendor Eve, model SoilGuard, firmware version 1.0.0) and a sprinkler controller (id sprinkler_garden, vendor Rachio, model R3, firmware version 1.0.0) for the garden. For now, you'll track them in the basement.
        • The sensor's state_params are moisture_pct and battery_level.
        • The sprinkler's state_params are power and duration_min.
        • You want the default sprinkler state to be power=off, duration_min=0.
        • The sprinkler currently has blank scheduled_updates list.
        • You want to schedule the sprinkler_garden to have power=on and duration_min=15 every day at 06:00.
        • You also need to make a reminder to "Change sprinkler filter" yearly on Mar 1 at 09:00.
        """,
        actions=[
            Action(
                name="upsert_device",
                kwargs={
                    "device": {
                        "id": "sensor_garden_moisture",
                        "type": "sensor",

                        "location": "Basement",
                        "vendor": "Eve",
                        "model": "SoilGuard",
                        "firmware_version": "1.0.0",
                        "state_params": ["moisture_pct", "battery_level"],
                        "state": {
                            "moisture_pct": 30,
                            "battery_level": 100,

                        }
                    }
                }
            ),
            Action(
                name="upsert_device",
                kwargs={
                    "device": {
                        "id": "sprinkler_garden",
                        "type": "sprinkler",

                        "location": "Basement",
                        "vendor": "Rachio",
                        "model": "R3",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "duration_min"],
                        "state": {
                            "power": "off",
                            "duration_min": 0
                        }
                    }
                }
            ),
            Action(
                name="add_device_to_room",
                kwargs={"room_id": "basement", "device_id": "sensor_garden_moisture"}
            ),
            Action(
                name="add_device_to_room",
                kwargs={"room_id": "basement", "device_id": "sprinkler_garden"}
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "sprinkler_garden",
                    "update": {"power": "on", "duration_min": 15},
                    "schedule_at": "2025-07-26T06:00:00",
                    "rrule": "FREQ=DAILY"
                }
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_sprinkler_filter",

                        "target": {"type": "note", "text": "Change sprinkler filter"},
                        "trigger": {"rrule": "FREQ=YEARLY;BYMONTH=3;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active"
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_15",
        instruction="""
        You want to create routines for the East-Bedroom on school nights (Sun-Thu) starting from today 2025-06-29.
        • The bedroom bedside lamp should turn on at 20:00 with brightness 10, and turn off at 22:00.
        • The bedroom curtain should close (position 0) at 20:10.
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "devices"}
            ),
            Action(
                name="modify_device_state_timer",
                kwargs={
                    "device_id": "lamp_be_bedside",
                    "schedule_end": "2025-06-29T22:00:00",
                    "update": {"power": "on", "brightness": 10},
                    "schedule_at": "2025-06-29T20:00:00",
                    "rrule": "FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "curtain_be",
                    "update": {"position": 0},
                    "schedule_at": "2025-06-29T20:10:00",
                    "rrule": "FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_16",
        instruction="""
        Today is 2025-02-16, and it's John Smith's birthday tomorrow.
        You want to create a new shopping list for him with id "list_john_birthday_shopping" with the tags "birthday" and "shopping".
        You want to add 1 quantity of his favorite food, Sushi, to this shopping list.
        You've also bought a new speaker with the following details:
        - Vendor: Sonos
        - Model: Move 2
        - Firmware version: 1.0.0
        - Adjustable parameters: power, volume, playlist
        - blank scheduled_updates list
        - It'll be in bedroom, so can call it "Bedroom Speaker"
        You want to place it in the Master Bedroom and give it an id of "speaker_bedroom".
        You want to schedule this speaker to be turned on at 8am on his birthday to play his favorite music at volume 50.
        """,
        actions=[
            Action(
                name="query_entities",
                kwargs={
                    "entity_type": "members",
                    "filters": {"first_name": "John", "last_name": "Smith"}
                }
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_john_birthday_shopping",
                        "tags": ["birthday", "shopping"],
                        "items": [
                            {
                                "item": "Sushi",
                                "quantity": 1
                            },
                        ]
                    }
                }
            ),
            Action(
                name="upsert_device",
                kwargs={
                    "device": {
                        "id": "speaker_bedroom",
                        "type": "speaker",
                        "location": "Master Bedroom",
                        "vendor": "Sonos",
                        "model": "Move 2",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "volume", "playlist"],
                        "state": {
                            "power": "off",
                            "volume": 0,
                            "playlist": "",

                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "speaker_bedroom",
                    "update": {"power": "on", "volume": 50, "playlist": "classic rock"},
                    "schedule_at": "2025-02-17T08:00:00"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_17",
        instruction="""
        It is 2025-07-25 14:00. You have a few tasks.
        • You want to schedule the dishwasher to run a self-clean cycle at 02:00 on 2025-07-26 with power=on and cycle=self_clean.
        • You want to create a daily reminder at 21:00 to "Empty dryer lint trap".
        • You want to add "High-efficiency detergent" x2 to the household shopping list.
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "devices"}
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "dishwasher_kt",
                    "update": {"power": "on", "cycle": "self_clean"},
                    "schedule_at": "2025-07-26T02:00:00"
                }
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_dryer_lint",

                        "target": {"type": "note", "text": "Empty dryer lint trap"},
                        "trigger": {"rrule": "FREQ=DAILY;BYHOUR=21;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active"
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_shopping",
                        "item": {"item": "High-efficiency detergent", "quantity": 2},
                        "action": "add"}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_18",
        instruction="""
        Today is 2025-07-29. You want to prepare for a severe heat-wave expected tomorrow (2025-07-30). You want to do all of the following:
        1. You want to read the Living-Room thermometer to log the current temperature.
        2. You want to close the Living-Room curtain (device id "curtain_lr") to position 0 at 12:50 tomorrow as a one-shot action.
        3. You want to dim the Living-Room ceiling light (device id "light_lr_ceiling") to brightness 30 at exactly 12:55 tomorrow, also a one-shot action.
        4. You want to create a new scene called "Heatwave Afternoon" (id "scene_heatwave_afternoon") that bundles the two device updates above, no need to schedule it.
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={
                    "entity_type": "sensors",
                }
            ),
            Action(
                name="get_entity",
                kwargs={
                    "entity_type": "devices",
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "curtain_lr",
                    "update": {"power": "on", "position": 0},
                    "schedule_at": "2025-07-30T12:50:00"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "light_lr_ceiling",
                    "update": {"power": "on", "brightness": 30},
                    "schedule_at": "2025-07-30T12:55:00"
                }
            ),
            Action(
                name="upsert_scene",
                kwargs={
                    "scene": {
                        "id": "scene_heatwave_afternoon",
                        "name": "Heatwave Afternoon",
                        "actions": [
                            {"device_id": "curtain_lr", "update": {"power": "on", "position": 0}},
                            {"device_id": "light_lr_ceiling", "update": {"power": "on", "brightness": 30}}
                        ]
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_19",
        instruction="""
        You just bought a new Bosch "Series 6 Silence" Dishwasher for the Kitchen.
        • You want to give it the id "dishwasher_kt2", firmware 1.0.0, and the same state-params as the other dishwasher, can be referred as Kitchen Dishwasher 2. The power must default to OFF.
        • You want to attach it to the Kitchen room record.
        • You want to schedule it to switch ON and start the "eco" cycle every Monday at 02:00 starting from 2025-07-28.
        • You want to create a monthly reminder to "Replace Dishwasher Salt" on the 1st of every month at 09:00 with an email notification with id "rem_dishwasher_salt" and priority "normal" and status "active".
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={
                    "entity_type": "devices",
                    "entity_id": "dishwasher_kt"
                }
            ),
            Action(
                name="upsert_device",
                kwargs={
                    "device": {
                        "id": "dishwasher_kt2",
                        "type": "dishwasher",
                        "location": "Kitchen",
                        "vendor": "Bosch",
                        "model": "Series 6 Silence",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "cycle", "time_remaining_min", "door"],
                        "state": {
                            "power": "off",
                            "cycle": "eco",
                            "time_remaining_min": 0,
                            "door": "closed",
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="add_device_to_room",
                kwargs={
                    "room_id": "kitchen",
                    "device_id": "dishwasher_kt2"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "dishwasher_kt2",
                    "update": { "power": "on", "cycle": "eco" },
                    "schedule_at": "2025-07-28T02:00:00",
                    "rrule": "FREQ=WEEKLY;BYDAY=MO"
                }
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_dishwasher_salt",
                        "target": { "type": "note", "text": "Replace Dishwasher Salt" },
                        "trigger": {
                            "rrule": "FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0"
                        },
                        "actions": [ { "type": "notify", "channel": "email" } ],
                        "meta": { "priority": "normal" },
                        "status": "active",
                    }
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_20",
        instruction="""
        Grandma Linda Johnson is visiting from 2025-07-26 to 2025-07-30. You must do the following to prepare:
        1. You want to verify (read) her member record.
        2. You want to add a new scene called "Grandma Welcome" (id "scene_grandma_welcome") that, at run-time:
           • opens the Master-Bedroom curtain to 100 and turns ON the night lamp at brightness 25,
           • sets the Central Heater to heat mode 23 °C,
           • turns OFF the Central AC.
           • The propose is set Comfort settings for Grandma's stay.
        3. You want to schedule that scene to run at 14:00 on 2025-07-26 and again at 08:00 every morning from 2025-07-27 to 2025-07-30.
        4. You want to create a custom list "grandma_visit_prep" with id "list_grandma_visit_prep" and with the tag "guest".
        5. You want to add three items to it: "Fresh Flowers" x 1, "Extra Towels" x 3, "Chamomile Tea" x 2.
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={
                    "entity_type": "members",
                    "entity_id": "linda_johnson"
                }
            ),
            Action(
                name="upsert_scene",
                kwargs={
                    "scene": {
                        "id": "scene_grandma_welcome",


                        "actions": [
                            { "device_id": "curtain_br",
                              "update": { "power": "on", "position": 100 } },
                            { "device_id": "lamp_br_night",
                              "update": { "power": "on", "brightness": 25 } },
                            { "device_id": "heater_home",
                              "update": { "power": "on", "mode": "heat", "setpoint_c": 23 } },
                            { "device_id": "ac_home",
                              "update": { "power": "off" } }
                        ],
                        "scheduled_runs": [
                            "2025-07-26T14:00:00",
                            "2025-07-27T08:00:00",
                            "2025-07-28T08:00:00",
                            "2025-07-29T08:00:00",
                            "2025-07-30T08:00:00"
                        ]
                    }
                }
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_grandma_visit_prep",
                        "name": "grandma_visit_prep",
                        "tags": ["guest"],
                        "items": []
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_grandma_visit_prep",
                    "item": { "item": "Fresh Flowers", "quantity": 1 },
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_grandma_visit_prep",
                    "item": { "item": "Extra Towels", "quantity": 3 },
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_grandma_visit_prep",
                    "item": { "item": "Chamomile Tea", "quantity": 2 },
                    "action": "add"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_21",
        instruction="""
        It's Sunday evening (2025-07-29). You want to prepare next week's grocery workflow.
        • You want to look up every custom list tagged "groceries".
        • You want to make a brand-new list "next_week_groceries" (id "list_groceries_next"), cloning today's weekend list items. However, you must increment the quantity of anything already below 2 up to exactly 2.
        • You want to add a reminder for "Grocery Pickup" for Saturday (2025-07-29) at 09:00 via mobile-push.
        • For budget tracking, you want to immediately output (get) the new list object.
        """,
        actions=[
            Action(
                name="query_entities",
                kwargs={
                    "entity_type": "custom_lists",
                    "filters": { "tags": ["groceries"] }
                }
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_groceries_next",
                        "name": "next_week_groceries",
                        "items": [
                                {
                                    "item": "Chicken Breast",
                                    "quantity": 2
                                },
                                {
                                    "item": "Eggs",
                                    "quantity": 2
                                }
                        ]
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_groceries_next",
                    "item": { "item": "Olive Oil", "quantity": 2 },
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_groceries_next",
                    "item": { "item": "Apples", "quantity": 2 },
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_groceries_next",
                    "item": { "item": "Cheese", "quantity": 2 },
                    "action": "add"
                }
            ),

            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_grocery_pickup_next",

                        "target": { "type": "entity", "entity_type": "list",
                                    "entity_id": "list_groceries_next" },
                        "trigger": {
                            "datetime": "2025-07-29T09:00:00"
                        },
                        "actions": [ { "type": "notify", "channel": "mobile_push" } ],
                        "meta": { "priority": "normal" },
                        "status": "scheduled",
                    }
                }
            ),
            Action(
                name="get_entity",
                kwargs={
                    "entity_type": "custom_lists",
                    "entity_id": "list_groceries_next"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_22",
        instruction="""
        Today is 2025-07-29. Emily Smith's hospital shift ends tomorrow (Mon 2025-07-30) at 15:00. You want to set up the house for her return.
        • At 14:55, you want to turn the **heater_home** on with mode "heat" and setpoint_c 22 °C.
        • At 14:55, you want to switch the **light_lr_ceiling** on with brightness 70 and color {{"kelvin": 3500}}.
        • At 15:00, you want to power the **dishwasher_kt** on and start the "auto" cycle.
        • At 18:00, you want to turn the **heater_home** off and start the **ac_home** cooling with setpoint_c 23 and fan_speed "auto".
        • You want to add 2 x "Salmon Fillet" to the existing list "weekend_groceries", id: (list_groceries_weekend).
        • You want to create a one-time reminder for Emily at 14:50 tomorrow: "Time to stretch before heading home!", with id "rem_stretch_emily".
        """,
        actions=[
            Action(
                name="query_entities",
                kwargs={"entity_type": "members",
                        "filters": {"first_name": "Emily", "last_name": "Smith"}}
            ),
            Action(
                name="modify_device_state_timer",
                kwargs={"device_id": "heater_home",
                        "schedule_end": "2025-07-30T18:00:00",
                        "update": {"power": "on", "mode": "heat", "setpoint_c": 22},
                        "schedule_at": "2025-07-30T14:55:00"}
            ),
            Action(
                name="modify_device_state",
                kwargs={"device_id": "light_lr_ceiling",
                        "update": {"power": "on", "brightness": 70,
                                   "color": {"kelvin": 3500}},
                        "schedule_at": "2025-07-30T14:55:00"}
            ),
            Action(
                name="modify_device_state",
                kwargs={"device_id": "dishwasher_kt",
                        "update": {"power": "on", "cycle": "auto"},
                        "schedule_at": "2025-07-30T15:00:00"}
            ),
            Action(
                name="modify_device_state",
                kwargs={"device_id": "ac_home",
                        "update": {"power": "on", "mode": "cool",
                                   "setpoint_c": 23, "fan_speed": "auto"},
                        "schedule_at": "2025-07-30T18:00:00"}
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_groceries_weekend",

                        "items": [
                            {"item": "Chicken Breast", "quantity": 2},
                            {"item": "Apples", "quantity": 1},
                            {"item": "Olive Oil", "quantity": 1},
                            {"item": "Cheese", "quantity": 1},
                            {"item": "Eggs", "quantity": 2},
                            {"item": "Salmon Fillet", "quantity": 2}
                        ]
                    }
                }
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_stretch_emily",
                        "member_id": "emily_smith",
                        "target": {"type": "note", "text": "Time to stretch before heading home!"},
                        "trigger": {"datetime": "2025-07-30T14:50:00"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active",
                        "meta": { "priority": "normal" },
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_23",
        instruction="""
        You want to install a new side-lamp beside the sofa.
        • You want its ID to be: lamp_lr_side.
        • It is a light of type: light, from vendor Ikea, model "Tradfri Floor Lamp v2", with firmware 2.0.0, and it is adjustable (power, brightness, color_temperature).
        You want to place it in the Living Room.
        Then, you want to build a "Saturday Movie Night" plan:
        1. You want to add lamp_lr_side to scene_movie_time so that when the scene runs at 19:00, the lamp turns on with brightness 35.
        2. You want to run scene_movie_time.
        3. You want to set the **ac_home** fan_speed to "low".
        4. You want to put "Popcorn (3 bags)" on the shopping list.
        """,
        actions=[
            Action(
                name="upsert_device",
                kwargs={
                    "device": {
                        "id": "lamp_lr_side",
                        "type": "light",
                        "location": "Living Room",
                        "vendor": "Ikea",
                        "model": "Tradfri Floor Lamp v2",
                        "firmware_version": "2.0.0",
                        "state_params": ["power", "brightness", "color_temperature"],
                        "state": {"power": "off", "brightness": 0,
                                  "color_temperature": 3000}
                    }
                }
            ),
            Action(
                name="upsert_scene",
                kwargs={
                    "scene": {
                        "id": "scene_movie_time",
                        "actions": [
                            { "device_id": "curtain_lr",
                            "update": { "power": "on", "position": 0 } },
                            { "device_id": "light_lr_floor",
                            "update": { "power": "on", "brightness": 20 } },
                            { "device_id": "light_lr_ceiling",
                            "update": { "power": "off" } },
                            { "device_id": "ac_home",
                            "update": { "power": "on", "fan_speed": "low" } },
                            {"device_id": "lamp_lr_side",
                             "update": {"power": "on", "brightness": 35}}
                        ]
                    }
                }
            ),
            Action(
                name="run_scene",
                kwargs={
                    "scene_id": "scene_movie_time"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "ac_home",
                    "update": {"fan_speed": "low"}
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_shopping",
                        "item": {"item": "Popcorn", "quantity": 3},
                        "action": "add"}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_24",
        instruction="""
        The family is leaving for vacation from 2025-08-10 to 2025-08-18. You want to create a "Holiday Mode" scene (id scene_holiday_mode).
        • You want to turn **heater_home** off.
        • You want to set **ac_home** to eco-cool at 26 °C with fan_speed "auto".
        • You want to switch **light_lr_ceiling** off and program it to randomly turn on at 20:00 (brightness 30, kelvin 2700) and off again at 23:00 every night during the vacation.
        You also need to add a reminder with id "rem_water_valve" for John Smith at 2025-08-09T21:00 to "Shut main water valve".
        Finally, you want to create a packing list called "vacation_packing" with id "list_vacation_packing" and with 1 x "Sunscreen", "Chargers", and "Passports".
        """,
        actions=[
            Action(
                name="upsert_scene",
                kwargs={
                    "scene": {
                        "id": "scene_holiday_mode",
                        "actions": [
                            {"device_id": "heater_home",
                             "update": {"power": "off"}},
                            {"device_id": "ac_home",
                             "update": {"power": "on", "mode": "cool",
                                        "setpoint_c": 26, "fan_speed": "auto"}},
                            {"device_id": "light_lr_ceiling",
                             "update": {"power": "off"}}
                        ]
                    }
                }
            ),
            Action(
                name="modify_device_state_timer",
                kwargs={"device_id": "light_lr_ceiling",
                        "schedule_end": "2025-08-10T23:00:00",
                        "update": {"power": "on", "brightness": 30,
                                   "color": {"kelvin": 2700}},
                        "schedule_at": "2025-08-10T20:00:00",
                        "rrule": "FREQ=DAILY;UNTIL=20250818T230000Z"}
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_water_valve",
                        "member_id": "john_smith",
                        "target": {"type": "note", "text": "Shut main water valve"},
                        "trigger": {"datetime": "2025-08-09T21:00:00"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active",
                        "meta": { "priority": "high" },
                    }
                }
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_vacation_packing",
                        "name": "vacation_packing",
                        "items": [
                            {"item": "Sunscreen", "quantity": 1},
                            {"item": "Chargers", "quantity": 1},
                            {"item": "Passports", "quantity": 1}
                        ]
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_25",
        instruction="""
        You want to create Ethan's "Bedtime Wind-Down" routine.
        • At 19:30, you want to close the **curtain_be** (position 0) and dim the **light_be_ceiling** to brightness 25, hue 260, and sat 20.
        • At 19:40, you want to switch the **lamp_be_bedside** on with brightness 5 and hue 30.
        • At 20:00, you want to turn both lights off.
        You also want to add a new reminder every night at 19:25: "Brush teeth!" for Ethan.
        Finally, you want to update the to-do list "todo" by appending "Lay out school clothes".
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "custom_lists", "entity_id": "list_todo"}
            ),
            Action(
                name="modify_device_state",
                kwargs={"device_id": "curtain_be",
                        "update": {"position": 0},
                        "schedule_at": "2025-07-29T19:30:00",
                        "rrule": "FREQ=DAILY"}
            ),
            Action(
                name="modify_device_state_timer",
                kwargs={"device_id": "light_be_ceiling",
                        "schedule_end": "2025-07-29T20:00:00",
                        "update": {"power": "on", "brightness": 25,
                                   "color": {"hue": 260, "saturation": 20}},
                        "schedule_at": "2025-07-29T19:30:00",
                        "rrule": "FREQ=DAILY"}
            ),
            Action(
                name="modify_device_state_timer",
                kwargs={"device_id": "lamp_be_bedside",
                        "schedule_end": "2025-07-29T20:00:00",
                        "update": {"power": "on", "brightness": 5,
                                   "color": {"hue": 30}},
                        "schedule_at": "2025-07-29T19:40:00",
                        "rrule": "FREQ=DAILY"}
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_brush_teeth_ethan",
                        "member_id": "ethan_smith",
                        "target": {"type": "note", "text": "Brush teeth!"},
                        "trigger": {"rrule": "FREQ=DAILY;BYHOUR=19;BYMINUTE=25"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active",
                        "meta": { "priority": "normal" },
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={"list_id": "list_todo",
                        "item": {"item": "Lay out school clothes", "quantity": 1},
                        "action": "add"}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_26",
        instruction="""
        You want to add a kitchen air-purifier (id purifier_kt). It is from vendor Coway, model AP-1512HHS, firmware 1.0.0, and is adjustable (power, fan_speed, eco_mode).
        You want to locate it in the Kitchen.
        Every day at 07:00, starting today 2025-07-29, you want to read the **sensor_lr_air_quality**. Regardless of the value, you want to run purifier_kt at fan_speed "high" for 30 minutes, and then switch it to eco_mode.
        You also need to append "Replacement filter (Coway 1512)" to the reading_list, that already has Clean Code and Designing Data-Intensive Applications both quantity 1, remember the tag "books".
        """,
        actions=[
            Action(
                name="upsert_device",
                kwargs={
                    "device": {
                        "id": "purifier_kt",
                        "type": "air_purifier",

                        "location": "Kitchen",
                        "vendor": "Coway",
                        "model": "AP-1512HHS",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "fan_speed", "eco_mode"],
                        "state": {"power": "off", "fan_speed": "low",
                                  "eco_mode": False},
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="query_entities",
                kwargs={"entity_type": "sensors",
                        "filters": {"id": "sensor_lr_air_quality"}}
            ),
            Action(
                name="modify_device_state",
                kwargs={"device_id": "purifier_kt",
                        "update": {"power": "on", "fan_speed": "high"},
                        "schedule_at": "2025-07-29T07:00:00",
                        "rrule": "FREQ=DAILY"}
            ),
            Action(
                name="modify_device_state",
                kwargs={"device_id": "purifier_kt",
                        "update": {"fan_speed": "low", "eco_mode": True},
                        "schedule_at": "2025-07-29T07:30:00",
                        "rrule": "FREQ=DAILY"}
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_reading",

                        "tags": ["books"],
                        "items": [
                            {"item": "Clean Code", "quantity": 1},
                            {"item": "Designing Data-Intensive Applications", "quantity": 1},
                            {"item": "Replacement filter (Coway 1512)", "quantity": 1}
                        ]
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_27",
        instruction="""
        Today is 2025-07-15 08:00. John Smith is working from home today and you want to set up an optimal work environment for him.
        1. First, you want to check the current temperature from the Living Room thermometer sensor.
        2. If the temperature is above 24°C, you want to turn on the Central AC with mode=cool, setpoint_c=22, fan_speed=medium.
        3. You want to check the current air quality from the Living Room air quality sensor.
        4. If CO2 levels are above 600 ppm, you want to open the Living Room curtain to position 100 for ventilation.
        5. You want to set up John's work lighting: turn on the Living Room ceiling light with brightness=80, color kelvin=5000.
        6. You want to create a new custom list called "John's Work Setup" (id "list_john_work") tagged "work" and "productivity".
        7. You want to add these items to the work list: "Ergonomic mouse pad" x1, "Blue light glasses" x1, "Desk organizer" x1.
        8. You want to schedule the dishwasher to run at 10:00 today with power=on, cycle=eco to minimize noise during work.
        9. You want to create a daily reminder at 11:30 called "Take work break" with a mobile_push notification.
        10. At 17:00 today, you want to automatically dim the Living Room ceiling light to brightness=50 and close the curtain to position=20.
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "sensors", "entity_id": "sensor_lr_thermometer"}
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "ac_home",
                    "update": {"power": "on", "mode": "cool", "setpoint_c": 22, "fan_speed": "medium"},
                }
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "sensors", "entity_id": "sensor_lr_air_quality"}
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "curtain_lr",
                    "update": {"power": "on", "position": 100},
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "light_lr_ceiling",
                    "update": {"power": "on", "brightness": 80, "color": {"kelvin": 5000}},
                }
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_john_work",
                        "name": "John's Work Setup",
                        "tags": ["work", "productivity"],
                        "items": []
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_john_work",
                    "item": {"item": "Ergonomic mouse pad", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_john_work",
                    "item": {"item": "Blue light glasses", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_john_work",
                    "item": {"item": "Desk organizer", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "dishwasher_kt",
                    "update": {"power": "on", "cycle": "eco"},
                    "schedule_at": "2025-07-15T10:00:00"
                }
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_work_break",
                        "target": {"type": "note", "text": "Take work break"},
                        "trigger": {"rrule": "FREQ=DAILY;BYHOUR=11;BYMINUTE=30"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active",
                        "meta": {"priority": "normal"}
                    }
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "light_lr_ceiling",
                    "update": {"power": "on", "brightness": 50},
                    "schedule_at": "2025-07-15T17:00:00"
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "curtain_lr",
                    "update": {"power": "on", "position": 20},
                    "schedule_at": "2025-07-15T17:00:00"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_28",
        instruction="""
        It's 2025-07-16 19:30. Emily Smith is returning from her hospital shift and you want to set up a relaxing evening routine for her.
        1. You want to check Emily's member profile to confirm her work schedule and preferences.
        2. You want to read the bedroom smoke detector to ensure the battery level is above 85%.
        3. You want to create a "Post-Shift Relaxation" scene (id "scene_emily_relax") that includes:
           - Master bedroom ceiling light on with brightness=40, hue=270, saturation=30 (purple ambiance)
           - Master bedroom night lamp on with brightness=20, hue=30 (warm orange)
           - Master bedroom curtain closed to position=0
           - Central heater on with mode=heat, setpoint_c=23
        4. You want to schedule this scene to run at 20:00 today.
        5. You want to update Emily's existing diet plan list by adding "Chamomile tea" x2 and "Dark chocolate" x1.
        6. You want to create a weekly reminder every Wednesday at 19:00 called "Prep relaxation bath" with mobile_push.
        7. At 21:30 tonight, you want to automatically turn off the master bedroom ceiling light and dim the night lamp to brightness=10.
        8. You want to add "Lavender essential oil" x1 to the shopping list for aromatherapy.
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "members", "entity_id": "emily_smith"}
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "sensors", "entity_id": "sensor_bed_smoke"}
            ),
            Action(
                name="upsert_scene",
                kwargs={
                    "scene": {
                        "id": "scene_emily_relax",
                        "actions": [
                            {"device_id": "light_br_ceiling",
                             "update": {"power": "on", "brightness": 40, "color": {"hue": 270, "saturation": 30}}},
                            {"device_id": "lamp_br_night",
                             "update": {"power": "on", "brightness": 20, "color": {"hue": 30}}},
                            {"device_id": "curtain_br",
                             "update": {"power": "on", "position": 0}},
                            {"device_id": "heater_home",
                             "update": {"power": "on", "mode": "heat", "setpoint_c": 23}}
                        ],
                        "scheduled_runs": ["2025-07-16T20:00:00"]
                    }
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "light_br_ceiling",
                    "update": {"power": "off"},
                    "schedule_at": "2025-07-16T21:30:00"
                }
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "custom_lists", "entity_id": "list_diet_plan"}
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_diet_plan",
                    "item": {"item": "Chamomile tea", "quantity": 2},
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_diet_plan",
                    "item": {"item": "Dark chocolate", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_emily_bath",
                        "target": {"type": "note", "text": "Prepare relaxing bath with oils"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=WE;BYHOUR=19;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active",
                        "meta": {"priority": "normal"}
                    }
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "lamp_br_night",
                    "update": {"brightness": 10},
                    "schedule_at": "2025-07-16T21:30:00"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_shopping",
                    "item": {"item": "Lavender essential oil", "quantity": 1},
                    "action": "add"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_29",
        instruction="""
        Today is 2025-07-25 14:00. Olivia Smith has a playdate with Mia Martinez at 16:00, and you want to prepare.
        1. You want to check Olivia's member profile for her room assignment and preferences.
        2. You want to check Mia's member profile for pickup requirements and allergies.
        3. You must verify that both girls have peanut allergies and ensure no peanut products are on any grocery lists.
        4. You want to create a "Playdate Setup" scene (id "scene_playdate") that includes the West Bedroom ceiling light at power on and brightness=70 and opens the West Bedroom curtain to position=100.
        5. You want to schedule the dishwasher to run at 15:30 with cycle=quiet to minimize noise during the playdate.
        6. You want to create a custom list "Playdate Snacks" (id "list_playdate_snacks") tagged "kids" and "snacks".
        7. You want to add safe snacks to the list: "Apple slices" x2, "Cheese sticks" x4, "Juice boxes" x2.
        8. You want to set a reminder at 17:30 today to "Call Ana Martinez for Mia pickup" with mobile_push and high priority.
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "members"}
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "custom_lists"}
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "devices"}
            ),
            Action(
                name="upsert_scene",
                kwargs={
                    "scene": {
                        "id": "scene_playdate",
                        "actions": [
                            {"device_id": "light_bw_ceiling",
                             "update": {"power": "on", "brightness": 70}},
                            {"device_id": "curtain_bw",
                             "update": {"power": "on", "position": 100}}
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "dishwasher_kt",
                    "update": {"power": "on", "cycle": "quiet"},
                    "schedule_at": "2025-07-25T15:30:00"
                }
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_playdate_snacks",
                        "name": "Playdate Snacks",
                        "tags": ["kids", "snacks"],
                        "items": []
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_playdate_snacks",
                    "item": {"item": "Apple slices", "quantity": 2},
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_playdate_snacks",
                    "item": {"item": "Cheese sticks", "quantity": 4},
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_playdate_snacks",
                    "item": {"item": "Juice boxes", "quantity": 2},
                    "action": "add"
                }
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_mia_pickup",
                        "target": {"type": "note", "text": "Call Ana Martinez for Mia pickup"},
                        "trigger": {"datetime": "2025-07-25T17:30:00"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active",
                        "meta": {"priority": "high"}
                    }
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_30",
        instruction="""
        Today is 2025-07-18 09:00. The family is preparing for David Lee and Sarah Lee's Sunday evening visit at 18:30. You want to get ready.
        1. You want to check David Lee's member profile for his vehicle type and parking needs.
        2. You want to check Sarah Lee's member profile for her dietary preferences and what she brings.
        3. You want to read the front door contact sensor and hallway motion sensor to ensure security systems are working.
        4. You want to create a "Sunday Dinner Prep" scene (id "scene_sunday_dinner"), described as "Warm and welcoming atmosphere for dinner guests", that includes:
           - Living room ceiling light on with brightness=75, kelvin=3000 (warm lighting)
           - Living room floor lamp on with brightness=50
           - Living room curtain open to position=80
           - Central AC on with mode=cool, setpoint_c=24, fan_speed=auto
        5. You want to schedule this scene to run at 17:30 today.
        6. You want to update the weekend groceries list by adding "Vegan cheese" x1 and "Sourdough bread" x1 for Sarah.
        7. You want to create a custom list "Sunday Dinner Menu" (id "list_sunday_menu") tagged "dinner" and "guests".
        8. You want to add menu items: "Grilled salmon" x4, "Roasted vegetables" x1, "Rice pilaf" x1, "Chocolate dessert" x1.
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "members", "entity_id": "david_lee"}
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "members", "entity_id": "sarah_lee"}
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "sensors", "entity_id": "sensor_front_door"}
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "sensors", "entity_id": "sensor_hall_motion"}
            ),
            Action(
                name="upsert_scene",
                kwargs={
                    "scene": {
                        "id": "scene_sunday_dinner",


                        "actions": [
                            {"device_id": "light_lr_ceiling",
                             "update": {"power": "on", "brightness": 75, "color": {"kelvin": 3000}}},
                            {"device_id": "light_lr_floor",
                             "update": {"power": "on", "brightness": 50}},
                            {"device_id": "curtain_lr",
                             "update": {"power": "on", "position": 80}},
                            {"device_id": "ac_home",
                             "update": {"power": "on", "mode": "cool", "setpoint_c": 24, "fan_speed": "auto"}}
                        ],
                        "scheduled_runs": ["2025-07-18T17:30:00"]
                    }
                }
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "custom_lists", "entity_id": "list_groceries_weekend"}
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_groceries_weekend",
                    "item": {"item": "Vegan cheese", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_groceries_weekend",
                    "item": {"item": "Sourdough bread", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_sunday_menu",

                        "tags": ["dinner", "guests"],
                        "items": []
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_sunday_menu",
                    "item": {"item": "Grilled salmon", "quantity": 4},
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_sunday_menu",
                    "item": {"item": "Roasted vegetables", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_sunday_menu",
                    "item": {"item": "Rice pilaf", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_sunday_menu",
                    "item": {"item": "Chocolate dessert", "quantity": 1},
                    "action": "add"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_31",
        instruction="""
        Today is 2025-07-19 07:00. You want to help Ethan Smith with his morning piano practice routine.
        1. You want to check Ethan's member profile for his room assignment, schedule, and music preferences.
        2. You want to read the current states of the East Bedroom ceiling light and bedside lamp.
        3. You want to create a "Piano Practice" scene (id "scene_piano_practice") that includes:
           - East bedroom ceiling light on with brightness=90, hue=60, saturation=20 (bright yellow-green for focus)
           - East bedroom bedside lamp off to avoid glare
           - East bedroom curtain open to position=100 for natural light
           - Central heater on with mode=heat, setpoint_c=21 (cooler for concentration)
        4. You want to schedule this scene to run on 2025-07-19 at 07:30 (after Ethan wakes up at 07:15).
        5. You want to create a custom list "Ethan's Music Goals" (id "list_ethan_music") tagged "education" and "music".
        6. You want to add practice goals: "Scale exercises" x1, "Beginner songs" x2, "Rhythm practice" x1.
        7. You want to set a daily reminder at 07:25: "Time for piano practice!" with mobile_push.
        8. At 08:00 daily, you want to automatically turn off the East bedroom ceiling light and close the curtain to position=50.
        9. You want to update the todo list by adding "Schedule Ethan's piano lesson" x1.
        """,
        actions=[
            Action(
                name="get_entity",
                kwargs={"entity_type": "members", "entity_id": "ethan_smith"}
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "devices"}
            ),
            Action(
                name="upsert_scene",
                kwargs={
                    "scene": {
                        "id": "scene_piano_practice",
                        "actions": [
                            {"device_id": "light_be_ceiling",
                             "update": {"power": "on", "brightness": 90, "color": {"hue": 60, "saturation": 20}}},
                            {"device_id": "lamp_be_bedside",
                             "update": {"power": "off"}},
                            {"device_id": "curtain_be",
                             "update": {"power": "on", "position": 100}},
                            {"device_id": "heater_home",
                             "update": {"power": "on", "mode": "heat", "setpoint_c": 21}}
                        ],
                        "scheduled_runs": ["2025-07-19T07:30"]
                    }
                }
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_ethan_music",

                        "tags": ["education", "music"],
                        "items": []
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_ethan_music",
                    "item": {"item": "Scale exercises", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_ethan_music",
                    "item": {"item": "Beginner songs", "quantity": 2},
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_ethan_music",
                    "item": {"item": "Rhythm practice", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="upsert_reminder",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_ethan_piano",
                        "target": {"type": "note", "text": "Time for piano practice!"},
                        "trigger": {"rrule": "FREQ=DAILY;BYHOUR=7;BYMINUTE=25"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "status": "active",
                        "meta": {"priority": "normal"}
                    }
                }
            ),
            Action(
                name="modify_device_state",
                kwargs={
                    "device_id": "curtain_be",
                    "update": {"power": "on", "position": 50},
                    "schedule_at": "2025-07-20T08:00:00",
                    "rrule": "FREQ=DAILY"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_todo",
                    "item": {"item": "Schedule Ethan's piano lesson", "quantity": 1},
                    "action": "add"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_32",
        instruction="""
        Today is 2025-07-20 15:00. Michael Brown is arriving for a weekend visit and you want to prepare guest accommodations.
        1. You want to check Michael Brown's member profile for his visit preferences, allergies, and hobbies.
        2. You want to read all bedroom devices to determine the best guest room setup.
        3. You want to check the current status of all existing reminders to avoid conflicts.
        4. You want to create a "Guest Welcome" scene (id "scene_guest_welcome") to be sure a Comfortable and welcoming environment for Michael's visit that includes:
           - Master bedroom ceiling light on with brightness=60, hue=45, saturation=40 (warm amber)
           - Master bedroom night lamp on with brightness=25
           - Master bedroom curtain open to position=90
           - Central AC on with mode=cool, setpoint_c=25, fan_speed=low (comfortable for guest)
        5. You want to schedule this scene to run at 16:30 today (30 minutes before expected arrival).
        6. You want to create a custom list "Guest Comfort Items" (id "list_guest_comfort") tagged "guest" and "hospitality".
        7. You want to add comfort items: "Extra towels" x3, "Board games" x2; and if he is allergic to cats, you want to add "Cat-free bedding" x1.
        8. You want to update the weekend groceries list by adding 1 quantity of his favorite food.
        """,
        actions=[
            Action(
                name="query_entities",
                kwargs={"entity_type": "members", "filters": {"first_name": "Michael", "last_name": "Brown"}}
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "rooms"}
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "reminders"}
            ),
            Action(
                name="upsert_scene",
                kwargs={
                    "scene": {
                        "id": "scene_guest_welcome",


                        "actions": [
                            {"device_id": "light_br_ceiling",
                             "update": {"power": "on", "brightness": 60, "color": {"hue": 45, "saturation": 40}}},
                            {"device_id": "lamp_br_night",
                             "update": {"power": "on", "brightness": 25}},
                            {"device_id": "curtain_br",
                             "update": {"power": "on", "position": 90}},
                            {"device_id": "ac_home",
                             "update": {"power": "on", "mode": "cool", "setpoint_c": 25, "fan_speed": "low"}}
                        ],
                        "scheduled_runs": ["2025-07-20T16:30:00"]
                    }
                }
            ),
            Action(
                name="upsert_custom_list",
                kwargs={
                    "custom_list": {
                        "list_id": "list_guest_comfort",

                        "tags": ["guest", "hospitality"],
                        "items": []
                    }
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_guest_comfort",
                    "item": {"item": "Extra towels", "quantity": 3},
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_guest_comfort",
                    "item": {"item": "Board games", "quantity": 2},
                    "action": "add"
                }
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_guest_comfort",
                    "item": {"item": "Cat-free bedding", "quantity": 1},
                    "action": "add"
                }
            ),
            Action(
                name="get_entity",
                kwargs={"entity_type": "custom_lists",}
            ),
            Action(
                name="modify_custom_list_item",
                kwargs={
                    "list_id": "list_groceries_weekend",
                    "item": {"item": "Thai green curry", "quantity": 1},
                    "action": "add"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_33",
        instruction="""
        Summer is hot and you want to swap the default morning routine for July only.
        • You want to empty the scheduled_runs array of **scene_good_morning**.
        • You want to create a scene **scene_summer_morning**, to get a Cool-summer wake-up routine, that:
            - opens curtain_lr, curtain_br, curtain_bw, curtain_be (position 100)
            - turns heater_home power:off
            - turns ac_home power:on, mode:cool, setpoint_c:23, fan_speed:low
            - turns light_lr_ceiling power:on, brightness:50, color:{kelvin:5000}
          You want this scheduled daily at 06:45 in July only (`scheduled_runs=["RRULE:FREQ=DAILY;BYMONTH=7;BYHOUR=6;BYMINUTE=45"]`).
        You want to run the new scene immediately once.
        """,
        actions=[
            Action(name="query_entities",
                   kwargs={"entity_type": "scenes",
                           "filters": {"id": "scene_good_morning"}}),
            Action(name="upsert_scene",
                   kwargs={"scene": {
                       "id": "scene_good_morning",
                       "scheduled_runs": []
                   }}),
            Action(name="query_entities",
                   kwargs={"entity_type": "rooms",
                           "filters": {"id": "living_room"}}),
            Action(name="upsert_scene",
                   kwargs={"scene": {
                       "id": "scene_summer_morning",


                       "actions": [
                           {"device_id": "curtain_lr",
                            "update": {"power": "on", "position": 100}},
                           {"device_id": "curtain_br",
                            "update": {"power": "on", "position": 100}},
                           {"device_id": "curtain_bw",
                            "update": {"power": "on", "position": 100}},
                           {"device_id": "curtain_be",
                            "update": {"power": "on", "position": 100}},
                           {"device_id": "heater_home",
                            "update": {"power": "off"}},
                           {"device_id": "ac_home",
                            "update": {"power": "on", "mode": "cool",
                                       "setpoint_c": 23,
                                       "fan_speed": "low"}},
                           {"device_id": "light_lr_ceiling",
                            "update": {"power": "on", "brightness": 50,
                                       "color": {"kelvin": 5000}}}
                       ],
                       "scheduled_runs": [
                           "RRULE:FREQ=DAILY;BYMONTH=7;BYHOUR=6;BYMINUTE=45"
                       ]
                   }}),
            Action(name="run_scene",
                   kwargs={"scene_id": "scene_summer_morning"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_34",
        instruction="""
        You want to turn on the front door camera and back door camera recording now and turn on stream online.
        • You also want to create two reminders:
            - **rem_cam_front_batt**: "Front Camera - check battery" monthly on the 1st at 09:00 (push)
            - **rem_cam_back_batt** : "Back Camera - check battery" monthly on the 1st at 09:05 (push).
        • For that, you intalled that two cameras, and localed Front door and Back door respectively, as they are new batery still 100%
        """,
        actions=[
            Action(name="get_entity",
                   kwargs={"entity_type": "sensors"}),
            Action(
                name="modify_sensor_state",
                kwargs={
                    "sensor_id": "camera_front_door",
                    "update": {"stream_online": True, "recording": True}
                }
            ),
            Action(
                name="modify_sensor_state",
                kwargs={
                    "sensor_id": "camera_back_door",
                    "update": {"stream_online": True, "recording": True}
                }
            ),
            Action(name="upsert_reminder",
                   kwargs={"reminder": {
                       "reminder_id": "rem_cam_front_batt",

                       "target": {"type": "note",
                                  "text": "Front Camera - check battery"},
                       "trigger": {
                           "rrule": "FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0"},
                       "actions": [{"type": "notify",
                                    "channel": "mobile_push"}],
                       "meta": {"priority": "normal"},
                       "status": "active"
                   }}),
            Action(name="upsert_reminder",
                   kwargs={"reminder": {
                       "reminder_id": "rem_cam_back_batt",

                       "target": {"type": "note",
                                  "text": "Back Camera - check battery"},
                       "trigger": {
                           "rrule": "FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=5"},
                       "actions": [{"type": "notify",
                                    "channel": "mobile_push"}],
                       "meta": {"priority": "normal"},
                       "status": "active"
                   }})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_35",
        instruction="""
        You are planning a camping trip for 2025-07-18 and need to set up packing.
        • You want to create a new custom list **list_camping_packing** ("Camping Packing List", with tags camping+travel). The items are:
            - Tent x1, Sleeping Bag x4, Flashlight x3, Marshmallows x2.
            (You want to set the current time as: 2025-07-29T14:40:00)
        • You also need to add 2 x "Bug Spray" to the list.
        • You want to create a new reminder with id **rem_camping_packing_check** named "Camping packing check" that targets that list on 2025-07-17 at 20:00 (push) with normal priority.
        • You also want to create another new reminder with id **rem_camping_car_pack** with the note "Pack car" for 2025-07-18 at 07:00 (push) and with normal priority.
        """,
        actions=[
            Action(name="upsert_custom_list",
                   kwargs={"custom_list": {
                       "list_id": "list_camping_packing",
                       "tags": ["camping", "travel"],
                       "items": [
                           {"item": "Tent", "quantity": 1},
                           {"item": "Sleeping Bag", "quantity": 4},
                           {"item": "Flashlight", "quantity": 3},
                           {"item": "Marshmallows", "quantity": 2}
                       ]
                   }}),
            Action(name="modify_custom_list_item",
                   kwargs={"list_id": "list_camping_packing",
                           "item": {"item": "Bug Spray", "quantity": 2},
                           "action": "add"}),
            Action(name="upsert_reminder",
                   kwargs={"reminder": {
                       "reminder_id": "rem_camping_packing_check",

                       "target": {"type": "entity",
                                  "entity_type": "list",
                                  "entity_id": "list_camping_packing"},
                       "trigger": {
                           "datetime": "2025-07-17T20:00:00"},
                       "actions": [{"type": "notify",
                                    "channel": "mobile_push"}],
                       "status": "active",
                       "meta": {"priority": "normal"}
                   }}),
            Action(name="upsert_reminder",
                   kwargs={"reminder": {
                       "reminder_id": "rem_camping_car_pack",

                       "target": {"type": "note",
                                  "text": "Pack car"},
                       "trigger": {
                           "datetime": "2025-07-18T07:00:00"},
                       "actions": [{"type": "notify",
                                    "channel": "mobile_push"}],
                       "status": "active",
                       "meta": {"priority": "normal"}
                   }}),
            Action(name="query_entities",
                   kwargs={"entity_type": "custom_lists",
                           "filters": {"list_id": "list_camping_packing"}})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_36",
        instruction="""
        You want to automate Ethan's Wednesday piano lesson routine.
        • You want to create a new reminder with id **rem_ethan_piano_practice** for "Leave for piano lesson" on Wednesdays at 15:30 (repeating weekly), via push, with high priority.
        • On every lesson day, starting 2025-07-25, you want Ethan's bedside lamp to do the following:
            - At 15:25, turn on with power:on and brightness:100.
            - At 15:40, turn off with power:off.
        • You also need to add 1 x "Piano Sheet Book - Level 2" to the shopping list.
        """,
        actions=[
            Action(name="query_entities",
                   kwargs={"entity_type": "members",
                           "filters": {"first_name": "Ethan",
                                       "last_name": "Smith"}}),
            Action(name="get_entity",
                   kwargs={"entity_type": "rooms",
                           "entity_id": "bedroom_east"}),
            Action(name="get_entity",
                   kwargs={"entity_type": "devices",
                           "entity_id": "lamp_be_bedside"}),
            Action(name="upsert_device",
                   kwargs={"device": {
                       "id": "lamp_be_bedside",
                       "scheduled_updates": [
                           {"timestamp": "2025-07-25T15:25:00",
                            "update": {"power": "on", "brightness": 100},
                            "rrule": "FREQ=WEEKLY;BYDAY=WE"},
                           {"timestamp": "2025-07-25T15:40:00",
                            "update": {"power": "off"},
                            "rrule": "FREQ=WEEKLY;BYDAY=WE"}
                       ]
                   }}),
            Action(name="get_entity",
                   kwargs={"entity_type": "custom_lists",}),
            Action(name="modify_custom_list_item",
                   kwargs={"list_id": "list_shopping",
                           "item": {"item": "Piano Sheet Book - Level 2",
                                    "quantity": 1},
                           "action": "add"}),
            Action(name="upsert_reminder",
                   kwargs={"reminder": {
                       "reminder_id": "rem_ethan_piano_practice",
                       "target": {"type": "note",
                                  "text": "Leave for piano lesson"},
                       "trigger": {
                           "rrule": "FREQ=WEEKLY;BYDAY=WE;BYHOUR=15;BYMINUTE=30"},
                       "actions": [{"type": "notify",
                                    "channel": "mobile_push"}],
                       "meta": {"priority": "high"},
                       "status": "active"
                   }})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_37",
        instruction="""
        You want to replace the outdated yearly car-maintenance reminder.
        • First, you want to delete the old car maintenance reminder.
        • Then, you want to create a new reminder **rem_car_maintenance_new** with the note "Annual car maintenance" for yearly on Dec 1st at 08:00 (via push).
        • You also need to create a new custom list **list_home_maintenance** (tagged maintenance) with the item "Change HVAC filter" x1. (Current time should be set to: 2025-07-29T14:50:00)
        """,
        actions=[
            Action(name="query_entities",
                   kwargs={"entity_type": "reminders",
                           "filters": {}}),
            Action(name="delete_reminder",
                   kwargs={"reminder_id": "rem_8f9fd8ae"}),
            Action(name="upsert_reminder",
                   kwargs={"reminder": {
                       "reminder_id": "rem_car_maintenance_new",
                       "target": {"type": "note",
                                  "text": "Annual car maintenance"},
                       "trigger": {
                           "rrule": "FREQ=YEARLY;BYMONTH=12;BYMONTHDAY=1;BYHOUR=8;BYMINUTE=0"},
                       "actions": [{"type": "notify",
                                    "channel": "mobile_push"}],
                       "meta": {"priority": "normal"},
                       "status": "active"
                   }}),
            Action(name="upsert_custom_list",
                   kwargs={"custom_list": {
                       "list_id": "list_home_maintenance",
                       "tags": ["maintenance"],
                       "items": []
                   }}),
            Action(name="modify_custom_list_item",
                   kwargs={"list_id": "list_home_maintenance",
                           "item": {"item": "Change HVAC filter", "quantity": 1},
                           "action": "add"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_38",
        instruction="""
        You want to prepare for the coming heat-wave.
        • You want to create a new scene with id **scene_heat_wave**.
            - The name should be: "Heat Wave"
            - The description should be: "Cool house & keep sun out."
            - The actions are:
                - curtain_lr should be power:on, position:0
                - ac_home should be power:on, mode:cool, setpoint_c:21, fan_speed:high
                - light_lr_ceiling should be power:off
          (You are not setting a schedule yet).
        • You want to run this scene now.
        • You also need to create a new reminder with id **rem_heat_wave_check** for "Check indoor temperature" daily at 12:00 via push.
        • Finally, you want to add 5 x "Ice cream" to the shopping list.
        """,
        actions=[
            Action(name="get_entity",
                   kwargs={"entity_type": "sensors",
                           "entity_id": "sensor_lr_thermometer"}),
            Action(name="upsert_scene",
                   kwargs={"scene": {
                       "id": "scene_heat_wave",
                       "name": "Heat Wave",
                       "description": "Cool house & keep sun out.",
                       "actions": [
                           {"device_id": "curtain_lr",
                            "update": {"power": "on", "position": 0}},
                           {"device_id": "ac_home",
                            "update": {"power": "on", "mode": "cool",
                                       "setpoint_c": 21,
                                       "fan_speed": "high"}},
                           {"device_id": "light_lr_ceiling",
                            "update": {"power": "off"}}
                       ]
                   }}),
            Action(name="run_scene",
                   kwargs={"scene_id": "scene_heat_wave"}),
            Action(name="get_entity",
                   kwargs={"entity_type": "custom_lists",}),
            Action(name="modify_custom_list_item",
                   kwargs={"list_id": "list_shopping",
                           "item": {"item": "Ice cream", "quantity": 5},
                           "action": "add"}),
            Action(name="upsert_reminder",
                   kwargs={"reminder": {
                       "reminder_id": "rem_heat_wave_check",
                       "target": {"type": "note",
                                  "text": "Check indoor temperature"},
                       "trigger": {
                           "rrule": "FREQ=DAILY;BYHOUR=12;BYMINUTE=0"},
                       "actions": [{"type": "notify",
                                    "channel": "mobile_push"}],
                       "status": "active",
                       "meta": {"priority": "normal"}
                   }})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_39",
        instruction="""
        Starting tomorrow (2025-07-30), you want to automate Olivia Smith's weekday wake-up routine. This should all occur every weekday.
        • At 06:55 every weekday, you want to turn her bedroom light on (at brightness 80).
        • At the same time, you want to open her bedroom curtain (position 100, power on).
        • You want to make a reminder **rem_olivia_pack_lunch** ("Olivia – pack lunch") that sends a push notification at 07:10 every weekday (with high priority).
        """,
        actions=[
            Action(name="query_entities",
                   kwargs={"entity_type": "members",
                           "filters": {"first_name": "Olivia",
                                       "last_name": "Smith"}}),
            Action(name="get_entity",
                   kwargs={"entity_type": "rooms",
                           "entity_id": "bedroom_west"}),
            Action(name="upsert_device",
                   kwargs={"device": {
                       "id": "light_bw_ceiling",
                       "scheduled_updates": [{
                           "timestamp": "2025-07-30T06:55:00",
                           "update": {"power": "on", "brightness": 80},
                           "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"
                       }]
                   }}),
            Action(name="get_entity",
                   kwargs={"entity_type": "devices",
                           "entity_id": "curtain_bw"}),
            Action(name="upsert_device",
                   kwargs={"device": {
                       "id": "curtain_bw",
                       "scheduled_updates": [{
                           "timestamp": "2025-07-30T06:55:00",
                           "update": {"power": "on", "position": 100},
                           "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"
                       }]
                   }}),
            Action(name="upsert_reminder",
                   kwargs={"reminder": {
                       "reminder_id": "rem_olivia_pack_lunch",

                       "target": {"type": "note",
                                  "text": "Pack lunch"},
                       "trigger": {
                           "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=7;BYMINUTE=10"},
                       "actions": [{"type": "notify",
                                    "channel": "mobile_push"}],
                       "meta": {"priority": "high"},
                       "status": "active",
                   }})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_40",
        instruction="""
        You want to set up bed-time comfort for the kids.
        • You want to add a new night-light device with id **nightlight_be**.
          It is of type light, from vendor Hatch, model "Rest 2nd Gen", with firmware 1.0.0.
          Its state_params are [power, brightness, color], and its initial state is off/0/kelvin:2700.
          (The updated at time is 2025-07-29T15:00:00)
        • You want to attach it to the east bedroom.
        • You want to set its daily scheduled_updates as follows:
            - 19:30 daily → power:on, brightness:10, color:{kelvin:2700}
            - 07:00 daily → power:off.
        • You want to create a new scene with id **scene_kids_bedtime**.
            - Its name should be "Kids Bedtime"
            - Its description should be "Wind-down lights for the kids."
            - Its actions are:
                - nightlight_be should be power:on, brightness:10, color:{kelvin:2700}
                - light_lr_ceiling should be power:off
            You want it scheduled to run at 20:00 tomorrow (2025-07-30).
        """,
        actions=[
            Action(name="get_entity",
                   kwargs={"entity_type": "rooms",}),
            Action(name="upsert_device",
                   kwargs={"device": {
                       "id": "nightlight_be",
                       "type": "light",

                       "location": "East Bedroom",
                       "vendor": "Hatch",
                       "model": "Rest 2nd Gen",
                       "firmware_version": "1.0.0",
                       "state_params": ["power", "brightness", "color"],
                       "state": {"power": "off",
                                 "brightness": 0,
                                 "color": {"kelvin": 2700}},
                       "scheduled_updates": [
                           {"timestamp": "2025-07-29T19:30:00",
                            "update": {"power": "on",
                                       "brightness": 10,
                                       "color": {"kelvin": 2700}},
                            "rrule": "FREQ=DAILY"},
                           {"timestamp": "2025-07-30T07:00:00",
                            "update": {"power": "off"},
                            "rrule": "FREQ=DAILY"}
                       ]
                   }}),
            Action(name="add_device_to_room",
                   kwargs={"room_id": "bedroom_east",
                           "device_id": "nightlight_be"}),
            Action(name="upsert_scene",
                   kwargs={"scene": {
                       "id": "scene_kids_bedtime",
                       "name": "Kids Bedtime",
                       "description": "Wind-down lights for the kids.",
                       "actions": [
                           {"device_id": "nightlight_be",
                            "update": {"power": "on",
                                       "brightness": 10,
                                       "color": {"kelvin": 2700}}},
                           {"device_id": "light_lr_ceiling",
                            "update": {"power": "off"}}
                       ],
                       "scheduled_runs": [
                           "2025-07-30T20:00:00"
                       ]
                   }}),
        ],
        outputs=[]
    )
]
