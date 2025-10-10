from domains.dto import Task, Action
# list of tasks
TASKS = [
    # ─────────────────────────────────────────────────────────────────────────────
    # Living-room air-quality­/temperature quick fix with scheduled rollback
    Task(
        annotator="0",
        user_id="res_01",
        instruction="""
        It's 15:00 on 2025-07-28. You want to know the current temperature from the Living Room Thermometer and the CO2 level from the Living Room Air-Quality Sensor.

        You want the following actions to happen if either the temperature goes above 22°C OR the CO2 levels exceed 750 ppm:
        • Turn on your central AC with these specific settings: cool mode, 22°C, and high fan speed
        • Open your Living Room curtain completely
        • Set your Living Room floor lamp to 40% brightness

        You also want all these devices to automatically return to different settings at 16:30 on 2025-07-28:
        • AC should turn off
        • Curtain should go to 50% position
        • Floor lamp should be at 60% brightness
        """,
        actions=[
            Action(name="list_sensor_names_ids",  kwargs={}),
            Action(name="list_devices",           kwargs={"type": "curtain"}),
            Action(name="list_devices",           kwargs={"type": "light"}),
            Action(name="list_devices",           kwargs={"type": "ac"}),
            Action(name="get_sensor_state",       kwargs={"sensor_id": "sensor_lr_thermometer"}),
            Action(name="get_sensor_state",       kwargs={"sensor_id": "sensor_lr_air_quality"}),
            Action(name="get_device",             kwargs={"device_id": "ac_home"}),
            Action(name="update_device_state_timer",     kwargs={"device_id": "ac_home",
                                                                 "timestamp_end": "2025-07-28T16:30:00",
                                                                 "update": {"power": "on",
                                                                             "mode": "cool",
                                                                             "setpoint_c": 22,
                                                                             "fan_speed": "high"}}),

            Action(name="update_device_state",    kwargs={"device_id": "curtain_lr",
                                                          "update": {"position": 100}}),
            Action(name="update_device_state",    kwargs={"device_id": "light_lr_floor",
                                                          "update": {"power": "on",
                                                                     "brightness": 40}}),
            Action(name="schedule_device_update", kwargs={"device_id": "curtain_lr",
                                                          "timestamp": "2025-07-28T16:30:00",
                                                          "update": {"position": 50}}),
            Action(name="schedule_device_update", kwargs={"device_id": "light_lr_floor",
                                                          "timestamp": "2025-07-28T16:30:00",
                                                          "update": {"brightness": 60}}),
        ],
        outputs=[
            '"temperature_c": 22.3',
            '"co2_ppm": 650',
        ],
    ),

    # ─────────────────────────────────────────────────────────────────────────────
    # Movie-night scene with full state capture & restoration
    Task(
        annotator="0",
        user_id="res_02",
        instruction="""
        You want to set up a "Movie Night" mode starting at 20:00 on 2025-07-28. Here's what you need:

        First, you want these changes:
        • Turn off your living room ceiling light
        • Set your living room floor lamp to 15% brightness
        • Close your living room curtain completely
        • Turn on the central AC to cool mode at 21°C with low fan speed

        You want the system to remember the current settings of all these devices, and then at 22:30, you want everything to return to these specific settings:
        • Ceiling light: on at 70% brightness
        • Floor lamp: 60% brightness
        • Curtain: fully open
        • AC: turned off
        """,
        actions=[
            Action(name="list_devices",           kwargs={"type": "light"}),
            Action(name="list_devices",           kwargs={"type": "curtain"}),
            Action(name="list_sensor_names_ids",  kwargs={}),
            Action(name="get_device",             kwargs={"device_id": "light_lr_ceiling"}),
            Action(name="get_device",             kwargs={"device_id": "light_lr_floor"}),
            Action(name="get_device",             kwargs={"device_id": "curtain_lr"}),
            Action(name="get_device",             kwargs={"device_id": "ac_home"}),
            Action(name="get_sensor_state",       kwargs={"sensor_id": "camera_front_door"}),

            Action(name="schedule_device_update", kwargs={"device_id": "light_lr_ceiling",
                                                          "timestamp": "2025-07-28T20:00:00",
                                                          "update": {"power": "off"}}),
            Action(name="schedule_device_update", kwargs={"device_id": "light_lr_floor",
                                                          "timestamp": "2025-07-28T20:00:00",
                                                          "update": {"power": "on",
                                                                     "brightness": 15}}),
            Action(name="schedule_device_update", kwargs={"device_id": "curtain_lr",
                                                          "timestamp": "2025-07-28T20:00:00",
                                                          "update": {"position": 0}}),
            Action(name="schedule_device_update_timer", kwargs={"device_id": "ac_home",
                                                                 "timestamp": "2025-07-28T20:00:00",
                                                                 "timestamp_end": "2025-07-28T22:30:00",
                                                                 "update": {"power": "on",
                                                                            "mode": "cool",
                                                                            "setpoint_c": 21,
                                                                            "fan_speed": "low"}}),
            Action(name="schedule_device_update", kwargs={"device_id": "light_lr_ceiling",
                                                          "timestamp": "2025-07-28T22:30:00",
                                                          "update": {"power": "on",
                                                                     "brightness": 70}}),
            Action(name="schedule_device_update", kwargs={"device_id": "light_lr_floor",
                                                          "timestamp": "2025-07-28T22:30:00",
                                                          "update": {"power": "on",
                                                                     "brightness": 60}}),
            Action(name="schedule_device_update", kwargs={"device_id": "curtain_lr",
                                                          "timestamp": "2025-07-28T22:30:00",
                                                          "update": {"position": 100}}),
        ],
        outputs=[
        ],
    ),

    # ─────────────────────────────────────────────────────────────────────────────
    # Week-day sunrise routine plus nightly dishwasher run
    Task(
        annotator="0",
        user_id="res_03",
        instruction="""
        Starting Monday, August 1st, 2025, you want to set up a weekday routine for your home:

        You need the following schedule for every weekday morning:
        • 06:45 - Open the west bedroom's curtain completely
        • 06:50 - Turn on the west bedroom ceiling light at 70% brightness
        • 06:55 - Open your living room curtain completely

        Additionally, you want your dishwasher to run on eco mode every weekday night at 23:00, with a 120-minute cycle time, making sure the door is closed.
        """,
        actions=[
            Action(name="list_devices", kwargs={"type": "curtain"}),
            Action(name="list_devices", kwargs={"type": "light"}),
            Action(name="list_devices", kwargs={"type": "dishwasher"}),
            Action(name="schedule_device_update", kwargs={"device_id": "curtain_bw",
                                                          "timestamp": "2025-08-01T06:45:00",
                                                          "update": {"position": 100},
                                                          "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"}),
            Action(name="schedule_device_update", kwargs={"device_id": "light_bw_ceiling",
                                                          "timestamp": "2025-08-01T06:50:00",
                                                          "update": {"power": "on",
                                                                     "brightness": 70},
                                                          "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"}),
            Action(name="schedule_device_update", kwargs={"device_id": "curtain_lr",
                                                          "timestamp": "2025-08-01T06:55:00",
                                                          "update": {"position": 100},
                                                          "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"}),
            Action(name="schedule_device_update", kwargs={"device_id": "dishwasher_kt",
                                                          "timestamp": "2025-08-01T23:00:00",
                                                          "update": {"power": "on",
                                                                     "cycle": "eco",
                                                                     "time_remaining_min": 120,
                                                                     "door": "closed"},
                                                          "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"}),
        ],
        outputs=[
        ],
    ),

    # ─────────────────────────────────────────────────────────────────────────────
    # Leaving-home full shutdown with evening presence light
    Task(
        annotator="0",
        user_id="res_04",
        instruction="""
        You're heading out now in the morning, and you need a comprehensive shutdown routine. Here's what you want:

        First, you want the system to report if the front door is open (sensor_id: sensor_front_door) and whether any motion is detected in the hallway (sensor_id: sensor_hall_motion).

        Then, you need these actions:
        • Turn off all lights in the house (living room ceiling and floor, all bedroom ceiling lights, night lamps, and desk lamps)
        • Turn off the AC
        • Close all curtains in the house completely

        For security, you want the living room ceiling light to turn on at 30% brightness at 19:30 that evening (July 29th, 2025).
        """,
        actions=[
            Action(name="get_sensor_state",       kwargs={"sensor_id": "sensor_front_door"}),
            Action(name="get_sensor_state",       kwargs={"sensor_id": "sensor_hall_motion"}),
            Action(name="list_devices",           kwargs={"type": "light"}),
            Action(name="list_devices",           kwargs={"type": "curtain"}),
            Action(name="list_devices",           kwargs={"type": "ac"}),

            # Eight lights off
            *[Action(name="update_device_state",
                     kwargs={"device_id": did, "update": {"power": "off"}})
              for did in ["light_lr_ceiling", "light_lr_floor", "light_br_ceiling",
                          "lamp_br_night", "light_bw_ceiling", "lamp_bw_desk",
                          "light_be_ceiling", "lamp_be_bedside"]],

            Action(name="update_device_state",    kwargs={"device_id": "ac_home",
                                                          "update": {"power": "off"}}),

            *[Action(name="update_device_state",
                     kwargs={"device_id": cid, "update": {"position": 0}})
              for cid in ["curtain_lr", "curtain_br", "curtain_bw", "curtain_be"]],

            Action(name="schedule_device_update", kwargs={"device_id": "light_lr_ceiling",
                                                          "timestamp": "2025-07-29T19:30:00",
                                                          "update": {"power": "on",
                                                                     "brightness": 30}}),
        ],
        outputs=[
            '"door_open": false',
            '"motion_detected": false',
        ],
    ),

    # ─────────────────────────────────────────────────────────────────────────────
    # Smoke / CO emergency lighting & HVAC shutdown
    Task(
        annotator="0",
        user_id="res_05",
        instruction="""
        You believe you smell smoke. You need:

        • Both your heater and AC to shut off immediately
        • Your bedroom ceiling light and night lamp to turn on at full brightness with a red alert color
        • Both front and back door cameras to start recording
        • The bedroom lights to automatically turn off at 02:00 on July 29th, 2025
        """,
        actions=[
            Action(name="list_devices",           kwargs={"type": "heater"}),
            Action(name="list_devices",           kwargs={"type": "ac"}),
            Action(name="list_devices",           kwargs={"type": "light"}),
            Action(name="list_sensor_names_ids",  kwargs={}),

            Action(name="update_device_state",    kwargs={"device_id": "heater_home",
                                                          "update": {"power": "off"}}),
            Action(name="update_device_state",    kwargs={"device_id": "ac_home",
                                                          "update": {"power": "off"}}),
            Action(name="update_device_state_timer", kwargs={"device_id": "light_br_ceiling",
                                                                 "timestamp_end": "2025-07-29T02:00:00",
                                                                 "update": {"power": "on",
                                                                             "brightness": 100,
                                                                             "color": {"hue": 0,
                                                                                     "saturation": 100}}}),
            Action(name="update_device_state_timer", kwargs={"device_id": "lamp_br_night",
                                                             "timestamp_end": "2025-07-29T02:00:00",
                                                             "update": {"power": "on",
                                                                        "brightness": 100,
                                                                        "color": {"hue": 0,
                                                                                  "saturation": 100}}}),
            Action(name="update_device_state",    kwargs={"device_id": "camera_front_door",
                                                          "update": {"recording": True}}),
            Action(name="update_device_state",    kwargs={"device_id": "camera_back_door",
                                                          "update": {"recording": True}}),
        ],
        outputs=[
        ],
    ),

    # ─────────────────────────────────────────────────────────────────────────────
    # NEW DEVICE – Living-room humidifier & 2-hour auto-off
    Task(
        annotator="0",
        user_id="res_06",
        instruction="""
        You want to add a new humidifier to your living room setup. You need it configured with these specific details:
        • ID: humidifier_lr
        • Name: Living Room Humidifier
        • Location: Living Room
        • Vendor: Levoit
        • Model: Classic300S
        • Firmware version: 1.0.0
        • State parameters: power, mode, humidity_setpoint_pct
        • State: power=off, mode=auto, humidity_setpoint_pct=45

        After it's set up, you want the system to:
        • Add it to your living room's device list
        • Turn on the humidifier in continuous mode at 45% target at 15:00 on July 28th, 2025
        • Schedule it to turn off automatically at 17:00 on July 28th, 2025
        """,
        actions=[
            Action(name="create_device",          kwargs={"id": "humidifier_lr",
                                                          "type": "humidifier",
                                                          "name": "Living Room Humidifier",
                                                          "location": "Living Room",
                                                          "vendor": "Levoit",
                                                          "model": "Classic300S",
                                                          "firmware_version": "1.0.0",
                                                          "state_params": ["power","mode","humidity_setpoint_pct"],
                                                          "state": {"power": "off",
                                                                    "mode": "auto",
                                                                    "humidity_setpoint_pct": 45}}),
            Action(name="add_device_to_room",     kwargs={"room_id": "living_room",
                                                          "device_id": "humidifier_lr"}),
            Action(name="schedule_device_update",    kwargs={"device_id": "humidifier_lr",
                                                          "timestamp": "2025-07-28T15:00:00",
                                                          "update": {"power": "on",
                                                                     "mode": "continuous",
                                                                     "humidity_setpoint_pct": 45}}),
            Action(name="schedule_device_update", kwargs={"device_id": "humidifier_lr",
                                                          "timestamp": "2025-07-28T17:00:00",
                                                          "update": {"power": "off"}}),
        ],
        outputs=[
            '"humidity_pct": 45.2',
        ],
    ),

    # ─────────────────────────────────────────────────────────────────────────────
    # NEW SENSOR + DEVICE – Basement freeze-protection heater
    Task(
        annotator="0",
        user_id="res_07",
        instruction="""
        You bought a Dyson HP04 auxiliary heater. You want to configure it as:
        • ID: heater_bs_aux
        • Initial settings: off, heat mode, 15°C target
        • Location: Basement
        • Vendor: Dyson
        • Model: HP04
        • Firmware version: 2.0.0
        • State parameters: power, mode, setpoint_c
        • State: power=off, mode=heat, setpoint_c=15

        For safety, you want the heater to automatically shut off at 07:00 every day starting July 29th, 2025
        """,
        actions=[
            Action(name="create_device",          kwargs={"id": "heater_bs_aux",
                                                          "type": "heater",

                                                          "location": "Basement",
                                                          "vendor": "Dyson",
                                                          "model": "HP04",
                                                          "firmware_version": "2.0.0",
                                                          "state_params": ["power","mode","setpoint_c"],
                                                          "state": {"power": "off",
                                                                    "mode": "heat",
                                                                    "setpoint_c": 15}}),
            Action(name="add_device_to_room",     kwargs={"room_id": "basement",
                                                          "device_id": "heater_bs_aux"}),
            Action(name="schedule_device_update", kwargs={"device_id": "heater_bs_aux",
                                                          "timestamp": "2025-07-29T07:00:00",
                                                          "update": {"power": "off"},
                                                          "rrule": "FREQ=DAILY"}),
        ],
        outputs=[
        ],
    ),

    # ─────────────────────────────────────────────────────────────────────────────
    # NEW DEVICE – Garden sprinkler with daily cycle
    Task(
        annotator="0",
        user_id="res_08",
        instruction="""
        You want to install a Rachio Gen 3 smart sprinkler controller for your garden. You need it set up with:
        • ID: sprinkler_garden
        • Initial state: off, auto mode
        • Vendor: Rachio
        • Name: Backyard Sprinkle
        • Location: "Backyard"
        • Model: Gen 3
        • Firmware version: 3.0.0
        • And set state with:
            • Power: Off
            • Mode: Auto
            • duration_min: 0

        For the watering schedule, you want:
        • Daily watering to start at 06:00 beginning July 29th, 2025
        • Each session should run for 20 minutes in manual mode
        • The system should automatically turn off at 06:20
        • You want to skip watering on July 4th and 5th, 2026
        """,
        actions=[
            Action(name="create_device",          kwargs={"id": "sprinkler_garden",
                                                          "type": "sprinkler",
                                                          "name": "Backyard Sprinkle",
                                                          "location": "Backyard",
                                                          "vendor": "Rachio",
                                                          "model": "Gen 3",
                                                          "firmware_version": "3.0.0",
                                                          "state_params": ["power","mode","duration_min"],
                                                          "state": {"power": "off",
                                                                    "mode": "auto",
                                                                    "duration_min": 0}}),
            Action(name= "schedule_device_update_timer", kwargs={"device_id": "sprinkler_garden",
                                                                 "timestamp": "2025-07-29T06:00:00",
                                                                 "timestamp_end": "2025-07-29T06:20:00",
                                                                 "update": {"power": "on",
                                                                            "mode": "manual",
                                                                            "duration_min": 20},
                                                                 "rrule": "FREQ=DAILY;UNTIL=20260703T235959"}),
            Action(name= "schedule_device_update_timer", kwargs={"device_id": "sprinkler_garden",
                                                                 "timestamp": "2026-07-06T06:00:00",
                                                                 "timestamp_end": "2026-07-06T06:20:00",
                                                                 "update": {"power": "on",
                                                                            "mode": "manual",
                                                                            "duration_min": 20},
                                                                 "rrule": "FREQ=DAILY"}),

        ],
        outputs=[
        ],
    ),

    # ─────────────────────────────────────────────────────────────────────────────
    # NEW SENSOR – Solar-power-aware AC control
    Task(
        annotator="0",
        user_id="res_09",
        instruction="""
        You want to add a rooftop solar power meter to make your AC usage more energy-efficient. You need:

        An Enphase IQ7 power meter installed with:
        • ID: device_solar_power
        • Type: sensor
        • Initial reading: 4200W generation
        • Name: Rooftop Solar Power Meter
        • Location: Roof
        • Vendor: Enphase
        • Model: IQ7
        • Firmware version: 1.0.1
        • State parameters: power_generation_w
        • State: power_generation_w=4200

        You want the system to check power generation and living room temperature, then turn on the AC in cool mode at 20°C with auto fan speed.

        You want the system to report living room temperature and power generation.
        """,
        actions=[
            Action(name="create_device",          kwargs={"id": "device_solar_power",
                                                          "type": "sensor",
                                                          "name": "Rooftop Solar Power Meter",
                                                          "location": "Roof",
                                                          "vendor": "Enphase",
                                                          "model": "IQ7",
                                                          "firmware_version": "1.0.1",
                                                          "state_params": ["power_generation_w"],
                                                          "state": {"power_generation_w": 4200}}),
            Action(name="list_sensor_names_ids",  kwargs={}),
            Action(name="get_sensor_state",       kwargs={"sensor_id": "sensor_lr_thermometer"}),
            Action(name="get_device",             kwargs={"device_id": "device_solar_power"}),
            Action(name="list_devices",           kwargs={"type": "ac"}),
            Action(name="update_device_state",    kwargs={"device_id": "ac_home",
                                                          "update": {"power": "on",
                                                                     "mode": "cool",
                                                                     "setpoint_c": 20,
                                                                     "fan_speed": "auto"}}),
        ],
        outputs=[
            '"temperature_c": 22.3',
            '"power_generation_w": 4200',
        ],
    ),

    # ─────────────────────────────────────────────────────────────────────────────
    # NEW SENSOR – Ambient-light-driven smart dimming
    Task(
        annotator="0",
        user_id="res_10",
        instruction="""
        You want to add an Aqara T1 ambient light sensor to control your living room lighting automatically. You need it set up as:
        • ID: device_lr_lux
        • Name: Aqara T1 Ambient Light Sensor
        • Type: sensor
        • Location: Living Room
        • Vendor: Aqara
        • Model: T1 Ambient Light
        • Firmware version: 1.0.0
        • State parameters: illuminance_lux, battery_level
        • State: illuminance_lux=400, battery_level=100

        You want the system to report the illuminance level from it. Then, you want the system to turn on the living room ceiling light at 50% brightness.
        """,
        actions=[
            Action(name="create_device",          kwargs={"id": "device_lr_lux",
                                                          "type": "sensor",
                                                          "name": "Aqara T1 Ambient Light Sensor",
                                                          "location": "Living Room",
                                                          "vendor": "Aqara",
                                                          "model": "T1 Ambient Light",
                                                          "firmware_version": "1.0.0",
                                                          "state_params": ["illuminance_lux","battery_level"],
                                                          "state": {"illuminance_lux": 400,
                                                                    "battery_level": 100}}),
            Action(name="add_device_to_room",     kwargs={"room_id": "living_room",
                                                          "device_id": "device_lr_lux"}),
            Action(name="get_device",             kwargs={"device_id": "device_lr_lux"}),
            Action(name="list_devices",           kwargs={"type": "light"}),
            Action(name="update_device_state",    kwargs={"device_id": "light_lr_ceiling",
                                                          "update": {"power": "on",
                                                                     "brightness": 50}}),
        ],
        outputs=[
        ],
    ),

    # ─────────────────────────────────────────────────────────────────────────────
    # Afternoon nap mode with timed restore
    Task(
        annotator="0",
        user_id="res_11",
        instruction="""
        You want to take a nap in the master bedroom. You need:
        • Close the bedroom curtain completely
        • Turn off the ceiling light
        • Set the night lamp to 10% brightness with hue 30 and saturation 20
        • Set the AC to cool mode at 24°C with low fan speed

        At 15:30 on the same day (July 28th), you want everything to return to these settings:
        • Open the curtain completely
        • Turn on ceiling light at 60% brightness
        • Set night lamp to 30% brightness with hue 30 and saturation 60
        • Turn off the AC
        """,
        actions=[
            Action(name="list_devices",           kwargs={"type": "curtain"}),
            Action(name="list_devices",           kwargs={"type": "light"}),
            Action(name="list_devices",           kwargs={"type": "ac"}),

            Action(name="get_device",             kwargs={"device_id": "curtain_br"}),

            Action(name="update_device_state",    kwargs={"device_id": "curtain_br",
                                                          "update": {"position": 0}}),
            Action(name="update_device_state",    kwargs={"device_id": "light_br_ceiling",
                                                          "update": {"power": "off"}}),
            Action(name="update_device_state",    kwargs={"device_id": "lamp_br_night",
                                                          "update": {"power": "on",
                                                                     "brightness": 10,
                                                                     "color": {"hue": 30,
                                                                               "saturation": 20}}}),
            Action(name="update_device_state_timer",    kwargs={"device_id": "ac_home",
                                                                "timestamp_end": "2025-07-28T15:30:00",
                                                                "update": {"power": "on",
                                                                           "mode": "cool",
                                                                           "setpoint_c": 24,
                                                                           "fan_speed": "low"}}),

            Action(name="schedule_device_update", kwargs={"device_id": "curtain_br",
                                                          "timestamp": "2025-07-28T15:30:00",
                                                          "update": {"position": 100}}),
            Action(name="schedule_device_update", kwargs={"device_id": "light_br_ceiling",
                                                          "timestamp": "2025-07-28T15:30:00",
                                                          "update": {"power": "on",
                                                                     "brightness": 60}}),
            Action(name="schedule_device_update", kwargs={"device_id": "lamp_br_night",
                                                          "timestamp": "2025-07-28T15:30:00",
                                                          "update": {"power":"on", "brightness": 30,
                                                                     "color": {"hue": 30,
                                                                               "saturation": 60}}}),
        ],
        outputs=[
        ],
    ),

    # ─────────────────────────────────────────────────────────────────────────────
    # Leak-detected automatic dishwasher kill & alert lights
    Task(
        annotator="0",
        user_id="res_12",
        instruction="""
        You believe your sink is leaking. You need:

        • The dishwasher to shut off immediately
        • The living room ceiling light to become bright red as a visual alert
        • Both front and back door cameras to start recording

        You want the system to report whether the leak detection sensor (sensor_id: sensor_sink_leak) detects a leak.
        """,
        actions=[
            Action(name="update_device_state",    kwargs={"device_id": "dishwasher_kt",
                                                          "update": {"power": "off"}}),
            Action(name="update_device_state",    kwargs={"device_id": "light_lr_ceiling",
                                                          "update": {"power": "on",
                                                                     "brightness": 100,
                                                                     "color": {"hue": 0,
                                                                               "saturation": 100}}}),
            Action(name="update_device_state",    kwargs={"device_id": "camera_front_door",
                                                          "update": {"recording": True}}),
            Action(name="update_device_state",    kwargs={"device_id": "camera_back_door",
                                                          "update": {"recording": True}}),
            Action(name="list_sensor_names_ids",  kwargs={}),
            Action(name="get_sensor_state",       kwargs={"sensor_id": "sensor_sink_leak"}),
        ],
        outputs=[
            '"leak_detected": false',
        ],
    ),

    # ─────────────────────────────────────────────────────────────────────────────
    # Mid-day energy-save check using motion & camera status
    Task(
        annotator="0",
        user_id="res_13",
        instruction="""
        You want to run an energy-saving check. First, report on the following conditions:
        • Whether motion is detected in the hallway
        • Whether people are detected on either front or back door cameras

        If no motion or people are detected, you want:
        • All bedroom lights to turn off (ceiling lights, night lamps, and desk lamps)
        • The system to check the living room temperature and:
          - Turn off the heater if it's above 20°C
          - Turn off the AC if it's below 23°C
        """,
        actions=[
            Action(name="list_sensor_names_ids",  kwargs={}),
            Action(name="get_sensor_state",       kwargs={"sensor_id": "sensor_hall_motion"}),
            Action(name="get_sensor_state",       kwargs={"sensor_id": "camera_front_door"}),
            Action(name="get_sensor_state",       kwargs={"sensor_id": "camera_back_door"}),
            Action(name="get_sensor_state",       kwargs={"sensor_id": "sensor_lr_thermometer"}),

            Action(name="list_devices",           kwargs={"type": "light"}),
            *[Action(name="update_device_state",
                     kwargs={"device_id": did, "update": {"power": "off"}})
              for did in ["light_br_ceiling", "lamp_br_night", "light_bw_ceiling",
                          "lamp_bw_desk", "light_be_ceiling", "lamp_be_bedside"]],

            Action(name="list_devices",           kwargs={"type": "heater"}),
            Action(name="list_devices",           kwargs={"type": "ac"}),
            Action(name="update_device_state",    kwargs={"device_id": "heater_home",
                                                          "update": {"power": "off"}}),
            Action(name="update_device_state",    kwargs={"device_id": "ac_home",
                                                          "update": {"power": "off"}}),
        ],
        outputs=[
            '"motion_detected": false',
            '"person_detected": false',
            '"person_detected": false',
        ],
    ),

    # ─────────────────────────────────────────────────────────────────────────────
    # Guest-prep lighting in East Bedroom with midnight shutdown
    Task(
        annotator="0",
        user_id="res_14",
        instruction="""
        You want to prepare the East Bedroom for a guest arriving on July 29th, 2025. At 21:00, you need:

        • Close the curtain completely
        • Set the bedside lamp to 40% brightness with hue 50 and saturation 80
        • Set the ceiling light to 30% brightness with hue 210 and saturation 50

        At midnight (00:00 on July 30th), you want:
        • Both lights to turn off
        • The curtain to open completely
        """,
        actions=[
            Action(name="list_devices",           kwargs={"type": "curtain"}),
            Action(name="list_devices",           kwargs={"type": "light"}),

            Action(name="schedule_device_update", kwargs={"device_id": "curtain_be",
                                                          "timestamp": "2025-07-29T21:00:00",
                                                          "update": {"position": 0}}),
            Action(name= "schedule_device_update_timer", kwargs={"device_id": "lamp_be_bedside",
                                                                 "timestamp": "2025-07-29T21:00:00",
                                                                 "timestamp_end": "2025-07-30T00:00:00",
                                                                 "update": {"power": "on",
                                                                            "brightness": 40,
                                                                            "color": {"hue": 50,
                                                                                      "saturation": 80}}}),
            Action(name= "schedule_device_update_timer", kwargs={"device_id": "light_be_ceiling",
                                                                 "timestamp": "2025-07-29T21:00:00",
                                                                 "timestamp_end": "2025-07-30T00:00:00",
                                                                 "update": {"power": "on",
                                                                            "brightness": 30,
                                                                            "color": {"hue": 210,
                                                                                      "saturation": 50}}}),
            Action(name="schedule_device_update", kwargs={"device_id": "curtain_be",
                                                          "timestamp": "2025-07-30T00:00:00",
                                                          "update": {"position": 100}}),
        ],
        outputs=[
        ],
    ),

    # ─────────────────────────────────────────────────────────────────────────────
    # Daily 08:00 sensor-battery audit with blinking alert
    Task(
        annotator="0",
        user_id="res_15",
        instruction="""
        You need the system to:

        • Check the battery levels of your key sensors:
          - Living room thermometer
          - Hall motion sensor
          - Front door sensor
          - Bedroom smoke detector
          - Sink leak sensor

        You want the system to report all. If any battery is below 80%, put in a reminder to charge it.
        Make reminder id: rem_battery_charge. Name: Charge battery (put in sensor_id). Priority: normal. Notify via: mobile push.
        """,
        actions=[
            Action(name="list_sensor_names_ids",  kwargs={}),

            *[Action(name="get_sensor_state", kwargs={"sensor_id": sid})
              for sid in ["sensor_lr_thermometer", "sensor_hall_motion",
                          "sensor_front_door", "sensor_bed_smoke",
                          "sensor_sink_leak"]],
            Action(name="manage_reminders", kwargs={"action": "create", "reminder_id": "rem_battery_charge", "reminder": {"name": "Charge battery (sensor_front_door)", "reminder_id": "rem_battery_charge", "priority": "normal", "notify_via": "mobile_push"}}),
        ],
        outputs=[
            '"battery_level": 95',
            '"battery_level": 88',
            '"battery_level": 79',
            '"battery_level": 90',
            '"battery_level": 93',
        ],
    ),
    Task(
        annotator="0",
        user_id="res_16",
        instruction="""
        You're John, on Monday (2025-07-30) you want a gentle 06:25 bedroom wake-up:
        • Add a smart coffee maker with the following details:
          - ID: coffee_maker_kt
          - Type: coffee_maker
          - Name: Kitchen Coffee Maker
          - Location: Kitchen
          - Vendor: Keurig
          - Model: K-Elite
          - Firmware version: 1.0.0
          - State parameters: power, brew_size, temperature_c
          - State: power=off, brew_size=mug, temperature_c=90
        • Add it to the kitchen and have it brew a large
          travel cup at 06:28, then switch itself off at 06:40.
        • Half-open the master-bedroom blackout curtain right away, then finish
          opening it at 06:30.
        • Turn the master-bedroom ceiling light on at a very dim warm glow now (brightness 10, hue 30, saturation 20),
          and raise it to 50 % brightness at 06:30.
        """,
        actions=[
            # create and schedule coffee maker
            Action(name="create_device",           kwargs={
                "id": "coffee_maker_kt",
                "type": "coffee_maker",

                "location": "Kitchen",
                "vendor": "Keurig",
                "model": "K-Elite",
                "firmware_version": "1.0.0",
                "state_params": ["power","brew_size","temperature_c"],
                "state": {"power":"off","brew_size":"mug","temperature_c":90}
            }),
            Action(name="add_device_to_room",      kwargs={
                "room_id": "kitchen",
                "device_id": "coffee_maker_kt"
            }),
            Action(name= "schedule_device_update_timer", kwargs={
                "device_id": "coffee_maker_kt",
                "timestamp": "2025-07-30T06:28:00",
                "timestamp_end": "2025-07-30T06:40:00",
                "update": {"power":"on","brew_size":"travel","temperature_c":90}
            }),
            Action(name="list_devices",           kwargs={"type": "curtain"}),
            Action(name="list_devices",           kwargs={"type": "light"}),

            # bedroom curtain & light
            Action(name="update_device_state",     kwargs={
                "device_id": "curtain_br",
                "update": {"position":50}
            }),
            Action(name="schedule_device_update",  kwargs={
                "device_id": "curtain_br",
                "timestamp": "2025-07-30T06:30:00",
                "update": {"position":100}
            }),
            Action(name="update_device_state",     kwargs={
                "device_id": "light_br_ceiling",
                "update": {"power":"on","brightness":10,
                           "color":{"hue":30,"saturation":20}}
            }),
            Action(name="schedule_device_update",  kwargs={
                "device_id": "light_br_ceiling",
                "timestamp": "2025-07-30T06:30:00",
                "update": {"brightness":50}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_17",
        instruction="""
        You've recently bought an EV charger with the following specifications:
        id=ev_charger_garage, type=ev_charger, name="Garage EV Charger",
        location="Basement", vendor="ChargePoint", model="Home Flex",
        firmware_version="1.0.0",
        state_params=["power","mode","current_a"],
        state={"power":"off","mode":"charge","current_a":0}

        Next weekday is Monday 2025-07-30.
        You want the system to check and report Emily's (emily_smith) shift details.
        Then, prepare the car by turing ON at 06:00 with mode "preheat" and current_a:16.
        You want to shut back OFF 06:50.

        Also, report the living room's temperature (sensor_id: sensor_lr_thermometer). If the temperature is less than 25 celsius then
        turn on the central heater with temperature set to 22.
        """,
        actions=[
            Action(name="create_device",           kwargs={
                "id": "ev_charger_garage",
                "type": "ev_charger",

                "location": "Basement",
                "vendor": "ChargePoint",
                "model": "Home Flex",
                "firmware_version": "1.0.0",
                "state_params": ["power","mode","current_a"],
                "state": {"power":"off","mode":"charge","current_a":0}
            }),
            Action(name="add_device_to_room",      kwargs={
                "room_id": "basement",
                "device_id": "ev_charger_garage"
            }),
            Action(name="list_members",            kwargs={}),
            Action(name= "schedule_device_update_timer", kwargs={
                "device_id": "ev_charger_garage",
                "timestamp": "2025-07-30T06:00:00",
                "timestamp_end": "2025-07-30T06:50:00",
                "update": {"power":"on","mode":"preheat","current_a":16}
            }),
            Action(name="list_sensor_names_ids",   kwargs={}),
            Action(name="get_sensor_state",        kwargs={"sensor_id":"sensor_lr_thermometer"}),
            Action(name="list_devices",            kwargs={"type": "heater"}),
            Action(name="update_device_state",     kwargs={
                "device_id": "heater_home",
                "update": {"power":"on","setpoint_c":22}
            }),
        ],
        outputs=[
            '"shift": "Mon-Wed 07:00-15:00"',
            '"temperature_c": 22.3',
        ]
    ),
    Task(
        annotator="0",
        user_id="res_18",
        instruction="""
        On Tuesday (2025-07-01) Olivia catches the bus:
        • At 06:50 fully open the window-side curtain in her bedroom and turn its
          ceiling light on to 60 % brightness.
        • Switch that light off at 07:40 and close the curtain at 07:45.
        """,
        actions=[
            Action(name="list_members",            kwargs={}),
            Action(name="list_devices",           kwargs={"type": "curtain"}),
            Action(name="list_devices",           kwargs={"type": "light"}),

            Action(name="schedule_device_update",  kwargs={
                "device_id": "curtain_bw",
                "timestamp": "2025-07-01T06:50:00",
                "update": {"position":100}
            }),
            Action(name="schedule_device_update",  kwargs={
                "device_id": "light_bw_ceiling",
                "timestamp": "2025-07-01T06:50:00",
                "update": {"power":"on","brightness":60}
            }),
            Action(name="schedule_device_update",  kwargs={
                "device_id": "light_bw_ceiling",
                "timestamp": "2025-07-01T07:40:00",
                "update": {"power":"off"}
            }),
            Action(name="schedule_device_update",  kwargs={
                "device_id": "curtain_bw",
                "timestamp": "2025-07-01T07:45:00",
                "update": {"position":0}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_19",
        instruction="""
        A friend named Mia is arriving for a play-date on 2025-07-02:
        • Make yourself a high-priority reminder at 17:30 to drive Mia home. (reminder_id: rem_mia_pickup, name: Mia Pickup, priority: high, notify via mobile push)
        • Start recording now on the front-door camera and set the living-room
          ceiling light to 80 % so she sees her way in.
        • Turn the light off at 17:45.
        """,
        actions=[
            Action(name="list_devices",   kwargs={}),
            Action(name="list_sensor_names_ids",  kwargs={}),

            Action(name="manage_reminders",         kwargs={
                "action":"create",
                "reminder_id": "rem_mia_pickup",
                "reminder": {"reminder_id":"rem_mia_pickup",

                             "target": {"type":"note","text":"Drive Mia home"},
                             "trigger": {"datetime":"2025-07-02T17:30:00"},
                             "actions": [{"type":"notify","channel":"mobile_push"}],
                             "meta": {"priority":"high"}}
            }),
            Action(name="manage_reminders",         kwargs={
                "action":"get",
                "reminder_id":"rem_mia_pickup"
            }),
            Action(name="update_device_state",     kwargs={
                "device_id": "camera_front_door",
                "update": {"recording": True}
            }),
            Action(name="update_device_state_timer",     kwargs={
                "device_id": "light_lr_ceiling",
                "timestamp_end": "2025-07-02T17:45:00",
                "update": {"power":"on","brightness":80}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_20",
        instruction="""
        It's trash night (2025-07-03). Please:
        • You want the system to report the details of the existing trash-night reminder (reminder_id: rem_eb55e94b).
        • Turn the living-room floor lamp to full brightness now, and
          switch it off again at 19:30.
        • You want the system to report if the front door is open (sensor_id: sensor_front_door).
        """,
        actions=[
            Action(name="manage_reminders",        kwargs={
                "action":"list_all_names_ids"
            }),
            Action(name="manage_reminders",        kwargs={
                "action":"get",
                "reminder_id":"rem_eb55e94b"
            }),
            Action(name="list_devices",            kwargs={"type": "light"}),
            Action(name="update_device_state_timer",     kwargs={
                "device_id": "light_lr_floor",
                "timestamp_end": "2025-07-03T19:30:00",
                "update": {"power":"on","brightness":100}
            }),

            Action(name="get_sensor_state",        kwargs={
                "sensor_id":"sensor_front_door"
            }),
        ],
        outputs=[
            '"text": "Take out trash"',
            '"door_open": false',
        ]
    ),
    Task(
        annotator="0",
        user_id="res_21",
        instruction="""
        You bought a motorized patio umbrella and a smart speaker in the backyard.
        The motorized umbrella is from SunSetter and the smart speaker is from Sonos.
        The umbrella model is SmartShade Pro (firmware version 1.0.0) and the speaker model is Move 2 (firmware version 1.0.0).
        Both have a power state that's either on or off.
        The umbrella's position is 0 when closed and 100 when fully open.
        The speaker's volume is 0 when off and 100 when fully on.
        The speaker also has a playlist field that can be set to a playlist name.

        With these newly bought devices, you want to plan a relaxing "Sunday-Garden Morning" for this weekend (2025-07-06):

        • At 06 : 30 fully open the newly-installed motorized patio umbrella in
        the backyard and start an outdoor speaker playing a gentle-jazz playlist
        at volume 30.
        • Ensure the music shuts off at 07 : 10.
        • Close the umbrella automatically at 10 : 30.
        """,
        actions=[
            Action(name="create_device",          kwargs={
                "id": "umbrella_by",
                "type": "motorized_umbrella",

                "location": "Backyard",
                "vendor": "SunSetter",
                "model": "SmartShade Pro",
                "firmware_version": "1.0.0",
                "state_params": ["position","power"],
                "state": {"position": 0, "power": "off"}          # 0 = closed
            }),
            Action(name="create_device",          kwargs={
                "id": "speaker_by",
                "type": "speaker",

                "location": "Backyard",
                "vendor": "Sonos",
                "model": "Move 2",
                "firmware_version": "1.0.0",
                "state_params": ["power","volume","playlist"],
                "state": {"power": "off", "volume": 0, "playlist": ""}
            }),
            Action(name="schedule_device_update", kwargs={
                "device_id": "umbrella_by",
                "timestamp": "2025-07-06T06:30:00",
                "update": {"power": "on", "position": 100}        # 100 = fully open
            }),
            Action(name= "schedule_device_update_timer", kwargs={
                "device_id": "speaker_by",
                "timestamp": "2025-07-06T06:30:00",
                "timestamp_end": "2025-07-06T07:10:00",
                "update": {"power": "on", "volume": 30,
                        "playlist": "gentle-jazz"}
            }),
            Action(name="schedule_device_update", kwargs={
                "device_id": "umbrella_by",
                "timestamp": "2025-07-06T10:30:00",
                "update": {"position": 0}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_22",
        instruction="""
        The credit-card bill is due today (2025-08-15):
        • Pull up the bill-payment reminder and CC John's e-mail on it.
        • Blink the master-bedroom ceiling light at 09:55 with brightness 25 and turn it off at
          10:30.
        """,
        actions=[
            Action(name="manage_reminders",        kwargs={
                "action":"list_all_names_ids"
            }),
            Action(name="manage_reminders",        kwargs={
                "action":"get",
                "reminder_id":"rem_94f92a43"
            }),
            Action(name="list_members",            kwargs={}),
            Action(name="manage_reminders",        kwargs={
                "action":"update",
                "reminder_id":"rem_94f92a43",
                "updates": {"meta":{"email_cc":"john@example.com"}}
            }),
            Action(name="list_devices",            kwargs={"type": "light"}),
            Action(name= "schedule_device_update_timer", kwargs={
                "device_id": "light_br_ceiling",
                "timestamp": "2025-08-15T09:55:00",
                "timestamp_end": "2025-08-15T10:30:00",
                "update": {"power":"on","brightness":25}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_23",
        instruction="""
        Get ready for annual car maintenance (due 2025-12-01):
        • Reactivate the dormant reminder for it.
        • At 07:55 on the due date, turn on the living-room ceiling light to warm orange (brightness 100, hue 30, saturation 90); turn it off at
          17:00.
        """,
        actions=[
            Action(name="manage_reminders",        kwargs={
                "action":"list_all_names_ids"
            }),
            Action(name="manage_reminders",        kwargs={
                "action":"get",
                "reminder_id":"rem_8f9fd8ae"
            }),
            Action(name="manage_reminders",        kwargs={
                "action":"update",
                "reminder_id":"rem_8f9fd8ae",
                "updates":{"status":"active"}
            }),
            Action(name="list_devices",            kwargs={"type": "light"}),
            Action(name= "schedule_device_update_timer", kwargs={
                "device_id":"light_lr_ceiling",
                "timestamp":"2025-12-01T07:55:00",
                "timestamp_end": "2025-12-01T17:00:00",
                "update":{"power":"on","brightness":100,
                          "color":{"hue":30,"saturation":90}}
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_24",
        instruction="""
        Grandma and Grandpa arrive on 2025-07-25:
        • Make a reminder for 2025-07-28 10am to wash the guest linens (reminder id: rem_laundry_guest, name: Wash guest linens,priority: normal, notify via mobile push).
        • On 2025-07-25 22:00, close the east-bedroom curtain and set its ceiling light to a cosy
          dim blue-white (brightness 40, hue 210, saturation 40), then switch that light off at 23:00.
        • Re-open the curtain automatically the next day at 10am.
        """,
        actions=[
            Action(name="list_devices",   kwargs={"type":"light"}),
            Action(name="list_devices",   kwargs={"type":"curtain"}),

            Action(name="manage_reminders",         kwargs={
                "action":"create",
                "reminder_id":"rem_laundry_guest",
                "reminder": { "reminder_id":"rem_laundry_guest",

                             "target": {"type":"note","text":"Wash guest linens"},
                             "trigger": {"datetime":"2025-07-28T10:00:00"},
                             "actions": [{"type":"notify","channel":"mobile_push"}],
                             "meta": {"priority":"normal"}}
            }),
            Action(name="schedule_device_update",  kwargs={
                "device_id":"curtain_be",
                "timestamp":"2025-07-25T22:00:00",
                "update":{"position":0}
            }),
            Action(name= "schedule_device_update_timer", kwargs={
                "device_id":"light_be_ceiling",
                "timestamp":"2025-07-25T22:00:00",
                "timestamp_end": "2025-07-25T23:00:00",
                "update":{"power":"on","brightness":40,
                          "color":{"hue":210,"saturation":40}}
            }),

            Action(name="schedule_device_update",  kwargs={
                "device_id":"curtain_be",
                "timestamp":"2025-07-26T10:00:00",
                "update":{"position":100}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_25",
        instruction="""
        Friends David and Sarah are coming for dinner on 2025-07-06:
        • At 18:20, turn the living-room ceiling light to a warm 70 % brightness (hue 50, saturation 70).
        • Shut it off at 21:30.
        """,
        actions=[
            Action(name="list_devices",   kwargs={"type":"light"}),
            Action(name= "schedule_device_update_timer", kwargs={
                "device_id":"light_lr_ceiling",
                "timestamp":"2025-07-06T18:20:00",
                "timestamp_end": "2025-07-06T21:30:00",
                "update":{"power":"on","brightness":70,
                          "color":{"hue":50,"saturation":70}}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_26",
        instruction="""
        You want the system to report the trigger time for your shopping-list reminder (reminder_id: rem_4fb3637f).
        Five minutes before the reminder, flash the living-room ceiling light bright yellow (brightness 100, hue 50, saturation 100) and switch
        it off five minutes later.
        """,
        actions=[
            Action(name="manage_reminders",        kwargs={
                "action":"list_all_names_ids"
            }),
            Action(name="manage_reminders",        kwargs={
                "action":"get",
                "reminder_id":"rem_4fb3637f"
            }),
            Action(name="list_devices",            kwargs={
                "type":"light"
            }),
            Action(name= "schedule_device_update_timer", kwargs={
                "device_id":"light_lr_ceiling",
                "timestamp":"2025-06-29T08:55:00",
                "timestamp_end": "2025-06-29T09:05:00",
                "update":{"power":"on","brightness":100,
                          "color":{"hue":50,"saturation":100}}
            }),
        ],
        outputs=[
            "2025-06-29T09:00:00-07:00"
        ]
    ),
    Task(
        annotator="0",
        user_id="res_27",
        instruction="""
        Starting tonight (2025-07-28) every night at 20:55:
        • Blink the master bedroom's bedside lamp (lamp_br_night) bright red (brightness 100, hue 0, saturation 100) to remind you to take medication,
          dim it after 10 minutes to 30% brightness, and turn it off at 21:10.
        • Extend the default snooze on the medication reminder to 10 minutes.
        """,
        actions=[
            Action(name="list_devices",   kwargs={"type":"light"}),
            Action(name= "schedule_device_update_timer", kwargs={
                "device_id":"lamp_br_night",
                "timestamp":"2025-07-28T20:55:00",
                "timestamp_end":"2025-07-28T21:10:00",
                "update":{"power":"on","brightness":100,
                          "color":{"hue":0,"saturation":100}},
                "rrule":"FREQ=DAILY"
            }),
            Action(name="schedule_device_update",  kwargs={
                "device_id":"lamp_br_night",
                "timestamp":"2025-07-28T21:05:00",
                "update":{"brightness":30},
                "rrule":"FREQ=DAILY"
            }),
            Action(name="manage_reminders",        kwargs={
                "action":"list_all_names_ids"
            }),
            Action(name="manage_reminders",        kwargs={
                "action":"get",
                "reminder_id":"rem_254afa34"
            }),
            Action(name="manage_reminders",        kwargs={
                "action":"update",
                "reminder_id":"rem_254afa34",
                "updates":{"meta":{"snooze_default_min":10}}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_28",
        instruction="""
        Dad's birthday party (2025-09-12):
        • At 17:45 set the living-room ceiling light to a warm festive glow (brightness 60, hue 30, saturation 70)
        • Turn it off at 19:00.
        • Set a remainder two days (2025-09-10) before at 9 AM to buy him a gift, push it to mobile.
        """,
        actions=[
            Action(name="list_devices",   kwargs={"type":"light"}),
            Action(name= "schedule_device_update_timer", kwargs={
                "device_id":"light_lr_ceiling",
                "timestamp":"2025-09-12T17:45:00",
                "timestamp_end":"2025-09-12T19:00:00",
                "update":{"power":"on","brightness":60,
                          "color":{"hue":30,"saturation":70}},
            }),

            Action(name="manage_reminders",         kwargs={
                "action":"create",
                "reminder_id":"rem_dads_gift",
                "reminder": {"reminder_id":"rem_dads_gift",

                             "trigger": {"datetime":"2025-09-10T09:00:00"},
                             "actions": [{"type":"notify","channel":"mobile_push"}],
                             "meta": {"priority":"normal"}}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_29",
        instruction="""
        On 2025-07-30 set up HVAC-filter maintenance:
        • Make a list called "HVAC Filter Replacements" (list id: list_hvac_filter, name: HVAC Filter Replacements, tags: maintenance, hvac).
        • Build a reminder for 2025-09-01 09:00 using that list (reminder id: rem_hvac_filter, name: Replace HVAC filter, priority: normal, notify via mobile push).
        • At 09:05 on the same day shut the main heater off for safety.
        """,
        actions=[
            Action(name="manage_custom_list",      kwargs={
                "action":"create",
                "list_id":"list_hvac_filter",
                "name": "HVAC Filter Replacements",
                "tags":["maintenance","hvac"]
            }),
            Action(name="manage_reminders",         kwargs={
                "action":"create",
                "reminder_id":"rem_hvac_filter",
                "reminder": {"reminder_id":"rem_hvac_filter",

                             "target": {"type":"entity","entity_type":"list",
                                        "entity_id":"list_hvac_filter"},
                             "trigger": {"datetime":"2025-09-01T09:00:00"},
                             "actions": [{"type":"notify","channel":"mobile_push"}],
                             "meta": {"priority":"normal"}}
            }),
            Action(name="list_devices",           kwargs={"type": "heater"}),
            Action(name="schedule_device_update",  kwargs={
                "device_id":"heater_home",
                "timestamp":"2025-09-01T09:05:00",
                "update":{"power":"off"}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_30",
        instruction="""
        Prepare the west-bedroom for Mike's weekend stay (visit runs 07-12 →
        07-14):
        • Update Mike's guest profile with his visit dates.
        • Close the west-bedroom blackout curtain and turn its ceiling light on
          to 30 %.
        • Remind yourself on 07-15 09:00 to wash Mike's guest linens (reminder id: rem_linen_wash_mb, name: Wash Mike guest linens, priority: normal, notify via mobile push).
        • Switch that ceiling light off at 23:00 tonight (2025-07-10).
        """,
        actions=[
            Action(name="list_devices",   kwargs={"type":"light"}),
            Action(name="list_devices",   kwargs={"type":"curtain"}),

            Action(name="upsert_member",           kwargs={
                "id":"michael_brown",
                "profile":{"visit_next_start":"2025-07-12",
                           "visit_next_end":"2025-07-14"}
            }),
            Action(name="update_device_state",     kwargs={
                "device_id":"curtain_bw",
                "update":{"position":0}
            }),
            Action(name="update_device_state_timer",     kwargs={
                "device_id":"light_bw_ceiling",
                "timestamp_end":"2025-07-10T23:00:00",
                "update":{"power":"on","brightness":30}
            }),
            Action(name="manage_reminders",         kwargs={
                "action": "create",
                "reminder_id":"rem_linen_wash_mb",
                "reminder": {"reminder_id":"rem_linen_wash_mb",

                             "target": {"type":"note","text":"Wash Mike guest linens"},
                             "trigger": {"datetime":"2025-07-15T09:00:00"},
                             "actions": [{"type":"notify","channel":"mobile_push"}],
                             "meta": {"priority":"normal"}}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_31",
        instruction="""
        Today is 2025-07-30. At 06:30 run the existing "Good Morning" scene.
        Five minutes later, raise the
        living-room ceiling light to 80 % brightness and fully open Olivia's west-bedroom curtain.
        """,
        actions=[
            Action(name="list_scenes",   kwargs={}),
            Action(name="list_sensor_names_ids",  kwargs={}),
            Action(name="schedule_scene_run",     kwargs={
                "scene_id": "scene_good_morning",
                "timestamp": "2025-07-30T06:30:00"
            }),
            Action(name="list_devices",           kwargs={"type": "light"}),
            Action(name="list_devices",           kwargs={"type": "curtain"}),
            Action(name="schedule_device_update", kwargs={
                "device_id": "light_lr_ceiling",
                "timestamp": "2025-07-30T06:35:00",
                "update": {"power": "on", "brightness": 80}
            }),
            Action(name="schedule_device_update", kwargs={
                "device_id": "curtain_bw",
                "timestamp": "2025-07-30T06:35:00",
                "update": {"position": 100}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_32",
        instruction="""
        Tonight (2025-07-28) at 22:00 trigger scene "Good Night"; at 22:30 dim the night-stand
        lamp to 5 % brightness and lower the central-heater set-point to 19 °C.
        """,
        actions=[
            Action(name="list_scenes",   kwargs={}),
            Action(name="list_devices",  kwargs={"type": "light"}),
            Action(name="list_devices",  kwargs={"type": "heater"}),

            Action(name="schedule_scene_run",     kwargs={
                "scene_id": "scene_good_night",
                "timestamp": "2025-07-28T22:00:00"
            }),
            Action(name="schedule_device_update", kwargs={
                "device_id": "lamp_br_night",
                "timestamp": "2025-07-28T22:30:00",
                "update": {"brightness": 5}
            }),
            Action(name="schedule_device_update", kwargs={
                "device_id": "heater_home",
                "timestamp": "2025-07-28T22:30:00",
                "update": {"setpoint_c": 19}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_33",
        instruction="""
        Create a new scene called "Homework Time":
        • East-bedroom ceiling light to cool-white 90 %.
        • East-bedroom ceiling light color to kelvin 5000
        • East-bedroom bedside lamp to 100 % bright white.
        • East-bedroom bedside light color to kelvin 5000
        • East-bedroom curtain closed.
        Schedule this scene to run at 4pm on 2025-07-01.
        Describe it as Bright focus lighting after school.
        """,
        actions=[
            Action(name="list_scenes",   kwargs={}),
            Action(name="list_devices",  kwargs={"type": "light"}),
            Action(name="list_devices",  kwargs={"type": "curtain"}),

            Action(name="upsert_scene",           kwargs={
                "id": "scene_homework_time",
                "name": "Homework Time",
                "description": "Bright focus lighting after school.",
                "actions": [
                    {"device_id": "light_be_ceiling",
                     "update": {"power": "on", "brightness": 90,
                                "color": {"kelvin": 5000}}},
                    {"device_id": "lamp_be_bedside",
                     "update": {"power": "on", "brightness": 100,
                                "color": {"kelvin": 5000}}},
                    {"device_id": "curtain_be",
                     "update": {"position": 0}}
                ]
            }),
            Action(name="schedule_scene_run",     kwargs={
                "scene_id": "scene_homework_time",
                "timestamp": "2025-07-01T16:00:00",
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_34",
        instruction="""
        This Saturday (2025-07-05) at 19:00 start "Movie Time".
        Two hours later restore the living-room ceiling light to 60 % brightness (kelvin 3000),
        half-open the curtain, and set the AC back to auto fan.
        """,
        actions=[
            Action(name="list_scenes",   kwargs={}),
            Action(name="list_devices",  kwargs={"type": "light"}),
            Action(name="list_devices",  kwargs={"type": "curtain"}),
            Action(name="list_devices",  kwargs={"type": "ac"}),

            Action(name="schedule_scene_run",     kwargs={
                "scene_id": "scene_movie_time",
                "timestamp": "2025-07-05T19:00:00"
            }),
            Action(name="schedule_device_update", kwargs={
                "device_id": "light_lr_ceiling",
                "timestamp": "2025-07-05T21:00:00",
                "update": {"power": "on", "brightness": 60,
                           "color": {"kelvin": 3000}}
            }),
            Action(name="schedule_device_update", kwargs={
                "device_id": "curtain_lr",
                "timestamp": "2025-07-05T21:00:00",
                "update": {"position": 50}
            }),
            Action(name="schedule_device_update", kwargs={
                "device_id": "ac_home",
                "timestamp": "2025-07-05T21:00:00",
                "update": {"fan_speed": "auto"}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_35",
        instruction="""
        Install a smart humidifier in the master bedroom
        - ID: humidifier_br
        - Type: humidifier
        - Name: Master-Bedroom Humidifier
        - Location: Master Bedroom
        - Vendor: Levoit
        - Model: Vital 200S
        - Firmware version: 1.0.0
        - State parameters: power, mode, humidity_setpoint_pct
        - State: power=off, mode=auto, humidity_setpoint_pct=45
        On 2025-07-28 at 22:00 turn it on in sleep-mode and shut it off at 03:00 the next morning.
        """,
        actions=[
            Action(name="create_device",          kwargs={
                "id": "humidifier_br",
                "type": "humidifier",

                "location": "Master Bedroom",
                "vendor": "Levoit",
                "model": "Vital 200S",
                "firmware_version": "1.0.0",
                "state_params": ["power","mode","humidity_setpoint_pct"],
                "state": {"power": "off", "mode": "auto", "humidity_setpoint_pct": 45}
            }),
            Action(name="add_device_to_room",     kwargs={
                "room_id": "bedroom_master",
                "device_id": "humidifier_br"
            }),
            Action(name= "schedule_device_update_timer", kwargs={
                "device_id": "humidifier_br",
                "timestamp": "2025-07-28T22:00:00",
                "timestamp_end": "2025-07-29T03:00:00",
                "update": {"power": "on", "mode": "sleep"}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_36",
        instruction="""
        Create an "Away Mode" scene that shuts every light (all ceiling lights, floor lamp, night lamps, and desk lamps) and the HVAC.
        Turn it on now (2025-07-29 11:00).
        """,
        actions=[
            Action(name="list_scenes",   kwargs={}),
            Action(name="list_devices",  kwargs={}),
            Action(name="upsert_scene",  kwargs={
                "id": "scene_away_mode",
                "name": "Away Mode",
                "description": "Shuts off all lights and HVAC.",
                "actions": [
                    {"device_id": "light_lr_ceiling", "update": {"power":"off"}},
                    {"device_id": "light_lr_floor", "update": {"power":"off"}},
                    {"device_id": "light_br_ceiling", "update": {"power":"off"}},
                    {"device_id": "lamp_br_night", "update": {"power":"off"}},
                    {"device_id": "light_bw_ceiling", "update": {"power":"off"}},
                    {"device_id": "lamp_bw_desk", "update": {"power":"off"}},
                    {"device_id": "light_be_ceiling", "update": {"power":"off"}},
                    {"device_id": "lamp_be_bedside", "update": {"power":"off"}},
                    {"device_id": "heater_home", "update": {"power":"off"}},
                    {"device_id": "ac_home", "update": {"power":"off"}}
                ]
            }),
            Action(name="schedule_scene_run",     kwargs={
                "scene_id": "scene_away_mode",
                "timestamp": "2025-07-29T11:00:00"
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_37",
        instruction="""
        On 2025-07-28 at 21:00, automatically run scene "Good Night".
        Turn on the night-stand lamp to 100 % brightness and turn it off 15 minutes later.
        """,
        actions=[
            Action(name="list_scenes",   kwargs={}),
            Action(name="schedule_scene_run",     kwargs={
                "scene_id": "scene_good_night",
                "timestamp": "2025-07-28T21:00:00"
            }),
            Action(name="list_devices",  kwargs={"type": "light"}),
            Action(name= "schedule_device_update_timer", kwargs={
                "device_id": "lamp_br_night",
                "timestamp": "2025-07-28T21:00:00",
                "timestamp_end": "2025-07-28T21:15:00",
                "update": {"brightness": 100}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_38",
        instruction="""
        Set up a "Family Movie Marathon" for Friday, 2025-08-18:
        • At 16:00 run the existing "Movie Time" scene.
        • Simultaneously dim the living-room floor lamp to 10 %
        • At 18:30 restore the floor lamp to 60 %, fully open the living-room
        curtain.
        """,
        actions=[
            Action(name="list_scenes",   kwargs={}),
            Action(name="list_devices",  kwargs={"type": "light"}),
            Action(name="list_devices",  kwargs={"type": "curtain"}),
            # 16:00 actions
            Action(name="schedule_scene_run",     kwargs={
                "scene_id": "scene_movie_time",
                "timestamp": "2025-08-18T16:00:00"
            }),
            Action(name="schedule_device_update", kwargs={
                "device_id": "light_lr_floor",
                "timestamp": "2025-08-18T16:00:00",
                "update": {"power":"on","brightness":10}
            }),

            # 18:30 restore actions
            Action(name="schedule_device_update", kwargs={
                "device_id": "light_lr_floor",
                "timestamp": "2025-08-18T18:30:00",
                "update": {"brightness":60}
            }),
            Action(name="schedule_device_update", kwargs={
                "device_id": "curtain_lr",
                "timestamp": "2025-08-18T18:30:00",
                "update": {"position":100}
            }),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_39",
        instruction="""
        Create an "Evacuate" scene: all lights full-bright, curtains open,
        HVAC off. You want the system to report if the bedroom smoke detector reports CO.
        """,
        actions=[
            Action(name="list_scenes",   kwargs={}),
            Action(name="list_devices",  kwargs={}),

            Action(name="upsert_scene",           kwargs={
                "id": "scene_evacuate",


                "actions": [
                    {"device_id": "light_lr_ceiling",
                     "update": {"power":"on","brightness":100}},
                    {"device_id": "light_lr_floor",
                     "update": {"power":"on","brightness":100}},
                    {"device_id": "light_br_ceiling",
                     "update": {"power":"on","brightness":100}},
                    {"device_id": "light_br_night",
                     "update": {"power":"on","brightness":100}},
                    {"device_id": "light_bw_ceiling",
                     "update": {"power":"on","brightness":100}},
                    {"device_id": "light_bw_desk",
                     "update": {"power":"on","brightness":100}},
                    {"device_id": "light_be_ceiling",
                     "update": {"power":"on","brightness":100}},
                    {"device_id": "light_be_bedside",
                     "update": {"power":"on","brightness":100}},
                    {"device_id": "curtain_lr",
                     "update": {"position":100}},
                    {"device_id": "curtain_br",
                     "update": {"position":100}},
                    {"device_id": "curtain_bw",
                     "update": {"position":100}},
                    {"device_id": "curtain_be",
                     "update": {"position":100}},
                    {"device_id": "heater_home",
                     "update": {"power":"off"}},
                    {"device_id": "ac_home",
                     "update": {"power":"off"}}
                ]
            }),
            Action(name="list_sensor_names_ids",   kwargs={}),
            Action(name="get_sensor_state", kwargs={
                "sensor_id": "sensor_bed_smoke"
            }),
        ],
        outputs=[
            '"co_detected": false',
        ]
    ),
    Task(
        annotator="0",
        user_id="res_40",
        instruction="""
        On August 1 2025 at 08:00 run "Good Morning" and then start the dishwasher for 2 hours.
        """,
        actions=[
            Action(name="list_scenes",   kwargs={}),
            Action(name="list_sensor_names_ids",  kwargs={}),
            Action(name="list_devices", kwargs={"type": "dishwasher"}),
            Action(name="schedule_scene_run",     kwargs={
                "scene_id": "scene_good_morning",
                "timestamp": "2025-08-01T08:00:00"
            }),
            Action(name="schedule_device_update_timer", kwargs={
                "device_id": "dishwasher_kt",
                "timestamp": "2025-08-01T08:00:00",
                "timestamp_end": "2025-08-01T10:00:00",
                "update": {"power":"on"}
            }),
        ],
        outputs=[]
    ),

]
