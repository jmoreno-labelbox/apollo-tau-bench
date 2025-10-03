from tau_bench.types import Action, Task
# list of tasks
TASKS = [
    # ─────────────────────────────────────────────────────────────────────────────
    # Living-room air-quality­/temperature quick fix with scheduled rollback
    Task(
        annotator="0",
        user_id="res_01",
        instruction="""
        The time is 15:00 on 2025-07-28. Check the current temperature from the Living Room Thermometer and the CO2 level from the Living Room Air-Quality Sensor.

        You need the following actions to take place if either the temperature rises above 22°C OR the CO2 levels surpass 750 ppm:
        • Activate your central AC with these specific settings: cool mode, 22°C, and high fan speed
        • Fully open your Living Room curtain
        • Adjust your Living Room floor lamp to 40% brightness

        Additionally, you want all these devices to automatically readjust to different settings at 16:30 on 2025-07-28:
        • AC should power off
        • Curtain should adjust to a 50% position
        • Floor lamp should be set to 60% brightness
        """,
        actions=[
            Action(name="ListSensorNamesIds",  kwargs={}),
            Action(name="ListDevices",           kwargs={"type": "curtain"}),
            Action(name="ListDevices",           kwargs={"type": "light"}),
            Action(name="ListDevices",           kwargs={"type": "ac"}),
            Action(name="GetSensorState",       kwargs={"sensor_id": "sensor_lr_thermometer"}),
            Action(name="GetSensorState",       kwargs={"sensor_id": "sensor_lr_air_quality"}),
            Action(name="GetDevice",             kwargs={"device_id": "ac_home"}),
            Action(name="UpdateDeviceStateTimer",     kwargs={"device_id": "ac_home",
                                                                 "timestamp_end": "2025-07-28T16:30:00",
                                                                 "update": {"power": "on",
                                                                             "mode": "cool",
                                                                             "setpoint_c": 22,
                                                                             "fan_speed": "high"}}),

            Action(name="UpdateDeviceState",    kwargs={"device_id": "curtain_lr",
                                                          "update": {"position": 100}}),
            Action(name="UpdateDeviceState",    kwargs={"device_id": "light_lr_floor",
                                                          "update": {"power": "on",
                                                                     "brightness": 40}}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "curtain_lr",
                                                          "timestamp": "2025-07-28T16:30:00",
                                                          "update": {"position": 50}}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "light_lr_floor",
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
        Initiate a "Movie Night" mode starting at 20:00 on 2025-07-28. This entails the following:

        First, apply these changes:
        • Switch off your living room ceiling light
        • Set your living room floor lamp to 15% brightness
        • Close your living room curtain completely
        • Set the central AC to cool mode at 21°C with low fan speed

        Ensure the system remembers the current settings of all these devices. Then at 22:30, you want everything to revert to these specific settings:
        • Ceiling light: on, at 70% brightness
        • Floor lamp: 60% brightness
        • Curtain: fully open
        • AC: turned off
        """,
        actions=[
            Action(name="ListDevices",           kwargs={"type": "light"}),
            Action(name="ListDevices",           kwargs={"type": "curtain"}),
            Action(name="ListSensorNamesIds",  kwargs={}),
            Action(name="GetDevice",             kwargs={"device_id": "light_lr_ceiling"}),
            Action(name="GetDevice",             kwargs={"device_id": "light_lr_floor"}),
            Action(name="GetDevice",             kwargs={"device_id": "curtain_lr"}),
            Action(name="GetDevice",             kwargs={"device_id": "ac_home"}),
            Action(name="GetSensorState",       kwargs={"sensor_id": "camera_front_door"}),

            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "light_lr_ceiling",
                                                          "timestamp": "2025-07-28T20:00:00",
                                                          "update": {"power": "off"}}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "light_lr_floor",
                                                          "timestamp": "2025-07-28T20:00:00",
                                                          "update": {"power": "on",
                                                                     "brightness": 15}}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "curtain_lr",
                                                          "timestamp": "2025-07-28T20:00:00",
                                                          "update": {"position": 0}}),
            Action(name="ScheduleDeviceUpdateTimer", kwargs={"device_id": "ac_home",
                                                                 "timestamp": "2025-07-28T20:00:00",
                                                                 "timestamp_end": "2025-07-28T22:30:00",
                                                                 "update": {"power": "on",
                                                                            "mode": "cool",
                                                                            "setpoint_c": 21,
                                                                            "fan_speed": "low"}}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "light_lr_ceiling",
                                                          "timestamp": "2025-07-28T22:30:00",
                                                          "update": {"power": "on",
                                                                     "brightness": 70}}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "light_lr_floor",
                                                          "timestamp": "2025-07-28T22:30:00",
                                                          "update": {"power": "on",
                                                                     "brightness": 60}}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "curtain_lr",
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
        Commencing on Monday, August 1st, 2025, you aim to establish a weekday home routine:

        Arrange the following schedule for each weekday morning:
        • 06:45 - Fully open the curtain in the west bedroom
        • 06:50 - Adjust the west bedroom ceiling light to 70% brightness
        • 06:55 - Fully open the curtain in the living room

        Moreover, ensure the dishwasher operates in eco mode every weekday night at 23:00, with a cycle duration of 120 minutes, confirming the door is securely closed.
        """,
        actions=[
            Action(name="ListDevices", kwargs={"type": "curtain"}),
            Action(name="ListDevices", kwargs={"type": "light"}),
            Action(name="ListDevices", kwargs={"type": "dishwasher"}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "curtain_bw",
                                                          "timestamp": "2025-08-01T06:45:00",
                                                          "update": {"position": 100},
                                                          "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "light_bw_ceiling",
                                                          "timestamp": "2025-08-01T06:50:00",
                                                          "update": {"power": "on",
                                                                     "brightness": 70},
                                                          "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "curtain_lr",
                                                          "timestamp": "2025-08-01T06:55:00",
                                                          "update": {"position": 100},
                                                          "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "dishwasher_kt",
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
        As you head out this morning, you need to carry out an extensive shutdown routine. Here's your requirement:

        Initially, have the system provide a report if the front door is open (sensor_id: sensor_front_door) and if there is any motion detected in the hallway (sensor_id: sensor_hall_motion).

        Next, execute these tasks:
        • Turn off every light in the house (including living room ceiling and floor lights, all bedroom ceiling lights, night lamps, and desk lamps)
        • Switch off the AC
        • Completely close all curtains in the house

        For added security, ensure the living room ceiling light is activated at 30% brightness at 19:30 that evening (July 29th, 2025).
        """,
        actions=[
            Action(name="GetSensorState",       kwargs={"sensor_id": "sensor_front_door"}),
            Action(name="GetSensorState",       kwargs={"sensor_id": "sensor_hall_motion"}),
            Action(name="ListDevices",           kwargs={"type": "light"}),
            Action(name="ListDevices",           kwargs={"type": "curtain"}),
            Action(name="ListDevices",           kwargs={"type": "ac"}),

            # Eight lights off
            *[Action(name="UpdateDeviceState",
                     kwargs={"device_id": did, "update": {"power": "off"}})
              for did in ["light_lr_ceiling", "light_lr_floor", "light_br_ceiling",
                          "lamp_br_night", "light_bw_ceiling", "lamp_bw_desk",
                          "light_be_ceiling", "lamp_be_bedside"]],

            Action(name="UpdateDeviceState",    kwargs={"device_id": "ac_home",
                                                          "update": {"power": "off"}}),

            *[Action(name="UpdateDeviceState",
                     kwargs={"device_id": cid, "update": {"position": 0}})
              for cid in ["curtain_lr", "curtain_br", "curtain_bw", "curtain_be"]],

            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "light_lr_ceiling",
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
        Upon detecting the smell of smoke, you require:

        • An immediate shutdown of both your heater and AC
        • The ceiling light and night lamp in your bedroom to activate at full brightness using a red alert color
        • Both your front and back door cameras to initiate recording
        • Automatic shutdown of the bedroom lights at 02:00 on July 29th, 2025
        """,
        actions=[
            Action(name="ListDevices",           kwargs={"type": "heater"}),
            Action(name="ListDevices",           kwargs={"type": "ac"}),
            Action(name="ListDevices",           kwargs={"type": "light"}),
            Action(name="ListSensorNamesIds",  kwargs={}),

            Action(name="UpdateDeviceState",    kwargs={"device_id": "heater_home",
                                                          "update": {"power": "off"}}),
            Action(name="UpdateDeviceState",    kwargs={"device_id": "ac_home",
                                                          "update": {"power": "off"}}),
            Action(name="UpdateDeviceStateTimer", kwargs={"device_id": "light_br_ceiling",
                                                                 "timestamp_end": "2025-07-29T02:00:00",
                                                                 "update": {"power": "on",
                                                                             "brightness": 100,
                                                                             "color": {"hue": 0,
                                                                                     "saturation": 100}}}),
            Action(name="UpdateDeviceStateTimer", kwargs={"device_id": "lamp_br_night",
                                                             "timestamp_end": "2025-07-29T02:00:00",
                                                             "update": {"power": "on",
                                                                        "brightness": 100,
                                                                        "color": {"hue": 0,
                                                                                  "saturation": 100}}}),
            Action(name="UpdateDeviceState",    kwargs={"device_id": "camera_front_door",
                                                          "update": {"recording": True}}),
            Action(name="UpdateDeviceState",    kwargs={"device_id": "camera_back_door",
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
        For integrating a new humidifier into your living room setup, ensure it is configured with these precise details:
        • ID: humidifier_lr
        • Name: Living Room Humidifier
        • Location: Living Room
        • Vendor: Levoit
        • Model: Classic300S
        • Firmware version: 1.0.0
        • State parameters: power, mode, humidity_setpoint_pct
        • State: power=off, mode=auto, humidity_setpoint_pct=45

        Once configuration is complete, direct the system to:
        • Include it in your living room's device list
        • Activate the humidifier in continuous mode with a 45% target at 15:00 on July 28th, 2025
        • Arrange for it to automatically deactivate at 17:00 on July 28th, 2025
        """,
        actions=[
            Action(name="CreateDevice",          kwargs={"id": "humidifier_lr",
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
            Action(name="AddDeviceToRoom",     kwargs={"room_id": "living_room",
                                                          "device_id": "humidifier_lr"}),
            Action(name="ScheduleDeviceUpdate",    kwargs={"device_id": "humidifier_lr",
                                                          "timestamp": "2025-07-28T15:00:00",
                                                          "update": {"power": "on",
                                                                     "mode": "continuous",
                                                                     "humidity_setpoint_pct": 45}}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "humidifier_lr",
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
        You purchased a Dyson HP04 auxiliary heater. Configure it with these settings:
        • ID: heater_bs_aux
        • Initial settings: off, heat mode, 15°C target
        • Location: Basement
        • Vendor: Dyson
        • Model: HP04
        • Firmware version: 2.0.0
        • State parameters: power, mode, setpoint_c
        • State: power=off, mode=heat, setpoint_c=15

        Ensure that, for safety reasons, the heater automatically shuts off at 07:00 daily starting July 29th, 2025
        """,
        actions=[
            Action(name="CreateDevice",          kwargs={"id": "heater_bs_aux",
                                                          "type": "heater",

                                                          "location": "Basement",
                                                          "vendor": "Dyson",
                                                          "model": "HP04",
                                                          "firmware_version": "2.0.0",
                                                          "state_params": ["power","mode","setpoint_c"],
                                                          "state": {"power": "off",
                                                                    "mode": "heat",
                                                                    "setpoint_c": 15}}),
            Action(name="AddDeviceToRoom",     kwargs={"room_id": "basement",
                                                          "device_id": "heater_bs_aux"}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "heater_bs_aux",
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
        You are setting up a Rachio Gen 3 smart sprinkler controller for your garden. Configure it as follows:
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

        For the watering schedule, arrange the following:
        • Daily watering should begin at 06:00 commencing July 29th, 2025
        • Each session is to run for 20 minutes in manual mode
        • Ensure the system automatically turns off at 06:20
        • Skip watering sessions on July 4th and 5th, 2026
        """,
        actions=[
            Action(name="CreateDevice",          kwargs={"id": "sprinkler_garden",
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
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={"device_id": "sprinkler_garden",
                                                                 "timestamp": "2025-07-29T06:00:00",
                                                                 "timestamp_end": "2025-07-29T06:20:00",
                                                                 "update": {"power": "on",
                                                                            "mode": "manual",
                                                                            "duration_min": 20},
                                                                 "rrule": "FREQ=DAILY;UNTIL=20260703T235959"}),
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={"device_id": "sprinkler_garden",
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
        Ensure a rooftop solar power meter is added to enhance energy efficiency of AC usage. Specifications include:

        An Enphase IQ7 power meter installation with:
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

        Coordinate the system to verify power generation and living room temperature, and set the AC to cool mode at 20°C with auto fan speed.

        Request the system to report on living room temperature and power generation.
        """,
        actions=[
            Action(name="CreateDevice",          kwargs={"id": "device_solar_power",
                                                          "type": "sensor",
                                                          "name": "Rooftop Solar Power Meter",
                                                          "location": "Roof",
                                                          "vendor": "Enphase",
                                                          "model": "IQ7",
                                                          "firmware_version": "1.0.1",
                                                          "state_params": ["power_generation_w"],
                                                          "state": {"power_generation_w": 4200}}),
            Action(name="ListSensorNamesIds",  kwargs={}),
            Action(name="GetSensorState",       kwargs={"sensor_id": "sensor_lr_thermometer"}),
            Action(name="GetDevice",             kwargs={"device_id": "device_solar_power"}),
            Action(name="ListDevices",           kwargs={"type": "ac"}),
            Action(name="UpdateDeviceState",    kwargs={"device_id": "ac_home",
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
        Implement an Aqara T1 ambient light sensor for automatic control of living room lighting. Requirements include:
        • ID: device_lr_lux
        • Name: Aqara T1 Ambient Light Sensor
        • Type: sensor
        • Location: Living Room
        • Vendor: Aqara
        • Model: T1 Ambient Light
        • Firmware version: 1.0.0
        • State parameters: illuminance_lux, battery_level
        • State: illuminance_lux=400, battery_level=100

        Ensure the system reports the illuminance level provided by it. Subsequently, have the system activate the living room ceiling light at 50% brightness.
        """,
        actions=[
            Action(name="CreateDevice",          kwargs={"id": "device_lr_lux",
                                                          "type": "sensor",
                                                          "name": "Aqara T1 Ambient Light Sensor",
                                                          "location": "Living Room",
                                                          "vendor": "Aqara",
                                                          "model": "T1 Ambient Light",
                                                          "firmware_version": "1.0.0",
                                                          "state_params": ["illuminance_lux","battery_level"],
                                                          "state": {"illuminance_lux": 400,
                                                                    "battery_level": 100}}),
            Action(name="AddDeviceToRoom",     kwargs={"room_id": "living_room",
                                                          "device_id": "device_lr_lux"}),
            Action(name="GetDevice",             kwargs={"device_id": "device_lr_lux"}),
            Action(name="ListDevices",           kwargs={"type": "light"}),
            Action(name="UpdateDeviceState",    kwargs={"device_id": "light_lr_ceiling",
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
        In the master bedroom, you wish to take a nap. To prepare, please:
        • Completely close the bedroom curtain
        • Switch off the ceiling light
        • Adjust the night lamp to 10% brightness with hue 30 and saturation 20
        • Set the AC to cool mode at 24°C with a low fan speed

        At 15:30 on the same day (July 28th), you would like everything to revert to these settings:
        • Open the curtain fully
        • Illuminate the ceiling light to 60% brightness
        • Adjust the night lamp to 30% brightness with hue 30 and saturation 60
        • Power off the AC
        """,
        actions=[
            Action(name="ListDevices",           kwargs={"type": "curtain"}),
            Action(name="ListDevices",           kwargs={"type": "light"}),
            Action(name="ListDevices",           kwargs={"type": "ac"}),

            Action(name="GetDevice",             kwargs={"device_id": "curtain_br"}),

            Action(name="UpdateDeviceState",    kwargs={"device_id": "curtain_br",
                                                          "update": {"position": 0}}),
            Action(name="UpdateDeviceState",    kwargs={"device_id": "light_br_ceiling",
                                                          "update": {"power": "off"}}),
            Action(name="UpdateDeviceState",    kwargs={"device_id": "lamp_br_night",
                                                          "update": {"power": "on",
                                                                     "brightness": 10,
                                                                     "color": {"hue": 30,
                                                                               "saturation": 20}}}),
            Action(name="UpdateDeviceStateTimer",    kwargs={"device_id": "ac_home",
                                                                "timestamp_end": "2025-07-28T15:30:00",
                                                                "update": {"power": "on",
                                                                           "mode": "cool",
                                                                           "setpoint_c": 24,
                                                                           "fan_speed": "low"}}),

            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "curtain_br",
                                                          "timestamp": "2025-07-28T15:30:00",
                                                          "update": {"position": 100}}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "light_br_ceiling",
                                                          "timestamp": "2025-07-28T15:30:00",
                                                          "update": {"power": "on",
                                                                     "brightness": 60}}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "lamp_br_night",
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
        You suspect that your sink may be leaking. Therefore, please:

        • Immediately switch off the dishwasher
        • Change the living room ceiling light to bright red as a visual alert
        • Activate recording on both front and back door cameras

        You desire a report from the system indicating if the leak detection sensor (sensor_id: sensor_sink_leak) confirms a leak.
        """,
        actions=[
            Action(name="UpdateDeviceState",    kwargs={"device_id": "dishwasher_kt",
                                                          "update": {"power": "off"}}),
            Action(name="UpdateDeviceState",    kwargs={"device_id": "light_lr_ceiling",
                                                          "update": {"power": "on",
                                                                     "brightness": 100,
                                                                     "color": {"hue": 0,
                                                                               "saturation": 100}}}),
            Action(name="UpdateDeviceState",    kwargs={"device_id": "camera_front_door",
                                                          "update": {"recording": True}}),
            Action(name="UpdateDeviceState",    kwargs={"device_id": "camera_back_door",
                                                          "update": {"recording": True}}),
            Action(name="ListSensorNamesIds",  kwargs={}),
            Action(name="GetSensorState",       kwargs={"sensor_id": "sensor_sink_leak"}),
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
        Initiate an energy-saving examination. Initially, generate a report on these conditions:
        • Presence of motion in the hallway
        • Detection of individuals at either the front or back door cameras

        If there is an absence of motion or individuals, you require:
        • All bedroom lighting fixtures to be deactivated (ceiling lights, night lamps, and desk lamps)
        • The system to examine the living room temperature and:
          - Deactivate the heater if it exceeds 20°C
          - Deactivate the AC if it is under 23°C
        """,
        actions=[
            Action(name="ListSensorNamesIds",  kwargs={}),
            Action(name="GetSensorState",       kwargs={"sensor_id": "sensor_hall_motion"}),
            Action(name="GetSensorState",       kwargs={"sensor_id": "camera_front_door"}),
            Action(name="GetSensorState",       kwargs={"sensor_id": "camera_back_door"}),
            Action(name="GetSensorState",       kwargs={"sensor_id": "sensor_lr_thermometer"}),

            Action(name="ListDevices",           kwargs={"type": "light"}),
            *[Action(name="UpdateDeviceState",
                     kwargs={"device_id": did, "update": {"power": "off"}})
              for did in ["light_br_ceiling", "lamp_br_night", "light_bw_ceiling",
                          "lamp_bw_desk", "light_be_ceiling", "lamp_be_bedside"]],

            Action(name="ListDevices",           kwargs={"type": "heater"}),
            Action(name="ListDevices",           kwargs={"type": "ac"}),
            Action(name="UpdateDeviceState",    kwargs={"device_id": "heater_home",
                                                          "update": {"power": "off"}}),
            Action(name="UpdateDeviceState",    kwargs={"device_id": "ac_home",
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
        Arrange the East Bedroom for an upcoming guest set to arrive on July 29th, 2025. By 21:00, ensure the following:

        • Fully close the curtain
        • Adjust the bedside lamp to 40% brightness with hue 50 and saturation 80
        • Adjust the ceiling light to 30% brightness with hue 210 and saturation 50

        By midnight (00:00 on July 30th), you necessitate:
        • Both lights to be switched off
        • The curtain to be fully open
        """,
        actions=[
            Action(name="ListDevices",           kwargs={"type": "curtain"}),
            Action(name="ListDevices",           kwargs={"type": "light"}),

            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "curtain_be",
                                                          "timestamp": "2025-07-29T21:00:00",
                                                          "update": {"position": 0}}),
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={"device_id": "lamp_be_bedside",
                                                                 "timestamp": "2025-07-29T21:00:00",
                                                                 "timestamp_end": "2025-07-30T00:00:00",
                                                                 "update": {"power": "on",
                                                                            "brightness": 40,
                                                                            "color": {"hue": 50,
                                                                                      "saturation": 80}}}),
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={"device_id": "light_be_ceiling",
                                                                 "timestamp": "2025-07-29T21:00:00",
                                                                 "timestamp_end": "2025-07-30T00:00:00",
                                                                 "update": {"power": "on",
                                                                            "brightness": 30,
                                                                            "color": {"hue": 210,
                                                                                      "saturation": 50}}}),
            Action(name="ScheduleDeviceUpdate", kwargs={"device_id": "curtain_be",
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
        Have the system perform the following tasks:

        • Evaluate the battery levels of your key sensors:
          - Living room thermometer
          - Hall motion sensor
          - Front door sensor
          - Bedroom smoke detector
          - Sink leak sensor

        Request the system to provide a full report. If any battery is under 80%, schedule a reminder to recharge it.
        Create reminder id: rem_battery_charge. Name: Charge battery (include sensor_id). Priority: normal. Notify via: mobile push.
        """,
        actions=[
            Action(name="ListSensorNamesIds",  kwargs={}),

            *[Action(name="GetSensorState", kwargs={"sensor_id": sid})
              for sid in ["sensor_lr_thermometer", "sensor_hall_motion",
                          "sensor_front_door", "sensor_bed_smoke",
                          "sensor_sink_leak"]],
            Action(name="ManageReminders", kwargs={"action": "create", "reminder_id": "rem_battery_charge", "reminder": {"name": "Charge battery (sensor_front_door)", "reminder_id": "rem_battery_charge", "priority": "normal", "notify_via": "mobile_push"}}),
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
        You are Robert, and on Monday (2025-07-30) desire a gentle 06:25 bedroom wake-up:
        • Include a smart coffee maker with the following specifications:
          - ID: coffee_maker_kt
          - Type: coffee_maker
          - Name: Kitchen Coffee Maker
          - Location: Kitchen
          - Vendor: Keurig
          - Model: K-Elite
          - Firmware version: 1.0.0
          - State parameters: power, brew_size, temperature_c
          - State: power=off, brew_size=mug, temperature_c=90
        • Position it in the kitchen and program it to brew a large
          travel cup at 06:28, then shut off at 06:40.
        • Partially open the master-bedroom blackout curtain immediately, then fully
          open it at 06:30.
        • Currently set the master-bedroom ceiling light to a very dim warm glow (brightness 10, hue 30, saturation 20),
          increasing to 50% brightness at 06:30.
        """,
        actions=[
            # create and schedule coffee maker
            Action(name="CreateDevice",           kwargs={
                "id": "coffee_maker_kt",
                "type": "coffee_maker",

                "location": "Kitchen",
                "vendor": "Keurig",
                "model": "K-Elite",
                "firmware_version": "1.0.0",
                "state_params": ["power","brew_size","temperature_c"],
                "state": {"power":"off","brew_size":"mug","temperature_c":90}
            }),
            Action(name="AddDeviceToRoom",      kwargs={
                "room_id": "kitchen",
                "device_id": "coffee_maker_kt"
            }),
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={
                "device_id": "coffee_maker_kt",
                "timestamp": "2025-07-30T06:28:00",
                "timestamp_end": "2025-07-30T06:40:00",
                "update": {"power":"on","brew_size":"travel","temperature_c":90}
            }),
            Action(name="ListDevices",           kwargs={"type": "curtain"}),
            Action(name="ListDevices",           kwargs={"type": "light"}),

            # bedroom curtain & light
            Action(name="UpdateDeviceState",     kwargs={
                "device_id": "curtain_br",
                "update": {"position":50}
            }),
            Action(name="ScheduleDeviceUpdate",  kwargs={
                "device_id": "curtain_br",
                "timestamp": "2025-07-30T06:30:00",
                "update": {"position":100}
            }),
            Action(name="UpdateDeviceState",     kwargs={
                "device_id": "light_br_ceiling",
                "update": {"power":"on","brightness":10,
                           "color":{"hue":30,"saturation":20}}
            }),
            Action(name="ScheduleDeviceUpdate",  kwargs={
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
        You have recently acquired an EV charger with the following specifications:
        id=ev_charger_garage, type=ev_charger, name="Garage EV Charger",
        location="Basement", vendor="ChargePoint", model="Home Flex",
        firmware_version="1.0.0",
        state_params=["power","mode","current_a"],
        state={"power":"off","mode":"charge","current_a":0}

        The next weekday is Monday 2025-07-30.
        You require the system to verify and provide Jessica's (emily_johnson) shift details.
        Subsequently, get the car ready by switching it ON at 06:00 with mode "preheat" and current_a:16.
        Proceed to turn it back OFF at 06:50.

        Additionally, give a report on the living room's temperature (sensor_id: sensor_lr_thermometer). If the temperature falls below 25 celsius, then
        activate the central heater with a temperature setting of 22.
        """,
        actions=[
            Action(name="CreateDevice",           kwargs={
                "id": "ev_charger_garage",
                "type": "ev_charger",

                "location": "Basement",
                "vendor": "ChargePoint",
                "model": "Home Flex",
                "firmware_version": "1.0.0",
                "state_params": ["power","mode","current_a"],
                "state": {"power":"off","mode":"charge","current_a":0}
            }),
            Action(name="AddDeviceToRoom",      kwargs={
                "room_id": "basement",
                "device_id": "ev_charger_garage"
            }),
            Action(name="ListMembers",            kwargs={}),
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={
                "device_id": "ev_charger_garage",
                "timestamp": "2025-07-30T06:00:00",
                "timestamp_end": "2025-07-30T06:50:00",
                "update": {"power":"on","mode":"preheat","current_a":16}
            }),
            Action(name="ListSensorNamesIds",   kwargs={}),
            Action(name="GetSensorState",        kwargs={"sensor_id":"sensor_lr_thermometer"}),
            Action(name="ListDevices",            kwargs={"type": "heater"}),
            Action(name="UpdateDeviceState",     kwargs={
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
        On Tuesday (2025-07-01), Emma boards the bus:
        • At 06:50, fully open the window-side curtain in her bedroom and adjust its
          ceiling light to 60% brightness.
        • Turn off that light at 07:40 and draw the curtain at 07:45.
        """,
        actions=[
            Action(name="ListMembers",            kwargs={}),
            Action(name="ListDevices",           kwargs={"type": "curtain"}),
            Action(name="ListDevices",           kwargs={"type": "light"}),

            Action(name="ScheduleDeviceUpdate",  kwargs={
                "device_id": "curtain_bw",
                "timestamp": "2025-07-01T06:50:00",
                "update": {"position":100}
            }),
            Action(name="ScheduleDeviceUpdate",  kwargs={
                "device_id": "light_bw_ceiling",
                "timestamp": "2025-07-01T06:50:00",
                "update": {"power":"on","brightness":60}
            }),
            Action(name="ScheduleDeviceUpdate",  kwargs={
                "device_id": "light_bw_ceiling",
                "timestamp": "2025-07-01T07:40:00",
                "update": {"power":"off"}
            }),
            Action(name="ScheduleDeviceUpdate",  kwargs={
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
        A friend named Sofia is coming over for a play-date on 2025-07-02:
        • Handle a high-priority reminder at 17:30 to drive Sofia home. (reminder_id: rem_mia_pickup, name: Sofia Pickup, priority: high, notify via mobile push)
        • Initiate recording now on the front-door camera and set the living-room
          ceiling light to 80% to guide her in.
        • Switch the light off at 17:45.
        """,
        actions=[
            Action(name="ListDevices",   kwargs={}),
            Action(name="ListSensorNamesIds",  kwargs={}),

            Action(name="ManageReminders",         kwargs={
                "action":"create",
                "reminder_id": "rem_mia_pickup",
                "reminder": {"reminder_id":"rem_mia_pickup",

                             "target": {"type":"note","text":"Drive Sofia home"},
                             "trigger": {"datetime":"2025-07-02T17:30:00"},
                             "actions": [{"type":"notify","channel":"mobile_push"}],
                             "meta": {"priority":"high"}}
            }),
            Action(name="ManageReminders",         kwargs={
                "action":"get",
                "reminder_id":"rem_mia_pickup"
            }),
            Action(name="UpdateDeviceState",     kwargs={
                "device_id": "camera_front_door",
                "update": {"recording": True}
            }),
            Action(name="UpdateDeviceStateTimer",     kwargs={
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
        It's trash night (2025-07-03). Kindly:
        • Request the system to report the details of the existing trash-night reminder (reminder_id: rem_eb55e94b).
        • Adjust the living-room floor lamp to full brightness now, and
          turn it off at 19:30.
        • Ask the system to check if the front door is open (sensor_id: sensor_front_door).
        """,
        actions=[
            Action(name="ManageReminders",        kwargs={
                "action":"list_all_names_ids"
            }),
            Action(name="ManageReminders",        kwargs={
                "action":"get",
                "reminder_id":"rem_eb55e94b"
            }),
            Action(name="ListDevices",            kwargs={"type": "light"}),
            Action(name="UpdateDeviceStateTimer",     kwargs={
                "device_id": "light_lr_floor",
                "timestamp_end": "2025-07-03T19:30:00",
                "update": {"power":"on","brightness":100}
            }),

            Action(name="GetSensorState",        kwargs={
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
        You purchased a motorized patio umbrella and a smart speaker for your backyard.
        The motorized umbrella is manufactured by SunSetter and the smart speaker is created by Sonos.
        The umbrella's model is SmartShade Pro (firmware version 1.0.0) and the speaker's model is Move 2 (firmware version 1.0.0).
        Both devices can be either on or off.
        The umbrella's position registers as 0 when it is closed and 100 when it's fully open.
        The speaker's volume level stands at 0 when turned off and 100 at maximum volume.
        The speaker also features a playlist option where you can set a playlist name.

        With these newly acquired devices, you plan to organize a relaxing "Sunday-Garden Morning" for this weekend (2025-07-06):

        • At 06 : 30, fully extend the newly-installed motorized patio umbrella in
        the backyard and initiate an outdoor speaker to play a gentle-jazz playlist
        at a volume of 30.
        • Make sure the music turns off by 07 : 10.
        • Automatically retract the umbrella at 10 : 30.
        """,
        actions=[
            Action(name="CreateDevice",          kwargs={
                "id": "umbrella_by",
                "type": "motorized_umbrella",

                "location": "Backyard",
                "vendor": "SunSetter",
                "model": "SmartShade Pro",
                "firmware_version": "1.0.0",
                "state_params": ["position","power"],
                "state": {"position": 0, "power": "off"}          # 0 = closed
            }),
            Action(name="CreateDevice",          kwargs={
                "id": "speaker_by",
                "type": "speaker",

                "location": "Backyard",
                "vendor": "Sonos",
                "model": "Move 2",
                "firmware_version": "1.0.0",
                "state_params": ["power","volume","playlist"],
                "state": {"power": "off", "volume": 0, "playlist": ""}
            }),
            Action(name="ScheduleDeviceUpdate", kwargs={
                "device_id": "umbrella_by",
                "timestamp": "2025-07-06T06:30:00",
                "update": {"power": "on", "position": 100}        # 100 = fully open
            }),
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={
                "device_id": "speaker_by",
                "timestamp": "2025-07-06T06:30:00",
                "timestamp_end": "2025-07-06T07:10:00",
                "update": {"power": "on", "volume": 30,
                        "playlist": "gentle-jazz"}
            }),
            Action(name="ScheduleDeviceUpdate", kwargs={
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
        The credit-card payment is due today (2025-08-15):
        • Display the bill-payment reminder and CC Robert's e-mail on it.
        • Flash the master-bedroom ceiling light at 09:55 with a brightness level of 25 and switch it off at
          10:30.
        """,
        actions=[
            Action(name="ManageReminders",        kwargs={
                "action":"list_all_names_ids"
            }),
            Action(name="ManageReminders",        kwargs={
                "action":"get",
                "reminder_id":"rem_94f92a43"
            }),
            Action(name="ListMembers",            kwargs={}),
            Action(name="ManageReminders",        kwargs={
                "action":"update",
                "reminder_id":"rem_94f92a43",
                "updates": {"meta":{"email_cc":"robert@example.com"}}
            }),
            Action(name="ListDevices",            kwargs={"type": "light"}),
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={
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
        Prepare for the annual car maintenance (scheduled for 2025-12-01):
        • Reactivate the dormant reminder associated with it.
        • On the due date at 07:55, activate the living-room ceiling light to a warm orange (brightness 100, hue 30, saturation 90), and switch it off at
          17:00.
        """,
        actions=[
            Action(name="ManageReminders",        kwargs={
                "action":"list_all_names_ids"
            }),
            Action(name="ManageReminders",        kwargs={
                "action":"get",
                "reminder_id":"rem_8f9fd8ae"
            }),
            Action(name="ManageReminders",        kwargs={
                "action":"update",
                "reminder_id":"rem_8f9fd8ae",
                "updates":{"status":"active"}
            }),
            Action(name="ListDevices",            kwargs={"type": "light"}),
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={
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
        Anticipate Grandma and Grandpa's visit on 2025-07-25:
        • Schedule a reminder for 2025-07-28 10am to handle the guest linens (reminder id: rem_laundry_guest, name: Wash guest linens,priority: normal, notify via mobile push).
        • On 2025-07-25 22:00, ensure the east-bedroom curtain is closed and the ceiling light is set to a cosy
          dim blue-white (brightness 40, hue 210, saturation 40), then ensure this light is turned off at 23:00.
        • Automatically open the curtain again the following day at 10am.
        """,
        actions=[
            Action(name="ListDevices",   kwargs={"type":"light"}),
            Action(name="ListDevices",   kwargs={"type":"curtain"}),

            Action(name="ManageReminders",         kwargs={
                "action":"create",
                "reminder_id":"rem_laundry_guest",
                "reminder": { "reminder_id":"rem_laundry_guest",

                             "target": {"type":"note","text":"Wash guest linens"},
                             "trigger": {"datetime":"2025-07-28T10:00:00"},
                             "actions": [{"type":"notify","channel":"mobile_push"}],
                             "meta": {"priority":"normal"}}
            }),
            Action(name="ScheduleDeviceUpdate",  kwargs={
                "device_id":"curtain_be",
                "timestamp":"2025-07-25T22:00:00",
                "update":{"position":0}
            }),
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={
                "device_id":"light_be_ceiling",
                "timestamp":"2025-07-25T22:00:00",
                "timestamp_end": "2025-07-25T23:00:00",
                "update":{"power":"on","brightness":40,
                          "color":{"hue":210,"saturation":40}}
            }),

            Action(name="ScheduleDeviceUpdate",  kwargs={
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
        On 2025-07-06, host a dinner for Michael and Jennifer:
        • At 18:20, adjust the living-room ceiling light to a warm glow with 70% brightness (hue 50, saturation 70).
        • Turn the light off at 21:30.
        """,
        actions=[
            Action(name="ListDevices",   kwargs={"type":"light"}),
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={
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
        Ensure the system provides the trigger time for your shopping-list reminder (reminder_id: rem_4fb3637f).
        Five minutes prior, flash the living-room ceiling light bright yellow (brightness 100, hue 50, saturation 100) and turn it off five minutes afterward.
        """,
        actions=[
            Action(name="ManageReminders",        kwargs={
                "action":"list_all_names_ids"
            }),
            Action(name="ManageReminders",        kwargs={
                "action":"get",
                "reminder_id":"rem_4fb3637f"
            }),
            Action(name="ListDevices",            kwargs={
                "type":"light"
            }),
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={
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
        Initiating tonight (2025-07-28) and at the same time every night at 20:55:
        • Flash the master bedroom's bedside lamp (lamp_br_night) in bright red (brightness 100, hue 0, saturation 100) as a reminder to take medication,
          then reduce it after 10 minutes to 30% brightness, turning it off at 21:10.
        • Adjust the default snooze for the medication reminder to 10 minutes.
        """,
        actions=[
            Action(name="ListDevices",   kwargs={"type":"light"}),
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={
                "device_id":"lamp_br_night",
                "timestamp":"2025-07-28T20:55:00",
                "timestamp_end":"2025-07-28T21:10:00",
                "update":{"power":"on","brightness":100,
                          "color":{"hue":0,"saturation":100}},
                "rrule":"FREQ=DAILY"
            }),
            Action(name="ScheduleDeviceUpdate",  kwargs={
                "device_id":"lamp_br_night",
                "timestamp":"2025-07-28T21:05:00",
                "update":{"brightness":30},
                "rrule":"FREQ=DAILY"
            }),
            Action(name="ManageReminders",        kwargs={
                "action":"list_all_names_ids"
            }),
            Action(name="ManageReminders",        kwargs={
                "action":"get",
                "reminder_id":"rem_254afa34"
            }),
            Action(name="ManageReminders",        kwargs={
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
        For Dad's birthday celebration (2025-09-12):
        • At 17:45 illuminate the living-room ceiling light with a warm festive glow (brightness 60, hue 30, saturation 70).
        • Ensure it is turned off at 19:00.
        • Schedule a reminder two days prior (2025-09-10) at 9 AM to purchase him a gift, pushing it to mobile.
        """,
        actions=[
            Action(name="ListDevices",   kwargs={"type":"light"}),
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={
                "device_id":"light_lr_ceiling",
                "timestamp":"2025-09-12T17:45:00",
                "timestamp_end":"2025-09-12T19:00:00",
                "update":{"power":"on","brightness":60,
                          "color":{"hue":30,"saturation":70}},
            }),

            Action(name="ManageReminders",         kwargs={
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
        Initiate HVAC-filter maintenance on 2025-07-30:
        • Create a list titled "HVAC Filter Replacements" (list id: list_hvac_filter, name: HVAC Filter Replacements, tags: maintenance, hvac).
        • Schedule a reminder for 2025-09-01 09:00 utilizing that list (reminder id: rem_hvac_filter, name: Replace HVAC filter, priority: normal, notify via mobile push).
        • At 09:05 on the same day, ensure the main heater is turned off for safety.
        """,
        actions=[
            Action(name="ManageCustomList",      kwargs={
                "action":"create",
                "list_id":"list_hvac_filter",
                "name": "HVAC Filter Replacements",
                "tags":["maintenance","hvac"]
            }),
            Action(name="ManageReminders",         kwargs={
                "action":"create",
                "reminder_id":"rem_hvac_filter",
                "reminder": {"reminder_id":"rem_hvac_filter",

                             "target": {"type":"entity","entity_type":"list",
                                        "entity_id":"list_hvac_filter"},
                             "trigger": {"datetime":"2025-09-01T09:00:00"},
                             "actions": [{"type":"notify","channel":"mobile_push"}],
                             "meta": {"priority":"normal"}}
            }),
            Action(name="ListDevices",           kwargs={"type": "heater"}),
            Action(name="ScheduleDeviceUpdate",  kwargs={
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
        Arrange the west-bedroom for Chris's weekend stay (visit spans 07-12 →
        07-14):
        • Update Chris's guest profile to include his visit dates.
        • Draw the west-bedroom blackout curtain shut and adjust its ceiling light to 30 %.
        • Set a reminder for 07-15 09:00 to launder Chris's guest linens (reminder id: rem_linen_wash_mb, name: Wash Chris guest linens, priority: normal, notify via mobile push).
        • Deactivate that ceiling light at 23:00 this evening (2025-07-10).
        """,
        actions=[
            Action(name="ListDevices",   kwargs={"type":"light"}),
            Action(name="ListDevices",   kwargs={"type":"curtain"}),

            Action(name="UpsertMember",           kwargs={
                "id":"michael_wilson",
                "profile":{"visit_next_start":"2025-07-12",
                           "visit_next_end":"2025-07-14"}
            }),
            Action(name="UpdateDeviceState",     kwargs={
                "device_id":"curtain_bw",
                "update":{"position":0}
            }),
            Action(name="UpdateDeviceStateTimer",     kwargs={
                "device_id":"light_bw_ceiling",
                "timestamp_end":"2025-07-10T23:00:00",
                "update":{"power":"on","brightness":30}
            }),
            Action(name="ManageReminders",         kwargs={
                "action": "create",
                "reminder_id":"rem_linen_wash_mb",
                "reminder": {"reminder_id":"rem_linen_wash_mb",

                             "target": {"type":"note","text":"Wash Chris guest linens"},
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
        On 2025-07-30, initiate the existing "Good Morning" scene at 06:30.
        After five minutes, increase the
        living-room ceiling light to 80% brightness and completely open Emma's west-bedroom curtain.
        """,
        actions=[
            Action(name="ListScenes",   kwargs={}),
            Action(name="ListSensorNamesIds",  kwargs={}),
            Action(name="ScheduleSceneRun",     kwargs={
                "scene_id": "scene_good_morning",
                "timestamp": "2025-07-30T06:30:00"
            }),
            Action(name="ListDevices",           kwargs={"type": "light"}),
            Action(name="ListDevices",           kwargs={"type": "curtain"}),
            Action(name="ScheduleDeviceUpdate", kwargs={
                "device_id": "light_lr_ceiling",
                "timestamp": "2025-07-30T06:35:00",
                "update": {"power": "on", "brightness": 80}
            }),
            Action(name="ScheduleDeviceUpdate", kwargs={
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
        On the night of 2025-07-28, activate the "Good Night" scene at 22:00; at 22:30, reduce the night-stand
        lamp brightness to 5% and adjust the central-heater set-point to 19 °C.
        """,
        actions=[
            Action(name="ListScenes",   kwargs={}),
            Action(name="ListDevices",  kwargs={"type": "light"}),
            Action(name="ListDevices",  kwargs={"type": "heater"}),

            Action(name="ScheduleSceneRun",     kwargs={
                "scene_id": "scene_good_night",
                "timestamp": "2025-07-28T22:00:00"
            }),
            Action(name="ScheduleDeviceUpdate", kwargs={
                "device_id": "lamp_br_night",
                "timestamp": "2025-07-28T22:30:00",
                "update": {"brightness": 5}
            }),
            Action(name="ScheduleDeviceUpdate", kwargs={
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
        Set up a new scene named "Homework Time":
        • Adjust the East-bedroom ceiling light to cool-white at 90 %.
        • Change the East-bedroom ceiling light color to kelvin 5000.
        • Set the East-bedroom bedside lamp to bright white at 100 %.
        • Adjust the East-bedroom bedside light color to kelvin 5000.
        • Close the East-bedroom curtain.
        Plan for this scene to activate at 4pm on 2025-07-01.
        Define it as Bright focus lighting after school.
        """,
        actions=[
            Action(name="ListScenes",   kwargs={}),
            Action(name="ListDevices",  kwargs={"type": "light"}),
            Action(name="ListDevices",  kwargs={"type": "curtain"}),

            Action(name="UpsertScene",           kwargs={
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
            Action(name="ScheduleSceneRun",     kwargs={
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
        On Saturday (2025-07-05) at 19:00, initiate "Movie Time".
        Two hours afterward, adjust the living-room ceiling light back to 60 % brightness (kelvin 3000),
        partially open the curtain, and switch the AC to auto fan.
        """,
        actions=[
            Action(name="ListScenes",   kwargs={}),
            Action(name="ListDevices",  kwargs={"type": "light"}),
            Action(name="ListDevices",  kwargs={"type": "curtain"}),
            Action(name="ListDevices",  kwargs={"type": "ac"}),

            Action(name="ScheduleSceneRun",     kwargs={
                "scene_id": "scene_movie_time",
                "timestamp": "2025-07-05T19:00:00"
            }),
            Action(name="ScheduleDeviceUpdate", kwargs={
                "device_id": "light_lr_ceiling",
                "timestamp": "2025-07-05T21:00:00",
                "update": {"power": "on", "brightness": 60,
                           "color": {"kelvin": 3000}}
            }),
            Action(name="ScheduleDeviceUpdate", kwargs={
                "device_id": "curtain_lr",
                "timestamp": "2025-07-05T21:00:00",
                "update": {"position": 50}
            }),
            Action(name="ScheduleDeviceUpdate", kwargs={
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
        Arrange the installation of a smart humidifier in the master bedroom
        - ID: humidifier_br
        - Type: humidifier
        - Name: Master-Bedroom Humidifier
        - Location: Master Bedroom
        - Vendor: Levoit
        - Model: Vital 200S
        - Firmware version: 1.0.0
        - State parameters: power, mode, humidity_setpoint_pct
        - State: power=off, mode=auto, humidity_setpoint_pct=45
        At 22:00 on 2025-07-28, enable it in sleep-mode and deactivate it at 03:00 the following morning.
        """,
        actions=[
            Action(name="CreateDevice",          kwargs={
                "id": "humidifier_br",
                "type": "humidifier",

                "location": "Master Bedroom",
                "vendor": "Levoit",
                "model": "Vital 200S",
                "firmware_version": "1.0.0",
                "state_params": ["power","mode","humidity_setpoint_pct"],
                "state": {"power": "off", "mode": "auto", "humidity_setpoint_pct": 45}
            }),
            Action(name="AddDeviceToRoom",     kwargs={
                "room_id": "bedroom_master",
                "device_id": "humidifier_br"
            }),
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={
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
        Develop an "Away Mode" scene that turns off every light (all ceiling lights, floor lamp, night lamps, and desk lamps) along with the HVAC.
        Activate it immediately (2025-07-29 11:00).
        """,
        actions=[
            Action(name="ListScenes",   kwargs={}),
            Action(name="ListDevices",  kwargs={}),
            Action(name="UpsertScene",  kwargs={
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
            Action(name="ScheduleSceneRun",     kwargs={
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
        On 2025-07-28 at 21:00, automatically initiate the scene "Good Night".
        Switch on the night-stand lamp to 100 % brightness, and switch it off 15 minutes later.
        """,
        actions=[
            Action(name="ListScenes",   kwargs={}),
            Action(name="ScheduleSceneRun",     kwargs={
                "scene_id": "scene_good_night",
                "timestamp": "2025-07-28T21:00:00"
            }),
            Action(name="ListDevices",  kwargs={"type": "light"}),
            Action(name= "ScheduleDeviceUpdateTimer", kwargs={
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
        Arrange a "Family Movie Marathon" for Friday, 2025-08-18:
        • At 16:00, activate the existing "Movie Time" scene.
        • Concurrently, dim the living-room floor lamp to 10 %
        • At 18:30, return the floor lamp to 60 %, and fully open the living-room
        curtain.
        """,
        actions=[
            Action(name="ListScenes",   kwargs={}),
            Action(name="ListDevices",  kwargs={"type": "light"}),
            Action(name="ListDevices",  kwargs={"type": "curtain"}),
            # 16:00 actions
            Action(name="ScheduleSceneRun",     kwargs={
                "scene_id": "scene_movie_time",
                "timestamp": "2025-08-18T16:00:00"
            }),
            Action(name="ScheduleDeviceUpdate", kwargs={
                "device_id": "light_lr_floor",
                "timestamp": "2025-08-18T16:00:00",
                "update": {"power":"on","brightness":10}
            }),

            # 18:30 restore actions
            Action(name="ScheduleDeviceUpdate", kwargs={
                "device_id": "light_lr_floor",
                "timestamp": "2025-08-18T18:30:00",
                "update": {"brightness":60}
            }),
            Action(name="ScheduleDeviceUpdate", kwargs={
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
        Handle the creation of an "Evacuate" scene: all lights full-bright, curtains open,
        HVAC off. The system should notify you if the bedroom smoke detector reports CO.
        """,
        actions=[
            Action(name="ListScenes",   kwargs={}),
            Action(name="ListDevices",  kwargs={}),

            Action(name="UpsertScene",           kwargs={
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
            Action(name="ListSensorNamesIds",   kwargs={}),
            Action(name="GetSensorState", kwargs={
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
        On August 1 2025 at 08:00, initiate "Good Morning" and subsequently run the dishwasher for 2 hours.
        """,
        actions=[
            Action(name="ListScenes",   kwargs={}),
            Action(name="ListSensorNamesIds",  kwargs={}),
            Action(name="ListDevices", kwargs={"type": "dishwasher"}),
            Action(name="ScheduleSceneRun",     kwargs={
                "scene_id": "scene_good_morning",
                "timestamp": "2025-08-01T08:00:00"
            }),
            Action(name="ScheduleDeviceUpdateTimer", kwargs={
                "device_id": "dishwasher_kt",
                "timestamp": "2025-08-01T08:00:00",
                "timestamp_end": "2025-08-01T10:00:00",
                "update": {"power":"on"}
            }),
        ],
        outputs=[]
    ),

]
