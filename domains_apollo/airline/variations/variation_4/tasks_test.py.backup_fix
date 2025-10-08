from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="USER_001",
        instruction="For Isabella Brown (emma.smith8074@example.com) on reservation NO6JO3, execute to rebook to HAT014 JFK→MIA on 2024-05-16 in business at total 270, paid only with payment_method_id credit_card_4421486. Also execute to record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-015, ATA 29), description 'Hydraulic system warning discovered during pre-flight inspection', corrective action 'Emergency repair procedures required for hydraulic system warning', technician TECH009, timestamp 2024-08-15T14:30:00Z, status In Progress. Provide the new flight number and the total cost.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "emma.smith8074@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "NO6JO3"}),
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-05-16", "status": ["available"], "origin": "JFK", "destination": "MIA"}),
            Action(name="GetFlightStatusByNumberAndDate", kwargs={"flight_number": "HAT014", "date": "2024-05-16"}),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-015",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(
                name="UpdateReservation",
                kwargs={
                    "reservation_id": "NO6JO3",
                    "cabin": "business",
                    "payment_method_id": "credit_card_4421486",
                    "flights": [
                        {"flight_number": "HAT014", "date": "2024-05-16", "origin": "JFK", "destination": "MIA", "price": 270}
                    ]
                }
            ),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "NO6JO3"})
        ],
        outputs=['"new_flight_number": "HAT014"', '"total_cost": 270'],
    ),


    Task(
        annotator="0",
        user_id="USER_002",
        instruction="Execute fleet operations management at PHX. Aircraft AC008 (PP-PTM, ATR72-600) requires scheduled B-Check maintenance. The aircraft status needs updating to 'Maintenance', along with a maintenance entry containing work order 'WO-2024-05-05-008' (ATA 05), description 'Scheduled B-Check inspection for PP-PTM at PHX', corrective action 'Perform scheduled B-Check inspection of systems and components', and timestamp '2024-05-05T11:00:00Z'. The current fleet utilization for ATR72-600 models should be checked with status filter for 'Active' and 'Maintenance' aircraft. Provide the created maintenance log ID.",
        actions=[
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC008",
                    "new_status": "Maintenance"
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC008",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check inspection for PP-PTM at PHX",
                    "work_order_id": "WO-2024-05-05-008",
                    "ata_chapter": "05",
                    "corrective_action": "Perform scheduled B-Check inspection of systems and components",
                    "event_timestamp_utc": "2024-05-05T11:00:00Z",
                    "status": "Scheduled"
                }
            ),
            Action(
                name="GetFleetUtilization",
                kwargs={
                    "model_filter": "ATR72-600",
                    "status_filter": ["Active", "Maintenance"]
                }
            )
        ],
        outputs=[
            '"maintenance_log_id": "ML026"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_003",
        instruction=(
            "Coordinate crew scheduling at DFW. Execute to log duty for Flight Attendants CM006 and CM021 on HAT022 (FL022) dated 2024-05-13 "
            "on A320neo: each 3.1 total (0 PIC, 0 SIC, 3.1 night, 0 instrument), 1 landing, 1 takeoff. Do not change assignments; verify via crew "
            "profiles. Also execute to record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-005, ATA 29), description "
            "'Hydraulic system warning discovered during pre-flight inspection', corrective action 'Emergency repair procedures required for hydraulic "
            "system warning', technician TECH009, timestamp 2024-08-15T14:30:00Z, status Completed. Return the flight number and confirmation."
        ),
        actions=[
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM006",
                    "flight_id": "FL022",
                    "flight_number": "HAT022",
                    "date": "2024-05-13",
                    "role": "Flight Attendant",
                    "aircraft_model": "A320neo",
                    "hours_flown": {"total": 3.1, "pic": 0, "sic": 0, "night": 3.1, "instrument": 0},
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM021",
                    "flight_id": "FL022",
                    "flight_number": "HAT022",
                    "date": "2024-05-13",
                    "role": "Flight Attendant",
                    "aircraft_model": "A320neo",
                    "hours_flown": {"total": 3.1, "pic": 0, "sic": 0, "night": 3.1, "instrument": 0},
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-005",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "Completed"
                }
            ),

            Action(name="GetCrewMemberDetails", kwargs={"crew_member_id": "CM006"}),
            Action(name="GetCrewMemberDetails", kwargs={"crew_member_id": "CM021"}),
        ],
        outputs=['"flight_number": "HAT022"', '"duty_time_logged": "confirmed"']
    ),



    Task(
        annotator="0",
        user_id="USER_004",
        instruction="Execute maintenance planning at MIA. Aircraft AC007 (PR-YJB, A220-300) has reported an avionics system malfunction during pre-flight inspection on 2024-05-04 at 07:30:00 UTC. The aircraft status requires updating to 'Maintenance', along with a maintenance entry for this 'Avionics Repair' (WO-2024-05-04-007, ATA 31, TECH012) containing status 'In Progress', description 'Avionics system malfunction discovered during pre-flight inspection' and corrective action 'Investigate and repair avionics system malfunction'. An 'Aircraft AOG' operational event should document this issue with details 'Aircraft PR-YJB AOG due to avionics system malfunction' and 'Resolved' status. Provide the maintenance log ID and the aircraft's updated status.",
        actions=[
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC007",
                    "new_status": "Maintenance"
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC007",
                    "maintenance_type": "Avionics Repair",
                    "description": "Avionics system malfunction discovered during pre-flight inspection",
                    "technician_id": "TECH012",
                    "work_order_id": "WO-2024-05-04-007",
                    "ata_chapter": "31",
                    "corrective_action": "Investigate and repair avionics system malfunction",
                    "event_timestamp_utc": "2024-05-04T07:30:00Z",
                    "status": "In Progress"
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Aircraft AOG",
                    "event_timestamp_utc": "2024-05-04T07:30:00Z",
                    "details": "Aircraft PR-YJB AOG due to avionics system malfunction",
                    "aircraft_id": "AC007",
                    "tail_number": "PR-YJB",
                    "status": "Resolved"
                }
            )
        ],
        outputs=[
            '"maintenance_log_id": "ML026"',
            '"aircraft_status": "Maintenance"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_005",
        instruction="Assist airline members regarding delays on flight HAT010 (FL009). For travel on 2024-06-03, you need to run a same-day DCA→ORD availability check (results may be none), summarize any operational events for HAT010, check Active fleet utilization, and create a tracking event: type 'Technical Issue', timestamp '2024-06-03T12:00:00Z', details 'Delay concerns on flight HAT010', status 'Active', linked to HAT010/FL009. Provide the availability check result (even if none), the HAT010 events summary, the fleet snapshot, and confirmation the customer-service event was created.",
        actions=[
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-06-03", "status": ["available"], "origin": "DCA", "destination": "ORD"}),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT010"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-06-03T12:00:00Z",
                    "details": "Delay concerns on flight HAT010",
                    "status": "Active",
                    "flight_number": "HAT010",
                    "flight_id": "FL009"
                }
            )
        ],
        outputs=[
            '"alternative_flights": "Same-day DCA→ORD search completed (may be none)"',
            '"operational_events": "Flight HAT010 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),


    Task(
        annotator="0",
        user_id="USER_006",
        instruction="Execute assisting a Gold member regarding delays on HAT029 (FL029). For travel on 2024-05-17, execute to list same-day ORD→LAX availability, summarize operational events for HAT029, check Active fleet utilization, and create a tracking event: type 'Technical Issue', timestamp '2024-05-17T12:45:00Z', details 'Delay concerns on flight HAT029', status 'Active', linked to HAT029/FL029. Provide alternatives, the HAT029 event summary, fleet status, and confirmation the customer-service event was created.",
        actions=[
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-05-17", "status": ["available"], "origin": "ORD", "destination": "LAX"}),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT029"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-17T12:45:00Z",
                    "details": "Delay concerns on flight HAT029",
                    "status": "Active",
                    "flight_number": "HAT029",
                    "flight_id": "FL029"
                }
            )
        ],
        outputs=[
            '"alternative_flights": "Available flights from ORD to LAX on 2024-05-17 identified"',
            '"operational_events": "Flight HAT029 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_007",
        instruction="Execute customer service duties to assist member Jennifer Johnson (daiki.johnson3136@example.com). Ivan wants to review reservation R9QDGB and explore alternatives for 2024-06-22 from SFO to PDX due to delays on flight HAT044 (flight_id: FL044). Provide her profile, reservation details, **run a same-day SFO→PDX availability search (results may be none)**, review HAT044 operational events, retrieve fleet utilization, and create a tracking event: 'Technical Issue', '2024-06-22T18:25:00Z', 'Delay concerns on flight HAT044', status 'Active', linked to HAT044/FL044.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "daiki.johnson3136@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "daiki.johnson3136@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "R9QDGB"}),
            Action(name="GetFlightsByCriteria", kwargs={
                "departure_date": "2024-06-22",
                "origin": "SFO",
                "destination": "PDX",
                "status": ["available", "waitlist"]
            }),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT044"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(name="CreateOperationalEvent", kwargs={
                "event_type": "Technical Issue",
                "event_timestamp_utc": "2024-06-22T18:25:00Z",
                "details": "Delay concerns on flight HAT044",
                "status": "Active",
                "flight_number": "HAT044",
                "flight_id": "FL044"
            }),
        ],
        outputs=[
            '"user_profile": "Member Jennifer Johnson profile retrieved"',
            '"reservation_details": "Reservation R9QDGB details retrieved successfully"',
            '"alternative_flights": "Same-day SFO→PDX search completed (may be none)"',
            '"operational_events": "Flight HAT044 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),


    Task(
        annotator="0",
        user_id="USER_008",
        instruction="Assist airline members regarding delays on flight HAT022 (FL022). For travel on 2024-05-22, list same-day LAX→DFW availability, you need to summarize operational events for HAT022, check Active fleet utilization, and create a tracking event: type 'Technical Issue', timestamp '2024-05-22T14:00:00Z', details 'Delay concerns on flight HAT022', status 'Active', linked to HAT022/FL022. Provide alternatives, the HAT022 event summary, fleet status, and confirmation the customer-service event was created.",
        actions=[
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-05-22", "status": ["available"], "origin": "LAX", "destination": "DFW"}),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT022"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-22T14:00:00Z",
                    "details": "Delay concerns on flight HAT022",
                    "status": "Active",
                    "flight_number": "HAT022",
                    "flight_id": "FL022"
                }
            )
        ],
        outputs=[
            '"alternative_flights": "Available flights from LAX to DFW on 2024-05-22 identified"',
            '"operational_events": "Flight HAT022 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_009",
        instruction="Execute assisting member Mohamed Lopez (sophia.wilson3098@example.com). Olivia wants to review reservation 6NSXQU and alternatives for 2024-05-19 from ATL to BWI because her flight HAT021 (flight_id: FL021) has delays. Provide her profile, reservation details, ATL→BWI options that day, operational events for HAT021, fleet utilization, and create a tracking event: 'Technical Issue', '2024-05-19T13:40:00Z', 'Delay concerns on flight HAT021', status 'Active', linked to HAT021/FL021.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "sophia.wilson3098@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "sophia.wilson3098@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "6NSXQU"}),
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-05-19", "status": ["available"], "origin": "ATL", "destination": "BWI"}),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT021"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-19T13:40:00Z",
                    "details": "Delay concerns on flight HAT021",
                    "status": "Active",
                    "flight_number": "HAT021",
                    "flight_id": "FL021"
                }
            ),
        ],
        outputs=[
            '"user_profile": "Member Mohamed Lopez profile retrieved"',
            '"reservation_details": "Reservation 6NSXQU details retrieved successfully"',
            '"alternative_flights": "Available flights from ATL to BWI on 2024-05-19 identified"',
            '"operational_events": "Flight HAT021 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_010",
        instruction="Execute maintenance planning at LAS. Update aircraft AC009 (PR-GUO, B737-800) to 'Maintenance', execute to create a scheduled C-Check entry with WO 'WO-2024-05-11-009' (ATA 05), description 'Scheduled C-Check inspection for PR-GUO at LAS', corrective action 'Perform scheduled C-Check inspection of systems and components', timestamp '2024-05-11T10:00:00Z', status 'Scheduled'. Then review B737-800 fleet utilization for 'Active' and 'Maintenance'. Return the created maintenance log ID.",
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC009", "new_status": "Maintenance"}),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC009",
                    "maintenance_type": "C-Check",
                    "description": "Scheduled C-Check inspection for PR-GUO at LAS",
                    "work_order_id": "WO-2024-05-11-009",
                    "ata_chapter": "05",
                    "corrective_action": "Perform scheduled C-Check inspection of systems and components",
                    "event_timestamp_utc": "2024-05-11T10:00:00Z",
                    "status": "Scheduled"
                }
            ),
            Action(name="GetFleetUtilization", kwargs={"model_filter": "B737-800", "status_filter": ["Active", "Maintenance"]})
        ],
        outputs=['"maintenance_log_id": "created"']
    ),

    Task(
        annotator="0",
        user_id="USER_011",
        instruction="Execute fleet operations management at JFK. Set aircraft AC005 (PR-XTD, A350-900) to 'Maintenance', you need to create an 'Emergency Repair' entry (WO-2024-05-12-005, ATA 32, TECH014) with description 'Landing gear warning discovered during pre-flight inspection', corrective action 'Investigate and repair landing gear warning system', timestamp '2024-05-12T08:45:00Z', status 'In Progress'. Document an 'Aircraft AOG' operational event at the same timestamp with details 'Aircraft PR-XTD AOG due to landing gear warning' and include both aircraft_id and tail_number. Provide the maintenance log ID and the aircraft's updated status.",
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC005", "new_status": "Maintenance"}),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC005",
                    "maintenance_type": "Emergency Repair",
                    "description": "Landing gear warning discovered during pre-flight inspection",
                    "technician_id": "TECH014",
                    "work_order_id": "WO-2024-05-12-005",
                    "ata_chapter": "32",
                    "corrective_action": "Investigate and repair landing gear warning system",
                    "event_timestamp_utc": "2024-05-12T08:45:00Z",
                    "status": "In Progress"
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Aircraft AOG",
                    "event_timestamp_utc": "2024-05-12T08:45:00Z",
                    "details": "Aircraft PR-XTD AOG due to landing gear warning",
                    "aircraft_id": "AC005",
                    "tail_number": "PR-XTD",
                    "status": "Active"
                }
            )
        ],
        outputs=['"maintenance_log_id": "created"', '"aircraft_status": "Maintenance"']
    ),

    Task(
        annotator="0",
        user_id="USER_012",
        instruction=(
            "As an ORD crew scheduler, For flight HAT015 (FL010) on 2024-05-03, you need to assign Jennifer Wilson (CM021) and Mohamed Lopez (CM025) "
            "as Flight Attendant. Log each on B787-9 with 2.5 total hours (pic 0, sic 0, night 2.5, instrument 0), 1 takeoff, 1 landing. "
            "Also record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-005, ATA 29), description "
            "'Hydraulic system warning discovered during pre-flight inspection', corrective action "
            "'Emergency repair procedures required for hydraulic system warning', technician TECH009, "
            "timestamp 2024-08-15T14:30:00Z, status In Progress. Confirm the flight number."
        ),
        actions=[
            Action(name="GetFlightCrewAssignments", kwargs={"flight_id": "FL010", "flight_number": "HAT015"}),
            Action(name="AssignCrewToFlight", kwargs={
                "flight_id": "FL010", "flight_number": "HAT015",
                "crew_member_id": "CM021", "assigned_role": "Flight Attendant"
            }),
            Action(name="AssignCrewToFlight", kwargs={
                "flight_id": "FL010", "flight_number": "HAT015",
                "crew_member_id": "CM025", "assigned_role": "Flight Attendant"
            }),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-005",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(name="UpdateCrewFlightLog", kwargs={
                "crew_member_id": "CM021", "flight_id": "FL010", "flight_number": "HAT015",
                "date": "2024-05-03", "role": "Flight Attendant", "aircraft_model": "B787-9",
                "hours_flown": {"total": 2.5, "pic": 0.0, "sic": 0.0, "night": 2.5, "instrument": 0.0},
                "landings": 1, "takeoffs": 1
            }),
            Action(name="UpdateCrewFlightLog", kwargs={
                "crew_member_id": "CM025", "flight_id": "FL010", "flight_number": "HAT015",
                "date": "2024-05-03", "role": "Flight Attendant", "aircraft_model": "B787-9",
                "hours_flown": {"total": 2.5, "pic": 0.0, "sic": 0.0, "night": 2.5, "instrument": 0.0},
                "landings": 1, "takeoffs": 1
            })
        ],
        outputs=[
            '"flight_number": "HAT015"',
            '"assignment": {"crew_member_id":"CM021","role":"Flight Attendant","status":"assigned"}',
            '"assignment": {"crew_member_id":"CM025","role":"Flight Attendant","status":"assigned","lead_cabin_designation":true}',
            '"log": {"crew_member_id":"CM021","status":"logged"}',
            '"log": {"crew_member_id":"CM025","status":"logged"}'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_013",
        instruction="Execute the maintenance supervisor at DFW. Aircraft AC002 (PR-XBE, A320neo) requires scheduled B-Check maintenance. The aircraft status needs updating to 'Maintenance', along with a maintenance entry containing work order 'WO-2024-05-02-002' (ATA 05), description 'Scheduled B-Check inspection for PR-XBE at DFW', corrective action 'Perform scheduled B-Check inspection of systems and components', and timestamp '2024-05-02T09:00:00Z'. The current fleet utilization for A320neo models should be checked with status filter for 'Active' and 'Maintenance' aircraft. Provide the created maintenance log ID.",
        actions=[
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC002",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check inspection for PR-XBE at DFW",
                    "work_order_id": "WO-2024-05-02-002",
                    "ata_chapter": "05",
                    "corrective_action": "Perform scheduled B-Check inspection of systems and components",
                    "event_timestamp_utc": "2024-05-02T09:00:00Z",
                    "status": "Scheduled"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC002",
                    "new_status": "Maintenance"
                }
            ),
            Action(
                name="GetFleetUtilization",
                kwargs={
                    "model_filter": "A320neo",
                    "status_filter": ["Active", "Maintenance"]
                }
            )
        ],
        outputs=[
            '"maintenance_log_id": "ML026"'
        ]
    ),


    Task(
        annotator="0",
        user_id="USER_014",
        instruction="Execute assisting member Jennifer Johnson (daiki.johnson3136@example.com). Ivan wants to review reservation R9QDGB and alternatives for 2024-05-28 from BOS to LGA due to delays on HAT007 (flight_id: FL007). You want to provide her profile, reservation details, BOS→LGA options that day, operational events for HAT007, fleet utilization, and create a tracking event: 'Technical Issue', '2024-05-28T09:15:00Z', 'Delay concerns on flight HAT007', status 'Active', linked to HAT007/FL007.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "daiki.johnson3136@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "daiki.johnson3136@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "R9QDGB"}),
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-05-28", "status": ["available"], "origin": "BOS", "destination": "LGA"}),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT007"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-28T09:15:00Z",
                    "details": "Delay concerns on flight HAT007",
                    "status": "Active",
                    "flight_number": "HAT007",
                    "flight_id": "FL007"
                }
            ),
        ],
        outputs=[
            '"user_profile": "Member Jennifer Johnson profile retrieved"',
            '"reservation_details": "Reservation R9QDGB details retrieved successfully"',
            '"alternative_flights": "No available flights from BOS to LGA on 2024-05-28 identified"',
            '"operational_events": "Flight HAT007 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_015",
        instruction="Execute fleet operations management at MIA. Aircraft AC007 (PR-YJB, A220-300) is scheduled for an A-Check. The aircraft status requires updating to 'Maintenance', along with a maintenance entry containing work order 'WO-2024-05-02-007' (ATA 05), description 'Scheduled A-Check inspection for PR-YJB at MIA', status 'Scheduled', and timestamp '2024-05-02T09:00:00Z' and 'Perform scheduled A-Check inspection of systems and components.' as the corrective action. The fleet utilization for A220-300 models should be checked with status filter for 'Active' and 'Maintenance' aircraft. Also, verify the aircraft's current location and status before proceeding with the maintenance. Additionally, check the aircraft's maintenance history and create an operational event with type 'Technical Issue', timestamp '2024-05-02T09:00:00Z', details 'Aircraft AC007 scheduled for A-Check maintenance at MIA', status 'Active', aircraft_id 'AC007', and tail_number 'PR-YJB' to document this scheduled maintenance. Provide the created maintenance log ID, the aircraft's pre-maintenance status, maintenance history, and the operational event ID.",
        actions=[
            Action(
                name="GetAircraftDetails",
                kwargs={
                    "aircraft_id": "AC007"
                }
            ),
            Action(
                name="GetAircraftMaintenanceHistory",
                kwargs={
                    "aircraft_id": "AC007"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC007",
                    "new_status": "Maintenance"
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC007",
                    "maintenance_type": "A-Check",
                    "description": "Scheduled A-Check inspection for PR-YJB at MIA",
                    "work_order_id": "WO-2024-05-02-007",
                    "ata_chapter": "05",
                    "corrective_action": "Perform scheduled A-Check inspection of systems and components.",
                    "event_timestamp_utc": "2024-05-02T09:00:00Z",
                    "status": "Scheduled"
                }
            ),
            Action(
                name="GetFleetUtilization",
                kwargs={
                    "model_filter": "A220-300",
                    "status_filter": ["Active", "Maintenance"]
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-02T09:00:00Z",
                    "details": "Aircraft AC007 scheduled for A-Check maintenance at MIA",
                    "status": "Active",
                    "aircraft_id": "AC007",
                    "tail_number": "PR-YJB"
                }
            )
        ],
        outputs=[
            '"maintenance_log_id": "ML026"',
            '"aircraft_pre_maintenance_status": "Aircraft AC007 details retrieved"',
            '"maintenance_history": "Aircraft AC007 maintenance history retrieved"',
            '"operational_event_id": "OE026"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_016",
        instruction=(
            "As a crew scheduler at LAX, for flight HAT016 (FL016) on 2024-05-03, you must assign Captain Isabella Brown (CM001) and First Officer Isabella Brown (CM002). "
            "Then log duty on B737-800 as 3.0 total hours each (Captain: all PIC; First Officer: all SIC), 1 landing and 1 takeoff apiece. "
            "Also have to record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-005, ATA 29), description "
            "'Hydraulic system warning discovered during pre-flight inspection', corrective action "
            "'Emergency repair procedures required for hydraulic system warning', technician TECH009, "
            "timestamp 2024-08-15T14:30:00Z, status In Progress. Execute provide confirmation of crew assignments and flight details."
        ),
        actions=[
            Action(
                name="AssignCrewToFlight",
                kwargs={
                    "flight_id": "FL016",
                    "flight_number": "HAT016",
                    "crew_member_id": "CM001",
                    "assigned_role": "Captain"
                }
            ),
            Action(
                name="AssignCrewToFlight",
                kwargs={
                    "flight_id": "FL016",
                    "flight_number": "HAT016",
                    "crew_member_id": "CM002",
                    "assigned_role": "First Officer"
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-005",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM001",
                    "flight_id": "FL016",
                    "flight_number": "HAT016",
                    "date": "2024-05-03",
                    "role": "Captain",
                    "aircraft_model": "B737-800",
                    "hours_flown": {"total": 3.0, "pic": 3.0, "sic": 0.0, "night": 0.0, "instrument": 0.0},
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM002",
                    "flight_id": "FL016",
                    "flight_number": "HAT016",
                    "date": "2024-05-03",
                    "role": "First Officer",
                    "aircraft_model": "B737-800",
                    "hours_flown": {"total": 3.0, "pic": 0.0, "sic": 3.0, "night": 0.0, "instrument": 0.0},
                    "landings": 1,
                    "takeoffs": 1
                }
            )
        ],
        outputs=[
            '"flight_number": "HAT016"',
            '"flight_id": "FL016"',
            '"crew_assignments": "Captain Isabella Brown (CM001) and First Officer Isabella Brown (CM002) assigned"',
            '"duty_time_logged": "Both crew members logged 3.0 total hours (PIC for Captain, SIC for First Officer) with 1 landing and 1 takeoff"',
            '"aircraft_model": "B737-800"'
        ]
    ),


    Task(
         annotator="0",
         user_id="USER_017",
         instruction="Execute the maintenance manager at ATL. Aircraft PR-GOL (AC001) has a hydraulic system warning at 2024-08-15T14:30:00Z and execute AC001 set to Maintenance, then a maintenance log created for an Emergency Repair (WO-2024-08-15-005, ATA 29, TECH009) with description 'Hydraulic system warning discovered during pre-flight inspection', status 'In Progress', and corrective action 'Emergency repair procedures required for hydraulic system warning'. You also want a single 'Aircraft AOG' operational event at the same UTC timestamp with detail 'Aircraft PR-GOL AOG situation due to hydraulic system warning discovered during pre-flight inspection', and you need to include ATL airport context (iata_code 'ATL' and airport_id 'ARP_ATL') and associate both aircraft_id 'AC001' and tail_number 'PR-GOL'. Return only the updated aircraft status and the maintenance log ID.",
         actions=[
             Action(
                 name="UpdateAircraftStatus",
                 kwargs={"aircraft_id": "AC001", "new_status": "Maintenance"}
             ),
             Action(
                 name="CreateMaintenanceEntry",
                 kwargs={
                     "aircraft_id": "AC001", "maintenance_type": "Emergency Repair", "description": "Hydraulic system warning discovered during pre-flight inspection", "technician_id": "TECH009", "work_order_id": "WO-2024-08-15-005", "ata_chapter": "29",
                     "corrective_action": "Emergency repair procedures required for hydraulic system warning", "event_timestamp_utc": "2024-08-15T14:30:00Z", "status": "In Progress"
                 }
             ),
             Action(
                 name="CreateOperationalEvent",
                 kwargs={
                     "event_type": "Aircraft AOG", "event_timestamp_utc": "2024-08-15T14:30:00Z", "details": "Aircraft PR-GOL AOG situation due to hydraulic system warning discovered during pre-flight inspection", "aircraft_id": "AC001", "tail_number": "PR-GOL", "airport_id": "ARP_ATL", "iata_code": "ATL"
                 }
             )
         ],
         outputs=['"aircraft_status": "Maintenance"', '"maintenance_log_id": "ML026"'],
     ),
    Task(
        annotator="0",
        user_id="USER_018",
        instruction="Assist a member regarding delays on flight HAT028 (FL028). For travel on 2024-06-07, execute to list same-day HOU→DEN availability, summarize operational events for HAT028, check Active fleet utilization, and create a tracking event: type 'Technical Issue', timestamp '2024-06-07T15:55:00Z', details 'Delay concerns on flight HAT028', status 'Active', linked to HAT028/FL028. Provide alternatives, the HAT028 event summary, fleet status, and confirmation the customer-service event was created.",
        actions=[
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-06-07", "status": ["available"], "origin": "HOU", "destination": "DEN"}),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT028"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-06-07T15:55:00Z",
                    "details": "Delay concerns on flight HAT028",
                    "status": "Active",
                    "flight_number": "HAT028",
                    "flight_id": "FL028"
                }
            )
        ],
        outputs=[
            '"alternative_flights": "Available flights from HOU to DEN on 2024-06-07 identified"',
            '"operational_events": "Flight HAT028 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_019",
        instruction="Execute member assistance for delays on flight HAT033 (FL033). For travel on 2024-06-14, you need to run a same-day MSP→PHX availability check (results may be none), summarize operational events for HAT033, check Active fleet utilization, and create a tracking event: type 'Technical Issue', timestamp '2024-06-14T20:05:00Z', details 'Delay concerns on flight HAT033', status 'Active', linked to HAT033/FL033. Provide the availability search result (even if none), the HAT033 event summary, the fleet snapshot, and confirmation the customer-service event was created.",
        actions=[
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-06-14", "status": ["available"], "origin": "MSP", "destination": "PHX"}),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT033"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-06-14T20:05:00Z",
                    "details": "Delay concerns on flight HAT033",
                    "status": "Active",
                    "flight_number": "HAT033",
                    "flight_id": "FL033"
                }
            )
        ],
        outputs=[
            '"alternative_flights": "No available flights from MSP to PHX on 2024-06-14"',
            '"operational_events": "Flight HAT033 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),



    Task(
        annotator="0",
        user_id="USER_020",
        instruction="Execute maintenance supervision at LAS. Aircraft AC009 (PR-GUO, B737-800) has finished maintenance. The aircraft status should be updated to 'Active' at LAS, along with a maintenance entry for the completed 'A-Check' containing work order 'WO-2024-05-18-009', ATA '05', details 'Scheduled maintenance inspection completed.', technician 'TECH013', and corrective action 'Scheduled maintenance inspection completed. All systems operational. Aircraft cleared for return to service.' Timestamp is 2024-05-18T18:00:00Z. A 'Technical Issue' operational event should document this completion with status 'Resolved' and details 'Aircraft AC009 maintenance completed and returned to service at LAS'. Flight hours should be logged for First Officer Susan Wilson (CM005) for flight HAT008 (FL005) on 2024-05-18 (B787-9, 5.0 total hours, 5.0 SIC, 1.0 night, 1.0 instrument, 1 landing, 1 takeoff). Please provide the maintenance log ID and the aircraft's final status.",
        actions=[
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC009", "new_status": "Active", "new_location_iata": "LAS"
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC009", "maintenance_type": "A-Check", "description": "Scheduled maintenance inspection completed.", "work_order_id": "WO-2024-05-18-009", "ata_chapter": "05",
                    "corrective_action": "Scheduled maintenance inspection completed. All systems operational. Aircraft cleared for return to service.", "event_timestamp_utc": "2024-05-18T18:00:00Z", "technician_id": "TECH013", "status": "Completed"
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue", "event_timestamp_utc": "2024-05-18T18:00:00Z", "details": "Aircraft AC009 maintenance completed and returned to service at LAS", "status": "Resolved", "aircraft_id": "AC009", "tail_number": "PR-GUO"
                }
            ),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM005", "flight_id": "FL005", "flight_number": "HAT008", "date": "2024-05-18", "role": "First Officer", "aircraft_model": "B787-9",
                    "hours_flown": {"total": 5.0, "pic": 0, "sic": 5.0, "night": 1.0, "instrument": 1.0},
                    "landings": 1, "takeoffs": 1
                }
            )
        ],
        outputs=[
            '"maintenance_log_id": "ML026"',
            '"aircraft_final_status": "Active"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_021",
        instruction="Execute a customer-care rep working a morning delay desk. Execute told Mohamed Lopez (sophia.wilson3098@example.com) wants a quick read on PNR 6NSXQU and execute you need a same-day SEA to SFO availability check for 2024-06-01 because HAT042 (FL042) has been running late. You want to surface her profile, pull the booking, run the SEA→SFO availability search for that date (results may be none), review any HAT042 operational notes, glance at overall Active fleet, and open a simple Technical Issue marker at 07:45Z that says 'Delay concerns on flight HAT042' tied to HAT042/FL042. Return the usual set: profile, reservation details, availability search result (even if none), ops context, fleet snapshot, and the tracking event.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "sophia.wilson3098@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "sophia.wilson3098@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "6NSXQU"}),
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-06-01", "status": ["available"], "origin": "SEA", "destination": "SFO"}),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT042"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-06-01T07:45:00Z",
                    "details": "Delay concerns on flight HAT042",
                    "status": "Active",
                    "flight_number": "HAT042",
                    "flight_id": "FL042"
                }
            ),
        ],
        outputs=[
            '"user_profile": "Member Mohamed Lopez profile retrieved"',
            '"reservation_details": "Reservation 6NSXQU details retrieved successfully"',
            '"alternative_flights": "Same-day SEA→SFO search completed (may be none)"',
            '"operational_events": "Flight HAT042 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),


    Task(
        annotator="0",
        user_id="USER_022",
        instruction=(
            "Execute covering cabin staffing at CLT. For HAT015 (FL010) on 2024-05-02 assign Jennifer Wilson (CM021) and Mohamed Lopez (CM025) as Flight Attendants "
            "and log duty on CRJ900 as 2.0 total hours (all night), 1 takeoff and 1 landing each; no other hour buckets. "
            "Also execute to record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-005, ATA 29), description "
            "'Hydraulic system warning discovered during pre-flight inspection', corrective action "
            "'Emergency repair procedures required for hydraulic system warning', technician TECH009, timestamp 2024-08-15T14:30:00Z, status In Progress. "
            "Execute return the flight readout with crew and a plain confirmation that duty posted."
        ),
        actions=[
            Action(
                name="AssignCrewToFlight",
                kwargs={"flight_id": "FL010", "flight_number": "HAT015", "crew_member_id": "CM021", "assigned_role": "Flight Attendant"}
            ),
            Action(
                name="AssignCrewToFlight",
                kwargs={"flight_id": "FL010", "flight_number": "HAT015", "crew_member_id": "CM025", "assigned_role": "Flight Attendant"}
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-005",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM021",
                    "flight_id": "FL010",
                    "flight_number": "HAT015",
                    "date": "2024-05-02",
                    "role": "Flight Attendant",
                    "aircraft_model": "CRJ900",
                    "hours_flown": {"total": 2.0, "pic": 0, "sic": 0, "night": 2.0, "instrument": 0},
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM025",
                    "flight_id": "FL010",
                    "flight_number": "HAT015",
                    "date": "2024-05-02",
                    "role": "Flight Attendant",
                    "aircraft_model": "CRJ900",
                    "hours_flown": {"total": 2.0, "pic": 0, "sic": 0, "night": 2.0, "instrument": 0},
                    "landings": 1,
                    "takeoffs": 1
                }
            )
        ],
        outputs=[
            '"flight_number": "HAT015"',
            '"flight_id": "FL010"',
            '"crew_assignments": "Jennifer Wilson (CM021) and Mohamed Lopez (CM025) assigned as Flight Attendants"',
            '"duty_time_logged": "Both crew members logged 2.0 total hours (2.0 night hours) with 1 landing and 1 takeoff"',
            '"aircraft_model": "CRJ900"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_023",
        instruction=(
            "Execute the ATL cert-tracking coordinator tidying HAT004 (FL004) dated 2024-05-15. Record B737-800 time: "
            "CM001 (Isabella Brown) Captain 3.0 total with 2.5 PIC and 0.5 instrument, no night, 1 landing, 1 takeoff; "
            "CM005 (Susan Wilson) First Officer 3.0 total with 2.5 SIC and 0.5 instrument, no night, 1 landing, 1 takeoff. "
            "Also execute to record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-005, ATA 29), description "
            "'Hydraulic system warning discovered during pre-flight inspection', corrective action "
            "'Emergency repair procedures required for hydraulic system warning', technician TECH009, "
            "timestamp 2024-08-15T14:30:00Z, status In Progress. After the entries, you will get the current crew certification view for both. "
            "Report that the logs took and whether the certs read current."
        ),
        actions=[
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM001", "flight_id": "FL004", "flight_number": "HAT004", "date": "2024-05-15",
                    "role": "Captain", "aircraft_model": "B737-800",
                    "hours_flown": {"total": 3.0, "pic": 2.5, "sic": 0, "night": 0.0, "instrument": 0.5},
                    "landings": 1, "takeoffs": 1
                }
            ),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM005", "flight_id": "FL004", "flight_number": "HAT004", "date": "2024-05-15",
                    "role": "First Officer", "aircraft_model": "B737-800",
                    "hours_flown": {"total": 3.0, "pic": 0, "sic": 2.5, "night": 0.0, "instrument": 0.5},
                    "landings": 1, "takeoffs": 1
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-005",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(name="GetCrewCertifications", kwargs={"crew_member_id": "CM001"}),
            Action(name="GetCrewCertifications", kwargs={"crew_member_id": "CM005"})
        ],
        outputs=['"flight_log_entries_saved": "confirmed"', '"crew_certification_status": "valid"'],
    ),


    Task(
        annotator="0",
        user_id="USER_024",
        instruction="Execute senior service duties looking after a Gold caller. You want to review Isabella Brown’s record (PNR NO6JO3, email emma.smith8074@example.com), then execute you should move the itinerary up to First and attach travel insurance if today’s ops allow it. Execute to rely on the primary stored payment method credit_card_4421486, no creative tender. You also want a quick status look at HAT083 on 2024-05-16 so the upgrade isn’t attempted against a non-operating flight. Bring back the refreshed reservation with the new cabin and insurance, plus the flight status.",
        actions=[
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "NO6JO3"}
            ),
            Action(
                name="GetUserProfile",
                kwargs={"user_email": "emma.smith8074@example.com"}
            ),
            Action(
                name="UpdateReservation",
                kwargs={
                    "reservation_id": "NO6JO3",
                    "cabin": "first",
                    "insurance": "yes",
                    "payment_method_id": "credit_card_4421486"
                }
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "NO6JO3"}
            ),
            Action(
                name="GetFlightStatusByNumberAndDate",
                kwargs={
                    "flight_number": "HAT083",
                    "date": "2024-05-16"
                }
            ),
        ],
        outputs=['"reservation_id": "NO6JO3"', '"cabin": "first"', '"flight_status": "Flight HAT083 status retrieved"'],
    ),
    Task(
        annotator="0",
        user_id="USER_025",
        instruction="Execute the MIA apron-ops supervisor on a tight push. You want HAT015 (FL010) noted for a gate swap on 2024-05-03 with a UTC stamp 15:30:00 and the detail 'Departure gate changed from D12 to D18 due to ramp constraints', and execute a one-hour delay should follow. Per on-gate policy, you also want a quick Line Maintenance verification logged on the affected aircraft (AC010) at the same time under ATA 05 before any downstream changes, with a simple completed note that no faults were found'Post-gate-change on-stand verification at MIA' ,WO-2024-05-03-010. You also want a quick look at aircraft AC010 status and its maintenance story, and execute to drop a small follow-up tag at 16:00Z labeled Minor Delay with 'Gate change delay impact assessment for flight HAT015' tied to FL010/HAT015. Return the gate-change event ID, the updated flight status, aircraft status, maintenance status, and that follow-up event ID.",
        actions=[
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": "MIA"}
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Gate Change",
                    "event_timestamp_utc": "2024-05-03T15:30:00Z",
                    "details": "Departure gate changed from D12 to D18 due to ramp constraints",
                    "status": "Active",
                    "flight_id": "FL010",
                    "flight_number": "HAT015",
                    "airport_id": "ARP_MIA",
                    "iata_code": "MIA"
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC010",
                    "maintenance_type": "Line Maintenance",
                    "description": "Post-gate-change on-stand verification at MIA",
                    "work_order_id": "WO-2024-05-03-010",
                    "ata_chapter": "05",
                    "corrective_action": "no faults were found.",
                    "event_timestamp_utc": "2024-05-03T15:30:00Z",
                    "status": "Completed"
                }
            ),
            Action(
                name="UpdateFlightStatusByNumberAndDate",
                kwargs={
                    "flight_number": "HAT015",
                    "date": "2024-05-03",
                    "new_status": "delayed",
                    "delay_hours": 1,
                    "reason_event_id": "OE026"
                }
            ),
            Action(
                name="GetAircraftDetails",
                kwargs={
                    "aircraft_id": "AC010"
                }
            ),
            Action(
                name="GetAircraftMaintenanceHistory",
                kwargs={
                    "aircraft_id": "AC010"
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Minor Delay",
                    "event_timestamp_utc": "2024-05-03T16:00:00Z",
                    "details": "Gate change delay impact assessment for flight HAT015",
                    "status": "Active",
                    "flight_id": "FL010",
                    "flight_number": "HAT015"
                }
            )
        ],
        outputs=['"event_id": "OE026"', '"updated_status": "delayed"', '"aircraft_status": "Aircraft AC010 details retrieved"', '"maintenance_status": "Aircraft AC010 maintenance history retrieved"', '"delay_impact_event_id": "OE027"'],
    ),

    Task(
        annotator="0",
        user_id="USER_026",
        instruction="Execute a DFW maintenance planner doing forward scheduling. You want AC002 (PR-XBE, A320neo) captured for a B-Check on 2024-09-20 at 09:00Z under WO-2024-09-20-002 for ATA 05, with the log created as Scheduled and the next due noted 2025-03-20, describing Scheduled B-Check for PR-XBE. You think the aircraft should read In Maintenance at DFW once set. You also want a simple Technical Issue note at the same time saying 'Aircraft AC002 scheduled for B-Check maintenance at DFW' tied to AC002 and PR-XBE. Before you lock it in, you need to glance at its current location and the A320neo Active/Maintenance utilization. Provide the new maintenance log ID, the updated status, the ops-event ID, plus the location and fleet snapshot.",
        actions=[
            Action(
                name="GetAircraftDetails",
                kwargs={
                    "aircraft_id": "AC002"
                }
            ),
            Action(
                name="GetAircraftMaintenanceHistory",
                kwargs={"aircraft_id": "AC002"}
            ),
            Action(
                name="GetFleetUtilization",
                kwargs={
                    "model_filter": "A320neo",
                    "status_filter": ["Active", "Maintenance"]
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC002",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check for PR-XBE",
                    "work_order_id": "WO-2024-09-20-002",
                    "ata_chapter": "05",
                    "corrective_action": "Scheduled B-Check maintenance per work order WO-2024-09-20-002",
                    "event_timestamp_utc": "2024-09-20T09:00:00Z",
                    "status": "Scheduled",
                    "next_due": "2025-03-20"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC002",
                    "new_status": "In Maintenance",
                    "new_location_iata": "DFW"
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-09-20T09:00:00Z",
                    "details": "Aircraft AC002 scheduled for B-Check maintenance at DFW",
                    "status": "Active",
                    "aircraft_id": "AC002",
                    "tail_number": "PR-XBE"
                }
            )
        ],
        outputs=[
            '"maintenance_log_id": "ML026"',
            '"aircraft_status": "In Maintenance"',
            '"operational_event_id": "OE026"',
            '"aircraft_location": "Aircraft AC002 location details retrieved"',
            '"fleet_utilization": "A320neo fleet utilization status retrieved"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_027",
        instruction="Execute fleet operations management at LAX Aircraft AC003 (PP-LTM, B787-9) needs scheduled maintenance. First, set its status to 'Maintenance', but you need to get the history for that. Then, create a maintenance entry for a 'B-Check' with work order 'WO-2024-05-04-003' (ATA 05), description 'Scheduled B-Check inspection for PP-LTM at LAX', corrective action 'Perform scheduled B-Check inspection of systems and components', and timestamp '2024-05-04T11:00:00Z'. Finally, check the fleet utilization for B787-9 aircraft with status filter for 'Active' and 'Maintenance' aircraft. Also, verify the aircraft's current location before setting it to maintenance. Additionally, check the aircraft's maintenance history and create an operational event with type 'Technical Issue', timestamp '2024-05-04T11:00:00Z', details 'Aircraft AC003 scheduled for B-Check maintenance at LAX', status 'Active', aircraft_id 'AC003', and tail_number 'PP-LTM' to document this scheduled maintenance. Provide the maintenance log ID created, the aircraft's pre-maintenance location, maintenance history, and the operational event ID.",
        actions=[
            Action(
                name="GetAircraftDetails",
                kwargs={
                    "aircraft_id": "AC003"
                }
            ),
            Action(
                name="GetAircraftMaintenanceHistory",
                kwargs={
                    "aircraft_id": "AC003"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC003",
                    "new_status": "Maintenance"
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC003",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check inspection for PP-LTM at LAX",
                    "work_order_id": "WO-2024-05-04-003",
                    "ata_chapter": "05",
                    "corrective_action": "Perform scheduled B-Check inspection of systems and components.",
                    "event_timestamp_utc": "2024-05-04T11:00:00Z",
                    "status": "Scheduled"
                }
            ),
            Action(
                name="GetFleetUtilization",
                kwargs={
                    "model_filter": "B787-9",
                    "status_filter": ["Active", "Maintenance"]
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-04T11:00:00Z",
                    "details": "Aircraft AC003 scheduled for B-Check maintenance at LAX",
                    "status": "Active",
                    "aircraft_id": "AC003",
                    "tail_number": "PP-LTM"
                }
            )
        ],
        outputs=[
            '"maintenance_log_id": "ML026"',
            '"aircraft_pre_maintenance_location": "Aircraft AC003 location details retrieved"',
            '"maintenance_history": "Aircraft AC003 maintenance history retrieved"',
            '"operational_event_id": "OE026"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_028",
        instruction=(
            "Book a one-way economy ticket for Mohamed Lopez (user_id/user_email sophia.wilson3098@example.com, DOB 1988-09-12) "
            "from ORD→DTW on 2024-05-25 on HAT020, reservation NEW567, payment credit_card_5260935, 2 total bags (1 non-free), "
            "no insurance, fare $125, created at 2024-05-23T16:45:00Z. Use exactly this identity (do not reconcile profile data). "
            "Also you will want to record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-005, ATA 29), description "
            "'Hydraulic system warning discovered during pre-flight inspection', corrective action "
            "'Emergency repair procedures required for hydraulic system warning', technician TECH009, "
            "timestamp 2024-08-15T14:30:00Z, status In Progress. After creation, you need to confirm reservation details."
        ),
        actions=[
            Action(
                name="SearchFlightsByRoute",
                kwargs={
                    "origin": "ORD", "destination": "DTW", "start_date": "2024-05-25", "end_date": "2024-05-25", "status_filter": ["available"]
                }
            ),

            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-005",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(
                name="CreateReservation",
                kwargs={
                    "reservation_id": "NEW567", "user_id": "sophia.wilson3098@example.com", "user_email": "sophia.wilson3098@example.com", "origin": "ORD", "destination": "DTW", "flight_type": "one_way", "cabin": "economy",
                    "flights": [{"origin": "ORD", "destination": "DTW", "flight_number": "HAT020", "date": "2024-05-25", "price": 125}],
                    "passengers": [{"first_name": "Sophia", "last_name": "Taylor", "dob": "1988-09-12"}],
                    "payment_method_id": "credit_card_5260935", "created_at": "2024-05-23T16:45:00Z", "total_baggages": 2, "nonfree_baggages": 1, "insurance": "no"
                }
            ),
            Action(
                name="GetReservationDetails",
                kwargs={"reservation_id": "NEW567"}
            )
        ],
        outputs=[
            '"flight_search_results": "Found available flight HAT020 from ORD to DTW on May 25, 2024 with economy price $125"',
            '"reservation_confirmation": "Reservation NEW567 created successfully for Mohamed Lopez on one-way flight HAT020 from ORD to DTW on May 25, 2024"',
            '"reservation_details": "Reservation NEW567 confirmed: Mohamed Lopez, Economy class, one-way flight HAT020, ORD-DTW, May 25, 2024"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_029",
        instruction=(
            "Execute fleet operations management at PHX. Reposition AC008 (ATR72-600, tail PP-PTM) from PHX to LAS and AC009 (B737-800, tail PR-GUO) "
            "from LAS to PHX; both remain Active. Log flight hours for Captain Jennifer Wilson (CM004) on HAT014 (FL006) dated 2024-05-04 on B787-9: "
            "5.0 total (5.0 PIC), 1.0 night, 1.0 instrument, 1 landing, 1 takeoff. Also record a maintenance entry for AC001: Emergency Repair "
            "(WO-2024-08-15-005, ATA 29), description 'Hydraulic system warning discovered during pre-flight inspection', corrective action "
            "'Emergency repair procedures required for hydraulic system warning', technician TECH009, timestamp 2024-08-15T14:30:00Z, status In Progress. "
            "Confirm the final status and location of both aircraft."
        ),
        actions=[
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC008", "new_status": "Active", "new_location_iata": "LAS"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC009", "new_status": "Active", "new_location_iata": "PHX"
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-005",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM004", "flight_id": "FL006", "flight_number": "HAT014", "date": "2024-05-04", "role": "Captain", "aircraft_model": "B787-9",
                    "hours_flown": {"total": 5.0, "pic": 5.0, "sic": 0, "night": 1.0, "instrument": 1.0},
                    "landings": 1, "takeoffs": 1
                }
            ),
            Action(
                name="GetAircraftDetails",
                kwargs={"aircraft_id": "AC008"}
            ),
            Action(
                name="GetAircraftDetails",
                kwargs={"aircraft_id": "AC009"}
            )
        ],
        outputs=[
            '"AC008_final_status": "Active", "AC008_final_location": "LAS"',
            '"AC009_final_status": "Active", "AC009_final_location": "PHX"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_030",
        instruction="Execute a customer care agent looking after a timing concern. You want to pull Ivan Wilson at evelyn.wilson9461@example.com with reservation 4WQ150 and you need to glance at same day LAX to DFW options for 2024-05-22 since HAT022 with flight id FL022 has been unstable. You also want a quick read on her profile and booking details plus whatever operational notes exist for HAT022 and a simple Active fleet snapshot. You think a light Technical Issue marker at 2024-05-22T14:00:00Z that says 'Delay concerns on flight HAT022 tied to HAT022' and FL022 will track the case. You want to return profile reservation alternatives the ops context the fleet view and the tracking entry.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={
                    "user_email": "evelyn.wilson9461@example.com"
                }
            ),
            Action(
                name="GetUserReservations",
                kwargs={
                    "user_email": "evelyn.wilson9461@example.com"
                }
            ),
            Action(
                name="GetReservationDetails",
                kwargs={
                    "reservation_id": "4WQ150"
                }
            ),
            Action(
                name="GetFlightsByCriteria",
                kwargs={
                    "departure_date": "2024-05-22",
                    "status": ["available"],
                    "origin": "LAX",
                    "destination": "DFW"
                }
            ),
            Action(
                name="GetOperationalEventsByFlight",
                kwargs={
                    "flight_number": "HAT022"
                }
            ),
            Action(
                name="GetFleetUtilization",
                kwargs={
                    "status_filter": ["Active"]
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-22T14:00:00Z",
                    "details": "Delay concerns on flight HAT022 tied to HAT022",
                    "status": "Active",
                    "flight_number": "HAT022",
                    "flight_id": "FL022",
                }
            ),
        ],
        outputs=[
            '"user_profile": "Regular member Ivan Wilson with 3 reservations and 4 payment methods"',
            '"reservation_details": "Reservation 4WQ150 details retrieved successfully"',
            '"alternative_flights": "Available flights from LAX to DFW on 2024-05-22 identified"',
            '"operational_events": "Flight HAT022 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_031",
        instruction=(
            "Place Isabella Brown (olivia.garcia1660@example.com) on HAT129 MIA→ORD for 2024-05-28 in business using reservation NEW789; "
            "passengers: Isabella dob 1985-03-15 and Ivan Wilson dob 1987-07-22; payment credit_card_7957134; 3 total bags (2 non-free); "
            "insurance included; price 460; created at 2024-05-22T15:30:00Z. Confirm reservation details. "
            "You also need to record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-005, ATA 31), description "
            "'Hydraulic system warning discovered during pre-flight inspection', corrective action "
            "'Emergency repair procedures required for hydraulic system warning', technician TECH009, "
            "timestamp 2024-08-15T14:30:00Z, status In Progress."
        ),
        actions=[
            Action(
                name="SearchFlightsByRoute",
                kwargs={"origin": "MIA", "destination": "ORD", "start_date": "2024-05-28", "end_date": "2024-05-28", "status_filter": ["available"]}
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-005",
                    "ata_chapter": "31",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(
                name="CreateReservation",
                kwargs={
                    "reservation_id": "NEW789",
                    "user_id": "olivia.garcia1660@example.com",
                    "user_email": "olivia.garcia1660@example.com",
                    "origin": "MIA",
                    "destination": "ORD",
                    "flight_type": "one_way",
                    "cabin": "business",
                    "flights": [{"origin": "MIA", "destination": "ORD", "flight_number": "HAT129", "date": "2024-05-28", "price": 460}],
                    "passengers": [
                        {"first_name": "Lucas", "last_name": "Hernandez", "dob": "1985-03-15"},
                        {"first_name": "Chen", "last_name": "Hernandez", "dob": "1987-07-22"}
                    ],
                    "payment_method_id": "credit_card_7957134",
                    "created_at": "2024-05-22T15:30:00Z",
                    "total_baggages": 3,
                    "nonfree_baggages": 2,
                    "insurance": "yes"
                }
            ),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "NEW789"})
        ],
        outputs=[
            '"flight_search_results": "Found available flight HAT129 from MIA to ORD on May 28, 2024 with business price $460"',
            '"reservation_confirmation": "Reservation NEW789 created successfully for Isabella Brown on one-way flight HAT129 from MIA to ORD on May 28, 2024"',
            '"reservation_details": "Reservation NEW789 confirmed: Isabella and Ivan Wilson, Business class, one-way flight HAT129, MIA-ORD, May 28, 2024"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_032",
        instruction=(
            "Overnight fleet shuffle at DFW: set AC002 to Active at LAX and AC005 to Active at DFW. "
            "Execute logging duties for Captain Elizabeth Davis (CM007) on HAT011 (FL011) for 2024-05-03 on A320neo with 4.8 total (all PIC), "
            "1.6 night, 0.9 instrument, and 1 landing/1 takeoff. But before logging the crew, you need to record a maintenance entry for AC001: Emergency Repair "
            "(WO-2024-08-15-006, ATA 31), description 'Hydraulic system warning discovered during pre-flight inspection', "
            "corrective action 'Emergency repair procedures required for hydraulic system warning', technician TECH009, "
            "timestamp 2024-08-15T14:30:00Z, status In Progress. Execute need to return the final status and location for both aircraft."
        ),
        actions=[
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC002",
                    "new_status": "Active",
                    "new_location_iata": "LAX"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC005",
                    "new_status": "Active",
                    "new_location_iata": "DFW"
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-006",
                    "ata_chapter": "31",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM007",
                    "flight_id": "FL011",
                    "flight_number": "HAT011",
                    "date": "2024-05-03",
                    "role": "Captain",
                    "aircraft_model": "A320neo",
                    "hours_flown": {
                        "total": 4.8, "pic": 4.8, "sic": 0, "night": 1.6, "instrument": 0.9
                    },
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC002"}),
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC005"})
        ],
        outputs=[
            '"AC002_final_status": "Active"',
            '"AC002_final_location": "LAX"',
            '"AC005_final_status": "Active"',
            '"AC005_final_location": "DFW"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_033",
        instruction=(
            "Execute round-trip booking creation for Susan Wilson (liam.garcia1258@example.com) in economy: LAX→DFW on 2024-05-19 (HAT022) "
            "and return DFW→LAX on 2024-05-26 (HAT023), reservation NEW456, payment credit_card_3662517, exactly one passenger "
            "Susan Wilson (dob 1974-01-01), 2 total bags (1 non-free), insurance yes, prices 196 outbound / 158 return, created at "
            "2024-05-21T14:00:00Z. After creation, execute to read back the reservation to confirm. Also record a maintenance entry for AC001: "
            "Emergency Repair (WO-2024-08-15-005, ATA 19), description 'Hydraulic system warning discovered during pre-flight inspection', "
            "corrective action 'Emergency repair procedures required for hydraulic system warning', technician TECH009, "
            "timestamp 2024-08-15T14:30:00Z, status In Progress."
        ),
        actions=[
            Action(
                name="CreateReservation",
                kwargs={
                    "reservation_id": "NEW456", "user_id": "liam.garcia1258@example.com", "user_email": "liam.garcia1258@example.com",
                    "origin": "LAX", "destination": "DFW", "flight_type": "round_trip", "cabin": "economy",
                    "flights": [
                        {"origin": "LAX", "destination": "DFW", "flight_number": "HAT022", "date": "2024-05-19", "price": 196},
                        {"origin": "DFW", "destination": "LAX", "flight_number": "HAT023", "date": "2024-05-26", "price": 158}
                    ],
                    "passengers": [{"first_name": "Aarav", "last_name": "Nguyen", "dob": "1974-01-01"}],
                    "payment_method_id": "credit_card_3662517", "created_at": "2024-05-21T14:00:00Z",
                    "total_baggages": 2, "nonfree_baggages": 1, "insurance": "yes"
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-005",
                    "ata_chapter": "19",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(name="GetReservationDetails", kwargs={"reservation_id": "NEW456"})
        ],
        outputs=[
            '"reservation_confirmation": "Reservation NEW456 created successfully for Susan Wilson on flight HAT022 from LAX to DFW on May 19, 2024"',
            '"reservation_details": "Reservation NEW456 confirmed: Susan Wilson, Economy class, flight HAT022, LAX-DFW, May 19-26, 2024"'
        ]
    ),


    Task(
        annotator="0",
        user_id="USER_034",
        instruction=(
            "Execute the PHX fleet desk and want a tidy swap: read AC009 and AC003 and glance at LAX/PHX operational status, then have AC009 Active at LAX and "
            "AC003 Active at PHX, and execute to reread both to confirm. Profile and certify Captain Jennifer Wilson (CM004) and log him on HAT014 (FL006) for 2024-05-04 on B787-9 "
            "with 5.0 total (5.0 PIC, 0 SIC, 1.0 night, 1.0 instrument), one landing and one takeoff. Also record a maintenance entry for AC001: Emergency Repair "
            "(WO-2024-08-15-005, ATA 29), description 'Hydraulic system warning discovered during pre-flight inspection', corrective action "
            "'Emergency repair procedures required for hydraulic system warning', technician TECH009, timestamp 2024-08-15T14:30:00Z, status In Progress. "
            "Return the final status and location of both aircraft."
        ),
        actions=[
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC009"}),
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC003"}),
            Action(name="GetAirportOperationalStatus", kwargs={"iata_code": "LAX"}),
            Action(name="GetAirportOperationalStatus", kwargs={"iata_code": "PHX"}),

            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-005",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC009", "new_status": "Active", "new_location_iata": "LAX"}),
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC003", "new_status": "Active", "new_location_iata": "PHX"}),
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC009"}),
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC003"}),
            Action(name="GetCrewMemberDetails", kwargs={"crew_member_id": "CM004"}),
            Action(name="GetCrewCertifications", kwargs={"crew_member_id": "CM004"}),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM004",
                    "flight_id": "FL006",
                    "flight_number": "HAT014",
                    "date": "2024-05-04",
                    "role": "Captain",
                    "aircraft_model": "B787-9",
                    "hours_flown": {"total": 5.0, "pic": 5.0, "sic": 0, "night": 1.0, "instrument": 1.0},
                    "landings": 1,
                    "takeoffs": 1
                }
            )
        ],
        outputs=[
            '"AC009_final_status": "Active"',
            '"AC009_final_location": "LAX"',
            '"AC003_final_status": "Active"',
            '"AC003_final_location": "PHX"'
        ]
    ),


    Task(
        annotator="0",
        user_id="USER_035",
        instruction="Execute service duties handling a disruption check. You want Olivia Martin at isabella.martin5652@example.com pulled up you need same day JFK to MIA choices for 2024-05-16 execute the HAT014 operational notes and a quick Active fleet snapshot and execute a simple Technical Issue note at 2024-05-16T13:00:00Z that says Delay concerns on flight HAT014 tied to HAT014 and FL006 will document the call. You want to return profile alternatives ops context fleet status and the tracking entry.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={"user_email": "isabella.martin5652@example.com"}
            ),
            Action(
                name="GetFlightsByCriteria",
                kwargs={
                    "departure_date": "2024-05-16", "status": ["available"], "origin": "JFK", "destination": "MIA"
                }
            ),
            Action(
                name="GetOperationalEventsByFlight",
                kwargs={"flight_number": "HAT014"}
            ),
            Action(
                name="GetFleetUtilization",
                kwargs={"status_filter": ["Active"]}
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue", "event_timestamp_utc": "2024-05-16T13:00:00Z", "details": "Delay concerns on flight HAT014", "status": "Active", "flight_number": "HAT014", "flight_id": "FL006",
                }
            ),
        ],
        outputs=[
            '"user_profile": "Regular member Olivia Martin with 2 reservations and 2 payment methods"',
            '"alternative_flights": "Available flights from JFK to MIA on 2024-05-16 identified"',
            '"operational_events": "Flight HAT014 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_036",
        instruction=(
            "Execute the LAX fleet operations lead looking at a rebalancing nudge. You want AC003 tail PP LTM details and a look at its maintenance history, "
            "then execute an Active Technical Issue at 2024-05-01T14:00:00Z saying Fleet rebalancing required linked to AC003 and PP LTM. You think ORD context "
            "should be checked and then AC003 should read In Maintenance at ORD with a fleet utilization snapshot taken. You want to close the loop with a Resolved "
            "Technical Issue at 2024-05-01T15:00:00Z that says Fleet rebalancing completed for aircraft AC003 and execute to reread the aircraft. Also record a "
            "maintenance entry for AC001: Emergency Repair (WO-2024-08-15-005, ATA 29), description 'Hydraulic system warning discovered during pre-flight inspection', "
            "corrective action 'Emergency repair procedures required for hydraulic system warning', technician TECH009, timestamp 2024-08-15T14:30:00Z, status In Progress. "
            "You plan to report the first event id the new status the pre rebalancing status a maintenance history note and the new completion event id."
        ),
        actions=[
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC003"}),
            Action(name="GetAircraftMaintenanceHistory", kwargs={"aircraft_id": "AC003"}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-01T14:00:00Z",
                    "details": "Fleet rebalancing required",
                    "status": "Active",
                    "aircraft_id": "AC003",
                    "tail_number": "PP-LTM"
                }
            ),
            Action(name="GetAirportDetailsByIataCode", kwargs={"iata_code": "ORD"}),

            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-005",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": "AC003", "new_status": "In Maintenance", "new_location_iata": "ORD"}
            ),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active", "Maintenance"]}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-01T15:00:00Z",
                    "details": "Fleet rebalancing completed for aircraft AC003",
                    "status": "Resolved",
                    "aircraft_id": "AC003",
                    "tail_number": "PP-LTM"
                }
            ),
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC003"})
        ],
        outputs=[
            '"fleet_rebalancing_event_id": "OE026"',
            '"ac003_maintenance_status": "In Maintenance"',
            '"ac003_pre_rebalancing_status": "Aircraft AC003 pre-rebalancing details retrieved"',
            '"maintenance_history": "Aircraft AC003 maintenance history retrieved"',
            '"rebalancing_completion_event_id": "OE027"'
        ],
    ),


    Task(
        annotator="0",
        user_id="USER_037",
        instruction="Coordinate fleet operations at IAH watching a planned check. You want AC006 PP YJC E175 to read Maintenance and execute a B Check entry made first, with WO 2024-05-13-006 ATA 05 description Scheduled B Check inspection for PP YJC at IAH corrective action Execute full B Check per program technician TECH010 timestamp 2024-05-13T12:40:00Z status Scheduled. You also want an E175 utilization view for Active and Maintenance. You plan to return the new maintenance log id.",
        actions=[
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC006",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B Check inspection for PP YJC at IAH",
                    "work_order_id": "WO 2024-05-13-006",
                    "ata_chapter": "05",
                    "corrective_action": "Execute full B Check per program",
                    "event_timestamp_utc": "2024-05-13T12:40:00Z",
                    "technician_id": "TECH010",
                    "status": "Scheduled"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": "AC006", "new_status": "Maintenance"}
            ),
            Action(
                name="GetFleetUtilization",
                kwargs={"model_filter": "E175", "status_filter": ["Active", "Maintenance"]}
            )
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),



    Task(
        annotator="0",
        user_id="USER_038",
        instruction="Execute customer service duties following up on a timing worry. You want Richard Martinez at evelyn.martin3593@example.com with reservation MEMLVX reviewed execute MIA to ATL choices for 2024-05-22 since HAT023 with flight id FL023 has delays and execute HAT023 operational notes plus an Active fleet snapshot. You think a Technical Issue note at 2024-05-22T09:10:00Z that reads 'Delay concerns on flight HAT023 tied to HAT023 and FL023 will track the case'. You want to return profile booking alternatives ops context fleet status and the tracking entry.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "evelyn.martin3593@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "evelyn.martin3593@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "MEMLVX"}),
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-05-22", "status": ["available"], "origin": "MIA", "destination": "ATL"}),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT023"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-22T09:10:00Z",
                    "details": "Delay concerns on flight HAT023 tied to HAT023 and FL023 will track the case",
                    "status": "Active",
                    "flight_number": "HAT023",
                    "flight_id": "FL023"
                }
            ),
        ],
        outputs=[
            '"user_profile": "Member Richard Martinez profile retrieved"',
            '"reservation_details": "Reservation MEMLVX details retrieved successfully"',
            '"alternative_flights": "No available flights from MIA to ATL on 2024-05-22 identified"',
            '"operational_events": "Flight HAT023 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_039",
        instruction="Execute assisting member Jennifer Wilson (aarav.moore8670@example.com). He wants to review reservation ZZSA4W and alternatives for 2024-05-30 from DEN to SEA because flight HAT031 (flight_id: FL031) has operational delays. Provide his profile, reservation details, available DEN→SEA flights that day, operational events for HAT031, fleet availability, and execute to create a tracking event: 'Technical Issue', '2024-05-30T16:00:00Z', 'Delay concerns on flight HAT031', status 'Active', linked to HAT031/FL031.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "aarav.moore8670@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "aarav.moore8670@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "ZZSA4W"}),
            Action(name="GetFlightsByCriteria", kwargs={
                "departure_date": "2024-05-30",
                "status": ["available"],
                "origin": "DEN",
                "destination": "SEA"
            }),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT031"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(name="CreateOperationalEvent", kwargs={
                "event_type": "Technical Issue",
                "event_timestamp_utc": "2024-05-30T16:00:00Z",
                "details": "Delay concerns on flight HAT031",
                "status": "Active",
                "flight_number": "HAT031",
                "flight_id": "FL031"
            }),
        ],
        outputs=[
            '"user_profile": "Member Jennifer Wilson profile retrieved"',
            '"reservation_details": "Reservation ZZSA4W details retrieved successfully"',
            '"alternative_flights": "Available flights from DEN to SEA on 2024-05-30 identified"',
            '"operational_events": "Flight HAT031 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),


    Task(
        annotator="0",
        user_id="USER_040",
        instruction="Execute the line-maintenance planner at MCO. Execute told AC004 (PS-AEF, E195-E2) has a scheduled B-Check on 2024-09-15 at 08:00 UTC under WO-2024-09-15-001 for ATA 05, and execute a maintenance log on file using description 'Scheduled B-Check for PS-AEF', technician TECH012, corrective action 'Scheduled B-Check maintenance per work order WO-2024-09-15-001', status 'Scheduled', timestamp 2024-09-15T08:00:00Z, and next due 2025-03-15. You then need the aircraft to read 'In Maintenance' at MCO. You want to return the created maintenance log ID and the new status.",
        actions=[
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                "aircraft_id": "AC004",
                "maintenance_type": "B-Check",
                "description": "Scheduled B-Check for PS-AEF",
                "work_order_id": "WO-2024-09-15-001",
                "ata_chapter": "05",
                "technician_id": "TECH012",
                "corrective_action": "Scheduled B-Check maintenance per work order WO-2024-09-15-001",
                "event_timestamp_utc": "2024-09-15T08:00:00Z",
                "status": "Scheduled",
                "next_due": "2025-03-15"
                }
            ),
                Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": "AC004", "new_status": "In Maintenance", "new_location_iata": "MCO"}
            )
        ],
        outputs=[
            '"maintenance_log_id": "ML026"',
            '"aircraft_status": "In Maintenance"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_041",
        instruction="Execute the ATL airport operations supervisor on a tight push. Execute informed that HAT004 FL001 needs to move from C22 to C27 for the 2024-05-01 departure and execute that captured as a Gate Change at 14:45 UTC with the exact wording Departure gate changed from C22 to C27 due to ramp constraints. You think a one hour delay follows from this and execute the flight updated accordingly. You plan to report the event id and the updated status.",
        actions=[
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Gate Change", "event_timestamp_utc": "2024-05-01T14:45:00Z", "details": "Departure gate changed from C22 to C27 due to ramp constraints", "status": "Active", "flight_id": "FL001", "flight_number": "HAT004", "airport_id": "ARP_ATL", "iata_code": "ATL"
                }
            ),
            Action(
                name="UpdateFlightStatusByNumberAndDate",
                kwargs={"flight_number": "HAT004", "date": "2024-05-01", "new_status": "delayed", "delay_hours": 1, "reason_event_id": "OE026"}
            )
        ],
        outputs=['"event_id": "OE026"', '"updated_status": "delayed"'],
    ),
    Task(
        annotator="0",
        user_id="USER_042",
        instruction=(
            "Execute working compliance prep for an audit and execute the flight time records to match policy. Normalize totals so they equal the sum of PIC, SIC, night, and instrument. "
            "Update CM001 on HAT004 FL001 dated 2024-05-15 as Captain on B737-800 with PIC 2.7, SIC 0.0, night 0.2, instrument 0.6 (total 3.5). "
            "Update CM002 on HAT038 FL038 dated 2024-05-23 as First Officer on A320neo with PIC 0.0, SIC 3.5, night 1.0, instrument 0.5 (total 5.0). "
            "One landing and one takeoff each. Then execute to confirm CM001 against CERT_B738 on 2024-12-01 and CM002 against CERT_A32N on 2024-05-23, and return both validity statuses. "
            "Also record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-005, ATA 29), description 'Hydraulic system warning discovered during pre-flight inspection', "
            "corrective action 'Emergency repair procedures required for hydraulic system warning', technician TECH009, timestamp 2024-08-15T14:30:00Z, status In Progress."
        ),
        actions=[
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM001",
                    "flight_id": "FL001",
                    "flight_number": "HAT004",
                    "date": "2024-05-15",
                    "role": "Captain",
                    "aircraft_model": "B737-800",
                    "hours_flown": {"total": 3.5, "pic": 2.7, "sic": 0.0, "night": 0.2, "instrument": 0.6},
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM002",
                    "flight_id": "FL038",
                    "flight_number": "HAT038",
                    "date": "2024-05-23",
                    "role": "First Officer",
                    "aircraft_model": "A320neo",
                    "hours_flown": {"total": 5.0, "pic": 0.0, "sic": 3.5, "night": 1.0, "instrument": 0.5},
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-005",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(
                name="CheckCertificationValidity",
                kwargs={"crew_member_id": "CM001", "certification_id": "CERT_B738", "check_date": "2024-12-01"}
            ),
            Action(
                name="CheckCertificationValidity",
                kwargs={"crew_member_id": "CM002", "certification_id": "CERT_A32N", "check_date": "2024-05-23"}
            )
        ],
        outputs=[
            '"cm001_cert_status": "valid"',
            '"cm002_cert_status": "valid"'
        ]
    ),



    Task(
        annotator="0",
        user_id="USER_043",
        instruction="Execute the ATL maintenance supervisor and execute to stabilize a pre flight snag. AC005 PR XTD reported intermittent navigation display failures at 2024-05-18T09:15:00Z and you need the aircraft set to Maintenance and an unscheduled Avionics Repair opened as the first step with WO 2024-05-18-012 ATA 31 TECH015 using the description Intermittent navigation display failures reported during pre flight inspection and corrective action Replacement of the primary flight display unit with status In Progress. You want to return the maintenance log id and the updated aircraft status.",
        actions=[
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC005",
                    "maintenance_type": "Avionics Repair",
                    "description": "Intermittent navigation display failures reported during pre flight inspection",
                    "technician_id": "TECH015",
                    "work_order_id": "WO-2024-05-18-012",
                    "ata_chapter": "31",
                    "corrective_action": "Replacement of the primary flight display unit",
                    "event_timestamp_utc": "2024-05-18T09:15:00Z",
                    "status": "In Progress"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": "AC005", "new_status": "Maintenance"}
            ),
        ],
        outputs=['"log_id": "ML026"', '"aircraft_status": "Maintenance"']
    ),

    Task(
        annotator="0",
        user_id="USER_044",
        instruction="Execute the MCO maintenance supervisor closing out routine work. AC004 PS AEF E195 E2 completed line maintenance under WO 2024-05-15-004 ATA 05 by TECH015 at 2024-05-15T14:00:00Z and execute a completion entry on record with the description: Scheduled line maintenance completed and the corrective action: Line maintenance completed per work order WO 2024-05-15-004 the plus the aircraft showing Active at MCO with a resolved technical note that says 'Aircraft AC004 maintenance completed and returned to service at MCO.' You also need Captain Elizabeth Davis CM007 logged on HAT022 FL022 dated 2024-05-15 on A350-900 with 4.3 total all PIC 0 SIC 3.2 night 0.4 instrument 0.7 and one landing one takeoff. You plan to return the maintenance log id and confirm the final status.",
        actions=[
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC004",
                    "maintenance_type": "Line Maintenance",
                    "description": "Scheduled line maintenance completed",
                    "work_order_id": "WO-2024-05-15-004",
                    "ata_chapter": "05",
                    "corrective_action": "Line maintenance completed per work order WO 2024-05-15-004",
                    "event_timestamp_utc": "2024-05-15T14:00:00Z",
                    "technician_id": "TECH015",
                    "status": "Completed"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": "AC004", "new_status": "Active", "new_location_iata": "MCO"}
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-15T14:00:00Z",
                    "details": "Aircraft AC004 maintenance completed and returned to service at MCO.",
                    "status": "Resolved",
                    "aircraft_id": "AC004",
                    "tail_number": "PS-AEF"
                }
            ),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM007",
                    "flight_id": "FL022",
                    "flight_number": "HAT022",
                    "date": "2024-05-15",
                    "role": "Captain",
                    "aircraft_model": "A350-900",
                    "hours_flown": {"total": 4.3, "pic": 0.0, "sic": 3.2, "night": 0.4, "instrument": 0.7},
                    "landings": 1,
                    "takeoffs": 1
                }
            )
        ],
        outputs=['"maintenance_log_id": "ML026"', '"aircraft_status": "Active"']
    ),


    Task(
        annotator="0",
        user_id="USER_045",
        instruction=(
            "Execute the DFW crew scheduling coordinator working a duty limit backfill. Verify First Officer Isabella Brown by employee code EMP002, "
            "check active certifications and ensure CERT_A32N is valid on 2024-05-23. If valid, assign CM002 to HAT038 (FL038) as First Officer and record duty on "
            "A320neo: 3.5 total, 0 PIC, 3.5 SIC, 0 night, 0 instrument, with 1 landing and 1 takeoff, then read the crew list to see his name present. "
            "Also execute to record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-005, ATA 29), description 'Hydraulic system warning discovered during pre-flight "
            "inspection', corrective action 'Emergency repair procedures required for hydraulic system warning', technician TECH009, timestamp 2024-08-15T14:30:00Z, "
            "status In Progress. Report his crew member id and certification validity status."
        ),
        actions=[
            Action(name="GetCrewMemberDetails", kwargs={"employee_code": "EMP002"}),
            Action(name="GetCrewCertifications", kwargs={"employee_code": "EMP002"}),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-005",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(
                name="CheckCertificationValidity",
                kwargs={"crew_member_id": "CM002", "certification_id": "CERT_A32N", "check_date": "2024-05-23"}
            ),
            Action(
                name="AssignCrewToFlight",
                kwargs={
                    "flight_id": "FL038",
                    "flight_number": "HAT038",
                    "crew_member_id": "CM002",
                    "assigned_role": "First Officer"
                }
            ),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM002",
                    "flight_id": "FL038",
                    "flight_number": "HAT038",
                    "date": "2024-05-23",
                    "role": "First Officer",
                    "aircraft_model": "A320neo",
                    "hours_flown": {"total": 3.5, "pic": 0, "sic": 3.5, "night": 0, "instrument": 0},
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(name="GetFlightCrewAssignments", kwargs={"flight_id": "FL038", "flight_number": "HAT038"})
        ],
        outputs=['"crew_member_id": "CM002"', '"certification_status": "valid"']
    ),



    Task(
        annotator="0",
        user_id="USER_046",
        instruction="Execute the LAX airport operations supervisor for flight HAT022 (FL022) on 2024-05-02. This flight requires a gate change. Create a 'Gate Change' event with timestamp 2024-05-02T06:30:00Z, detailing 'Departure gate changed from B5 to B9 due to ramp constraints'. Subsequently, update the flight status to reflect a 1-hour delay caused by this event. Please provide the created event ID and the updated flight status.",
        actions=[
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Gate Change",
                    "event_timestamp_utc": "2024-05-02T06:30:00Z",
                    "details": "Departure gate changed from B5 to B9 due to ramp constraints",
                    "status": "Active",
                    "flight_id": "FL022",
                    "flight_number": "HAT022",
                    "airport_id": "ARP_LAX",
                    "iata_code": "LAX"
                }
            ),
            Action(
                name="UpdateFlightStatusByNumberAndDate",
                kwargs={
                    "flight_number": "HAT022",
                    "date": "2024-05-02",
                    "new_status": "delayed",
                    "delay_hours": 1,
                    "reason_event_id": "OE026"
                }
            )
        ],
        outputs=['"event_id": "OE026"', '"updated_status": "delayed"'],
    ),
    Task(
        annotator="0",
        user_id="USER_047",
        instruction="Execute a maintenance planner at DFW. Execute to schedule a B-Check for aircraft AC002 (A320neo, PR-XBE) on 2024-09-20 at 09:00 UTC (WO-2024-09-20-002, ATA 05). Create the maintenance log (next due 2025-03-20) with technician TECH003 and the description Scheduled B-Check for PR-XBE, then execute to update the aircraft status to 'In Maintenance' at DFW. You want to provide the created maintenance-log ID and confirm the aircraft's status.",
        actions=[
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC002",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check for PR-XBE",
                    "work_order_id": "WO-2024-09-20-002",
                    "ata_chapter": "05",
                    "technician_id": "TECH003",
                    "corrective_action": "Scheduled B-Check maintenance per work order WO-2024-09-20-002",
                    "event_timestamp_utc": "2024-09-20T09:00:00Z",
                    "status": "Scheduled",
                    "next_due": "2025-03-20"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC002",
                    "new_status": "In Maintenance",
                    "new_location_iata": "DFW"
                }
            )
        ],
        outputs=[
            '"maintenance_log_id": "ML026"',
            '"aircraft_status": "In Maintenance"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_048",
        instruction="Execute the maintenance supervisor at DFW. You want to verify airport details and operational status for DFW and ATL and you will need to read current details for AC002 (A320neo) and AC001 (B737-800). Reposition AC002 from DFW to ATL and AC001 from ATL to DFW, both remaining Active, then confirm each aircraft’s updated details. Also record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-006, ATA 31) with description 'Hydraulic system warning discovered during pre-flight inspection', corrective action 'Emergency repair procedures required for hydraulic system warning', technician TECH009, timestamp 2024-08-15T14:30:00Z, status In Progress. Additionally, execute to log Captain Olivia Johnson (CM015) on HAT010 (FL010) on 2024-05-02 as Captain on B787-9 with 4.2 total/PIC hours, 0.8 night, 1.2 instrument, and 1 landing/1 takeoff, and review Active utilization snapshots for A320neo and B737-800. Provide the final status and location for both aircraft.",
        actions=[
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC002"}),
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC001"}),
            Action(name="GetAirportDetailsByIataCode", kwargs={"iata_code": "DFW"}),
            Action(name="GetAirportDetailsByIataCode", kwargs={"iata_code": "ATL"}),
            Action(name="GetAirportOperationalStatus", kwargs={"iata_code": "DFW"}),
            Action(name="GetAirportOperationalStatus", kwargs={"iata_code": "ATL"}),

            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-006",
                    "ata_chapter": "31",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC002", "new_status": "Active", "new_location_iata": "ATL"}),
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC001", "new_status": "Active", "new_location_iata": "DFW"}),
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC002"}),
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC001"}),
            Action(name="GetCrewMemberDetails", kwargs={"crew_member_id": "CM015"}),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM015",
                    "flight_id": "FL010",
                    "flight_number": "HAT010",
                    "date": "2024-05-02",
                    "role": "Captain",
                    "aircraft_model": "B787-9",
                    "hours_flown": {"total": 4.2, "pic": 4.2, "sic": 0, "night": 0.8, "instrument": 1.2},
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(name="GetFleetUtilization", kwargs={"model_filter": "A320neo", "status_filter": ["Active"]}),
            Action(name="GetFleetUtilization", kwargs={"model_filter": "B737-800", "status_filter": ["Active"]})
        ],
        outputs=[
            '"AC002_final_status": "Active"',
            '"AC002_final_location": "ATL"',
            '"AC001_final_status": "Active"',
            '"AC001_final_location": "DFW"'
        ]
    ),


    Task(
        annotator="0",
        user_id="USER_049",
        instruction="Execute customer service duties to assist member Richard Martinez (evelyn.martin3593@example.com) with travel arrangements. Execute to check reservation MEMLVX and explore alternative flight options for May 24, 2024 from JFK to MIA due to concerns about current flight HAT020 (flight_id: FL020), which has experienced operational delays. Execute explain membership benefits, review the reservation details, check available flights for the same route and date, examine any operational events affecting HAT020, and assess fleet availability for potential rebooking. After analyzing the situation, you must create an operational event with event type 'Technical Issue', timestamp '2024-05-24T13:30:00Z', and detail 'Delay concerns on flight HAT020' to track the customer service interaction. Provide profile information, current reservation details, alternative flight options, operational event analysis for HAT020, and fleet utilization status to support travel planning.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "evelyn.martin3593@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "evelyn.martin3593@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "MEMLVX"}),
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-05-24", "status": ["available"], "origin": "JFK", "destination": "MIA"}),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT020"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(name="CreateOperationalEvent", kwargs={
                "event_type": "Technical Issue",
                "event_timestamp_utc": "2024-05-24T13:30:00Z",
                "details": "Delay concerns on flight HAT020",
                "status": "Active",
                "flight_number": "HAT020",
                "flight_id": "FL020"
            }),
        ],
        outputs=[
            '"user_profile": "Member Richard Martinez profile retrieved"',
            '"reservation_details": "Reservation MEMLVX details retrieved successfully"',
            '"alternative_flights": "Available flights from JFK to MIA on 2024-05-24 identified"',
            '"operational_events": "Flight HAT020 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_050",
        instruction="Execute the LAX ops lead working pre-departure. You want HAT022 (FL022) on 2024-05-02 to reflect a same-day gate swap at LAX with a UTC stamp 2024-05-02T06:30:00Z and the exact detail text 'Departure gate changed from B5 to B9 due to ramp constraints'. You think the flight should read delayed by one hour tied to that record. Execute to return the created event ID and the updated flight status.",
        actions=[
            Action(
                name="GetAirportDetailsByIataCode",
                kwargs={"iata_code": "LAX"}
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Gate Change",
                    "event_timestamp_utc": "2024-05-02T06:30:00Z",
                    "details": "Departure gate changed from B5 to B9 due to ramp constraints",
                    "status": "Active",
                    "flight_id": "FL022",
                    "flight_number": "HAT022",
                    "airport_id": "ARP_LAX",
                    "iata_code": "LAX"
                }
            ),
            Action(
                name="UpdateFlightStatusByNumberAndDate",
                kwargs={
                    "flight_number": "HAT022",
                    "date": "2024-05-02",
                    "new_status": "delayed",
                    "delay_hours": 1,
                    "reason_event_id": "OE026"
                }
            )
        ],
        outputs=['"event_id": "OE026"', '"updated_status": "delayed"'],
    ),
    Task(
        annotator="0",
        user_id="USER_051",
        instruction="Execute a DFW line-maintenance planner looking ahead on AC002 (PR-XBE, A320neo). You want the B-Check logged for 2024-09-20 at 09:00Z under WO-2024-09-20-002 for ATA 05 with next due 2025-03-20 and describe it as Scheduled B-Check for PR-XBE, and you need the aircraft to read In Maintenance at DFW once set. Provide the created maintenance-log ID and the post-change aircraft status.",
        actions=[
            Action(
                name="GetAircraftMaintenanceHistory",
                kwargs={"aircraft_id": "AC002"}
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC002",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check for PR-XBE",
                    "work_order_id": "WO-2024-09-20-002",
                    "ata_chapter": "05",
                    "corrective_action": "Scheduled B-Check maintenance per work order WO-2024-09-20-002",
                    "event_timestamp_utc": "2024-09-20T09:00:00Z",
                    "status": "Scheduled",
                    "next_due": "2025-03-20"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC002",
                    "new_status": "In Maintenance",
                    "new_location_iata": "DFW"
                }
            )
        ],
        outputs=[
            '"maintenance_log_id": "ML026"',
            '"aircraft_status": "In Maintenance"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_052",
        instruction="Execute the MIA apron-ops supervisor. You want to log a Gate Change for HAT015 (FL010) at 15:30 UTC on 2024-05-03 with the exact detail 'Departure gate changed from D12 to D18 due to ramp constraints' at MIA, then you need to set the flight to delayed by 1 hour and link the delay to that event. Provide the created event ID and the updated flight status.",
        actions=[
            Action(name="GetAirportDetailsByIataCode", kwargs={"iata_code": "MIA"}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Gate Change",
                    "event_timestamp_utc": "2024-05-03T15:30:00Z",
                    "details": "Departure gate changed from D12 to D18 due to ramp constraints",
                    "status": "Active",
                    "flight_id": "FL010",
                    "flight_number": "HAT015",
                    "airport_id": "ARP_MIA",
                    "iata_code": "MIA"
                }
            ),
            Action(
                name="UpdateFlightStatusByNumberAndDate",
                kwargs={
                    "flight_number": "HAT015",
                    "date": "2024-05-03",
                    "new_status": "delayed",
                    "delay_hours": 1,
                    "reason_event_id": "OE026"
                }
            )
        ],
        outputs=[
            '"event_id": "OE026"',
            '"updated_status": "delayed"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_053",
        instruction="Coordinate fleet operations at IAH watching a planned check. You want AC006 (PP-YJC, E175) carried into Maintenance and a B-Check entry created with WO-2024-05-13-006 for ATA 05, description 'Scheduled B-Check inspection for PP-YJC at IAH', corrective action 'Execute full B-Check per program', technician TECH010, timestamp 2024-05-13T12:40:00Z, status Scheduled. You also want an E175 utilization snapshot for Active and Maintenance. Return the new maintenance log ID.",
        actions=[
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": "AC006", "new_status": "Maintenance"}
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC006",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check inspection for PP-YJC at IAH",
                    "work_order_id": "WO-2024-05-13-006",
                    "ata_chapter": "05",
                    "corrective_action": "Execute full B-Check per program",
                    "event_timestamp_utc": "2024-05-13T12:40:00Z",
                    "technician_id": "TECH010",
                    "status": "Scheduled"
                }
            ),
            Action(
                name="GetFleetUtilization",
                kwargs={"model_filter": "E175", "status_filter": ["Active", "Maintenance"]}
            )
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),


    Task(
        annotator="0",
        user_id="USER_054",
        instruction="Execute the BOS fleet operations manager. You want to set AC009 (PR-GUO, B737-800) to Maintenance, then you need to create a B-Check maintenance entry using work order WO-2024-05-14-009 (ATA 05) with description 'Scheduled B-Check inspection for PR-GUO at BOS', corrective action 'Conduct B-Check and ops checks', technician TECH018, and timestamp 2024-05-14T08:05:00Z. After that, execute to review B737-800 fleet utilization for Active and Maintenance. Provide the created maintenance log ID.",
        actions=[
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": "AC009", "new_status": "Maintenance"}
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC009",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check inspection for PR-GUO at BOS",
                    "work_order_id": "WO-2024-05-14-009",
                    "ata_chapter": "05",
                    "corrective_action": "Conduct B-Check and ops checks",
                    "event_timestamp_utc": "2024-05-14T08:05:00Z",
                    "technician_id": "TECH018",
                    "status": "Scheduled"
                }
            ),
            Action(
                name="GetFleetUtilization",
                kwargs={"model_filter": "B737-800", "status_filter": ["Active", "Maintenance"]}
            )
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),

    Task(
        annotator="0",
        user_id="USER_055",
        instruction="Execute a customer-care agent handling a timing concern. You want to look up Ivan Wilson (evelyn.wilson9461@example.com), pull reservation 4WQ150, scan same-day choices LAX to DFW for 2024-05-22 since HAT022 (FL022) has been wobbly, review HAT022 operational notes, and get a quick Active-fleet view. You think a simple Technical Issue marker at 14:00Z saying 'Delay concerns on flight HAT022' tied to HAT022/FL022 will track the case. Bring back profile, reservation details, alternatives, ops context, fleet status, and the tracking event.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={
                    "user_email": "evelyn.wilson9461@example.com"
                }
            ),
            Action(
                name="GetUserReservations",
                kwargs={
                    "user_email": "evelyn.wilson9461@example.com"
                }
            ),
            Action(
                name="GetReservationDetails",
                kwargs={
                    "reservation_id": "4WQ150"
                }
            ),
            Action(
                name="GetFlightsByCriteria",
                kwargs={
                    "departure_date": "2024-05-22",
                    "status": ["available"],
                    "origin": "LAX",
                    "destination": "DFW"
                }
            ),
            Action(
                name="GetOperationalEventsByFlight",
                kwargs={
                    "flight_number": "HAT022"
                }
            ),
            Action(
                name="GetFleetUtilization",
                kwargs={
                    "status_filter": ["Active"]
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-22T14:00:00Z",
                    "details": "Delay concerns on flight HAT022",
                    "status": "Active",
                    "flight_number": "HAT022",
                    "flight_id": "FL022",
                }
            ),
        ],
        outputs=[
            '"user_profile": "Regular member Ivan Wilson with 6 reservations and 2 payment methods"',
            '"reservation_details": "Reservation 4WQ150 details retrieved successfully"',
            '"alternative_flights": "Available flights from LAX to DFW on 2024-05-22 identified"',
            '"operational_events": "Flight HAT022 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_056",
        instruction="Execute the LAX fleet desk. You want a quick picture for AC003 (PP-LTM, B787-9): get a B787-9 utilization snapshot, then set AC003 to Maintenance and log a Scheduled B-Check under WO-2024-05-04-003 for ATA 05 with description 'Scheduled B-Check inspection for PP-LTM at LAX', corrective action 'Perform scheduled B-Check inspection of systems and components', and timestamp 2024-05-04T11:00:00Z. Execute the created maintenance log ID.",
        actions=[
            Action(
                name="GetFleetUtilization",
                kwargs={
                    "model_filter": "B787-9",
                    "status_filter": ["Active", "Maintenance"]
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC003",
                    "new_status": "Maintenance"
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC003",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check inspection for PP-LTM at LAX",
                    "work_order_id": "WO-2024-05-04-003",
                    "ata_chapter": "05",
                    "corrective_action": "Perform scheduled B-Check inspection of systems and components",
                    "event_timestamp_utc": "2024-05-04T11:00:00Z",
                    "status": "Scheduled"
                }
            )
        ],
        outputs=[
            '"maintenance_log_id": "ML026'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_057",
        instruction="Execute a customer service rep doing a disruption follow-up. You want to surface Ivan Anderson (liam.taylor8460@example.com), check reservation ZVWQ08, look for ORD to DEN options for 2024-06-01 because HAT027 (FL027) has been showing delays, review HAT027 ops events, and capture an Active fleet snapshot. You also want a light Technical Issue note at 10:15Z that reads 'Delay concerns on flight HAT027' tied to HAT027/FL027. Return the profile, booking details, alternatives, ops context, fleet status, and the tracking event.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "liam.taylor8460@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "liam.taylor8460@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "ZVWQ08"}),
            Action(
                name="GetFlightsByCriteria",
                kwargs={
                    "departure_date": "2024-06-01",
                    "status": ["available"],
                    "origin": "ORD",
                    "destination": "DEN"
                }
            ),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT027"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-06-01T10:15:00Z",
                    "details": "Delay concerns on flight HAT027",
                    "status": "Active",
                    "flight_number": "HAT027",
                    "flight_id": "FL027"
                }
            ),
        ],
        outputs=[
            '"user_profile": "Member Ivan Anderson profile retrieved"',
            '"reservation_details": "Reservation ZVWQ08 details retrieved successfully"',
            '"alternative_flights": "No available flights from ORD to DEN on 2024-06-01"',
            '"operational_events": "Flight HAT027 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),


    Task(
        annotator="0",
        user_id="USER_058",
        instruction=(
            "Execute the PHX fleet ops manager juggling a quick swap. Execute want to take AC008 (PP-PTM, ATR72-600) Active at LAS and AC009 (PR-GUO, B737-800) "
            "Active at PHX after a simple reposition, checking PHX/LAS airport details and ops first and reconfirming each aircraft after the move. "
            "Post Captain Jennifer Wilson (CM004) on HAT014 (FL006) for 2024-05-04 as Captain on B787-9 with 5.0 total/PIC, 1.0 night, 1.0 instrument, "
            "one landing and one takeoff. Also record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-006, ATA 29), description "
            "'Hydraulic system warning discovered during pre-flight inspection', corrective action 'Emergency repair procedures required for hydraulic system warning', "
            "technician TECH009, timestamp 2024-08-15T14:30:00Z, status In Progress. Finally take Active utilization snapshots for ATR72-600 and B737-800. "
            "Execute finally need to provide the final status and location for both aircraft."
        ),
        actions=[
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC008"}),
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC009"}),
            Action(name="GetAirportDetailsByIataCode", kwargs={"iata_code": "PHX"}),
            Action(name="GetAirportDetailsByIataCode", kwargs={"iata_code": "LAS"}),
            Action(name="GetAirportOperationalStatus", kwargs={"iata_code": "PHX"}),
            Action(name="GetAirportOperationalStatus", kwargs={"iata_code": "LAS"}),

            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-006",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC008", "new_status": "Active", "new_location_iata": "LAS"}),
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC009", "new_status": "Active", "new_location_iata": "PHX"}),
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC008"}),
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC009"}),
            Action(name="GetCrewMemberDetails", kwargs={"crew_member_id": "CM004"}),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM004",
                    "flight_id": "FL006",
                    "flight_number": "HAT014",
                    "date": "2024-05-04",
                    "role": "Captain",
                    "aircraft_model": "B787-9",
                    "hours_flown": {"total": 5.0, "pic": 5.0, "sic": 0, "night": 1.0, "instrument": 1.0},
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(name="GetFleetUtilization", kwargs={"model_filter": "ATR72-600", "status_filter": ["Active"]}),
            Action(name="GetFleetUtilization", kwargs={"model_filter": "B737-800", "status_filter": ["Active"]})
        ],
        outputs=[
            '"AC008_final_status": "Active"',
            '"AC008_final_location": "LAS"',
            '"AC009_final_status": "Active"',
            '"AC009_final_location": "PHX"'
        ]
    ),


    Task(
        annotator="0",
        user_id="USER_059",
        instruction="Execute customer service duties to assist member Jennifer Johnson (daiki.johnson3136@example.com). Ivan wants to check her current reservation R9QDGB and explore alternative flight options for May 18, 2024 from DFW to ORD due to concerns about her current flight HAT008 (flight_id: FL003) which has experienced operational delays. You want to provide her profile, reservation details, same-day DFW→ORD availability, operational events for HAT008, and fleet availability. After analysis, create an event 'Technical Issue' at '2024-05-18T11:00:00Z' with detail 'Delay concerns on flight HAT008'.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "daiki.johnson3136@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "daiki.johnson3136@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "R9QDGB"}),
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-05-18", "status": ["available"], "origin": "DFW", "destination": "ORD"}),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT008"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(name="CreateOperationalEvent", kwargs={"event_type": "Technical Issue", "event_timestamp_utc": "2024-05-18T11:00:00Z", "details": "Delay concerns on flight HAT008", "status": "Active", "flight_number": "HAT008", "flight_id": "FL003"}),
        ],
        outputs=[
            '"user_profile": "Member Jennifer Johnson profile retrieved"',
            '"reservation_details": "Reservation R9QDGB details retrieved successfully"',
            '"alternative_flights": "No available flights from DFW to ORD on 2024-05-18 identified"',
            '"operational_events": "Flight HAT008 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),


    Task(
        annotator="0",
        user_id="USER_060",
        instruction="Execute customer service duties to assist member Isabella Brown (sofia.taylor9399@example.com) with his travel arrangements. Isabella wants to check his current reservation OP3VYE and explore alternative flight options for May 26, 2024 from DFW to LAS due to concerns about his current flight HAT036 (flight_id: FL036) which has experienced operational delays. He wants membership benefits, reservation details, available same-day flights, operational events for HAT036, and fleet utilization. After analysis, execute to create 'Technical Issue' at '2024-05-26T16:45:00Z' with detail 'Delay concerns on flight HAT036'. Provide his profile, reservation details, alternatives, HAT036 events, and fleet utilization.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "sofia.taylor9399@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "sofia.taylor9399@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "OP3VYE"}),
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-05-26", "status": ["available"], "origin": "DFW", "destination": "LAS"}),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT036"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(name="CreateOperationalEvent", kwargs={
                "event_type": "Technical Issue",
                "event_timestamp_utc": "2024-05-26T16:45:00Z",
                "details": "Delay concerns on flight HAT036",
                "status": "Active",
                "flight_number": "HAT036",
                "flight_id": "FL036"
            }),
        ],
        outputs=[
            '"user_profile": "Member Isabella Brown profile retrieved"',
            '"reservation_details": "Reservation OP3VYE details retrieved successfully"',
            '"alternative_flights": "No available flights from DFW to LAS on 2024-05-26 identified"',
            '"operational_events": "Flight HAT036 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_061",
        instruction="Execute fleet operations management at LAS. Aircraft AC009 (PR-GUO, B737-800) requires a scheduled B-Check. You want the B-Check recorded under WO 'WO-2024-05-11-009' (ATA '05') with description 'Scheduled B-Check inspection for PR-GUO at LAS', corrective action 'Perform B-Check and system checks', technician TECH018, timestamp '2024-05-11T10:30:00Z', then execute AC009 set to 'Maintenance' and to review B737-800 utilization for 'Active' and 'Maintenance'. Return the created maintenance log ID.",
        actions=[
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC009",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check inspection for PR-GUO at LAS",
                    "work_order_id": "WO-2024-05-11-009",
                    "ata_chapter": "05",
                    "corrective_action": "Perform B-Check and system checks",
                    "event_timestamp_utc": "2024-05-11T10:30:00Z",
                    "technician_id": "TECH018",
                    "status": "Scheduled"
                }
            ),
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC009", "new_status": "Maintenance"}),
            Action(name="GetFleetUtilization", kwargs={"model_filter": "B737-800", "status_filter": ["Active", "Maintenance"]})
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),


    Task(
        annotator="0",
        user_id="USER_062",
        instruction="Execute a DFW operations supervisor handling a 'microburst risk on 2024-05-11 affecting HAT019 (FL019).' First create a weather delay at 21:35Z, and then record a diversion to ORD at 22:05Z, reposition aircraft AC010 to ORD, and set flight status to 'delayed' with a 2-hour delay, without any reason id. Provide the diversion event ID and the aircraft's updated location code.",
        actions=[
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Weather Delay",
                    "event_timestamp_utc": "2024-05-11T21:35:00Z",
                    "details": "microburst risk on 2024-05-11 affecting HAT019 (FL019).",
                    "status": "Active",
                    "flight_id": "FL019",
                    "flight_number": "HAT019",
                    "airport_id": "ARP_DFW",
                    "iata_code": "DFW"
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Diversion Landing",
                    "event_timestamp_utc": "2024-05-11T22:05:00Z",
                    "details": "Flight diverted to ORD after extended ground stop.",
                    "status": "Active",
                    "flight_id": "FL019",
                    "flight_number": "HAT019",
                    "airport_id": "ARP_ORD",
                    "iata_code": "ORD"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": "AC010", "new_status": "Active", "new_location_iata": "ORD"}
            ),
            Action(
                name="UpdateFlightStatusByNumberAndDate",
                kwargs={"flight_number": "HAT019", "date": "2024-05-11", "new_status": "delayed", "delay_hours": 2}
            )
        ],
        outputs=['"diversion_event_id": "OE027"', '"aircraft_location": "ORD"']
    ),



    Task(
        annotator="0",
        user_id="USER_063",
        instruction=(
            "Execute the fleet operations manager. Before moving aircraft, verify destination airport operational status. "
            "If the destination status is 'Operational', reposition AC002 (PR-XBE, A320neo) from DFW to LAX and AC005 (PR-XTD, A350-900) from JFK to DFW; both remain Active. "
            "If a destination is NOT 'Operational', do not change that aircraft's location—leave it Active at its current station—and record a 'reposition_skipped_reason' in outputs. "
            "Then execute to log Captain Elizabeth Davis (CM007) on HAT011 (FL005) dated 2024-05-03 as Captain on A320neo: 4.8 total (4.8 PIC, 0.0 SIC), 2.1 night, 1.2 instrument, 2 landings, 2 takeoffs. "
            "Also record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-007, ATA 29), description 'Hydraulic system warning discovered during pre-flight inspection', "
            "corrective action 'Emergency repair procedures required for hydraulic system warning', technician TECH009, timestamp 2024-08-15T14:30:00Z, status In Progress. "
            "Execute to provide final status and location of both aircraft and any skip reasons."
        ),
        actions=[
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC002"}),
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC005"}),
            Action(name="GetAirportOperationalStatus", kwargs={"iata_code": "LAX"}),
            Action(name="GetAirportOperationalStatus", kwargs={"iata_code": "DFW"}),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-007",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC002", "new_status": "Active", "new_location_iata": "LAX"}),
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC005", "new_status": "Active", "new_location_iata": "DFW"}),

            Action(name="GetCrewMemberDetails", kwargs={"employee_code": "EMP007"}),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM007",
                    "flight_id": "FL005",
                    "flight_number": "HAT011",
                    "date": "2024-05-03",
                    "role": "Captain",
                    "aircraft_model": "A320neo",
                    "hours_flown": {"total": 4.8, "pic": 4.8, "sic": 0.0, "night": 2.1, "instrument": 1.2},
                    "landings": 2,
                    "takeoffs": 2
                }
            )
        ],
        outputs=[
            '"AC002_final_status": "Active"',
            '"AC002_final_location": "LAX"',
            '"AC002_reposition_skipped_reason": None',
            '"AC005_final_status": "Active"',
            '"AC005_final_location": "DFW"',
            '"AC005_reposition_skipped_reason": None'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_064",
        instruction="Execute fleet operations management at CLT. Aircraft AC003 (PP-LTM, E195-E2) requires a scheduled B-Check. You want to update status to 'Maintenance' at CLT, execute to create a maintenance entry using work order 'WO-2024-05-12-003' (ATA 05), description 'Scheduled B-Check inspection for PP-LTM at CLT', corrective action 'Perform scheduled B-Check inspection of systems and components', technician TECH012, timestamp '2024-05-12T10:20:00Z'. Then check fleet utilization for E195-E2 with status filters 'Active' and 'Maintenance'. Provide the created maintenance log ID.",
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC003", "new_status": "Maintenance", "new_location_iata": "CLT"}),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC003",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check inspection for PP-LTM at CLT",
                    "work_order_id": "WO-2024-05-12-003",
                    "ata_chapter": "05",
                    "corrective_action": "Perform scheduled B-Check inspection of systems and components",
                    "event_timestamp_utc": "2024-05-12T10:20:00Z",
                    "technician_id": "TECH012",
                    "status": "Scheduled"
                }
            ),
            Action(name="GetFleetUtilization", kwargs={"model_filter": "E195-E2", "status_filter": ["Active", "Maintenance"]})
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),


    Task(
        annotator="0",
        user_id="USER_065",
        instruction="Execute customer service duties to assist member Jennifer Johnson (daiki.johnson3136@example.com) with her travel arrangements. Ivan wants to check her current reservation R9QDGB and explore alternative flight options for May 18, 2024 from DFW to ORD due to concerns about her current flight HAT008 (flight_id: FL003) which has experienced operational delays. She wants to understand her membership benefits, review her reservation details, check available flights for the same route and date, and execute to examine any operational events affecting her current flight, and assess fleet availability for potential rebooking. After analyzing the situation, you need to create an operational event with event type 'Technical Issue', timestamp '2024-05-18T11:00:00Z', and you need to detail 'Delay concerns on flight HAT008' to track the customer service interaction. Provide her profile information, current reservation details, alternative flight options, operational event analysis for HAT008, and fleet utilization status to help with her travel planning.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={
                    "user_email": "daiki.johnson3136@example.com"
                }
            ),
            Action(
                name="GetUserReservations",
                kwargs={
                    "user_email": "daiki.johnson3136@example.com"
                }
            ),
            Action(
                name="GetReservationDetails",
                kwargs={
                    "reservation_id": "R9QDGB"
                }
            ),
            Action(
                name="GetFlightsByCriteria",
                kwargs={
                    "departure_date": "2024-05-18",
                    "status": ["available"],
                    "origin": "DFW",
                    "destination": "ORD"
                }
            ),
            Action(
                name="GetOperationalEventsByFlight",
                kwargs={
                    "flight_number": "HAT008"
                }
            ),
            Action(
                name="GetFleetUtilization",
                kwargs={
                    "status_filter": ["Active"]
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-18T11:00:00Z",
                    "details": "Delay concerns on flight HAT008",
                    "status": "Active",
                    "flight_number": "HAT008",
                    "flight_id": "FL003",
                }
            ),
        ],
        outputs=[
            '"user_profile": "Platinum member Jennifer Johnson with 4 reservations and 5 payment methods"',
            '"reservation_details": "Reservation R9QDGB details retrieved successfully"',
            '"alternative_flights": "Available flights from DFW to ORD on 2024-05-18 identified"',
            '"operational_events": "Flight HAT008 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_066",
        instruction="Execute to manage scheduled maintenance at MIA for aircraft AC007 (PR-YJB, A220-300). You want to confirm A220-300 fleet utilization, set AC007 to 'Maintenance' at MIA, and create a scheduled A-Check maintenance record with work order 'WO-2024-05-02-007' (ATA 05), description 'Scheduled A-Check inspection for PR-YJB at MIA', corrective action 'Perform scheduled A-Check inspection of systems and components', timestamp '2024-05-02T09:00:00Z', and status 'Scheduled'. Provide the maintenance log ID that is created.",
        actions=[
            Action(
                name="GetFleetUtilization",
                kwargs={"model_filter": "A220-300", "status_filter": ["Active", "Maintenance"]}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": "AC007", "new_status": "Maintenance", "new_location_iata": "MIA"}
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC007",
                    "maintenance_type": "A-Check",
                    "description": "Scheduled A-Check inspection for PR-YJB at MIA",
                    "work_order_id": "WO-2024-05-02-007",
                    "ata_chapter": "05",
                    "corrective_action": "Perform scheduled A-Check inspection of systems and components",
                    "event_timestamp_utc": "2024-05-02T09:00:00Z",
                    "status": "Scheduled"
                }
            )
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),

    Task(
        annotator="0",
        user_id="USER_067",
        instruction="Execute customer service duties to assist member Mohamed Lopez (sophia.wilson3098@example.com) with her travel arrangements. Olivia wants to check her current reservation 6NSXQU and explore alternative flight options for June 5, 2024 from BOS to IAD due to concerns about her current flight HAT013 (flight_id: FL013) which has experienced operational delays. She wants membership overview, reservation details, same-day options, HAT013 operational events, and fleet availability. After review, create 'Technical Issue' at '2024-06-05T12:10:00Z' with detail 'Delay concerns on flight HAT013'. You want to provide her profile, reservation details, alternatives, HAT013 event analysis, and fleet utilization.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "sophia.wilson3098@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "sophia.wilson3098@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "6NSXQU"}),
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-06-05", "status": ["available"], "origin": "BOS", "destination": "IAD"}),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT013"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(name="CreateOperationalEvent", kwargs={
                "event_type": "Technical Issue",
                "event_timestamp_utc": "2024-06-05T12:10:00Z",
                "details": "Delay concerns on flight HAT013",
                "status": "Active",
                "flight_number": "HAT013",
                "flight_id": "FL013"
            }),
        ],
        outputs=[
            '"user_profile": "Member Mohamed Lopez profile retrieved"',
            '"reservation_details": "Reservation 6NSXQU details retrieved successfully"',
            '"alternative_flights": "Available flights from BOS to IAD on 2024-06-05 identified"',
            '"operational_events": "Flight HAT013 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_068",
        instruction="Execute customer service duties to assist member Isabella Brown (sofia.taylor9399@example.com) with his travel arrangements. Isabella wants to check his current reservation OP3VYE and explore alternative flight options for May 29, 2024 from PHX to SAN due to concerns about his current flight HAT025 (flight_id: FL025) which has experienced operational delays. He wants membership benefits, reservation details, same-day options, operational events for HAT025, and fleet utilization. After analysis, create 'Technical Issue' at '2024-05-29T14:50:00Z' with detail 'Delay concerns on flight HAT025'. Execute to provide his profile, reservation details, alternatives, HAT025 event analysis, and fleet utilization.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "sofia.taylor9399@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "sofia.taylor9399@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "OP3VYE"}),
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-05-29", "status": ["available"], "origin": "PHX", "destination": "SAN"}),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT025"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(name="CreateOperationalEvent", kwargs={
                "event_type": "Technical Issue",
                "event_timestamp_utc": "2024-05-29T14:50:00Z",
                "details": "Delay concerns on flight HAT025",
                "status": "Active",
                "flight_number": "HAT025",
                "flight_id": "FL025"
            }),
        ],
        outputs=[
            '"user_profile": "Member Isabella Brown profile retrieved"',
            '"reservation_details": "Reservation OP3VYE details retrieved successfully"',
            '"alternative_flights": "Available flights from PHX to SAN on 2024-05-29 identified"',
            '"operational_events": "Flight HAT025 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_069",
        instruction="Execute to assist member Ivan Wilson (evelyn.wilson9461@example.com) with travel planning. Review reservation 4WQ150 and execute to check same-day alternatives for May 22, 2024 from LAX to DFW due to concerns about her current flight HAT022 (flight_id: FL022). Provide her profile, reservation details, available LAX→DFW options that day, operational events for HAT022, and fleet utilization. After analysis, create a tracking event: type 'Technical Issue', timestamp '2024-05-22T14:00:00Z', details 'Delay concerns on flight HAT022', status 'Active', linked to HAT022/FL022.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "evelyn.wilson9461@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "evelyn.wilson9461@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "4WQ150"}),
            Action(name="GetFlightsByCriteria", kwargs={"departure_date": "2024-05-22", "status": ["available"], "origin": "LAX", "destination": "DFW"}),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT022"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(name="CreateOperationalEvent", kwargs={"event_type": "Technical Issue", "event_timestamp_utc": "2024-05-22T14:00:00Z", "details": "Delay concerns on flight HAT022", "status": "Active", "flight_number": "HAT022", "flight_id": "FL022"}),
        ],
        outputs=[
            '"user_profile": "Member Ivan Wilson profile retrieved"',
            '"reservation_details": "Reservation 4WQ150 details retrieved successfully"',
            '"alternative_flights": "Available flights from LAX to DFW on 2024-05-22 identified"',
            '"operational_events": "Flight HAT022 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_070",
        instruction="Execute customer service duties to assist member Olivia Martin (isabella.martin5652@example.com) with his travel arrangements. You want to check your current reservation AQSRNQ and explore alternative flight options for May 20, 2024 from JFK to MIA due to concerns about your current flight HAT014 (flight_id: FL006) which has experienced operational delays. You want to understand your membership benefits, review your reservation details, check available flights for the same route and date, examine any operational events affecting your current flight, and assess fleet availability for potential rebooking. After analyzing the situation, you need to create an operational event with event type 'Technical Issue', timestamp '2024-05-20T13:00:00Z', and detail 'Delay concerns on flight HAT014' to track the customer service interaction. Provide his profile information, current reservation details, alternative flight options, operational event analysis for HAT014, and fleet utilization status to help with his travel planning.",
        actions=[
            Action(
                name="GetUserProfile",
                kwargs={
                    "user_email": "isabella.martin5652@example.com"
                }
            ),
            Action(
                name="GetUserReservations",
                kwargs={
                    "user_email": "isabella.martin5652@example.com"
                }
            ),
            Action(
                name="GetReservationDetails",
                kwargs={
                    "reservation_id": "AQSRNQ"
                }
            ),
            Action(
                name="GetFlightsByCriteria",
                kwargs={
                    "departure_date": "2024-05-20",
                    "status": ["available"],
                    "origin": "JFK",
                    "destination": "MIA"
                }
            ),
            Action(
                name="GetOperationalEventsByFlight",
                kwargs={
                    "flight_number": "HAT014"
                }
            ),
            Action(
                name="GetFleetUtilization",
                kwargs={
                    "status_filter": ["Active"]
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-20T13:00:00Z",
                    "details": "Delay concerns on flight HAT014",
                    "status": "Active",
                    "flight_number": "HAT014",
                    "flight_id": "FL006",
                }
            ),
        ],
        outputs=[
            '"user_profile": "Regular member Olivia Martin with 2 reservations and 2 payment methods"',
            '"reservation_details": "Reservation AQSRNQ details retrieved successfully"',
            '"alternative_flights": "Available flights from JFK to MIA on 2024-05-20 identified"',
            '"operational_events": "Flight HAT014 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),
    Task(
        annotator="0",
        user_id="USER_071",
        instruction="Execute fleet operations management at MIA. Aircraft AC007 (PR-YJB, A220-300) requires a scheduled B-Check. You want to update status to 'Maintenance', log a maintenance entry with WO 'WO-2024-05-08-007' (ATA 05), description 'Scheduled B-Check inspection for PR-YJB at MIA', corrective action 'Perform B-Check and functional checks', technician TECH017, timestamp '2024-05-08T09:45:00Z'. Then check A220-300 fleet utilization for 'Active' and 'Maintenance'. Return the created maintenance log ID.",
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC007", "new_status": "Maintenance"}),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC007",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check inspection for PR-YJB at MIA",
                    "work_order_id": "WO-2024-05-08-007",
                    "ata_chapter": "05",
                    "corrective_action": "Perform B-Check and functional checks",
                    "event_timestamp_utc": "2024-05-08T09:45:00Z",
                    "technician_id": "TECH017",
                    "status": "Scheduled"
                }
            ),
            Action(name="GetFleetUtilization", kwargs={"model_filter": "A220-300", "status_filter": ["Active", "Maintenance"]})
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),


    Task(
        annotator="0",
        user_id="USER_072",
        instruction="Execute assisting member Richard Martinez (evelyn.martin3593@example.com). She wants to review reservation MEMLVX and see alternatives for 2024-05-28 from DFW to ORD due to delays on HAT008 (flight_id: FL003). Execute to provide her profile, reservation details, same-day DFW→ORD options, operational events for HAT008, fleet utilization, and execute to create a tracking event ('Technical Issue', '2024-05-28T08:20:00Z', details 'Delay concerns on flight HAT008') linked to HAT008/FL003.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "evelyn.martin3593@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "evelyn.martin3593@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "MEMLVX"}),
            Action(name="GetFlightsByCriteria", kwargs={
                "departure_date": "2024-05-28", "status": ["available"], "origin": "DFW", "destination": "ORD"
            }),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT008"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(name="CreateOperationalEvent", kwargs={
                "event_type": "Technical Issue",
                "event_timestamp_utc": "2024-05-28T08:20:00Z",
                "details": "Delay concerns on flight HAT008",
                "status": "Active",
                "flight_number": "HAT008",
                "flight_id": "FL003"
            }),
        ],
        outputs=[
            '"user_profile": "Member Richard Martinez profile retrieved"',
            '"reservation_details": "Reservation MEMLVX details retrieved successfully"',
            '"alternative_flights": "Available flights from DFW to ORD on 2024-05-28 identified"',
            '"operational_events": "Flight HAT008 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_073",
        instruction="Execute assisting member Mohamed Lopez (sophia.wilson3098@example.com). She wants to review reservation 6NSXQU and see alternatives for 2024-05-27 from DFW to ORD due to delays on HAT011 (flight_id: FL005). You want to provide her profile, reservation details, same-day DFW→ORD options, operational events for HAT011, fleet utilization, and create a tracking event ('Technical Issue', '2024-05-27T07:35:00Z', details 'Delay concerns on flight HAT011') linked to HAT011/FL005.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "sophia.wilson3098@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "sophia.wilson3098@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "6NSXQU"}),
            Action(name="GetFlightsByCriteria", kwargs={
                "departure_date": "2024-05-27", "status": ["available"], "origin": "DFW", "destination": "ORD"
            }),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT011"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(name="CreateOperationalEvent", kwargs={
                "event_type": "Technical Issue",
                "event_timestamp_utc": "2024-05-27T07:35:00Z",
                "details": "Delay concerns on flight HAT011",
                "status": "Active",
                "flight_number": "HAT011",
                "flight_id": "FL005"
            }),
        ],
        outputs=[
            '"user_profile": "Member Mohamed Lopez profile retrieved"',
            '"reservation_details": "Reservation 6NSXQU details retrieved successfully"',
            '"alternative_flights": "No available flights from DFW to ORD on 2024-05-27 identified"',
            '"operational_events": "Flight HAT011 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_074",
        instruction=(
            "Execute the maintenance supervisor at DFW coordinating fleet repositioning. Move AC002 (PR-XBE) from DFW to ATL and AC001 (PR-GOL) from ATL to DFW, "
            "keeping both 'Active'. Then log Captain Elizabeth Davis (CM007) for HAT011 (FL011) on 2024-05-02 as Captain on A320neo with 4.2 total hours "
            "(4.2 PIC, 0 SIC, 0.8 night, 1.2 instrument, 1 landing, 1 takeoff). Also you will want to record a maintenance entry for AC001: Emergency Repair "
            "(WO-2024-08-15-008, ATA 29), description 'Hydraulic system warning discovered during pre-flight inspection', corrective action "
            "'Emergency repair procedures required for hydraulic system warning', technician TECH009, timestamp 2024-08-15T14:30:00Z, status In Progress. "
            "Provide final status and location of both aircraft."
        ),
        actions=[
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC002"}),
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC001"}),
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC002", "new_status": "Active", "new_location_iata": "ATL"}),
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC001", "new_status": "Active", "new_location_iata": "DFW"}),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-008",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(name="GetCrewMemberDetails", kwargs={"crew_member_id": "CM007"}),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM007",
                    "flight_id": "FL011",
                    "flight_number": "HAT011",
                    "date": "2024-05-02",
                    "role": "Captain",
                    "aircraft_model": "A320neo",
                    "hours_flown": {"total": 4.2, "pic": 4.2, "sic": 0, "night": 0.8, "instrument": 1.2},
                    "landings": 1,
                    "takeoffs": 1
                }
            )
        ],
        outputs=[
            '"AC002_final_status": "Active"',
            '"AC002_final_location": "ATL"',
            '"AC001_final_status": "Active"',
            '"AC001_final_location": "DFW"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_075",
        instruction="Assist member Ivan Anderson (liam.taylor8460@example.com). She wants to review reservation ZVWQ08 and see alternatives for 2024-06-02 from MCO to ORD due to delays on HAT019 (flight_id: FL019). You want to provide her profile, reservation details, same-day MCO→ORD availability, operational events for HAT019, fleet utilization, and create a tracking event ('Technical Issue', '2024-06-02T18:00:00Z', details 'Delay concerns on flight HAT019') linked to HAT019/FL019.",
        actions=[
            Action(name="GetUserProfile", kwargs={"user_email": "liam.taylor8460@example.com"}),
            Action(name="GetUserReservations", kwargs={"user_email": "liam.taylor8460@example.com"}),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "ZVWQ08"}),
            Action(
                name="GetFlightsByCriteria",
                kwargs={"departure_date": "2024-06-02", "status": ["available"], "origin": "MCO", "destination": "ORD"}
            ),
            Action(name="GetOperationalEventsByFlight", kwargs={"flight_number": "HAT019"}),
            Action(name="GetFleetUtilization", kwargs={"status_filter": ["Active"]}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-06-02T18:00:00Z",
                    "details": "Delay concerns on flight HAT019",
                    "status": "Active",
                    "flight_number": "HAT019",
                    "flight_id": "FL019"
                }
            ),
        ],
        outputs=[
            '"user_profile": "Member Ivan Anderson profile retrieved"',
            '"reservation_details": "Reservation ZVWQ08 details retrieved successfully"',
            '"alternative_flights": "Available flights from MCO to ORD on 2024-06-02 identified"',
            '"operational_events": "Flight HAT019 operational events analyzed"',
            '"fleet_status": "Active fleet utilization status retrieved"',
            '"customer_service_event": "Operational event created to track customer service interaction"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_076",
        instruction=(
            "YOu are a supervisor. You want to lose out the A-Check for PS-AEF (AC004): maintenance log 'ML001' is 'Completed' with corrective_action 'A-Check inspection completed'; "
            "AC004 is 'Active' at MCO; a Resolved 'Technical Issue' at 2024-07-28T12:15:00Z with details 'A-Check ML001 closed for AC004 (PS-AEF) at MCO' "
            "is associated to AC004 / PS-AEF / MCO. You want to also confirm AC004 and return only the updated log ID and the aircraft’s final status."
        ),
        actions=[
            Action(name="GetAircraftMaintenanceHistory", kwargs={"aircraft_id": "AC004"}),
            Action(
                name="UpdateMaintenanceStatus",
                kwargs={"log_id": "ML001", "status": "Completed", "corrective_action": "A-Check inspection completed"}
            ),
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC004", "new_status": "Active", "new_location_iata": "MCO"}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-07-28T12:15:00Z",
                    "details": "A-Check ML001 closed for AC004 (PS-AEF) at MCO",
                    "status": "Resolved",
                    "aircraft_id": "AC004",
                    "tail_number": "PS-AEF",
                    "airport_id": "ARP_MCO",
                    "iata_code": "MCO"
                }
            ),
            Action(name="GetAircraftDetails", kwargs={"aircraft_id": "AC004"})
        ],
        outputs=[
            '"log_id_updated": "ML001"',
            '"aircraft_final_status": "Active"'
        ]
    ),



    Task(
        annotator="0",
        user_id="USER_077",
        instruction=(
            "Execute the chief compliance officer at DFW preparing for an FAA certification audit. Validate certifications for Captain CM007 "
            "(CERT_A359 on 2024-11-15) and Flight Attendant CM006 (CERT_B738 on 2024-09-20). Then record duty: CM007 completed HAT022 (FL022) "
            "on 2024-05-07 as Captain on A350-900 (3.2 total, 3.2 PIC, 0 SIC, 0.4 night, 0.7 instrument, 1 landing, 1 takeoff); CM006 completed "
            "HAT025 (FL025) on 2024-05-08 as Flight Attendant on B737-800 (2.8 total, 0 PIC, 2.8 SIC, 0.1 night, 0.4 instrument, 1 landing, 1 takeoff). "
            "Also you will need record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-009, ATA 29), description "
            "'Hydraulic system warning discovered during pre-flight inspection', corrective action "
            "'Emergency repair procedures required for hydraulic system warning', technician TECH009, "
            "timestamp 2024-08-15T14:30:00Z, status In Progress. Execute want to provide both crew members' certification validity statuses and confirm the two flight-log entries were saved."
        ),
        actions=[
            Action(name="GetCrewMemberDetails", kwargs={"crew_member_id": "CM007"}),
            Action(name="GetCrewCertifications", kwargs={"crew_member_id": "CM007"}),
            Action(name="GetCertificationDetails", kwargs={"certification_id": "CERT_A359"}),
            Action(
                name="CheckCertificationValidity",
                kwargs={"crew_member_id": "CM007", "certification_id": "CERT_A359", "check_date": "2024-11-15"}
            ),

            Action(name="GetCrewMemberDetails", kwargs={"crew_member_id": "CM006"}),
            Action(name="GetCrewCertifications", kwargs={"crew_member_id": "CM006"}),
            Action(name="GetCertificationDetails", kwargs={"certification_id": "CERT_B738"}),
            Action(
                name="CheckCertificationValidity",
                kwargs={"crew_member_id": "CM006", "certification_id": "CERT_B738", "check_date": "2024-09-20"}
            ),

            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-009",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM007",
                    "flight_id": "FL022",
                    "flight_number": "HAT022",
                    "date": "2024-05-07",
                    "role": "Captain",
                    "aircraft_model": "A350-900",
                    "hours_flown": {"total": 3.2, "pic": 3.2, "sic": 0, "night": 0.4, "instrument": 0.7},
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM006",
                    "flight_id": "FL025",
                    "flight_number": "HAT025",
                    "date": "2024-05-08",
                    "role": "Flight Attendant",
                    "aircraft_model": "B737-800",
                    "hours_flown": {"total": 2.8, "pic": 0, "sic": 2.8, "night": 0.1, "instrument": 0.4},
                    "landings": 1,
                    "takeoffs": 1
                }
            )
        ],
        outputs=[
            '"cm007_cert_status": "valid"',
            '"cm006_cert_status": "valid"',
            '"flight_log_entries_saved": "confirmed"'
        ]
    ),


    Task(
        annotator="0",
        user_id="USER_078",
        instruction=(
            "You as the fleet operations manager at LAX, will need to address a technical issue involving aircraft AC003 (tail PP-LTM) by first assessing the current fleet utilization, "
            "then creating an active operational event detailing the need for fleet rebalancing with the detail 'Fleet rebalancing required', scheduled for 2024-05-01T14:00:00Z. "
            "Update AC003's status to 'In Maintenance' at ORD accordingly. Also record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-010, ATA 29), "
            "description 'Hydraulic system warning discovered during pre-flight inspection', corrective action 'Emergency repair procedures required for hydraulic system warning', "
            "technician TECH009, timestamp 2024-08-15T14:30:00Z, status In Progress. Then you will want to provide the operational event ID and confirm AC003's updated maintenance status."
        ),
        actions=[
            Action(
                name="GetFleetUtilization",
                kwargs={"status_filter": ["Active", "Maintenance"]}
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-01T14:00:00Z",
                    "details": "Fleet rebalancing required",
                    "status": "Active",
                    "aircraft_id": "AC003",
                    "tail_number": "PP-LTM"
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-010",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC003",
                    "new_status": "In Maintenance",
                    "new_location_iata": "ORD"
                }
            ),
        ],
        outputs=['"fleet_utilization_status": "Current fleet utilization assessed"', '"fleet_rebalancing_event_id": "OE026"', '"ac003_maintenance_status": "In Maintenance"'],
    ),

    Task(
        annotator="0",
        user_id="USER_079",
        instruction=(
            "SEA ops, 2024-05-12, HAT029 (FL029): you will want to record a Weather Delay at 08:10Z with "
            "'Low visibility at SEA impacting HAT029.' (include SEA IATA); execute to record a Diversion Landing at 08:55Z to DFW with "
            "'Flight diverted to DFW due to prolonged LVP.' and make sure to have the airport associated; set AC009 Active at DFW; mark HAT029 delayed 3h for 2024-05-12. "
            "Finally, execute to return the diversion event ID and the aircraft’s IATA location."
        ),
        actions=[
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Weather Delay",
                    "event_timestamp_utc": "2024-05-12T08:10:00Z",
                    "details": "Low visibility at SEA impacting HAT029.",
                    "status": "Active",
                    "flight_id": "FL029",
                    "flight_number": "HAT029",
                    "airport_id": "ARP_SEA",
                    "iata_code": "SEA"
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Diversion Landing",
                    "event_timestamp_utc": "2024-05-12T08:55:00Z",
                    "details": "Flight diverted to DFW due to prolonged LVP.",
                    "status": "Active",
                    "flight_id": "FL029",
                    "flight_number": "HAT029",
                    "airport_id": "ARP_DFW",
                    "iata_code": "DFW"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": "AC009", "new_status": "Active", "new_location_iata": "DFW"}
            ),
            Action(
                name="UpdateFlightStatusByNumberAndDate",
                kwargs={"flight_number": "HAT029", "date": "2024-05-12", "new_status": "delayed", "delay_hours": 3}
            )
        ],
        outputs=['"diversion_event_id": "OE027"', '"aircraft_location": "DFW"']
    ),



    Task(
        annotator="0",
        user_id="USER_80",
        instruction="Execute fleet operations management at LAS. Aircraft AC009 (PR-GUO, B737-800) is scheduled for a C-Check. You want to update status to 'Maintenance', log a maintenance entry with WO 'WO-2024-05-11-009' (ATA 05), description 'Scheduled C-Check inspection for PR-GUO at LAS', corrective action 'Perform scheduled C-Check inspection of systems and components', technician TECH013, timestamp '2024-05-11T10:00:00Z'. Then check B737-800 fleet utilization for 'Active' and 'Maintenance'. Return the created maintenance log ID.",
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC009", "new_status": "Maintenance"}),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC009",
                    "maintenance_type": "C-Check",
                    "description": "Scheduled C-Check inspection for PR-GUO at LAS",
                    "work_order_id": "WO-2024-05-11-009",
                    "ata_chapter": "05",
                    "corrective_action": "Perform scheduled C-Check inspection of systems and components",
                    "event_timestamp_utc": "2024-05-11T10:00:00Z",
                    "technician_id": "TECH013",
                    "status": "Scheduled"
                }
            ),
            Action(name="GetFleetUtilization", kwargs={"model_filter": "B737-800", "status_filter": ["Active", "Maintenance"]})
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),


    Task(
        annotator="0",
        user_id="USER_081",
        instruction="Execute fleet operations management at CLT for aircraft AC003 (PP-LTM, E195-E2) coming due for a routine A-Check. You want the A-Check maintenance entry captured first—WO 'WO-2024-05-12-003', ATA '05', description 'Scheduled A-Check inspection for PP-LTM at CLT', corrective action 'Perform A-Check and function tests per program', technician TECH012, timestamp '2024-05-12T10:20:00Z'—and then execute the aircraft placed into status 'Maintenance' at CLT. After that, execute an E195-E2 utilization snapshot limited to 'Active' and 'Maintenance'. Return the created maintenance log ID.",
        actions=[
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC003",
                    "maintenance_type": "A-Check",
                    "description": "Scheduled A-Check inspection for PP-LTM at CLT",
                    "work_order_id": "WO-2024-05-12-003",
                    "ata_chapter": "05",
                    "corrective_action": "Perform A-Check and function tests per program",
                    "event_timestamp_utc": "2024-05-12T10:20:00Z",
                    "technician_id": "TECH012",
                    "status": "Scheduled"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": "AC003", "new_status": "Maintenance", "new_location_iata": "CLT"}
            ),
            Action(
                name="GetFleetUtilization",
                kwargs={"model_filter": "E195-E2", "status_filter": ["Active", "Maintenance"]}
            )
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),



    Task(
        annotator="0",
        user_id="USER_082",
        instruction="Execute the CLT turn coordinator addressing a galley power fault on AC011 (E175) impacting HAT015 (FL010) on 2024-05-02. Follow this exact sequence—no extra fields, no substitutions: execute to create a single Technical Issue operational event at 13:40 UTC tied to HAT015/FL010 at CLT; then to record a Line Maintenance entry for AC011 with ATA 24 under WO-2024-05-02-021 assigned to TECH020, timestamped 13:40 UTC and set to In Progress; please create a Gate Change operational event at 13:45 UTC for HAT015 at CLT; and update HAT015 (date 2024-05-02) to status ‘delayed’ with a 1-hour delay and reference the gate-change event as the reason. Scheduled departure 2024-05-02T13:50:00Z and arrival 2024-05-02T15:46:00Z are context only and must not be altered. You want to return only the gate-change event ID and the flight’s updated status.",
        actions=[
            Action(
                name="GetAirportOperationalStatus",
                kwargs={"iata_code": "CLT"}
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-05-02T13:40:00Z",
                    "details": "Galley power fault on AC011 affecting flight HAT015.",
                    "status": "Active",
                    "flight_id": "FL010",
                    "flight_number": "HAT015",
                    "airport_id": "ARP_CLT",
                    "iata_code": "CLT"
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC011",
                    "maintenance_type": "Line Maintenance",
                    "description": "Pre-departure galley power fault correction at CLT.",
                    "technician_id": "TECH020",
                    "work_order_id": "WO-2024-05-02-021",
                    "ata_chapter": "24",
                    "corrective_action": "Restore galley power and verify system checks.",
                    "event_timestamp_utc": "2024-05-02T13:40:00Z",
                    "status": "In Progress"
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Gate Change",
                    "event_timestamp_utc": "2024-05-02T13:45:00Z",
                    "details": "Gate change required for maintenance on AC011 flight HAT015.",
                    "status": "Active",
                    "flight_id": "FL010",
                    "flight_number": "HAT015",
                    "airport_id": "ARP_CLT",
                    "iata_code": "CLT"
                }
            ),
            Action(
                name="UpdateFlightStatusByNumberAndDate",
                kwargs={
                    "flight_number": "HAT015",
                    "date": "2024-05-02",
                    "new_status": "delayed",
                    "delay_hours": 1,
                    "reason_event_id": "OE027"
                }
            )
        ],
        outputs=['"event_id": "OE027"', '"updated_status": "delayed"']
    ),



    Task(
        annotator="0",
        user_id="USER_083",
        instruction=(
            "Execute the SEA crew scheduler. For flight HAT011 (FL005) on 2024-05-01, do not change existing assignments. "
            "Log block time for Captain CM007 and First Officer CM008 on E175 (CM007: 2.2 total/2.2 PIC/0 night/0.3 instrument; "
            "CM008: 2.2 total/0 PIC/2.2 SIC/0 night/0.3 instrument), each with 1 landing and 1 takeoff. Then retrieve current crew assignments. "
            "Also execute to record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-011, ATA 29), description "
            "'Hydraulic system warning discovered during pre-flight inspection', corrective action "
            "'Emergency repair procedures required for hydraulic system warning', technician TECH009, timestamp 2024-08-15T14:30:00Z, status In Progress. "
            "Execute need to provide the total assigned crew members and the flight number."
        ),
        actions=[
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM007",
                    "flight_id": "FL005",
                    "flight_number": "HAT011",
                    "date": "2024-05-01",
                    "role": "Captain",
                    "aircraft_model": "E175",
                    "hours_flown": {"total": 2.2, "pic": 2.2, "sic": 0, "night": 0, "instrument": 0.3},
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM008",
                    "flight_id": "FL005",
                    "flight_number": "HAT011",
                    "date": "2024-05-01",
                    "role": "First Officer",
                    "aircraft_model": "E175",
                    "hours_flown": {"total": 2.2, "pic": 0, "sic": 2.2, "night": 0, "instrument": 0.3},
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-011",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(
                name="GetFlightCrewAssignments",
                kwargs={"flight_id": "FL005", "flight_number": "HAT011"}
            )
        ],
        outputs=['"assigned_crew_members": 3', '"flight_number": "HAT011"']
    ),



    Task(
        annotator="0",
        user_id="USER_084",
        instruction="Execute the fleet compliance auditor verifying type-rating validity and duty records. Confirm CM004 (Captain) holds CERT_E195 valid on 2024-05-09 and CM009 (Elizabeth Brown) holds CERT_A359 valid on 2024-08-22. Then capture recent duty: CM004 on HAT010 (FL010) dated 2024-05-01 as Captain on E195‑E2 (2.0 total, 2.0 PIC, 0 night, 0.3 instrument, 1 landing, 1 takeoff) and CM009 on HAT014 (FL014) dated 2024-05-04 as Flight Attendant on A350-900 (3.0 total, 0 PIC, 0 SIC, 0 night, 0 instrument, 1 landing, 1 takeoff). Provide certification validity statuses for both crew members.",
        actions=[
            Action(
                name="GetCrewMemberDetails",
                kwargs={"crew_member_id": "CM004"}
            ),
            Action(
                name="GetCrewCertifications",
                kwargs={"crew_member_id": "CM004"}
            ),
            Action(
                name="GetCertificationDetails",
                kwargs={"certification_id": "CERT_E195"}
            ),
            Action(
                name="CheckCertificationValidity",
                kwargs={
                    "crew_member_id": "CM004",
                    "certification_id": "CERT_E195",
                    "check_date": "2024-05-09"
                }
            ),
            Action(
                name="GetCrewMemberDetails",
                kwargs={"crew_member_id": "CM009"}
            ),
            Action(
                name="GetCrewCertifications",
                kwargs={"crew_member_id": "CM009"}
            ),
            Action(
                name="GetCertificationDetails",
                kwargs={"certification_id": "CERT_A359"}
            ),
            Action(
                name="CheckCertificationValidity",
                kwargs={
                    "crew_member_id": "CM009",
                    "certification_id": "CERT_A359",
                    "check_date": "2024-08-22"
                }
            ),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM004",
                    "flight_id": "FL010",
                    "flight_number": "HAT010",
                    "date": "2024-05-01",
                    "role": "Captain",
                    "aircraft_model": "E195-E2",
                    "hours_flown": {
                        "total": 2.0,
                        "pic": 2.0,
                        "sic": 0,
                        "night": 0,
                        "instrument": 0.3
                    },
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM009",
                    "flight_id": "FL014",
                    "flight_number": "HAT014",
                    "date": "2024-05-04",
                    "role": "Flight Attendant",
                    "aircraft_model": "A350-900",
                    "hours_flown": {
                        "total": 3.0,
                        "pic": 0,
                        "sic": 0,
                        "night": 0,
                        "instrument": 0
                    },
                    "landings": 1,
                    "takeoffs": 1
                }
            )
        ],
        outputs=['"cm004_cert_status": "valid"', '"cm009_cert_status": "valid"'],
    ),

    Task(
        annotator="0",
        user_id="USER_085",
        instruction="Execute fleet operations management at ORD. Aircraft AC002 (PR-XBE, A320neo) requires a scheduled B-Check. You want to update status to 'Maintenance', log a maintenance entry with WO 'WO-2024-05-09-002' (ATA 05), description 'Scheduled B-Check inspection for PR-XBE at ORD', technician TECH019, timestamp '2024-05-09T15:20:00Z'. Then check A320neo fleet utilization for 'Active' and 'Maintenance'. Return the created maintenance log ID.",
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC002", "new_status": "Maintenance"}),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC002",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check inspection for PR-XBE at ORD",
                    "work_order_id": "WO-2024-05-09-002",
                    "ata_chapter": "05",
                    "corrective_action": "Scheduled B-Check maintenance per work order WO-2024-05-09-002",
                    "event_timestamp_utc": "2024-05-09T15:20:00Z",
                    "technician_id": "TECH019",
                    "status": "Scheduled"
                }
            ),
            Action(name="GetFleetUtilization", kwargs={"model_filter": "A320neo", "status_filter": ["Active", "Maintenance"]})
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),

    Task(
        annotator="0",
        user_id="USER_086",
        instruction="Execute the ATL maintenance controller on duty responding to a hydraulic-pressure AOG on AC001 (PR-GOL) at 14:30 UTC on 2024-05-01 that is impacting flight HAT004. Execute the recovery sequence in this exact order without adding nonstandard fields: execute to verify ATL’s operational status; log a single AOG operational event explicitly linked to both the aircraft and the flight; then please also set the aircraft status to ‘Maintenance’ at ATL; create one emergency-repair maintenance record marked ‘Completed’; apply a 2-hour delay to the affected flight; return the aircraft to ‘Active’ at ATL; and confirm aircraft details after recovery. When finished, execute to return only the created maintenance log ID and the flight’s updated status.",
        actions=[
            Action(
                name="GetAirportOperationalStatus",
                kwargs={"iata_code": "ATL"}
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Aircraft AOG",
                    "event_timestamp_utc": "2024-05-01T14:30:00Z",
                    "details": "Hydraulic pressure AOG for AC001 at ATL affecting HAT004.",
                    "status": "Active",
                    "aircraft_id": "AC001",
                    "tail_number": "PR-GOL",
                    "flight_id": "FL001",
                    "flight_number": "HAT004",
                    "airport_id": "ARP_ATL",
                    "iata_code": "ATL"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": "AC001", "new_status": "Maintenance", "new_location_iata": "ATL"}
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic anomaly before departure",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-005",
                    "ata_chapter": "29",
                    "corrective_action": "Scheduled B-Check maintenance per work order WO-2024-08-15-005",
                    "event_timestamp_utc": "2024-05-01T14:30:00Z",
                    "status": "Completed"
                }
            ),
            Action(
                name="UpdateFlightStatusByNumberAndDate",
                kwargs={"flight_number": "HAT004", "date": "2024-05-01", "new_status": "delayed", "delay_hours": 2}
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": "AC001", "new_status": "Active", "new_location_iata": "ATL"}
            ),
            Action(
                name="GetAircraftDetails",
                kwargs={"aircraft_id": "AC001"}
            )
        ],
        outputs=[
            '"maintenance_log_id": "ML026"',
            '"updated_flight_status": "delayed"'
        ]
    ),




    Task(
        annotator="0",
        user_id="USER_087",
        instruction="Execute fleet operations management at DEN. Aircraft AC012 (PR-ABX, A320neo) requires scheduled B-Check maintenance. You want to update the aircraft status to 'Maintenance' at DEN, create a maintenance entry with work order 'WO-2024-05-06-012' (ATA 05), description 'Scheduled B-Check inspection for PR-ABX at DEN', corrective action 'Perform scheduled B-Check inspection of systems and components', technician TECH014, timestamp '2024-05-06T09:15:00Z', and check fleet utilization for A320neo models with 'Active' and 'Maintenance' statuses. Provide the created maintenance log ID.",
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC012", "new_status": "Maintenance", "new_location_iata": "DEN"}),
            Action(name="CreateMaintenanceEntry", kwargs={
                "aircraft_id": "AC012", "maintenance_type": "B-Check",
                "description": "Scheduled B-Check inspection for PR-ABX at DEN",
                "work_order_id": "WO-2024-05-06-012", "ata_chapter": "05",
                "corrective_action": "Perform scheduled B-Check inspection of systems and components",
                "event_timestamp_utc": "2024-05-06T09:15:00Z", "technician_id": "TECH014", "status": "Scheduled"
            }),
            Action(name="GetFleetUtilization", kwargs={"model_filter": "A320neo", "status_filter": ["Active", "Maintenance"]})
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),

    Task(
        annotator="0",
        user_id="USER_088",
        instruction="Execute the SEA airport operations supervisor managing a weather disruption on 2024-05-01-7:30:00 affecting flight HAT011 (FL005) execute to use the details: 'Weather program in effect at SEA impacting departure sequencing for HAT011.' but first check if the airport is operational. You want to create a weather delay event at SEA, execute to record a diversion landing at ORD,9:10:00 , and you will update the aircraft’s (AC010) status to reflect continued ops, you will also need to specify the details 'Flight diverted to ORD due to sustained adverse weather at SEA'. Provide the diversion event ID and the aircraft’s updated location IATA code.",
        actions=[
            Action(name="GetAirportOperationalStatus", kwargs={"iata_code": "SEA"}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Weather Delay",
                    "event_timestamp_utc": "2024-05-01T07:30:00Z",
                    "details": "Weather program in effect at SEA impacting departure sequencing for HAT011.",
                    "status": "Active",
                    "flight_id": "FL005",
                    "flight_number": "HAT011",
                    "airport_id": "ARP_SEA",
                    "iata_code": "SEA"
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Diversion Landing",
                    "event_timestamp_utc": "2024-05-01T09:10:00Z",
                    "details": "Flight diverted to ORD due to sustained adverse weather at SEA",
                    "status": "Active",
                    "flight_id": "FL005",
                    "flight_number": "HAT011",
                    "airport_id": "ARP_ORD",
                    "iata_code": "ORD"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC010",
                    "new_status": "Active",
                    "new_location_iata": "ORD"
                }
            )
        ],
        outputs=[
            '"diversion_event_id": "OE027"',
            '"aircraft_location": "ORD"'
        ]
    ),

    Task(
        annotator="0",
        user_id="USER_089",
        instruction="Execute the DFW maintenance-ops duty manager executing a scheduled heavy-check flow. Per C-Check completion SOP, perform the sequence for aircraft AC014 on 2024-09-10 as follows: first, register a tracking operational event at 2024-09-10T09:00:00Z (Tracking scheduled C-Check at DFW for AC014.) with the airport associated, (for audit only—no nonstandard metadata); second, set the aircraft status to 'Maintenance' at DFW; third, create exactly one maintenance record for a C-Check with Status 'Completed' and Next Due 2025-03-10 ('Scheduled C-Check for AC014 at DFW', WO-2024-09-10-010,TECH021). When finished, execute to return only the created maintenance log ID and the aircraft’s final status.",
        actions=[
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Technical Issue",
                    "event_timestamp_utc": "2024-09-10T09:00:00Z",
                    "details": "Tracking scheduled C-Check at DFW for AC014.",
                    "status": "Active",
                    "airport_id": "ARP_DFW",
                    "iata_code": "DFW"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC014",
                    "new_status": "Maintenance",
                    "new_location_iata": "DFW"
                }
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC014",
                    "maintenance_type": "C-Check",
                    "description": "Scheduled C-Check for AC014 at DFW",
                    "technician_id": "TECH021",
                    "work_order_id": "WO-2024-09-10-010",
                    "ata_chapter": "05",
                    "event_timestamp_utc": "2024-09-10T09:00:00Z",
                    "status": "Completed",
                    "corrective_action": "Scheduled C-Check maintenance per work order WO-2024-09-10-010",
                    "next_due": "2025-03-10"
                }
            )
        ],
        outputs=[
            '"maintenance_log_id": "ML026"',
            '"aircraft_status": "Active"'
        ]
    ),


    Task(
        annotator="0",
        user_id="USER_090",
        instruction="Execute fleet operations management at CLT. Aircraft AC003 (PP-LTM, E195-E2) requires a scheduled B-Check. You want to update status to 'Maintenance', log a maintenance entry with WO 'WO-2024-05-12-003' (ATA 05), description 'Scheduled B-Check inspection for PP-LTM at CLT', corrective action 'Perform B-Check and function tests', technician TECH013, timestamp '2024-05-12T10:20:00Z'. Then check E195-E2 fleet utilization for 'Active' and 'Maintenance'. You then want to return the created maintenance log ID.",
        actions=[
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC003",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check inspection for PP-LTM at CLT",
                    "work_order_id": "WO-2024-05-12-003",
                    "ata_chapter": "05",
                    "corrective_action": "Perform B-Check and function tests",
                    "event_timestamp_utc": "2024-05-12T10:20:00Z",
                    "technician_id": "TECH013",
                    "status": "Scheduled"
                }
            ),
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC003", "new_status": "Maintenance"}),
            Action(name="GetFleetUtilization", kwargs={"model_filter": "B787-9", "status_filter": ["Active", "Maintenance"]})
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),


    Task(
        annotator="0",
        user_id="USER_091",
        instruction="Execute fleet operations management at JFK. Aircraft AC005 (PP-ZVK, E175) requires a scheduled B-Check. You want to update status to 'Maintenance', log a maintenance entry with WO 'WO-2024-05-10-005' (ATA 05), description 'Scheduled B-Check inspection for PP-ZVK at JFK', corrective action 'Execute B-Check tasks and ops checks', technician TECH016, timestamp '2024-05-10T07:55:00Z'. Then check E175 fleet utilization for 'Active' and 'Maintenance'. Return the created maintenance log ID.",
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC005", "new_status": "Maintenance"}),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC005",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check inspection for PP-ZVK at JFK",
                    "work_order_id": "WO-2024-05-10-005",
                    "ata_chapter": "05",
                    "corrective_action": "Execute B-Check tasks and ops checks",
                    "event_timestamp_utc": "2024-05-10T07:55:00Z",
                    "technician_id": "TECH016",
                    "status": "Scheduled"
                }
            ),
            Action(name="GetFleetUtilization", kwargs={"model_filter": "E175", "status_filter": ["Active", "Maintenance"]})
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),

    Task(
        annotator="0",
        user_id="USER_092",
        instruction="Execute the JFK fleet-ops duty manager on a scheduled heavy-maintenance turn. Per MP-BCHK-A350 and maintenance-logging SOP, execute to process aircraft AC005 (tail PR-XTD, model A350-900) for a planned B-Check as follows: first, set the aircraft operational status to 'Maintenance' at JFK (no other metadata changes); next, create exactly one maintenance log with Work Order WO-2024-05-12-005, ATA Chapter 05, Maintenance Type B-Check, Description 'Scheduled B-Check inspection for PR-XTD at JFK', Corrective Action 'Perform B-Check and leak checks', Technician TECH014, Event Timestamp (UTC) 2024-05-12T08:45:00Z, and Status 'Scheduled'; then perform a fleet-utilization query limited to A350-900 units with status filters ['Active','Maintenance'] and make no additional updates or events; finally, return only the created maintenance log ID.",
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC005", "new_status": "Maintenance"}),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC005",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check inspection for PR-XTD at JFK",
                    "work_order_id": "WO-2024-05-12-005",
                    "ata_chapter": "05",
                    "corrective_action": "Perform B-Check and leak checks",
                    "event_timestamp_utc": "2024-05-12T08:45:00Z",
                    "technician_id": "TECH014",
                    "status": "Scheduled"
                }
            ),
            Action(name="GetFleetUtilization", kwargs={"model_filter": "A350-900", "status_filter": ["Active", "Maintenance"]})
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),



    Task(
        annotator="0",
        user_id="USER_093",
        instruction="Execute the ATL airport-operations supervisor on day-of-departure. Ramp Control reports a stand conflict at Concourse C preventing use of C22 for the next outbound. Per IR-OPS-420 and the event taxonomy, execute to log a single 'Gate Change' for flight HAT004 (FL001) at ATL on 2024-05-01, timestamped 14:45 UTC with the exact detail 'Departure gate changed from C22 to C27 due to ramp constraints'. Execute to include ATL airport context (iata_code 'ATL' and airport_id 'ARP_ATL') when creating the event, then execute to set that same flight/date to status 'delayed' for one hour without a reason id. Return only the created event ID and the updated flight status.",
        actions=[
            Action(name="GetAirportDetailsByIataCode", kwargs={"iata_code": "ATL"}),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Gate Change",
                    "event_timestamp_utc": "2024-05-01T14:45:00Z",
                    "details": "Departure gate changed from C22 to C27 due to ramp constraints",
                    "status": "Active",
                    "flight_id": "FL001",
                    "flight_number": "HAT004",
                    "airport_id": "ARP_ATL",
                    "iata_code": "ATL"
                }
            ),
            Action(
                name="UpdateFlightStatusByNumberAndDate",
                kwargs={
                    "flight_number": "HAT004",
                    "date": "2024-05-01",
                    "new_status": "delayed",
                    "delay_hours": 1
                }
            )
        ],
        outputs=[
            '"event_id": "OE026"',
            '"updated_status": "delayed"'
        ]
    ),


    Task(
        annotator="0",
        user_id="USER_094",
        instruction="Execute fleet operations management at MIA. Aircraft AC011 (PP-EJA, E195-E2) is due for a scheduled B-Check. You want to set the aircraft to 'Maintenance', add a maintenance entry with WO 'WO-2024-05-07-011' (ATA 05), description 'Scheduled B-Check inspection for PP-EJA at MIA', corrective action 'Execute B-Check per maintenance program', technician TECH022, timestamp '2024-05-07T13:40:00Z', status 'Scheduled'. Then check E195-E2 fleet utilization for 'Active' and 'Maintenance'. Provide the created maintenance log ID.",
        actions=[
            Action(name="UpdateAircraftStatus", kwargs={"aircraft_id": "AC011", "new_status": "Maintenance"}),
            Action(name="CreateMaintenanceEntry", kwargs={
                "aircraft_id": "AC011",
                "maintenance_type": "B-Check",
                "description": "Scheduled B-Check inspection for PP-EJA at MIA",
                "work_order_id": "WO-2024-05-07-011",
                "ata_chapter": "05",
                "corrective_action": "Execute B-Check per maintenance program",
                "event_timestamp_utc": "2024-05-07T13:40:00Z",
                "technician_id": "TECH022",
                "status": "Scheduled"
            }),
            Action(name="GetFleetUtilization", kwargs={"model_filter": "E195-E2", "status_filter": ["Active", "Maintenance"]})
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),

    Task(
        annotator="0",
        user_id="USER_095",
        instruction=(
            "Execute an SEA fleet ops manager. You want to record a B-Check for AC007 (PR-QMN, B737-800) — WO-2024-05-08-007, ATA '05', "
            "description 'Scheduled B-Check inspection for PR-QMN at SEA', corrective action 'Scheduled B-Check maintenance per work order WO-2024-05-08-007', "
            "TECH011, timestamp 2024-05-08T08:10:00Z, status 'Completed'. Execute to set AC007 to 'Maintenance' at SEA. "
            "You also want to show a B737-800 utilization snapshot for 'Active' and 'Maintenance'. "
            "Return the new maintenance log ID."
        ),
        actions=[
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC007",
                    "maintenance_type": "B-Check",
                    "description": "Scheduled B-Check inspection for PR-QMN at SEA",
                    "work_order_id": "WO-2024-05-08-007",
                    "ata_chapter": "05",
                    "corrective_action": "Scheduled B-Check maintenance per work order WO-2024-05-08-007",
                    "event_timestamp_utc": "2024-05-08T08:10:00Z",
                    "technician_id": "TECH011",
                    "status": "Completed"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": "AC007", "new_status": "Maintenance", "new_location_iata": "SEA"}
            ),
            Action(
                name="GetFleetUtilization",
                kwargs={"model_filter": "B737-800", "status_filter": ["Active", "Maintenance"]}
            )
        ],
        outputs=['"maintenance_log_id": "ML026"']
    ),



    Task(
        annotator="0",
        user_id="USER_096",
        instruction=(
            "As the ATL crew-certification coordinator preparing a quarterly audit, execute to verify the current details and certifications for Captain CM001 (Isabella Brown) and "
            "First Officer CM005 (Susan Wilson). Then update their flight logs to reflect both operated HAT004 (FL001) on 2024-05-15: CM001 logged 2.5 h total "
            "(all PIC) with 0.5 h instrument and one landing/takeoff; CM005 logged 2.5 h total as SIC with 0.5 h instrument and one landing/takeoff. "
            "Also you will need to record a maintenance entry for AC001: Emergency Repair (WO-2024-08-15-012, ATA 29), description 'Hydraulic system warning discovered during "
            "pre-flight inspection', corrective action 'Emergency repair procedures required for hydraulic system warning', technician TECH009, timestamp "
            "2024-08-15T14:30:00Z, status In Progress. You want to return their certification validity and confirmation that both flight-log entries were saved."
        ),
        actions=[
            Action(name="GetCrewMemberDetails", kwargs={"crew_member_id": "CM001"}),
            Action(name="GetCrewCertifications", kwargs={"crew_member_id": "CM001"}),
            Action(name="GetCrewMemberDetails", kwargs={"crew_member_id": "CM005"}),
            Action(name="GetCrewCertifications", kwargs={"crew_member_id": "CM005"}),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-012",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),

            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM001",
                    "flight_id": "FL001",
                    "flight_number": "HAT004",
                    "date": "2024-05-15",
                    "role": "Captain",
                    "aircraft_model": "B737-800",
                    "hours_flown": {"total": 2.5, "pic": 2.5, "sic": 0, "night": 0, "instrument": 0.5},
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM005",
                    "flight_id": "FL001",
                    "flight_number": "HAT004",
                    "date": "2024-05-15",
                    "role": "First Officer",
                    "aircraft_model": "B737-800",
                    "hours_flown": {"total": 2.5, "pic": 0, "sic": 2.5, "night": 0, "instrument": 0.5},
                    "landings": 1,
                    "takeoffs": 1
                }
            )
        ],
        outputs=[
            '"crew_certification_status": "valid"',
            '"flight_log_entries_saved": "confirmed"'
        ]
    ),


    Task(
        annotator="0",
        user_id="USER_097",
        instruction="Execute the maintenance supervisor at ATL. Execute to create an UNSCHEDULED avionics-repair record for AC005 (tail PR-XTD) for intermittent navigation-display failures reported at 2024-05-18T09:15:00Z (UTC) under ATA 31. Use work order WO-2024-05-18-012, assign TECH015, set status 'In Progress', corrective action 'Replacement of the primary flight display unit.', and description 'Intermittent navigation display failures reported during pre-flight inspection.'. Immediately set the aircraft’s primary status to 'Maintenance' at ATL (no other attributes changed). Return the created maintenance log ID and the aircraft’s updated status.",
        actions=[
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC005",
                    "maintenance_type": "Avionics Repair",
                    "description": "Intermittent navigation display failures reported during pre-flight inspection.",
                    "technician_id": "TECH015",
                    "work_order_id": "WO-2024-05-18-012",
                    "ata_chapter": "31",
                    "corrective_action": "Replacement of the primary flight display unit.",
                    "event_timestamp_utc": "2024-05-18T09:15:00Z",
                    "status": "In Progress"
                }
            ),
            Action(
                name="UpdateAircraftStatus",
                kwargs={
                    "aircraft_id": "AC005",
                    "new_status": "Maintenance",
                    "new_location_iata": "ATL"
                }
            ),
            Action(
                name="GetAircraftDetails",
                kwargs={"aircraft_id": "AC005"}
            )
        ],
        outputs=[
            '"log_id": "ML026"',
            '"aircraft_status": "Maintenance"'
        ]
    ),




    Task(
        annotator="0",
        user_id="USER_098",
        instruction="Execute the customer service supervisor at JFK. Passenger Isabella Brown needs urgent rebooking: move her 2024-05-16 travel to JFK→MIA in Business class on the most cost-effective option while keeping reservation NO6JO3. Execute to provide the new flight number and total cost.",
        actions=[
            Action(name="GetReservationDetails", kwargs={"reservation_id": "NO6JO3"}),
            Action(name="GetFlightsByCriteria", kwargs={
                "departure_date": "2024-05-16",
                "status": ["available"],
                "origin": "JFK",
                "destination": "MIA"
            }),
            Action(name="UpdateReservation", kwargs={
                "reservation_id": "NO6JO3",
                "cabin": "business",
                "flights": [{
                    "flight_number": "HAT014",
                    "date": "2024-05-16",
                    "origin": "JFK",
                    "destination": "MIA",
                    "price": 270
                }]
            }),
            Action(name="GetReservationDetails", kwargs={"reservation_id": "NO6JO3"})
        ],
        outputs=['"new_flight_number": "HAT014"', '"total_cost": 270']
    ),

    Task(
        annotator="0",
        user_id="USER_099",
        instruction="Coordinate crew scheduling at DFW airport. Due to severe weather delays, First Officer Isabella Brown (EMP002) must be assigned to flight HAT038 (FL038) on 2024-05-23, replacing a crew member who exceeded duty time limits. The A320neo flight requires: verify Lucas’s identity and A320neo certification validity for the date, confirm current crew complement for FL038/HAT038 to avoid duplicate assignment, assign Isabella as First Officer, and execute to log duty with 3.5 total hours, 0 PIC, 3.5 SIC, 1.0 night, 0.5 instrument, with 1 landing and 1 takeoff. After logging, re-verify the crew list to confirm assignment. Provide his crew member ID and certification validity status.",
        actions=[
            Action(
                name="GetCrewMemberDetails",
                kwargs={"employee_code": "EMP002"}
            ),
            Action(
                name="CheckCertificationValidity",
                kwargs={
                    "crew_member_id": "CM002",
                    "certification_id": "CERT_A32N",
                    "check_date": "2024-05-23"
                }
            ),
            Action(
                name="GetFlightCrewAssignments",
                kwargs={"flight_id": "FL038", "flight_number": "HAT038"}
            ),
            Action(
                name="AssignCrewToFlight",
                kwargs={
                    "flight_id": "FL038",
                    "flight_number": "HAT038",
                    "crew_member_id": "CM002",
                    "assigned_role": "First Officer"
                }
            ),
            Action(
                name="UpdateCrewFlightLog",
                kwargs={
                    "crew_member_id": "CM002",
                    "flight_id": "FL038",
                    "flight_number": "HAT038",
                    "date": "2024-05-23",
                    "role": "First Officer",
                    "aircraft_model": "A320neo",
                    "hours_flown": {
                        "total": 3.5,
                        "pic": 0.0,
                        "sic": 3.5,
                        "night": 1.0,
                        "instrument": 0.5
                    },
                    "landings": 1,
                    "takeoffs": 1
                }
            ),
            Action(
                name="GetFlightCrewAssignments",
                kwargs={"flight_id": "FL038", "flight_number": "HAT038"}
            )
        ],
        outputs=['"crew_member_id": "CM002"', '"certification_status": "valid"'],
    ),

    Task(
        annotator="0",
        user_id="USER_100",
        instruction="Execute the maintenance manager at ATL. Document an AOG hydraulic warning for AC001 (PR-GOL) at 2024-08-15T14:30:00Z: execute to set aircraft to Maintenance, create an Emergency Repair entry (WO-2024-08-15-005, ATA 29) with description 'Hydraulic system warning discovered during pre-flight inspection', corrective action 'Emergency repair procedures required for hydraulic system warning' and status should be 'In Progress', and create an AOG operational event. Provide the aircraft’s new status and the maintenance log ID.",
        actions=[
            Action(
                name="UpdateAircraftStatus",
                kwargs={"aircraft_id": "AC001", "new_status": "Maintenance"}
            ),
            Action(
                name="CreateMaintenanceEntry",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Emergency Repair",
                    "description": "Hydraulic system warning discovered during pre-flight inspection",
                    "technician_id": "TECH009",
                    "work_order_id": "WO-2024-08-15-005",
                    "ata_chapter": "29",
                    "corrective_action": "Emergency repair procedures required for hydraulic system warning",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "status": "In Progress"
                }
            ),
            Action(
                name="CreateOperationalEvent",
                kwargs={
                    "event_type": "Aircraft AOG",
                    "event_timestamp_utc": "2024-08-15T14:30:00Z",
                    "details": "Aircraft PR-GOL AOG situation due to hydraulic system warning discovered during pre-flight inspection",
                    "aircraft_id": "AC001",
                    "tail_number": "PR-GOL",
                    "airport_id": "ARP_ATL",
                    "iata_code": "ATL",
                    "status": "Active"
                }
            )
        ],
        outputs=[
            '"aircraft_status": "Maintenance"',
            '"maintenance_log_id": "ML026"'
        ]
    ),


]
