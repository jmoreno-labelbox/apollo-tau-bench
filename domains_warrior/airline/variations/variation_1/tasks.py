from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="task_001",
        instruction="You are the operations manager on duty at ATL. A SIGMET was issued at 2024-05-16 because of a Severe thunderstorm warning impacting ARP_ATL. You need to execute the standard Severe Weather Protocol for ATL, applying a 3-hour delay to all flights to ATL with status 'available' in a single update operation.",
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                     "airport_id": "ARP_ATL",
                     "event_type": "SIGMET",
                     "details": "Severe Weather Protocol initiated.",
                     "date": "2024-05-16"
                }
            ),
            Action(
                name="find_flights",
                kwargs={
                     "destination": "ATL",
                     "departure_date": "2024-05-16",
                     "status": [
                         "available"
                     ]
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                     "flight_number": ["HAT005", "HAT007", "HAT057", "HAT061", "HAT070", "HAT077", "HAT093", "HAT128", "HAT136", "HAT177", "HAT218", "HAT220", "HAT223", "HAT268", "HAT282"],
                     "delay_hours": 3,
                     "new_status": "DELAYED",
                     "flight_date": "2024-05-16",
                     "reason_event_id": "OE026"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_002",
        instruction="You are the operations controller at DFW. You need to execute the 'AOG Protocol' for aircraft PR-XBE, which reported an engine sensor failure. This affects flight HAT170 on 2024-05-22. Use the following details for the report: description 'Engine sensor failure discovered during pre-flight checks.', technician_id 'TECH008', work_order 'WO-2024-05-22-601'.",
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={
                     "tail_number": "PR-XBE"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                     "aircraft_id": "AC002",
                     "new_status": "Grounded"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                     "aircraft_id": "AC002",
                     "maintenance_type": "Unscheduled",
                     "event_date": "2024-05-22",
                     "description": "Engine sensor failure discovered during pre-flight checks.",
                     "status": "In Progress",
                     "technician_id": "TECH008",
                     "work_order_id": "WO-2024-05-22-601"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "AOG",
                     "details": "Aircraft AC002 grounded. Flight HAT170 on 2024-05-22 cancelled due to unscheduled maintenance: Engine sensor failure discovered during pre-flight checks.",
                     "flight_number": "HAT170",
                     "airport_id": "ARP_DFW",
                     "date": "2024-05-22"
                }
            ),
            Action(
                name="update_flight_status",
                kwargs={
                     "flight_number": "HAT170",
                     "date": "2024-05-22",
                     "new_status": "cancelled"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT170",
                     "date": "2024-05-22"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "4WQ150",
                     "new_status": "CANCELLED_AOG"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "USJI8D",
                     "new_status": "CANCELLED_AOG"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "2GWL5L",
                     "new_status": "CANCELLED_AOG"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_003",
        instruction="You are the Operations Controller at JFK. You need to execute the 'AOG Protocol' for the aircraft with tail number PR-XTD, which has a reported hydraulic fluid leak. This grounds the aircraft, affecting flight HAT014 to MIA on 2024-05-16. Use the following details for the maintenance log: description 'Hydraulic fluid leak detected from the right-wing flap actuator during pre-flight inspection.', technician_id 'TECH009', and work_order 'WO-2024-05-16-778'.",
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={
                     "tail_number": "PR-XTD"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                     "aircraft_id": "AC005",
                     "new_status": "Grounded"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                     "aircraft_id": "AC005",
                     "maintenance_type": "Unscheduled",
                     "event_date": "2024-05-16",
                     "description": "Hydraulic fluid leak detected from the right-wing flap actuator during pre-flight inspection.",
                     "status": "In Progress",
                     "technician_id": "TECH009",
                     "work_order_id": "WO-2024-05-16-778"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "AOG",
                     "details": "Aircraft AC005 grounded. Flight HAT014 on 2024-05-16 cancelled due to unscheduled maintenance: Hydraulic fluid leak detected from the right-wing flap actuator during pre-flight inspection.",
                     "flight_number": "HAT014",
                     "airport_id": "ARP_JFK",
                     "date": "2024-05-16"
                }
            ),
            Action(
                name="update_flight_status",
                kwargs={
                     "flight_number": "HAT014",
                     "date": "2024-05-16",
                     "new_status": "cancelled"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT014",
                     "date": "2024-05-16"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "OK5IEN",
                     "new_status": "CANCELLED_AOG"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_004",
        instruction="You are the Crew Scheduler for the SEA base. You need to execute the 'Crew Unavailability Protocol' for Captain Noah Williams (employee code EMP007). You have reported sick and is unable to work his shift for flight HAT011 on 2024-05-17. The unavailability reason to be used is 'On Sick Leave'.",
        actions=[
            Action(
                name="find_crew_member",
                kwargs={
                     "employee_code": "EMP007"
                }
            ),
            Action(
                name="update_crew_member_status",
                kwargs={
                     "crew_member_id": "CM007",
                     "new_status": "On Sick Leave"
                }
            ),
            Action(
                name="find_crew_assignments",
                kwargs={
                     "crew_member_id": "CM007"
                }
            ),
            Action(
                name="get_airport_by_code",
                kwargs={
                     "iata_code": "SEA"
                }
            ),
            Action(
                name="find_available_crew",
                kwargs={
                     "role": "Captain",
                     "home_base_iata": "SEA",
                     "status": "Active"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "CREW_UNAVAILABLE",
                     "details": "Crew replacement failed for flight HAT011 on 2024-05-17. Original crew member CM007 is unavailable.",
                     "airport_id": "ARP_SEA",
                     "flight_number": "HAT011",
                     "date": "2024-05-17"
                }
            ),
            Action(
                name="update_flight_status",
                kwargs={
                     "flight_number": "HAT011",
                     "date": "2024-05-17",
                     "new_status": "cancelled"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_005",
        instruction="You are the Fleet Manager at ARP_PHX. The airline is launching a new route from Phoenix (PHX) to Las Vegas (LAS) under flight number HAT451, with a scheduled departure of 11:30:00 and arrival of 12:45:00. To service this route, you need to execute the 'Return to Service Protocol' for aircraft with tail number PP-PTM. The process must be logged with technician ID TECH015, work order 'WO-2025-08-10-005', and use the maintenance date 2025-08-09.",
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={
                     "tail_number": "PP-PTM"
                }
            ),
            Action(
                name="create_flight",
                kwargs={
                     "flight_number": "HAT451",
                     "origin": "PHX",
                     "destination": "LAS",
                     "scheduled_departure_time_est": "11:30:00",
                     "scheduled_arrival_time_est": "12:45:00"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                     "aircraft_id": "AC008",
                     "new_status": "Maintenance"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                     "aircraft_id": "AC008",
                     "maintenance_type": "Return to Service Inspection",
                     "description": "Return to Service inspection for flight operations.",
                     "technician_id": "TECH015",
                     "work_order_id": "WO-2025-08-10-005",
                     "event_date": "2025-08-09",
                     "status": "Completed"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                     "aircraft_id": "AC008",
                     "new_status": "Active"
                }
            ),
            Action(
                name="get_airport_by_code",
                kwargs={
                     "iata_code": "PHX"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "AIRCRAFT_ACTIVATED",
                     "details": "Aircraft AC008 (PP-PTM) activated from storage at PHX for new flight route HAT451.",
                     "airport_id": "ARP_PHX",
                     "flight_number": "HAT451"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_006",
        instruction=("You are the Operations Manager at LGA. You need to apply the “Route Suspension Protocol” with an override to suspend flight HAT002 (LGA–PHX) only on 2024-05-17, and issue a $100 compensation travel voucher per reservation."),
        actions=[
            Action(
                name="create_operational_event",
                kwargs={"event_type": "ROUTE_SUSPENSION", "airport_id": "ARP_LGA", "flight_number": "HAT002",
                        "details": "Route HAT002 (LGA-PHX) suspended for 2024-05-17. Flight HAT002 on 2024-05-17 is cancelled.", "date": "2024-05-17"}
            ),
            Action(
                name="update_flight_status",
                kwargs={"flight_number": "HAT002",
                        "date": "2024-05-17", "new_status": "cancelled"}
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={"flight_number": "HAT002", "date": "2024-05-17"}
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "BU71UY",
                     "new_status": "CANCELLED_ROUTE_SUSPENSION"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "CC80AJ",
                     "new_status": "CANCELLED_ROUTE_SUSPENSION"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "HDUF3Q",
                     "new_status": "CANCELLED_ROUTE_SUSPENSION"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={"reservation_id": "BU71UY", "message": "FLIGHT CANCELLATION: Your flight HAT002 on 2024-05-17 has been cancelled due to a route suspension. A $100 travel voucher has been issued to your account."}
            ),
            Action(
                name="send_passenger_notification",
                kwargs={"reservation_id": "HDUF3Q", "message": "FLIGHT CANCELLATION: Your flight HAT002 on 2024-05-17 has been cancelled due to a route suspension. A $100 travel voucher has been issued to your account."}
            ),
            Action(
                name="send_passenger_notification",
                kwargs={"reservation_id": "CC80AJ", "message": "FLIGHT CANCELLATION: Your flight HAT002 on 2024-05-17 has been cancelled due to a route suspension. A $100 travel voucher has been issued to your account."}
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Finance",
                    "message": "FINANCE NOTICE: Route HAT002 suspended. Total of $300 in vouchers issued for 3 affected reservations."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_007",
        instruction="You are the Operations Controller for the DFW airport. The cabin crew on flight HAT004 (operated by aircraft PR-GOL), en route from ATL to DFW on 2024-05-15, has reported that passenger Ethan Silva requires medical assistance upon arrival. You need to execute the standard medical alert.",
        actions=[
            Action(
                name="get_flight_by_number",
                kwargs={
                     "flight_number": "HAT004",
                     "date": "2024-05-15"
                }
            ),
            Action(
                name="get_airport_by_code",
                kwargs={
                     "iata_code": "DFW"
                }
            ),
            Action(
                name="find_flight_crew",
                kwargs={
                     "flight_number": "HAT004"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "MEDICAL_ASSISTANCE",
                     "airport_id": "ARP_DFW",
                     "flight_number": "HAT004",
                     "date": "2024-05-15",
                     "details": "Medical assistance requested for passenger Ethan Silva on flight HAT004 upon arrival at DFW."
                }
            ),
            Action(
                name="send_ground_notification",
                kwargs={
                     "airport_id": "ARP_DFW",
                     "priority": "HIGH",
                     "message": "MEDICAL ALERT: Flight HAT004 arriving from ATL requires immediate medical assistance for passenger Ethan Silva at the gate. Awaiting arrival."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_008",
        instruction="You are the Operations Manager for the CLT airport. Due to sustained low passenger demand, executive management has decided to suspend the HAT015 route from CLT to EWR. You need to execute the 'Route Suspension Protocol' for all scheduled flights on 2024-05-17 and 2024-05-18, ensuring all operational records and affected passenger reservations are updated accordingly.",
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "ROUTE_SUSPENSION",
                     "airport_id": "ARP_CLT",
                     "flight_number": "HAT015",
                     "details": "Route HAT015 (CLT-EWR) has been suspended. All flights from 2024-05-17 to 2024-05-18 are cancelled."
                }
            ),
            Action(
                name="update_flight_status",
                kwargs={
                     "flight_number": "HAT015",
                     "date": "2024-05-17",
                     "new_status": "cancelled"
                }
            ),
            Action(
                name="update_flight_status",
                kwargs={
                     "flight_number": "HAT015",
                     "date": "2024-05-18",
                     "new_status": "cancelled"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT015",
                     "date": "2024-05-17"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "RNL6HR",
                     "new_status": "CANCELLED_ROUTE_SUSPENSION"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "4MB0L3",
                     "new_status": "CANCELLED_ROUTE_SUSPENSION"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT015",
                     "date": "2024-05-18"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "W8DUJ8",
                     "new_status": "CANCELLED_ROUTE_SUSPENSION"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_009",
        instruction="You are a Schedule Planner at headquarters. Due to new slot allocations at LGA, you need to execute the 'Route Retiming Protocol' for flight number HAT002 (LGA-PHX). The new schedule will be a 22:30:00 departure from LGA on each scheduled day and a 03:00:00 arrival at PHX on the following calendar day (explicitly next day). Apply this change to all flights on the dates 2024-05-16, 2024-05-17, and 2024-05-18, ensuring that the arrival reflects the next day after departure. Make sure all affected passengers are notified accordingly.",
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "SCHEDULE_CHANGE",
                     "airport_id": "ARP_LGA",
                     "flight_number": "HAT002",
                     "details": "Route HAT002 (LGA-PHX) retiming process initiated. New schedule: 22:30:00-03:00:00."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                     "flight_number": "HAT002",
                     "flight_date": "2024-05-16",
                     "new_departure_date": "2024-05-16",
                     "new_departure_time_est": "22:30:00",
                     "new_arrival_date": "2024-05-17",
                     "new_arrival_time_est": "03:00:00",
                     "reason_event_id": "OE026"
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                     "flight_number": "HAT002",
                     "flight_date": "2024-05-17",
                     "new_departure_date": "2024-05-17",
                     "new_departure_time_est": "22:30:00",
                     "new_arrival_date": "2024-05-18",
                     "new_arrival_time_est": "03:00:00",
                     "reason_event_id": "OE026"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT002",
                     "date": "2024-05-16"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT002",
                     "date": "2024-05-17"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                     "reservation_id": "BU71UY",
                     "message": "FLIGHT UPDATE for reservation BU71UY: Your flight HAT002 on 2024-05-17 has been rescheduled. New departure is 22:30:00 and new arrival is 03:00:00. We apologize for any inconvenience."
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                     "reservation_id": "HDUF3Q",
                     "message": "FLIGHT UPDATE for reservation HDUF3Q: Your flight HAT002 on 2024-05-17 has been rescheduled. New departure is 22:30:00 and new arrival is 03:00:00. We apologize for any inconvenience."
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                     "reservation_id": "CC80AJ",
                     "message": "FLIGHT UPDATE for reservation CC80AJ: Your flight HAT002 on 2024-05-17 has been rescheduled. New departure is 22:30:00 and new arrival is 03:00:00. We apologize for any inconvenience."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                     "flight_number": "HAT002",
                     "flight_date": "2024-05-18",
                     "new_departure_date": "2024-05-18",
                     "new_arrival_date": "2024-05-19",
                     "new_departure_time_est": "22:30:00",
                     "new_arrival_time_est": "03:00:00",
                     "reason_event_id": "OE026"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT002",
                     "date": "2024-05-18"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                     "reservation_id": "J3SAZF",
                     "message": "FLIGHT UPDATE for reservation J3SAZF: Your flight HAT002 on 2024-05-18 has been rescheduled. New departure is 22:30:00 and new arrival is 03:00:00. We apologize for any inconvenience."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_010",
        instruction="You are the Operations Manager at ORD. You need to execute the 'AOG Protocol' for aircraft PT-MUI. This grounds the aircraft, cancelling flight HAT014 to JFK on 2024-05-17. For this specific event, override the standard reservation cancellation and update the status of all affected reservations to 'REBOOKING_PENDING' to flag them for the service recovery team. Use technician ID TECH009 and work order 'WO-2024-05-17-901' for the maintenance log.",
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={
                     "tail_number": "PT-MUI"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                     "aircraft_id": "AC006",
                     "new_status": "Grounded"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                     "aircraft_id": "AC006",
                     "maintenance_type": "Unscheduled",
                     "description": "Aircraft is AOG.",
                     "status": "In Progress",
                     "technician_id": "TECH009",
                     "event_date": "2024-05-17",
                     "work_order_id": "WO-2024-05-17-901"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "AOG",
                     "airport_id": "ARP_ORD",
                     "flight_number": "HAT014",
                     "date": "2024-05-17",
                     "details": "Aircraft AC006 grounded. Flight HAT014 on 2024-05-17 cancelled due to unscheduled maintenance: Aircraft is AOG."
                }
            ),
            Action(
                name="update_flight_status",
                kwargs={
                     "flight_number": "HAT014",
                     "date": "2024-05-17",
                     "new_status": "cancelled"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT014",
                     "date": "2024-05-17"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "QS2N5D",
                     "new_status": "REBOOKING_PENDING"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_011",
        instruction="You are the Operations Manager at ARP_DFW. A “Severe Thunderstorm” warning is in effect for 2024-05-17 in the DFW area. You need to execute the “Severe Weather Protocol” in this custom way: still create operational event but next only do the following:- For flight HAT022 from LAX on 2024-05-17: cancel the flight updating its status to 'CANCELLED_WEATHER' and update all affected reservations accordingly. - For flight HAT004 from ATL on 2024-05-17: apply a 3-hour delay and update all affected reservations to SCHEDULE_CHANGE, ensuring passengers receive the updated departure and arrival times.",
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "SIGMET",
                     "airport_id": "ARP_DFW",
                     "details": 'Severe Weather Protocol initiated.',
                     "date": "2024-05-17"
                }
            ),
            Action(
                name="update_flight_status",
                kwargs={
                     "flight_number": "HAT022",
                     "date": "2024-05-17",
                     "new_status": "CANCELLED_WEATHER"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT022",
                     "date": "2024-05-17"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "HVU16N",
                     "new_status": "CANCELLED_WEATHER"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                     "reservation_id": "HVU16N",
                    "message": "FLIGHT CANCELLATION NOTICE: Due to severe weather, your flight HAT022 on 2024-05-17 has been cancelled."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                     "flight_number": "HAT004",
                     "flight_date": "2024-05-17",
                     "delay_hours": 3,
                     "new_status": "DELAYED",
                     "reason_event_id": "OE026"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT004",
                     "date": "2024-05-17"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "KKKYCG",
                     "new_status": "SCHEDULE_CHANGE"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                     "reservation_id": "KKKYCG",
                     "message": "FLIGHT UPDATE for reservation KKKYCG: Your flight HAT004 on 2024-05-17 has been rescheduled. New departure is 17:00:00 and new arrival is 19:00:00. We apologize for any inconvenience."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_012",
        instruction="You are the Operations Manager for the SEA airport. Captain Noah Williams (EMP007) is unavailable for flight HAT011 to SFO on 2024-05-18. You need to execute the “Crew Unavailability Protocol” with a critical override to source an available Captain from the ATL base if no replacement is found at SEA; also no checking of certifications is needed if the person is known to be a captain.",
        actions=[
            Action(
                name="find_crew_member",
                kwargs={
                     "employee_code": "EMP007"
                }
            ),
            Action(
                name="update_crew_member_status",
                kwargs={
                     "crew_member_id": "CM007",
                     "new_status": "On Sick Leave"
                }
            ),
            Action(
                name="find_available_crew",
                kwargs={
                     "role": "Captain",
                     "home_base_iata": "SEA",
                     "status": "Active"
                }
            ),
            Action(
                name="find_available_crew",
                kwargs={
                     "role": "Captain",
                     "home_base_iata": "ATL",
                     "status": "Active"
                }
            ),
            Action(
                name="find_crew_assignments",
                kwargs={
                     "crew_member_id": "CM007"
                }
            ),
            Action(
                name="update_crew_assignment",
                kwargs={
                     "assignment_id": "AS010",
                     "new_crew_member_id": "CM001",
                     "new_crew_member_full_name": "Mia Li"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "CREW_UNAVAILABLE",
                     "airport_id": "ARP_SEA",
                     "flight_number": "HAT011",
                     "date": "2024-05-18",
                     "details": "Crew replacement successful for flight HAT011 on 2024-05-18. Original crew member CM007 is unavailable."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_013",
        instruction="You are the Fleet Manager at MCO. As part of the fleet modernization plan, you need permanently decommission the oldest aircraft at your base, tail number PS-MND. You need to execute the 'Aircraft Decommissioning Protocol' for this aircraft using the date August 10, 2025. The final maintenance log must be assigned to technician TECH015 with work order 'WO-2025-DECOM-001'.",
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={
                     "tail_number": "PS-MND"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                     "aircraft_id": "AC012",
                     "new_status": "Decommissioned"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                     "aircraft_id": "AC012",
                     "maintenance_type": "Decommissioning",
                     "description": "Final log entry for aircraft decommissioning and permanent retirement from service.",
                     "status": "Completed",
                     "technician_id": "TECH015",
                     "event_date": "2025-08-10",
                     "work_order_id": "WO-2025-DECOM-001"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "AIRCRAFT_DECOMMISSIONED",
                     "airport_id": "ARP_MCO",
                     "details": "Aircraft AC012 (PS-MND), model CRJ900, has been officially decommissioned and removed from the active fleet at MCO."
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                     "department_name": "Finance",
                     "message": "AIRCRAFT ALERT: Aircraft PS-MND (AC012) has been officially decommissioned. Please update all relevant asset and scheduling records."
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                     "department_name": "Scheduling",
                     "message": "AIRCRAFT ALERT: Aircraft PS-MND (AC012) has been officially decommissioned. Please update all relevant asset and scheduling records."
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                     "department_name": "MRO_Planning",
                     "message": "AIRCRAFT ALERT: Aircraft PS-MND (AC012) has been officially decommissioned. Please update all relevant asset and scheduling records."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_014",
        instruction="You are a Schedule Planner. You need to apply the “Route Retiming Protocol” to the HAT014 route (JFK–MIA) with a new schedule of 18:00:00 departure and 21:00:00 arrival for the flights on 2024-05-16 and 2024-05-17. You need to process the updates in chronological order.",
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "SCHEDULE_CHANGE",
                     "airport_id": "ARP_JFK",
                     "flight_number": "HAT014",
                     "details": "Route HAT014 (JFK-MIA) retiming process initiated. New schedule: 18:00:00-21:00:00."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                     "flight_number": "HAT014",
                     "flight_date": "2024-05-16",
                     "new_departure_time_est": "18:00:00",
                     "new_arrival_time_est": "21:00:00",
                     "reason_event_id": "OE026"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT014",
                     "date": "2024-05-16"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                     "reservation_id": "OK5IEN",
                     "message": "FLIGHT UPDATE for reservation OK5IEN: Your flight HAT014 on 2024-05-16 has been rescheduled. New departure is 18:00:00 and new arrival is 21:00:00. We apologize for any inconvenience."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                     "flight_number": "HAT014",
                     "flight_date": "2024-05-17",
                     "new_departure_time_est": "18:00:00",
                     "new_arrival_time_est": "21:00:00",
                     "reason_event_id": "OE026"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT014",
                     "date": "2024-05-17"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                     "reservation_id": "QS2N5D",
                     "message": "FLIGHT UPDATE for reservation QS2N5D: Your flight HAT014 on 2024-05-17 has been rescheduled. New departure is 18:00:00 and new arrival is 21:00:00. We apologize for any inconvenience."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_015",
        instruction="You are the Crew Scheduler at ATL. First Officer Lucas Hernandez (employee code EMP002) has reported sick and is unavailable for flight HAT004 to DFW on 2024-05-21. You need to execute the 'Crew Unavailability Protocol'. You need override the standard procedure: if no replacement First Officer is available locally, attempt to find an available Captain at the ATL base to operate in the First Officer role. Before any assignment, their B737-800 certification must be validated.",
        actions=[
            Action(
                name="find_crew_member",
                kwargs={
                     "employee_code": "EMP002"
                }
            ),
            Action(
                name="update_crew_member_status",
                kwargs={
                     "crew_member_id": "CM002",
                     "new_status": "On Sick Leave"
                }
            ),
            Action(
                name="find_available_crew",
                kwargs={
                     "role": "First Officer",
                     "home_base_iata": "ATL",
                     "status": "Active"
                }
            ),
            Action(
                name="find_available_crew",
                kwargs={
                     "role": "Captain",
                     "home_base_iata": "ATL",
                     "status": "Active"
                }
            ),
            Action(
                name="find_crew_certifications",
                kwargs={
                     "crew_member_id": "CM001",
                     "certification_code": "B737-800"
                }
            ),
            Action(
                name="find_crew_assignments",
                kwargs={
                     "crew_member_id": "CM002",
                     "flight_number": "HAT004",
                }
            ),
            Action(
                name="update_crew_assignment",
                kwargs={
                     "assignment_id": "AS002",
                     "new_crew_member_id": "CM001",
                     "new_crew_member_full_name": "Mia Li"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "CREW_UNAVAILABLE",
                     "airport_id": "ARP_ATL",
                     "flight_number": "HAT004",
                     "date": "2024-05-21",
                     "details": "Crew replacement successful for flight HAT004 on 2024-05-21. Original crew member CM002 is unavailable."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_016",
        instruction="You are the Maintenance Controller at JFK. Aircraft AC005 has reported a faulty landing gear sensor ahead of flight HAT014 on 2024-05-17. You need to the “AOG Protocol” with the following override: - Apply a “repair and reinstate” procedure that's like follows: repair AC005, return it to Active status, and delay flight HAT014 instead of cancelling it. - Log the maintenance using technician ID TECH008, work order WO-2024-05-17-915, and description “Faulty landing gear sensor.”.",
        actions=[
            Action(name="update_aircraft_status", kwargs={
                   "aircraft_id": "AC005", "new_status": "Grounded"}),
            Action(name="create_maintenance_log", kwargs={
                "aircraft_id": "AC005",
                "maintenance_type": "Unscheduled",
                "description": "Faulty landing gear sensor.",
                "status": "In Progress",
                "technician_id": "TECH008",
                "event_date": "2024-05-17",
                "work_order_id": "WO-2024-05-17-915"
            }),
            Action(
                name="update_aircraft_status",
                kwargs={
                     "aircraft_id": "AC005",
                     "new_status": "Active"
                }
            ),
            Action(name="create_operational_event",
                   kwargs={
                       "event_type": "AOG_REPAIR",
                       "airport_id": "ARP_JFK",
                       "flight_number": "HAT014",
                       "date": "2024-05-17",
                       "details": "Aircraft AC005 returned to service after repair. Flight HAT014 on 2024-05-17 delayed due to unscheduled maintenance: Faulty landing gear sensor."
                   }),
            Action(name="update_flight_status", kwargs={
                "flight_number": "HAT014",
                "date": "2024-05-17",
                "new_status": "delayed",
            })
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_017",
        instruction="You are the Customer Experience Manager for the ATL airport (ARP_ATL). To reward customers on a competitive route, you need to execute the “Service Upgrade Protocol” for flight HAT004 to DFW on 2024-05-16, upgrading all passengers from economy to business as part of a PROMOTIONAL_UPGRADE initiative.",
        actions=[
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT004",
                     "date": "2024-05-16"
                }
            ),
            Action(
                name="update_reservation_details",
                kwargs={
                     "reservation_id": "D975WV",
                     "new_cabin": "business",
                     "new_status": "Upgraded"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                     "reservation_id": "D975WV",
                     "message": "SERVICE UPGRADE for reservation D975WV: As a valued customer, your booking for flight HAT004 has been upgraded to business. Enjoy your flight!"
                }
            ),
            Action(
                name="update_reservation_details",
                kwargs={
                     "reservation_id": "BMZ6Y9",
                     "new_cabin": "business",
                     "new_status": "Upgraded"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                     "reservation_id": "BMZ6Y9",
                     "message": "SERVICE UPGRADE for reservation BMZ6Y9: As a valued customer, your booking for flight HAT004 has been upgraded to business. Enjoy your flight!"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "PROMOTIONAL_UPGRADE",
                     "airport_id": "ARP_ATL",
                     "flight_number": "HAT004",
                     "date": "2024-05-16",
                     "details": "Promotional upgrade initiative applied to flight HAT004 on 2024-05-16. All economy passengers upgraded."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_018",
        instruction="You are the Operations Controller at JFK. During pre-flight checks, aircraft PR-XTD reported a critical avionics fault. You need to execute the standard 'AOG Protocol' for its scheduled flight, HAT014 to MIA, on May 17, 2024. Use the following details for the maintenance log: description 'Critical FMS failure detected during power-up test.', technician_id 'TECH008', and work_order 'WO-2024-05-17-JFK-02'. Finally, provide the ID of the new maintenance log that was created.",
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={
                     "tail_number": "PR-XTD"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                     "aircraft_id": "AC005",
                     "new_status": "Grounded"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                     "aircraft_id": "AC005",
                     "maintenance_type": "Unscheduled",
                     "description": "Critical FMS failure detected during power-up test.",
                     "status": "In Progress",
                     "technician_id": "TECH008",
                     "event_date": "2024-05-17",
                     "work_order_id": "WO-2024-05-17-JFK-02"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "AOG",
                     "airport_id": "ARP_JFK",
                     "flight_number": "HAT014",
                     "date": "2024-05-17",
                     "details": "Aircraft AC005 grounded. Flight HAT014 on 2024-05-17 cancelled due to unscheduled maintenance: Critical FMS failure detected during power-up test."
                }
            ),
            Action(
                name="update_flight_status",
                kwargs={
                     "flight_number": "HAT014",
                     "date": "2024-05-17",
                     "new_status": "cancelled"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT014",
                     "date": "2024-05-17"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "QS2N5D",
                     "new_status": "CANCELLED_AOG"
                }
            ),
        ],
        outputs=[
            "ML026"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_019",
        instruction="You are a Schedule Planner. Due to low profitability and fleet reallocation, the decision has been made to suspend the HAT004 route between ATL and DFW. You need to execute the 'Route Suspension Protocol' for all scheduled flights on this route for the dates May 16, 2024, and May 17, 2024. You also needs to provide the total count of cancelled reservations.",         actions=[
            Action(
                name="create_operational_event",
                kwargs={
                     "event_type": "ROUTE_SUSPENSION",
                     "airport_id": "ARP_ATL",
                     "flight_number": "HAT004",
                     "details": "Route HAT004 (ATL-DFW) has been suspended. All flights from 2024-05-16 to 2024-05-17 are cancelled."
                }
            ),
            Action(
                name="update_flight_status",
                kwargs={
                     "flight_number": "HAT004",
                     "date": "2024-05-16",
                     "new_status": "cancelled"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT004",
                     "date": "2024-05-16"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "D975WV",
                     "new_status": "CANCELLED_ROUTE_SUSPENSION"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "BMZ6Y9",
                     "new_status": "CANCELLED_ROUTE_SUSPENSION"
                }
            ),
            Action(
                name="update_flight_status",
                kwargs={
                     "flight_number": "HAT004",
                     "date": "2024-05-17",
                     "new_status": "cancelled"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                     "flight_number": "HAT004",
                     "date": "2024-05-17"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                     "reservation_id": "KKKYCG",
                     "new_status": "CANCELLED_ROUTE_SUSPENSION"
                }
            )
        ],
        outputs=[
            "3"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_020",
        instruction="You are the Operations Controller at ATL. Aircraft PR-GOL reported a bird strike impacting the left engine during taxi. The aircraft is now AOG. You need to execute the standard 'AOG Protocol' for its scheduled flight, HAT004 to DFW, on May 17, 2024. Use the following details for the log: description 'Left engine bird strike during taxi, requires full inspection.', technician_id 'TECH005', and work_order 'WO-2024-05-17-ATL-01'. Finally, provide the ID of the new maintenance log that was created.",
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={
                    "tail_number": "PR-GOL"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                    "aircraft_id": "AC001",
                    "new_status": "Grounded"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Unscheduled",
                    "description": "Left engine bird strike during taxi, requires full inspection.",
                    "status": "In Progress",
                    "technician_id": "TECH005",
                    "event_date": "2024-05-17",
                    "work_order_id": "WO-2024-05-17-ATL-01"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "AOG",
                    "airport_id": "ARP_ATL",
                    "flight_number": "HAT004",
                    "date": "2024-05-17",
                    "details": "Aircraft AC001 grounded. Flight HAT004 on 2024-05-17 cancelled due to unscheduled maintenance: Left engine bird strike during taxi, requires full inspection."
                }
            ),
            Action(
                name="update_flight_status",
                kwargs={
                    "flight_number": "HAT004",
                    "date": "2024-05-17",
                    "new_status": "cancelled"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                    "flight_number": "HAT004",
                    "date": "2024-05-17"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                    "reservation_id": "KKKYCG",
                    "new_status": "CANCELLED_AOG"
                }
            )
        ],
        outputs=[
            "ML026"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_021",
        instruction="You are a Crew Scheduler at ORD. Flight Attendant Sophia Taylor (EMP003) is unavailable for flight HAT002 to PHX on 2024-05-18. You need to execute the “Crew Unavailability Protocol”.",
        actions=[
                Action(
                    name="find_crew_member",
                    kwargs={
                         "employee_code": "EMP003"
                    }
                ),
            Action(
                    name="update_crew_member_status",
                    kwargs={
                         "crew_member_id": "CM003",
                         "new_status": "On Sick Leave"
                    }
            ),
            Action(
                    name="find_available_crew",
                    kwargs={
                         "role": "Flight Attendant",
                         "home_base_iata": "ORD",
                         "status": "Active"
                    }
            ),
            Action(
                    name="create_operational_event",
                    kwargs={
                         "event_type": "CREW_UNAVAILABLE",
                         "airport_id": "ARP_ORD",
                         "flight_number": "HAT002",
                         "date": "2024-05-18",
                         "details": "Crew replacement failed for flight HAT002 on 2024-05-18. Original crew member CM003 is unavailable."
                    }
            ),
            Action(
                    name="update_flight_status",
                    kwargs={
                         "flight_number": "HAT002",
                         "date": "2024-05-18",
                         "new_status": "cancelled"
                    }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_022",
        instruction="You are a Schedule Planner. To improve on-time performance, you need to adjust the schedule for the regional route HAT015 (CLT-EWR). You need to execute the 'Route Retiming Protocol' to set a new schedule of 02:00:00 departure and 04:00:00 arrival. This change must be applied to all flights on the dates May 17, 2024, and May 18, 2024. Finally, provide a list of reservation IDs for all notified passengers.",
        actions=[
                Action(
                    name="create_operational_event",
                    kwargs={
                         "event_type": "SCHEDULE_CHANGE",
                         "airport_id": "ARP_CLT",
                         "flight_number": "HAT015",
                         "details": "Route HAT015 (CLT-EWR) retiming process initiated. New schedule: 02:00:00-04:00:00."
                    }
                ),
            Action(
                    name="update_flight_schedule",
                    kwargs={
                         "flight_number": "HAT015",
                         "flight_date": "2024-05-17",
                         "new_departure_time_est": "02:00:00",
                         "new_arrival_time_est": "04:00:00",
                         "reason_event_id": "OE026"
                    }
            ),
            Action(
                    name="find_reservations_by_flight",
                    kwargs={
                         "flight_number": "HAT015",
                         "date": "2024-05-17"
                    }
            ),
            Action(
                    name="send_passenger_notification",
                    kwargs={
                         "reservation_id": "4MB0L3",
                         "message": "FLIGHT UPDATE for reservation 4MB0L3: Your flight HAT015 on 2024-05-17 has been rescheduled. New departure is 02:00:00 and new arrival is 04:00:00. We apologize for any inconvenience."
                    }
            ),
            Action(
                    name="send_passenger_notification",
                    kwargs={
                         "reservation_id": "RNL6HR",
                         "message": "FLIGHT UPDATE for reservation RNL6HR: Your flight HAT015 on 2024-05-17 has been rescheduled. New departure is 02:00:00 and new arrival is 04:00:00. We apologize for any inconvenience."
                    }
            ),
            Action(
                    name="update_flight_schedule",
                    kwargs={
                         "flight_number": "HAT015",
                         "flight_date": "2024-05-18",
                         "new_departure_time_est": "02:00:00",
                         "new_arrival_time_est": "04:00:00",
                         "reason_event_id": "OE026"
                    }
            ),
            Action(
                    name="find_reservations_by_flight",
                    kwargs={
                         "flight_number": "HAT015",
                         "date": "2024-05-18"
                    }
            ),
            Action(
                    name="send_passenger_notification",
                    kwargs={
                         "reservation_id": "W8DUJ8",
                         "message": "FLIGHT UPDATE for reservation W8DUJ8: Your flight HAT015 on 2024-05-18 has been rescheduled. New departure is 02:00:00 and new arrival is 04:00:00. We apologize for any inconvenience."
                    }
            )
        ],
        outputs=[
            "4MB0L3",
            "RNL6HR",
            "W8DUJ8"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_023",
        instruction="You are the Customer Experience Manager for the ATL airport (ARP_ATL). To reward customers on the competitive ATL-DFW route, you need to execute the 'Service Upgrade Protocol' for flight HAT004 on 2024-05-16. All passengers currently booked in the 'economy' cabin are to receive a complimentary upgrade to 'business' with status 'Upgraded'.",
        actions=[
            Action(
                name="find_reservations_by_flight",
                kwargs={
                    "flight_number": "HAT004",
                    "date": "2024-05-16"
                }
            ),
            Action(
                name="update_reservation_details",
                kwargs={
                    "reservation_id": "D975WV",
                    "new_cabin": "business",
                    "new_status": "Upgraded"
                }
            ),
            Action(
                name="update_reservation_details",
                kwargs={
                    "reservation_id": "BMZ6Y9",
                    "new_cabin": "business",
                    "new_status": "Upgraded"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "D975WV",
                    "message": "SERVICE UPGRADE for reservation D975WV: As a valued customer, your booking for flight HAT004 has been upgraded to business. Enjoy your flight!"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "BMZ6Y9",
                    "message": "SERVICE UPGRADE for reservation BMZ6Y9: As a valued customer, your booking for flight HAT004 has been upgraded to business. Enjoy your flight!"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "PROMOTIONAL_UPGRADE",
                    "airport_id": "ARP_ATL",
                    "flight_number": "HAT004",
                    "date": "2024-05-16",
                    "details": "Promotional upgrade initiative applied to flight HAT004 on 2024-05-16. All economy passengers upgraded."
                }
            )
        ],
        outputs=[
            "2"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_024",
        instruction="You are the Fleet Safety Manager. A service audit has revealed a recurring safety issue with cracked rudder trim actuators across the CRJ900 fleet. You need to execute the 'Fleet Airworthiness Directive Protocol' for all non-stored CRJ900 aircraft identified by their internal aircraft IDs: AC023, AC013, and AC020. The directive must be logged against the ATL airport for 2025-08-10, using technician ID TECH020 and the respective work orders 'WO-AUG25-INSP-AC023', 'WO-AUG25-INSP-AC013', and 'WO-AUG25-INSP-AC020'.",
        actions=[
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "AIRWORTHINESS_DIRECTIVE",
                        "airport_id": "ARP_ATL",
                        "details": "FLEET DIRECTIVE ISSUED.",
                        "date": "2025-08-10"
                    }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                    "aircraft_id": "AC023",
                    "new_status": "Maintenance"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC023",
                    "maintenance_type": "Mandatory Inspection",
                    "description": "Mandatory Inspection per manufacturer service bulletin.",
                    "status": "In Progress",
                    "technician_id": "TECH020",
                    "event_date": "2025-08-10",
                    "work_order_id": "WO-AUG25-INSP-AC023"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                    "aircraft_id": "AC013",
                    "new_status": "Maintenance"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC013",
                    "maintenance_type": "Mandatory Inspection",
                    "description": "Mandatory Inspection per manufacturer service bulletin.",
                    "status": "In Progress",
                    "technician_id": "TECH020",
                    "event_date": "2025-08-10",
                    "work_order_id": "WO-AUG25-INSP-AC013"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                    "aircraft_id": "AC020",
                    "new_status": "Maintenance"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC020",
                    "maintenance_type": "Mandatory Inspection",
                    "description": "Mandatory Inspection per manufacturer service bulletin.",
                    "status": "In Progress",
                    "technician_id": "TECH020",
                    "event_date": "2025-08-10",
                    "work_order_id": "WO-AUG25-INSP-AC020"
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "MRO_Planning",
                    "message": "FLEET DIRECTIVE: All CRJ900 aircraft have been moved to Maintenance status for mandatory inspection."
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Scheduling",
                    "message": "SCHEDULING ALERT: All CRJ900 aircraft are now in Maintenance status and unavailable for flight operations."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_025",
        instruction="You are the Maintenance Controller at ATL. Aircraft AC001 reported a cabin pressurization warning during pre-flight checks for its flight HAT004 to DFW on May 17, 2024. The issue is repaired as of now but not logged. You need to execute the 'AOG Protocol' with a 'repair and reinstate' override, delaying the flight. Use the exact description 'Cabin pressurization warning sensor replaced.' for the maintenance log. Use technician ID TECH005 and work order 'WO-2024-05-17-ATL-CP1'.",
        actions=[
            Action(
                    name="update_aircraft_status",
                    kwargs={
                         "aircraft_id": "AC001",
                         "new_status": "Grounded"
                    }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "Unscheduled",
                    "description": "Cabin pressurization warning sensor replaced.",
                    "status": "In Progress",
                    "technician_id": "TECH005",
                    "event_date": "2024-05-17",
                    "work_order_id": "WO-2024-05-17-ATL-CP1"
                }
            ),
            Action(
                name="update_flight_status",
                kwargs={
                    "flight_number": "HAT004",
                    "date": "2024-05-17",
                    "new_status": "DELAYED",
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "AOG_REPAIR",
                    "airport_id": "ARP_ATL",
                    "flight_number": "HAT004",
                    "date": "2024-05-17",
                    "details": "Aircraft AC001 returned to service after repair. Flight HAT004 on 2024-05-17 delayed due to unscheduled maintenance: Cabin pressurization warning sensor replaced."
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                    "aircraft_id": "AC001",
                    "new_status": "Active"
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_026",
        instruction="You are the Fleet Manager at ARP_PHX. To launch a new regional route, you need bring aircraft N-DXJ out of long-term storage on 2025-08-11. You need to execute the 'Return to Service Protocol' for this aircraft. The new flight will be HAT452 from PHX to SEA, with a schedule of 09:00:00 departure and 11:30:00 arrival. Use technician ID TECH015 and work order 'WO-2025-08-12-RTS-01' for the maintenance log. Finally, provide the log_id of the 'Return to Service Inspection' created.",
        actions=[
                Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={
                         "tail_number": "N-DXJ"
                    }
                ),
            Action(
                    name="create_flight",
                    kwargs={
                         "flight_number": "HAT452",
                         "origin": "PHX",
                         "destination": "SEA",
                         "scheduled_departure_time_est": "09:00:00",
                         "scheduled_arrival_time_est": "11:30:00"
                    }
            ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                         "aircraft_id": "AC016",
                         "new_status": "Maintenance"
                    }
            ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC016",
                        "maintenance_type": "Return to Service Inspection",
                        "description": "Return to Service inspection for flight operations.",
                        "technician_id": "TECH015",
                        "work_order_id": "WO-2025-08-12-RTS-01",
                        "event_date": "2025-08-11",
                        "status": "Completed"
                    }
                ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                         "aircraft_id": "AC016",
                         "new_status": "Active"
                    }
            ),
            Action(
                    name="get_airport_by_code",
                    kwargs={
                         "iata_code": "PHX"
                    }
            ),
            Action(
                    name="create_operational_event",
                    kwargs={
                         "event_type": "AIRCRAFT_ACTIVATED",
                         "airport_id": "ARP_PHX",
                         "details": "Aircraft AC016 (N-DXJ) activated from storage at PHX for new flight route HAT452."
                    }
            )
        ],
        outputs=[
            "ML026"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_027",
        instruction="You are a Schedule Planner. Due to a strategic fleet reallocation away from the East Coast, the HAT002 route from LGA to PHX is being suspended. You need to execute the 'Route Suspension Protocol' for all flights on this route for the dates May 17, 2024, and May 18, 2024 and provide a list of all cancelled reservation IDs.",        
        actions=[
                Action(
                    name="create_operational_event",
                    kwargs={
                         "event_type": "ROUTE_SUSPENSION",
                         "airport_id": "ARP_LGA",
                         "flight_number": "HAT002",
                         "details": "Route HAT002 (LGA-PHX) has been suspended. All flights from 2024-05-17 to 2024-05-18 are cancelled."
                    }
                ),
            Action(
                    name="update_flight_status",
                    kwargs={
                         "flight_number": "HAT002",
                         "date": "2024-05-17",
                         "new_status": "cancelled"
                    }
            ),
            Action(
                    name="find_reservations_by_flight",
                    kwargs={
                         "flight_number": "HAT002",
                         "date": "2024-05-17"
                    }
            ),
            Action(
                    name="update_reservation_status",
                    kwargs={
                         "reservation_id": "BU71UY",
                         "new_status": "CANCELLED_ROUTE_SUSPENSION"
                    }
            ),
            Action(
                    name="update_reservation_status",
                    kwargs={
                         "reservation_id": "CC80AJ",
                         "new_status": "CANCELLED_ROUTE_SUSPENSION"
                    }
            ),
            Action(
                    name="update_reservation_status",
                    kwargs={
                         "reservation_id": "HDUF3Q",
                         "new_status": "CANCELLED_ROUTE_SUSPENSION"
                    }
            ),
            Action(
                    name="update_flight_status",
                    kwargs={
                         "flight_number": "HAT002",
                         "date": "2024-05-18",
                         "new_status": "cancelled"
                    }
            ),
            Action(
                    name="find_reservations_by_flight",
                    kwargs={
                         "flight_number": "HAT002",
                         "date": "2024-05-18"
                    }
            ),
            Action(
                    name="update_reservation_status",
                    kwargs={
                         "reservation_id": "J3SAZF",
                         "new_status": "CANCELLED_ROUTE_SUSPENSION"
                    }
            )
        ],
        outputs=[
            "BU71UY",
            "CC80AJ",
            "HDUF3Q",
            "J3SAZF"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_028",
        instruction="You are the Customer Experience Manager at CLT. As a service recovery gesture for recent operational issues at the airport, you need to execute the 'Service Upgrade Protocol' for flight HAT015 to EWR on 2024-05-17. All passengers currently booked in 'basic_economy' are to be upgraded to 'economy' and provide the total number of passengers that were upgraded.",
        actions=[
            Action(
                    name="find_reservations_by_flight",
                    kwargs={
                         "flight_number": "HAT015",
                         "date": "2024-05-17"
                    }
            ),
            Action(
                name="update_reservation_details",
                kwargs={
                    "reservation_id": "RNL6HR",
                    "new_cabin": "economy",
                    "new_status": "Upgraded"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "RNL6HR",
                    "message": "SERVICE UPGRADE for reservation RNL6HR: As a valued customer, your booking for flight HAT015 has been upgraded to economy. Enjoy your flight!"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "PROMOTIONAL_UPGRADE",
                    "airport_id": "ARP_CLT",
                    "flight_number": "HAT015",
                    "date": "2024-05-17",
                    "details": "Promotional upgrade initiative applied to flight HAT015 on 2024-05-17. All basic_economy passengers upgraded."
                }
            )
        ],
        outputs=[
            "1"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_029",
        instruction="You are the Operations Controller at JFK. You need to execute the “Route Retiming Protocol” for flight HAT014 (JFK–MIA) on 2024-05-17, setting the new schedule to 18:20:00–21:20:00 and notifying reservation QS2N5D.",
        actions=[
            Action(
                name="create_operational_event",
                kwargs={"event_type": "SCHEDULE_CHANGE", "airport_id": "ARP_JFK", "flight_number": "HAT014", "date": "2024-05-17",
                        "details": "Route HAT014 (JFK-MIA) retiming process initiated. New schedule: 18:20:00-21:20:00."}
            ),
            Action(
                name="update_flight_schedule",
                kwargs={"flight_number": "HAT014", "flight_date": "2024-05-17",
                        "new_departure_time_est": "18:20:00", "new_arrival_time_est": "21:20:00", "reason_event_id": "OE026"}
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={"flight_number": "HAT014", "date": "2024-05-17"}
            ),
            Action(
                name="send_passenger_notification",
                kwargs={"reservation_id": "QS2N5D", "message": "FLIGHT UPDATE for reservation QS2N5D: Your flight HAT014 on 2024-05-17 has been rescheduled. New departure is 18:20:00 and new arrival is 21:20:00. We apologize for any inconvenience."}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_030",
        instruction="You are the Fleet Manager at MCO. Due to its age and high maintenance costs, you need permanently decommission aircraft G-E-RKI. You need to execute the 'Aircraft Decommissioning Protocol' for this aircraft as of August 11, 2025. The final maintenance log should be assigned to technician ID TECH003 with work order 'WO-2025-DECOM-002’. You need to also provide the event_id of the formal decommissioning event.",        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={
                    "tail_number": "G-E-RKI"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                    "aircraft_id": "AC015",
                    "new_status": "Decommissioned"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC015",
                    "maintenance_type": "Decommissioning",
                    "description": "Final log entry for aircraft decommissioning and permanent retirement from service.",
                    "status": "Completed",
                    "technician_id": "TECH003",
                    "event_date": "2025-08-11",
                    "work_order_id": "WO-2025-DECOM-002"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "AIRCRAFT_DECOMMISSIONED",
                    "airport_id": "ARP_MCO",
                    "details": "Aircraft AC015 (G-E-RKI), model E175, has been officially decommissioned and removed from the active fleet at MCO."
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Finance",
                    "message": "AIRCRAFT ALERT: Aircraft G-E-RKI (AC015) has been officially decommissioned. Please update all relevant asset and scheduling records."
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Scheduling",
                    "message": "AIRCRAFT ALERT: Aircraft G-E-RKI (AC015) has been officially decommissioned. Please update all relevant asset and scheduling records."
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "MRO_Planning",
                    "message": "AIRCRAFT ALERT: Aircraft G-E-RKI (AC015) has been officially decommissioned. Please update all relevant asset and scheduling records."
                }
            )
        ],
        outputs=[
            "OE026"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_031",
        instruction="You are the Fleet Safety Manager. A manufacturer service bulletin requires a mandatory inspection on our A320neo fleet. You need apply the 'Fleet Airworthiness Directive Protocol' to the active aircraft, PR-XBE and PR-YSH. Log the primary directive event against our main airport, ATL, using the date 2025-08-12. The maintenance must be assigned to technician TECH020, with work orders 'WO-AD-25-001' for PR-XBE and 'WO-AD-25-002' for PR-YSH. Finally, confirm the tail numbers of the aircraft that were processed under this directive.",
        actions=[
                Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "AIRWORTHINESS_DIRECTIVE",
                        "airport_id": "ARP_ATL",
                        "details": "FLEET DIRECTIVE ISSUED.",
                        "date": "2025-08-12"
                    }
                ),
            Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={
                        "tail_number": "PR-XBE"
                    }
                    ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                        "aircraft_id": "AC002",
                        "new_status": "Maintenance"
                    }
                    ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC002",
                        "maintenance_type": "Mandatory Inspection",
                        "description": "Mandatory Inspection per manufacturer service bulletin.",
                        "status": "In Progress",
                        "technician_id": "TECH020",
                        "event_date": "2025-08-12",
                        "work_order_id": "WO-AD-25-001"
                    }
                    ),
            Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={
                        "tail_number": "PR-YSH"
                    }
                    ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                        "aircraft_id": "AC010",
                        "new_status": "Maintenance"
                    }
                    ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC010",
                        "maintenance_type": "Mandatory Inspection",
                        "description": "Mandatory Inspection per manufacturer service bulletin.",
                        "status": "In Progress",
                        "technician_id": "TECH020",
                        "event_date": "2025-08-12",
                        "work_order_id": "WO-AD-25-002"
                    }
                    ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "MRO_Planning",
                        "message": "FLEET DIRECTIVE: All A320neo aircraft have been moved to Maintenance status for mandatory inspection."
                    }
                    ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Scheduling",
                        "message": "SCHEDULING ALERT: All A320neo aircraft are now in Maintenance status and unavailable for flight operations."
                    }
                    )
        ],
        outputs=[
            "PR-XBE",
            "PR-YSH"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_032",
        instruction="You are the Crew Compliance Officer. You need to execute the “Crew Certification Expiry Protocol” to audit the B787-9 certification for Liam Santos (EMP004) and the B737-800 certification for Mia Li (EMP001). Log a primary audit event for the ATL airport and provide the list of all operational event IDs created.",
        actions=[
            Action(
                name="find_crew_member",
                kwargs={
                    "employee_code": "EMP004"
                }
            ),
            Action(
                name="find_crew_certifications",
                kwargs={
                    "crew_member_id": "CM004",
                    "certification_code": "B787-9"
                }
            ),
            Action(
                name="update_crew_member_status",
                kwargs={
                    "crew_member_id": "CM004",
                    "new_status": "Training Required"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "CREW_CERT_EXPIRY",
                    "airport_id": "ARP_ATL",
                    "details": "Crew member CM004 (Liam Santos) flagged for certification B787-9 expiring on 2026-02-28. Status updated."
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Crew_Scheduling",
                    "message": "CERTIFICATION ALERT: Crew member CM004 (Liam Santos) requires attention for certification B787-9 (Expires: 2026-02-28). Status set to Training Required. Please update rosters and schedule training."
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Training",
                    "message": "CERTIFICATION ALERT: Crew member CM004 (Liam Santos) requires attention for certification B787-9 (Expires: 2026-02-28). Status set to Training Required. Please update rosters and schedule training."
                }
            ),
            Action(
                name="find_crew_member",
                kwargs={
                    "employee_code": "EMP001"
                }
            ),
            Action(
                name="find_crew_certifications",
                kwargs={
                    "crew_member_id": "CM001",
                    "certification_code": "B737-800"
                }
            ),
            Action(
                name="update_crew_member_status",
                kwargs={
                    "crew_member_id": "CM001",
                    "new_status": "Training Required"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "CREW_CERT_EXPIRY",
                    "airport_id": "ARP_ATL",
                    "details": "Crew member CM001 (Mia Li) flagged for certification B737-800 expiring on 2025-04-20. Status updated."
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Crew_Scheduling",
                    "message": "CERTIFICATION ALERT: Crew member CM001 (Mia Li) requires attention for certification B737-800 (Expires: 2025-04-20). Status set to Training Required. Please update rosters and schedule training."
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Training",
                    "message": "CERTIFICATION ALERT: Crew member CM001 (Mia Li) requires attention for certification B737-800 (Expires: 2025-04-20). Status set to Training Required. Please update rosters and schedule training."
                }
            )
        ],
        outputs=[
            "OE026",
            "OE027"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_033",
        instruction="You are the Maintenance Controller at MIA. The crew of aircraft PR-YJB has reported an inoperative component 'Entertainment System'. The aircraft is needed for service. You need to execute the “Maintenance Deferral and Logistics Protocol” citing MEL 44-10-01a. Log the deferral on 2025-08-12 with technician TECH011 and work order WO-2025-08-12-003, and provide the log_id of the new deferral maintenance log.",
        actions=[
                Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={"tail_number": "PR-YJB"}
                ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                         "aircraft_id": "AC007",
                         "maintenance_type": "Deferred",
                         "description": "Repair deferred per MEL 44-10-01a",
                         "status": "Deferred",
                         "technician_id": "TECH011",
                         "work_order_id": "WO-2025-08-12-003",
                         "event_date": "2025-08-12"
                    }
            ),
            Action(
                    name="create_operational_event",
                    kwargs={
                         "event_type": "MAINTENANCE_DEFERRAL",
                         "airport_id": "ARP_MIA",
                         "details": "A non-essential cabin defect on aircraft PR-YJB (AC007) has been deferred per MEL reference 44-10-01a. Aircraft remains in service."
                    }
            ),
            Action(
                    name="send_department_notification",
                    kwargs={
                         "department_name": "Logistics",
                         "message": "PARTS_REQUEST: Order and ship replacement parts for deferred defect on PR-YJB (AC007) to MIA. Ref Log: ML026."
                    }
            ),
            Action(
                    name="send_department_notification",
                    kwargs={
                         "department_name": "MRO_Planning",
                         "message": "DEFERRAL NOTICE: Defect on PR-YJB has been deferred per 44-10-01a. Please schedule final repair during next maintenance check."
                    }
            ),
            Action(
                    name="send_department_notification",
                    kwargs={
                         "department_name": "Flight_Dispatch",
                         "message": "AIRCRAFT STATUS: PR-YJB is operating with a deferred cabin defect (Entertainment System) under MEL 44-10-01a. No operational impact."
                    }
            ),
            Action(
                    name="send_department_notification",
                    kwargs={
                         "department_name": "Cabin_Services",
                         "message": "CABIN ALERT: Entertainment System on PR-YJB is inoperative and deferred. Please inform cabin crew."
                    }
            )
        ],
        outputs=["ML026"]
    ),
    Task(
        annotator="0",
        user_id="task_034",
        instruction="You are a Network Planner. Due to a major convention in Orlando, demand for flight HAT010 from ATL to MCO on May 18, 2024, has far exceeded the capacity of the scheduled ATR 72-600 aircraft. You need to execute the “Aircraft Upgauge Protocol” substituting the ATR 72-600 (PP-PTM) with the B737-800 (PR-GOL). Use technician TECH005 and work order WO-UPG-240518-01 for the pre-flight check, and provide the tail number of the new aircraft.",
        actions=[
                Action(
                    name="get_flight_by_number",
                    kwargs={"flight_number": "HAT010", "date": "2024-05-18"}
                ),
            Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={"tail_number": "PP-PTM"}
            ),
            Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={"tail_number": "PR-GOL"}
            ),
            Action(
                    name="update_aircraft_status",
                    kwargs={"aircraft_id": "AC008", "new_status": "Standby"}
            ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                         "aircraft_id": "AC001",
                         "maintenance_type": "Line Maintenance",
                         "description": "Pre-flight check for upgauge assignment of aircraft AC001 to flight HAT010.",
                         "status": "Completed",
                         "technician_id": "TECH005",
                         "event_date": "2024-05-18",
                         "work_order_id": "WO-UPG-240518-01"
                    }
            ),
            Action(
                    name="create_operational_event",
                    kwargs={
                         "event_type": "AIRCRAFT_UPGAUGE",
                         "airport_id": "ARP_ATL",
                         "details": "Aircraft AC008 on flight HAT010 is being replaced by larger model AC001 due to high passenger demand."
                    }
                    ),
            Action(
                    name="assign_aircraft_to_flight",
                    kwargs={
                         "aircraft_id": "AC001",
                         "flight_number": "HAT010",
                         "date": "2024-05-18"
                    }
            ),
            Action(
                    name="send_department_notification",
                    kwargs={
                         "department_name": "Scheduling",
                         "message": "OPERATIONAL UPDATE: Flight HAT010 on 2024-05-18 will now be operated by aircraft PR-GOL (AC001). Original aircraft PP-PTM is now on Standby at ATL."
                    }
            ),
            Action(
                    name="send_department_notification",
                    kwargs={
                         "department_name": "Flight_Dispatch",
                         "message": "AIRCRAFT CHANGE: Flight HAT010 on 2024-05-18 has been upgauged to B737-800 (PR-GOL). Update performance and weight/balance calculations."
                    }
            )
        ],
        outputs=["PR-GOL"]
    ),
    Task(
        annotator="0",
        user_id="task_035",
        instruction="You are a customer service agent processing a flight request for Evelyn Silva (evelyn.silva5743@example.com). She needs to book a one-way trip from New York (JFK) to Seattle (SEA) on 2024-05-20 in economy class with no insurance. She wants to find cheapest flight in economy class among one stop options. Per Protocol, her Silver status entitles her to two complimentary checked bags. She is traveling with three bags, so only one is chargeable at the standard fee of $35. Compute total cost from flight and bag. The full amount must be paid using her travel certificate, and the payment history must explicitly record this deduction from the certificate. You need to complete the booking using these rules. As a final confirmation, provide the ID of the new reservation.",
        actions=[
            Action(
                name="get_user_details",
                kwargs={
                    "user_email": "evelyn.silva5743@example.com"
                }
            ),
            Action(
                name="search_onestop_flight",
                kwargs={
                    "origin": "JFK",
                    "destination": "SEA",
                    "date": "2024-05-20"
                }
            ),
            Action(
                name="book_reservation",
                kwargs={
                    "user_id": "evelyn.silva5743",
                    "origin": "JFK",
                    "destination": "SEA",
                    "flight_type": "one_way",
                    "cabin": "economy",
                    "flights": [
                        {
                            "flight_number": "HAT268",
                            "date": "2024-05-20"
                        },
                        {
                            "flight_number": "HAT039",
                            "date": "2024-05-20"
                        }
                    ],
                    "passengers": [
                        {
                            "first_name": "Evelyn",
                            "last_name": "Silva",
                            "dob": "1979-02-23"
                        }
                    ],
                    "payment_methods": [
                        {
                            "payment_id": "certificate_3781045",
                            "amount": 239
                        }
                    ],
                    "total_baggages": 3,
                    "nonfree_baggages": 1,
                    "insurance": "no"
                }
            )
        ],
        outputs=[
            "RES0001"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_036",
        instruction="You are a customer service agent handling a request from Yusuf Thomas (yusuf.thomas4677@example.com) regarding his reservation RNL6HR for a trip from Charlotte to Newark on May 17, 2024. You want to find a later return flight for the same day or, if not possible, the earliest option on May 18. After you investigate and confirm that his basic economy ticket is non-changeable, you need to cancel the reservation, citing illness as the reason to leverage his travel insurance. As a final confirmation, provide the ID of the reservation that was cancelled.",
        actions=[
                Action(
                    name="get_user_details",
                    kwargs={
                        "user_email": "yusuf.thomas4677@example.com"
                    }
                ),
            Action(
                    name="get_reservation_details",
                    kwargs={
                        "reservation_id": "RNL6HR"
                    }
                    ),
            Action(
                    name="find_flights",
                    kwargs={
                        "origin": "CLT",
                        "destination": "EWR",
                        "departure_date": "2024-05-17",
                        "status": [
                            "available"
                        ]
                    }
                    ),
            Action(
                    name="find_flights",
                    kwargs={
                        "origin": "CLT",
                        "destination": "EWR",
                        "departure_date": "2024-05-18",
                        "status": [
                            "available"
                        ]
                    }
                    ),
            Action(
                    name="cancel_reservation",
                    kwargs={
                        "reservation_id": "RNL6HR"
                    }
                    )
        ],
        outputs=[
            "RNL6HR"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_037",
        instruction="You are a customer service agent assisting Aarav Anderson (aarav.anderson2369@example.com). You are facing financial difficulties and needs to downgrade his business class booking (reservation BU71UY) for flight HAT002 on May 17, 2024, to economy for all passengers. The flights and passengers must remain the same. Process the downgrade, calculate the total refund amount to be credited to his original payment method gift_card_5333120, and confirm the total savings as the final output.",
        actions=[
                Action(
                    name="get_user_details",
                    kwargs={
                        "user_email": "aarav.anderson2369@example.com"
                    }
                ),
            Action(
                    name="get_reservation_details",
                    kwargs={
                        "reservation_id": "BU71UY"
                    }
                    ),
            Action(
                    name="get_flight_by_number",
                    kwargs={
                        "flight_number": "HAT002",
                        "date": "2024-05-17"
                    }
                    ),
            Action(
                    name="calculate",
                    kwargs={
                        "expression": "(419 - 132) * 2"
                    }
                    ),
            Action(
                    name="update_reservation_flights",
                    kwargs={
                        "reservation_id": "BU71UY",
                        "cabin": "economy",
                        "flights": [
                            {
                                "flight_number": "HAT002",
                                "date": "2024-05-17"
                            }
                        ],
                        "payment_id": "gift_card_5333120"
                    }
                    )
        ],
        outputs=[
            "574"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_038",
        instruction="You are the Fleet Safety Manager at ARP_DFW. A manufacturer service bulletin has been issued requiring a mandatory inspection of the main landing gear hydraulic lines on the entire A320neo fleet. You need to execute the “Fleet Airworthiness Directive Protocol” for the fleet, grounding aircraft AC002 and AC010 on 2024-05-18. Use technician TECH008 with work orders WO-2024-05-18-001 and WO-2024-05-18-002 respectively, and provide the list of aircraft IDs grounded.",
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "AIRWORTHINESS_DIRECTIVE",
                    "airport_id": "ARP_DFW",
                    "date": "2024-05-18",
                    "details": "FLEET DIRECTIVE ISSUED."
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                    "aircraft_id": "AC002",
                    "new_status": "Maintenance"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC002",
                    "maintenance_type": "Mandatory Inspection",
                    "description": "Mandatory Inspection per manufacturer service bulletin.",
                    "status": "In Progress",
                    "technician_id": "TECH008",
                    "event_date": "2024-05-18",
                    "work_order_id": "WO-2024-05-18-001"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                    "aircraft_id": "AC010",
                    "new_status": "Maintenance"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC010",
                    "maintenance_type": "Mandatory Inspection",
                    "description": "Mandatory Inspection per manufacturer service bulletin.",
                    "status": "In Progress",
                    "technician_id": "TECH008",
                    "event_date": "2024-05-18",
                    "work_order_id": "WO-2024-05-18-002"
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "MRO_Planning",
                    "message": "FLEET DIRECTIVE: All A320neo aircraft have been moved to Maintenance status for mandatory inspection."
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Scheduling",
                    "message": "SCHEDULING ALERT: All A320neo aircraft are now in Maintenance status and unavailable for flight operations."
                }
            )
        ],
        outputs=[
            "AC002",
            "AC010"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_039",
        instruction="You are the gate agent for flight HAT004 to DFW on May 17, 2024. The boarding process is complete, but passenger James Thomas, associated with reservation 'KKKYCG', has failed to board. You need now execute the “Passenger No-Show Protocol” for reservation KKKYCG. Confirm completion by providing the event_id of the passenger offload event.",            actions=[
                Action(
                    name="get_flight_by_number",
                    kwargs={
                        "flight_number": "HAT004",
                        "date": "2024-05-17"
                    }
                ),
            Action(
                    name="find_reservation_by_code",
                    kwargs={
                        "reservation_code": "KKKYCG"
                    }
                    ),
            Action(
                    name="update_reservation_status",
                    kwargs={
                        "reservation_id": "KKKYCG",
                        "new_status": "NO_SHOW"
                    }
                    ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "PASSENGER_OFFLOAD",
                        "airport_id": "ARP_ATL",
                        "flight_number": "HAT004",
                        "date": "2024-05-17",
                        "details": "Passenger on reservation KKKYCG for flight HAT004 flagged as NO_SHOW. Initiating offload procedures."
                    }
                    ),
            Action(
                    name="send_ground_notification",
                    kwargs={
                        "airport_id": "ARP_ATL",
                        "priority": "HIGH",
                        "message": "URGENT BAGGAGE: Offload all bags for reservation KKKYCG from flight HAT004 immediately."
                    }
                    ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Revenue Management",
                        "message": "Reservation KKKYCG has been flagged as NO_SHOW for flight HAT004. Review for applicable fees."
                    }
                    ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Flight Dispatch",
                        "message": "Reservation KKKYCG has been flagged as NO_SHOW for flight HAT004. Review for applicable fees."
                    }
                    )
        ],
        outputs=[
            "OE026"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_040",
        instruction="You are the Operations Controller at LAS. Aircraft PR-GUO is AOG, affecting its scheduled flight HAT003 to DEN on May 16, 2024. You need to move the aircraft to our maintenance airport at DFW for repair by executing the 'AOG Ferry Recovery Protocol'. The ferry flight must be scheduled for a 23:00:00 departure, arriving at 02:00:00. For the maintenance logs, use technician 'TECH010', with work order 'WO-2024-05-16-415' for the AOG defect and 'WO-2024-05-16-416' for the ferry clearance. Provide the flight number of the newly created ferry flight as confirmation.",
        actions=[
                Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={
                        "tail_number": "PR-GUO"
                    }
                ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                        "aircraft_id": "AC009",
                        "new_status": "Grounded"
                    }
                    ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC009",
                        "maintenance_type": "Unscheduled",
                        "description": "Aircraft is AOG.",
                        "status": "In Progress",
                        "technician_id": "TECH010",
                        "event_date": "2024-05-16",
                        "work_order_id": "WO-2024-05-16-415"
                    }
                    ),
            Action(
                    name="update_flight_status",
                    kwargs={
                        "flight_number": "HAT003",
                        "date": "2024-05-16",
                        "new_status": "cancelled"
                    }
                    ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC009",
                        "maintenance_type": "Ferry Flight Clearance",
                        "description": "Maintenance clearance for non-revenue ferry flight under MEL.",
                        "status": "Completed",
                        "technician_id": "TECH010",
                        "event_date": "2024-05-16",
                        "work_order_id": "WO-2024-05-16-416"
                    }
                    ),
            Action(
                    name="create_flight",
                    kwargs={
                        "flight_number": "HAT9001",
                        "origin": "LAS",
                        "destination": "DFW",
                        "scheduled_departure_time_est": "23:00:00",
                        "scheduled_arrival_time_est": "02:00:00"
                    }
                    ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "AOG_FERRY",
                        "airport_id": "ARP_LAS",
                        "flight_number": "HAT9001",
                        "date": "2024-05-16",
                        "details": "AOG Recovery: Ferry flight HAT9001 created to move aircraft AC009 (PR-GUO) from LAS to DFW for maintenance."
                    }
                    ),
        ],
        outputs=[
            "HAT9001"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_041",
        instruction="You are the Fleet Manager at ARP_MIA. We have an AOG situation with aircraft PR-XTD due to 'Navigation System Failure', which was scheduled for flight HAT014 to JFK on May 18, 2024. The only available substitute is the smaller PR-YJB, forcing a downgrade. Please execute the 'Involuntary Downgrade Protocol' for the passenger on reservation 'QS2N5D'. Use technician 'TECH009' and work order 'WO-2024-05-18-811' for the maintenance log. As a final confirmation, please provide the reservation ID of the passenger whose booking status was changed.",        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={
                    "tail_number": "PR-XTD"
                }
            ),
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={
                    "tail_number": "PR-YJB"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                    "aircraft_id": "AC005",
                    "new_status": "Grounded"
                }
            ),
            Action(
                name="assign_aircraft_to_flight",
                kwargs={
                    "flight_number": "HAT014",
                    "date": "2024-05-18",
                    "new_aircraft_id": "AC007"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                    "reservation_id": "QS2N5D",
                    "new_status": "REBOOKED_DOWNGRADE"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC005",
                    "maintenance_type": "Unscheduled",
                    "description": "Aircraft is AOG.",
                    "status": "In Progress",
                    "technician_id": "TECH009",
                    "event_date": "2024-05-18",
                    "work_order_id": "WO-2024-05-18-811"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "INVOLUNTARY_DOWNGRADE",
                    "airport_id": "ARP_MIA",
                    "flight_number": "HAT014",
                    "date": "2024-05-18",
                    "details": "Aircraft downgrade on flight HAT014 from A350-900 to A220-300 due to maintenance. Rebooking required."
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "QS2N5D",
                    "message": "FLIGHT CHANGE NOTICE: Due to an aircraft substitution on flight HAT014, we could not accommodate your original booking. A service agent will contact you shortly to arrange rebooking. We apologize for the inconvenience. Ref: QS2N5D."
                }
            )
        ],
        outputs=[
            "QS2N5D"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_042",
        instruction="You are the Fleet Safety Manager at ARP_CLT. A safety bulletin has been issued requiring an urgent inspection of the elevator control system on all E175 aircraft. You need to execute the 'Fleet Airworthiness Directive Protocol' for the entire E175 fleet, which is comprised of IDs AC011 and AC015. The directive should be logged against the CLT airport for August 12, 2025. All maintenance must be assigned to technician 'TECH020', using work orders 'WO-AD-25-E175-AC011' and 'WO-AD-25-E175-AC015' for the respective aircraft. Provide a list of the tail numbers of the aircraft processed.",
        actions=[
                Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "AIRWORTHINESS_DIRECTIVE",
                        "airport_id": "ARP_CLT",
                        "date": "2025-08-12",
                        "details": "FLEET DIRECTIVE ISSUED."
                    }
                ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                        "aircraft_id": "AC011",
                        "new_status": "Maintenance"
                    }
                ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC011",
                        "maintenance_type": "Mandatory Inspection",
                        "description": "Mandatory Inspection per manufacturer service bulletin.",
                        "status": "In Progress",
                        "technician_id": "TECH020",
                        "event_date": "2025-08-12",
                        "work_order_id": "WO-AD-25-E175-AC011"
                    }
                ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                        "aircraft_id": "AC015",
                        "new_status": "Maintenance"
                    }
                ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC015",
                        "maintenance_type": "Mandatory Inspection",
                        "description": "Mandatory Inspection per manufacturer service bulletin.",
                        "status": "In Progress",
                        "technician_id": "TECH020",
                        "event_date": "2025-08-12",
                        "work_order_id": "WO-AD-25-E175-AC015"
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "MRO_Planning",
                        "message": "FLEET DIRECTIVE: All E175 aircraft have been moved to Maintenance status for mandatory inspection."
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Scheduling",
                        "message": "SCHEDULING ALERT: All E175 aircraft are now in Maintenance status and unavailable for flight operations."
                    }
                )
        ],
        outputs=[
            "PP-EJA",
            "G-E-RKI"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_043",
        instruction="You are a Route Planner. Due to a strategic network realignment, the decision has been made to permanently cease operations on the HAT015 route from CLT to EWR. You need to execute the 'Route Suspension Protocol' for all scheduled flights on this route for May 17 and May 18, 2024. All affected passengers are to be issued a standard $100 travel voucher as compensation.  For confirmation, provide the total number of reservations that were cancelled.",
        actions=[
                Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "ROUTE_SUSPENSION",
                        "airport_id": "ARP_CLT",
                        "details": "Route HAT015 (CLT-EWR) has been suspended. All flights from 2024-05-17 to 2024-05-18 are cancelled."
                    }
                ),
            Action(
                    name="update_flight_status",
                    kwargs={
                        "flight_number": "HAT015",
                        "date": "2024-05-17",
                        "new_status": "cancelled"
                    }
                ),
            Action(
                    name="update_flight_status",
                    kwargs={
                        "flight_number": "HAT015",
                        "date": "2024-05-18",
                        "new_status": "cancelled"
                    }
                ),
            Action(
                    name="find_reservations_by_flight",
                    kwargs={
                        "flight_number": "HAT015",
                        "date": "2024-05-17"
                    }
                ),
            Action(
                    name="find_reservations_by_flight",
                    kwargs={
                        "flight_number": "HAT015",
                        "date": "2024-05-18"
                    }
                ),
            Action(
                    name="update_reservation_status",
                    kwargs={
                        "reservation_id": "RNL6HR",
                        "new_status": "CANCELLED_ROUTE_SUSPENSION"
                    }
                ),
            Action(
                    name="send_passenger_notification",
                    kwargs={
                        "reservation_id": "RNL6HR",
                        "message": "FLIGHT CANCELLATION: Your flight HAT015 on 2024-05-17 has been cancelled due to a route suspension. A $100 travel voucher has been issued to your account."
                    }
                ),
            Action(
                    name="update_reservation_status",
                    kwargs={
                        "reservation_id": "4MB0L3",
                        "new_status": "CANCELLED_ROUTE_SUSPENSION"
                    }
                ),
            Action(
                    name="send_passenger_notification",
                    kwargs={
                        "reservation_id": "4MB0L3",
                        "message": "FLIGHT CANCELLATION: Your flight HAT015 on 2024-05-17 has been cancelled due to a route suspension. A $100 travel voucher has been issued to your account."
                    }
                ),
            Action(
                    name="update_reservation_status",
                    kwargs={
                        "reservation_id": "W8DUJ8",
                        "new_status": "CANCELLED_ROUTE_SUSPENSION"
                    }
                ),
            Action(
                    name="send_passenger_notification",
                    kwargs={
                        "reservation_id": "W8DUJ8",
                        "message": "FLIGHT CANCELLATION: Your flight HAT015 on 2024-05-18 has been cancelled due to a route suspension. A $100 travel voucher has been issued to your account."
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Finance",
                        "message": "FINANCE NOTICE: Route HAT015 suspended. Total of $300.00 in vouchers issued for 3 affected reservations."
                    }
                )
        ],
        outputs=[
            "3"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_044",
        instruction="You are the Maintenance Controller at MIA. The crew of aircraft PR-YJB has reported an inoperative component 'Galley Oven'. The aircraft is needed for its next service, so the defect must be deferred. You need to execute the 'Maintenance Deferral and Logistics Protocol', citing MEL reference 25-20-01a. Log the deferral on August 12, 2025, with technician TECH011 and work order 'WO-2025-08-12-005'. Finally, provide the log_id of the new 'Deferred' maintenance log.",
        actions=[
                Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={
                        "tail_number": "PR-YJB"
                    }
                ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC007",
                        "maintenance_type": "Deferred",
                        "description": "Repair deferred per MEL 25-20-01a",
                        "status": "Deferred",
                        "technician_id": "TECH011",
                        "work_order_id": "WO-2025-08-12-005",
                        "event_date": "2025-08-12"
                    }
                ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "MAINTENANCE_DEFERRAL",
                        "airport_id": "ARP_MIA",
                        "details": "A non-essential cabin defect on aircraft AC007 (PR-YJB) has been deferred per MEL reference 25-20-01a. Aircraft remains in service."
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "MRO_Planning",
                        "message": "DEFERRAL NOTICE: Defect on PR-YJB has been deferred per 25-20-01a. Please schedule final repair during next maintenance check."
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Logistics",
                        "message": "PARTS_REQUEST: Order and ship replacement parts for deferred defect on PR-YJB (AC007) to MIA. Ref Log: ML026."
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Flight_Dispatch",
                        "message": "AIRCRAFT STATUS: PR-YJB is operating with a deferred cabin defect (Galley Oven) under MEL 25-20-01a. No operational impact."
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Cabin_Services",
                        "message": "CABIN ALERT: Galley Oven on PR-YJB is inoperative and deferred. Please inform cabin crew."
                    }
                )
        ],
        outputs=[
            "ML026"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_045",
        instruction="You are the dispatcher at LAX. An active AOG situation affects flight HAT022 to DFW on May 18, 2024, involving aircraft PP-LTM. The aircraft required a repair, resulting in a 5-hour operational delay. You need to manage this event by executing the 'AOG Repair and Crew Compliance Protocol' for the assigned Captain, Liam Santos EMP004. Use technician 'TECH017' and work order 'WO-2024-05-18-LAX-01' for the maintenance log. As a final confirmation, provide the captain's final compliance status (True/False).",
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={
                    "tail_number": "PP-LTM"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                    "aircraft_id": "AC003",
                    "new_status": "Active"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC003",
                    "maintenance_type": "AOG_REPAIR",
                    "description": "Maintenance Completed",
                    "status": "Completed",
                    "technician_id": "TECH017",
                    "event_date": "2024-05-18",
                    "work_order_id": "WO-2024-05-18-LAX-01"
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                    "flight_number": "HAT022",
                    "flight_date": "2024-05-18",
                    "delay_hours": 5,
                    "new_status": "DELAYED"
                }
            ),
            Action(
                name="find_crew_member",
                kwargs={
                    "employee_code": "EMP004"
                }
            ),
            Action(
                name="verify_crew_duty_time",
                kwargs={
                    "crew_member_id": "CM004",
                    "reference_date": "2024-05-18"
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Flight_Dispatch",
                    "message": "AOG RECOVERY UPDATE: Aircraft PP-LTM is active after repair for flight HAT022. New ETD: 17:00:00. Crew member CM004 compliance check passed: True."
                }
            )
        ],
        outputs=[
            "True"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_046",
        instruction=(
                "You are the gate agent at ATL. Using the Passenger No-Show Protocol, you need to process a no-show for reservation "
                "KKKYCG on flight HAT004 dated 2024-05-17."
        ),
        actions=[
            Action(
                name="get_flight_by_number",
                kwargs={"flight_number": "HAT004", "date": "2024-05-17"}
            ),
            Action(
                name="find_reservation_by_code",
                kwargs={"reservation_code": "KKKYCG"}
            ),
            Action(
                name="update_reservation_status",
                kwargs={"reservation_id": "KKKYCG",
                        "new_status": "NO_SHOW"}
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "PASSENGER_OFFLOAD",
                    "airport_id": "ARP_ATL",
                    "flight_number": "HAT004",
                    "date": "2024-05-17",
                    "details": "Passenger on reservation KKKYCG for flight HAT004 flagged as NO_SHOW. Initiating offload procedures."
                }
            ),
            Action(
                name="send_ground_notification",
                kwargs={"airport_id": "ARP_ATL", "priority": "HIGH",
                        "message": "URGENT BAGGAGE: Offload all bags for reservation KKKYCG from flight HAT004 immediately."}
            ),
            Action(
                name="send_department_notification",
                kwargs={"department_name": "Revenue Management",
                        "message": "Reservation KKKYCG has been flagged as NO_SHOW for flight HAT004. Review for applicable fees."}
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Flight Dispatch",
                    "message": "Reservation KKKYCG has been flagged as NO_SHOW for flight HAT004. Review for applicable fees."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_047",
        instruction="You are the Operations Recovery Manager at SEA. Aircraft PR-GUO, currently located at LAS following a previous diversion, must be repositioned to its home base at SEA to meet operational needs. Please execute the 'Irregular Ops Recovery Protocol'. The objective is to create a non-revenue ferry flight for this aircraft for today, May 18, 2024. Use flight number HAT9002, scheduled to depart LAS at 15:00:00 and arrive at SEA at 17:30:00. Provide the event_id of the FERRY_FLIGHT_RECOVERY log as confirmation.",
        actions=[
                Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={
                        "tail_number": "PR-GUO"
                    }
                ),
            Action(
                    name="create_flight",
                    kwargs={
                        "flight_number": "HAT9002",
                        "origin": "LAS",
                        "destination": "SEA",
                        "scheduled_departure_time_est": "15:00:00",
                        "scheduled_arrival_time_est": "17:30:00"
                    }
                ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "FERRY_FLIGHT_RECOVERY",
                        "airport_id": "ARP_SEA",
                        "details": "Aircraft AC009 (PR-GUO) is being repositioned from LAS to SEA via ferry flight HAT9002 to resolve operational imbalance."
                    }
                ),
            Action(
                    name="update_aircraft_location",
                    kwargs={
                        "aircraft_id": "AC009",
                        "new_location_airport_id": "ARP_SEA"
                    }
                )
        ],
        outputs=[
            "OE026"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_048",
        instruction="You are a Service Recovery Agent. Flight HAT002 from LGA to PHX on May 18, 2024, has been cancelled due to an operational issue. You need to execute the 'Passenger Re-accommodation Protocol' for the user Sophia Taylor (email: sophia.taylor4639@example.com), who is on reservation 'J3SAZF' for this flight. You need to proactively rebook her and her travel party on the next available flight, which is HAT201 on May 19, 2024. Please provide the reservation_id of the new booking as confirmation.",        actions=[
            Action(
                    name="find_reservation_by_code",
                    kwargs={
                        "reservation_code": "J3SAZF"
                    }
            ),
            Action(
                name="update_reservation_details",
                kwargs={
                    "reservation_id": "J3SAZF",
                    "new_status": "REBOOKED"
                }
            ),
            Action(
                name="create_reservation",
                kwargs={
                    "user_email": "sophia.taylor4639@example.com",
                    "flight_details": [
                        {
                            "flight_number": "HAT201",
                            "date": "2024-05-19",
                            "origin": "LGA",
                            "destination": "PHX"
                        }
                    ],
                    "passengers": [
                        {
                            "first_name": "Sophia",
                            "last_name": "Taylor",
                            "dob": "1999-05-27"
                        },
                        {
                            "first_name": "Lucas",
                            "last_name": "Davis",
                            "dob": "1987-10-27"
                        },
                        {
                            "first_name": "Mason",
                            "last_name": "Khan",
                            "dob": "1983-09-06"
                        }
                    ],
                    "cabin": "business"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "RES0001",
                    "message": "REBOOKING CONFIRMATION: Following your original flight's cancellation, you have been rebooked on flight HAT201 on 2024-05-19. Your new reservation ID is RES0001."
                }
            )
        ],
        outputs=[
            "RES0001"
        ]
    ),
    Task(
        annotator="0",
        user_id="task_049",
        instruction="You are the Maintenance Operations lead at ORD. Aircraft PT-MUI, scheduled for flight HAT014 to JFK on May 17, 2024, has two reported defects: an 'engine bleed air fault' (critical) and an inoperative component 'cabin light' (non-critical). You need to return the aircraft to service with a 4-hour delay. You need to execute the MEL deferral protocl and 'AOG Repair with MEL Deferral' protocol. You know the critical fault is already repaired, while the light issue will be formally deferred per MEL 33-20-01. For the logs, use technician 'TECH009', work orders 'WO-240517-955' for the repair and 'WO-240517-956' for the deferral. Ensure the passenger on reservation 'QS2N5D' is notified of the delay (remember to use exact timestamps that are confirmed by update flight). Provide the final status of the aircraft as confirmation.",
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={"tail_number": "PT-MUI"}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": "AC006",
                        "new_status": "Active - MEL Deferred"}
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC006",
                    "maintenance_type": "Deferred",
                    "description": "cabin light inoperative. Repair deferred per MEL 33-20-01.",
                    "status": "Deferred",
                    "technician_id": "TECH009",
                    "event_date": "2024-05-17",
                    "work_order_id": "WO-240517-956"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "AOG_REPAIR",
                    "airport_id": "ARP_ORD",
                    "details": "Aircraft AC006 returned to service after repair of engine bleed air fault. Flight HAT014 on 2024-05-17 delayed. Non-critical defect (inoperative cabin light) deferred per MEL."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                    "flight_number": "HAT014",
                    "flight_date": "2024-05-17",
                    "delay_hours": 4,
                    "new_status": "DELAYED"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "QS2N5D",
                    "message": "FLIGHT UPDATE for reservation QS2N5D: Your flight HAT014 on 2024-05-17 has been rescheduled. New departure is 2024-05-17T21:00:00 and new arrival is 2024-05-18T00:00:00. We apologize for any inconvenience."
                }
            )
        ],
        outputs=["Active - MEL Deferred"]
    ),
    Task(
        annotator="0",
        user_id="task_050",
        instruction="You are the Customer Experience Manager at ARP_LGA. Flight HAT002 to ARP_PHX on May 15, 2024, experienced a significant delay. As a gesture of goodwill, you need to execute the 'Service Recovery Compensation Protocol' for the following reservations 'LWTEDF', 'J3SAZF', '9EUD4C' and 'NQ4Y0O'. For confirmation, please provide the event_id of the service recovery log.",
        actions=[
            Action(
                    name="find_reservations_by_flight",
                    kwargs={
                        "flight_number": "HAT002",
                        "date": "2024-05-15"
                    }
            ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "SERVICE_RECOVERY",
                        "airport_id": "ARP_LGA",
                        "details": "SERVICE RECOVERY INITIATED: Compensation issued for flight HAT002 on 2024-05-15 due to significant delay.",
                        "flight_number": "HAT002",
                        "date": "2024-05-15"
                    }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "LWTEDF",
                    "message": "We apologize for the significant delay on your recent flight HAT002. A travel credit has been issued to your account as a gesture of goodwill."
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "J3SAZF",
                    "message": "We apologize for the significant delay on your recent flight HAT002. A travel credit has been issued to your account as a gesture of goodwill."
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "9EUD4C",
                    "message": "We apologize for the significant delay on your recent flight HAT002. A travel credit has been issued to your account as a gesture of goodwill."
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "NQ4Y0O",
                    "message": "We apologize for the significant delay on your recent flight HAT002. A travel credit has been issued to your account as a gesture of goodwill."
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Finance",
                    "message": "FINANCE NOTICE: Service recovery credits have been issued for all passengers on flight HAT002 (2024-05-15). Please process."
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Loyalty",
                    "message": "LOYALTY NOTICE: Service recovery credits issued for passengers on flight HAT002 (2024-05-15). Please update member accounts accordingly."
                }
            ),
            Action(
                name="send_ground_notification",
                kwargs={
                    "airport_id": "ARP_LGA",
                    "priority": "NORMAL",
                    "message": "STATION NOTICE: Service recovery compensation issued for passengers on flight HAT002 which operated from/to your station."
                }
            ),
            Action(
                name="send_ground_notification",
                kwargs={
                    "airport_id": "ARP_PHX",
                    "priority": "NORMAL",
                    "message": "STATION NOTICE: Service recovery compensation issued for passengers on flight HAT002 which operated from/to your station."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_051",
        instruction="You are a Network Planner. Demand for flight HAT010 from ATL to MCO on May 18, 2024, has significantly exceeded capacity. Your goal is to substitute the currently scheduled aircraft with a larger one by executing the 'Aircraft Upgauge Protocol'. The original aircraft is PP-PTM (ATR 72-600), which must be placed on Standby. The new, larger aircraft will be PR-GOL (B737-800), which is available at ARP_ATL. You need log a mandatory pre-flight Line Maintenance check for the new aircraft with technician 'TECH005' and work order 'WO-UPG-240518-01'. Ensure both Scheduling and Flight Dispatch are notified using their specific, deterministic message templates. As a final output, provide the log_id for the new maintenance check.",
        actions=[
                Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={"tail_number": "PP-PTM"}
                ),
            Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={"tail_number": "PR-GOL"}
                ),
            Action(
                    name="update_aircraft_status",
                    kwargs={"aircraft_id": "AC008", "new_status": "Standby"}
                ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC001",
                        "maintenance_type": "Line Maintenance",
                        "description": "Pre-flight check for upgauge assignment of aircraft AC001 to flight HAT010.",
                        "status": "Completed",
                        "technician_id": "TECH005",
                        "event_date": "2024-05-18",
                        "work_order_id": "WO-UPG-240518-01"
                    }
                ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "AIRCRAFT_UPGAUGE",
                        "airport_id": "ARP_ATL",
                        "details": "Aircraft AC008 on flight HAT010 is being replaced by larger model AC001 due to high passenger demand."
                    }
                ),
            Action(
                    name="assign_aircraft_to_flight",
                    kwargs={
                        "flight_number": "HAT010",
                        "date": "2024-05-18",
                        "new_aircraft_id": "AC001"
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Scheduling",
                        "message": "OPERATIONAL UPDATE: Flight HAT010 on 2024-05-18 will now be operated by aircraft PR-GOL (AC001). Original aircraft PP-PTM is now on Standby at ATL."
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Flight_Dispatch",
                        "message": "AIRCRAFT CHANGE: Flight HAT010 on 2024-05-18 has been upgauged to B737-800 (PR-GOL). Update performance and weight/balance calculations."
                    }
                )
        ],
        outputs=["ML026"]
    ),
    Task(
        annotator="0",
        user_id="task_052",
        instruction="You are a Crew Scheduler at MIA. You urgently need a Captain for flight HAT008 to LAX on May 18, 2024, which operates on a B787-9 aircraft. You are considering assigning Captain Mia Li (employee code EMP001). You need to validate her suitability by executing the 'Crew Staffing Validation Protocol'. You need verify both her duty time compliance and if it holds the required B787-9 type-rating. The validation event must belogged against the flight's origin airport. If the validation fails, you need log the failure and notify Crew Scheduling. As a final output, provide the reason for the validation failure.",
        actions=[
                Action(
                    name="get_flight_by_number",
                    kwargs={"flight_number": "HAT008", "date": "2024-05-18"}
                ),
            Action(
                    name="get_airport_by_code",
                    kwargs={"iata_code": "MIA"}
                ),
            Action(
                    name="find_crew_member",
                    kwargs={"employee_code": "EMP001"}
                ),
            Action(
                    name="find_crew_certifications",
                    kwargs={"crew_member_id": "CM001",
                            "certification_code": "B787-9"}
                ),
            Action(
                    name="verify_crew_duty_time",
                    kwargs={"crew_member_id": "CM001",
                            "reference_date": "2024-05-18"}
                ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "CREW_VALIDATION_FAILED",
                        "airport_id": "ARP_MIA",
                        "flight_number": "HAT008",
                        "date": "2024-05-18",
                        "details": "Crew member CM001 validation failed for flight HAT008 on 2024-05-18."
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Crew_Scheduling",
                        "message": "STAFFING ALERT: Validation for crew member CM001 on flight HAT008 failed."
                    }
                )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_053",
        instruction="You are a Crew Scheduler at MIA. You urgently need a Captain for flight HAT008 to LAX on May 18, 2024, which operates on a B787-9 aircraft. You are considering assigning Captain Mia Li (employee code EMP001). You need to validate her suitability by executing the 'Crew Staffing Validation Protocol'. You need verify both her duty time compliance and if she holds the required B787-9 type-rating. The validation event must be logged against the flight's origin airport. If the validation fails, you need log the failure and notify Crew Scheduling.",
        actions=[
                Action(
                    name="get_flight_by_number",
                    kwargs={"flight_number": "HAT008", "date": "2024-05-18"}
                ),
            Action(
                    name="get_airport_by_code",
                    kwargs={"iata_code": "MIA"}
                ),
            Action(
                    name="find_crew_member",
                    kwargs={"employee_code": "EMP001"}
                ),
            Action(
                    name="find_crew_certifications",
                    kwargs={"crew_member_id": "CM001",
                            "certification_code": "B787-9"}
                ),
            Action(
                    name="verify_crew_duty_time",
                    kwargs={"crew_member_id": "CM001",
                            "reference_date": "2024-05-18"}
                ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "CREW_VALIDATION_FAILED",
                        "airport_id": "ARP_MIA",
                        "flight_number": "HAT008",
                        "date": "2024-05-18",
                        "details": "Crew member CM001 validation failed for flight HAT008 on 2024-05-18."
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Crew_Scheduling",
                        "message": "STAFFING ALERT: Validation for crew member CM001 on flight HAT008 failed."
                    }
                )
        ],
        outputs=[""]
    ),
    Task(
        annotator="0",
        user_id="task_054",
        instruction="You are a Baggage Service Agent at DFW. Gold member Evelyn Johnson (velyn.johnson2294@example.com) has arrived from flight HAT004 on May 16, 2024, and reported her bag missing from reservation 'BMZ6Y9'. You need to execute the 'Lost Baggage Recovery and Compensation Protocol'. Confirm the task by providing the newly generated baggage claim ID.",
        actions=[
                Action(name="find_reservation_by_code",
                       kwargs={"reservation_code": "BMZ6Y9"}),
                Action(name="get_user_details", kwargs={
                       "user_email": "evelyn.johnson2294@example.com"}),
                Action(name="get_flight_by_number", kwargs={
                       "flight_number": "HAT004", "date": "2024-05-16"}),
                Action(name="get_airport_by_code",
                       kwargs={"iata_code": "ATL"}),
                Action(name="get_airport_by_code",
                       kwargs={"iata_code": "DFW"}),
                Action(name="create_operational_event", kwargs={
                    "event_type": "BAGGAGE_MISHANDLING", "airport_id": "ARP_DFW",
                    "details": "Lost baggage claim initiated for reservation BMZ6Y9. Claim ID: BCLAIM_BMZ6Y9_HAT004.",
                    "flight_number": "HAT004",
                    "date": "2024-05-16"
                }),
            Action(name="update_reservation_details", kwargs={
                "reservation_id": "BMZ6Y9", "new_status": "BAGGAGE_CLAIM_OPEN"}),
            Action(name="send_ground_notification", kwargs={
                "airport_id": "ARP_ATL", "priority": "HIGH",
                "message": "BAGGAGE ALERT: Initiate search for lost baggage for passenger Evelyn Johnson on flight HAT004 (ATL-DFW). Reservation BMZ6Y9."
            }),
            Action(name="send_ground_notification", kwargs={
                "airport_id": "ARP_DFW", "priority": "HIGH",
                "message": "BAGGAGE ALERT: Initiate search for lost baggage for passenger Evelyn Johnson on flight HAT004 (ATL-DFW). Reservation BMZ6Y9."
            }),
            Action(name="send_passenger_notification", kwargs={
                "reservation_id": "BMZ6Y9",
                "message": "BAGGAGE CLAIM FILED: Your claim BCLAIM_BMZ6Y9_HAT004 has been filed for your lost baggage on reservation BMZ6Y9. We will contact you with updates."
            }),
            Action(name="send_certificate", kwargs={
                "user_email": "evelyn.johnson2294@example.com", "amount": 100})
        ],
        outputs=["BCLAIM_BMZ6Y9_HAT004"]
    ),
    Task(
        annotator="0",
        user_id="task_055",
        instruction="You are the Operations Manager at DFW. A 'Severe Thunderstorm' is approaching, effective on May 17, 2024. You need to execute a strategic override of the 'Severe Weather Protocol'. You need to mitigate impact by diverting the long-haul flight HAT022 from LAX to DEN, with a new estimated arrival of 18:30:00. You need also cancel the short-haul flight HAT004 from ATL. Ensure all affected passengers on both flights (reservations 'HVU16N' and 'KKKYCG' respectively) are informed of their status changes using the correct deterministic templates. Provide the event_id for the primary weather event as confirmation.",
        actions=[
                Action(name="create_operational_event", kwargs={
                    "event_type": "SIGMET", "airport_id": "ARP_DFW", "date": "2024-05-17",
                    "details": "Severe Weather Protocol initiated."
                }),
            Action(name="update_flight_schedule", kwargs={
                "flight_number": "HAT022", "flight_date": "2024-05-17", "new_status": "Diverted", "new_arrival_time_est": "18:30:00", "reason_event_id": "OE026"}),
            Action(name="get_airport_by_code",
                   kwargs={"iata_code": "DEN"}),
            Action(name="find_reservations_by_flight", kwargs={
                "flight_number": "HAT022", "date": "2024-05-17"}),
            Action(name="find_reservations_by_flight", kwargs={
                "flight_number": "HAT004", "date": "2024-05-17"}),
            Action(name="send_passenger_notification", kwargs={
                "reservation_id": "HVU16N", "message": "FLIGHT DIVERSION NOTICE: Due to severe weather, your flight HAT022 on 2024-05-17 has been diverted to DEN."}),
            Action(name="update_flight_status", kwargs={
                "flight_number": "HAT004", "date": "2024-05-17", "new_status": "cancelled"}),
            Action(name="update_reservation_status", kwargs={
                "reservation_id": "KKKYCG", "new_status": "CANCELLED_WEATHER"}),
            Action(name="send_passenger_notification", kwargs={
                "reservation_id": "KKKYCG", "message": "FLIGHT CANCELLATION NOTICE: Due to severe weather, your flight HAT004 on 2024-05-17 has been cancelled."})
        ],
        outputs=["OE026"]
    ),
    Task(
        annotator="0",
        user_id="task_056",
        instruction="You are the Operations Controller at PHX. You need to provide a Medical Assistance for a passenger following the standard medical alert policy, The passenger is Sophia Taylor on flight HAT002 on 2024-05-18 at ARP_PHX. Send a HIGH-priority alert to the PHX ground team.",
        actions=[
            Action(
                name="get_flight_by_number",
                kwargs={"flight_number": "HAT002", "date": "2024-05-18"}
            ),
            Action(
                name="get_airport_by_code",
                kwargs={"iata_code": "PHX"}
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "MEDICAL_ASSISTANCE",
                    "airport_id": "ARP_PHX",
                    "flight_number": "HAT002",
                    "date": "2024-05-18",
                    "details": "Medical assistance requested for passenger Sophia Taylor on flight HAT002 upon arrival at PHX."
                }
            ),
            Action(
                name="send_ground_notification",
                kwargs={
                    "airport_id": "ARP_PHX",
                    "priority": "HIGH",
                    "message": "MEDICAL ALERT: Flight HAT002 arriving from LGA requires immediate medical assistance for passenger Sophia Taylor at the gate. Awaiting arrival."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_057",
        instruction=(
                "You are the Operations Manager at DFW. Using the Severe Weather Protocol, you need to record a SIGMET event at "
                "ARP_DFW for 2024-05-17, divert flight HAT022 to DEN with status Diverted and an updated arrival of 18:30:00, and "
                "notify reservation HVU16N."
        ),
        actions=[
            Action(
                name="create_operational_event",
                kwargs={"event_type": "SIGMET",
                        "airport_id": "ARP_DFW",
                        "details": "Severe Weather Protocol initiated.",
                        "date": "2024-05-17"}
            ),
            Action(
                name="update_flight_schedule",
                kwargs={"flight_number": "HAT022", "flight_date": "2024-05-17",
                        "new_status": "Diverted", "new_arrival_time_est": "18:30:00", "reason_event_id": "OE026"}
            ),
            Action(
                name="send_passenger_notification",
                kwargs={"reservation_id": "HVU16N",
                        "message": "FLIGHT DIVERSION NOTICE: Due to severe weather, your flight HAT022 on 2024-05-17 has been diverted to DEN."}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_058",
        instruction="You are the Fleet Manager at ATL. The aircraft PR-GOL (B737-800) scheduled for flight HAT004 to DFW on May 17, 2024, is now AOG due to a 'Hydraulic Issue'. The only available substitute is the smaller A220-300, tail number G-E-SKM. This aircraft change necessitates a downgrade. You need to execute the 'Involuntary Downgrade Protocol'. The passenger on reservation 'KKKYCG' must be downgraded. Log the maintenance event with technician 'TECH005' and work order 'WO-240518-HYD-01'.",
        actions=[
                Action(name="get_aircraft_by_tail_number",
                       kwargs={"tail_number": "PR-GOL"}),
                Action(name="get_aircraft_by_tail_number",
                       kwargs={"tail_number": "G-E-SKM"}),
                Action(name="update_aircraft_status", kwargs={
                       "aircraft_id": "AC001", "new_status": "Grounded"}),
                Action(name="assign_aircraft_to_flight", kwargs={
                       "flight_number": "HAT004", "date": "2024-05-17", "new_aircraft_id": "AC025"}),
                Action(name="create_maintenance_log", kwargs={
                    "aircraft_id": "AC001", "maintenance_type": "Unscheduled", "description": "Aircraft is AOG.", "status": "In Progress", "technician_id": "TECH005", "event_date": "2024-05-17", "work_order_id": "WO-240518-HYD-01"
                }),
            Action(name="create_operational_event", kwargs={"event_type": "INVOLUNTARY_DOWNGRADE", "airport_id": "ARP_ATL", "flight_number": "HAT004",
                                                            "date": "2024-05-17", "details": "Aircraft downgrade on flight HAT004 from B737-800 to A220-300 due to maintenance. Rebooking required."}),
            Action(name="find_reservations_by_flight", kwargs={
                "flight_number": "HAT004", "date": "2024-05-17"}),
            Action(name="update_reservation_status", kwargs={
                "reservation_id": "KKKYCG", "new_status": "REBOOKED_DOWNGRADE"}),
            Action(name="send_passenger_notification", kwargs={
                "reservation_id": "KKKYCG", "message": "FLIGHT CHANGE NOTICE: Due to an aircraft substitution on flight HAT004, we could not accommodate your original booking. A service agent will contact you shortly to arrange rebooking. We apologize for the inconvenience. Ref: KKKYCG."})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_059",
        instruction=(
                "You are the Operations Controller at ARP_LGA. Using the Route Retiming Protocol, you need to record a SCHEDULE_CHANGE at "
                "ARP_LGA for flight HAT002 (LGA-PHX) on 2024-05-17 with details 'Route HAT002 (LGA-PHX) retiming process initiated. New schedule: 22:30:00-03:00:00.', adjust the schedule to a new departure of 22:30:00 and a new arrival of "
                "03:00:00 on the following calendar day (explicitly next day), and notify the impacted reservation BU71UY."
        ),
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "SCHEDULE_CHANGE",
                    "airport_id": "ARP_LGA",
                    "flight_number": "HAT002",
                    "date": "2024-05-17",
                    "details": "Route HAT002 (LGA-PHX) retiming process initiated. New schedule: 22:30:00-03:00:00."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={"flight_number": "HAT002",
                        "flight_date": "2024-05-17",
                        "new_arrival_date": "2024-05-18",
                        "new_departure_time_est": "22:30:00",
                        "new_arrival_time_est": "03:00:00",
                        "reason_event_id": "OE026"}
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={"flight_number": "HAT002", "date": "2024-05-17"}
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "BU71UY",
                    "message": "FLIGHT UPDATE for reservation BU71UY: Your flight HAT002 on 2024-05-17 has been rescheduled. New departure is 22:30:00 and new arrival is 03:00:00. We apologize for any inconvenience."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_060",
        instruction=(
                "You are the Operations Controller at ARP_ATL. Using the Gate Conflict Resolution Protocol, you need to record a gate conflict "
                "for flight HAT004 on 2024-05-16, move the flight to gate C25 with a 15-minute incremental "
                "delay and status DELAYED, alert ground staff at ARP_ATL with HIGH priority, and notify reservations D975WV and BMZ6Y9."
        ),
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "GATE_CONFLICT",
                    "airport_id": "ARP_ATL",
                    "flight_number": "HAT004",
                    "date": "2024-05-16",
                    "details": "Gate conflict for flight HAT004. Reassigning gate C25 with 15-minute delay for passenger movement."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={"flight_number": "HAT004", "flight_date": "2024-05-16",
                        "new_gate": "C25", "delay_minutes": 15, "new_status": "DELAYED", "reason_event_id": "OE026"}
            ),
            Action(
                name="send_ground_notification",
                kwargs={"airport_id": "ARP_ATL", "priority": "HIGH",
                        "message": "GATE CHANGE ALERT: Flight HAT004 has been reassigned to Gate C25. Update all systems and signage immediately."}
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={"flight_number": "HAT004", "date": "2024-05-16"}
            ),
            Action(
                name="send_passenger_notification",
                kwargs={"reservation_id": "D975WV", "message": "FLIGHT UPDATE for reservation D975WV: Your flight HAT004 on 2024-05-16 has a new gate C25 and a 15-minute delay. We apologize for any inconvenience."}
            ),
            Action(
                name="send_passenger_notification",
                kwargs={"reservation_id": "BMZ6Y9", "message": "FLIGHT UPDATE for reservation BMZ6Y9: Your flight HAT004 on 2024-05-16 has a new gate C25 and a 15-minute delay. We apologize for any inconvenience."}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_061",
        instruction=(
                "You are the dispatcher at LAX. You need to apply the AOG Repair and Crew Compliance Protocol to aircraft PP-LTM for flight "
                "HAT022 on 2024-05-18, you need to update the flight status to DELAYED, document the repair completion under TECH017 with work order WO-2024-05-18-LAX-01, "
                "reflect a 5-hour delay. You also need to verify captain CM004 duty-time compliance for 2024-05-18."
        ),
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={"tail_number": "PP-LTM"}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": "AC003",
                        "new_status": "Active"}
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC003",
                    "maintenance_type": "AOG_REPAIR",
                    "description": "Maintenance Completed",
                    "status": "Completed",
                    "technician_id": "TECH017",
                    "event_date": "2024-05-18",
                    "work_order_id": "WO-2024-05-18-LAX-01"
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={"flight_number": "HAT022", "flight_date": "2024-05-18",
                        "delay_hours": 5, "new_status": "DELAYED"}
            ),
            Action(
                name="find_crew_member",
                kwargs={"employee_code": "EMP004"}
            ),
            Action(
                name="verify_crew_duty_time",
                kwargs={"crew_member_id": "CM004",
                        "reference_date": "2024-05-18"}
            ),
            Action(
                name="send_department_notification",
                kwargs={"department_name": "Flight_Dispatch",
                        "message": "AOG RECOVERY UPDATE: Aircraft PP-LTM is active after repair for flight HAT022. New ETD: 17:00:00. Crew member CM004 compliance check passed: True."}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_062",
        instruction=(
                "You are the Customer Experience Manager at ARP_CLT. Using the Service Upgrade Protocol, you need to apply a goodwill "
                "PROMOTIONAL_UPGRADE upgrade on flight HAT015 for 2024-05-18: update reservation W8DUJ8 and AH5UQZ from basic_economy to economy with status Upgraded."
        ),
        actions=[
            Action(
                name="get_flight_by_number",
                kwargs={"flight_number": "HAT015", "date": "2024-05-18"}
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={"flight_number": "HAT015", "date": "2024-05-18"}
            ),
            Action(
                name="update_reservation_details",
                kwargs={"reservation_id": "W8DUJ8",
                        "new_cabin": "economy", "new_status": "Upgraded"}
            ),
            Action(
                name="update_reservation_details",
                kwargs={"reservation_id": "AH5UQZ",
                        "new_cabin": "economy", "new_status": "Upgraded"}
            ),
            Action(
                name="send_passenger_notification",
                kwargs={"reservation_id": "W8DUJ8", "message": "SERVICE UPGRADE for reservation W8DUJ8: As a valued customer, your booking for flight HAT015 has been upgraded to economy. Enjoy your flight!"}
            ),
            Action(
                name="send_passenger_notification",
                kwargs={"reservation_id": "AH5UQZ", "message": "SERVICE UPGRADE for reservation AH5UQZ: As a valued customer, your booking for flight HAT015 has been upgraded to economy. Enjoy your flight!"}
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "PROMOTIONAL_UPGRADE",
                    "airport_id": "ARP_CLT",
                    "details": "Promotional upgrade initiative applied to flight HAT015 on 2024-05-18. All basic_economy passengers upgraded."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_063",
        instruction="You are a Network Planner. Due to a major convention in Orlando, demand for flight HAT010 from ATL to MCO on May 18, 2024, has far exceeded the capacity of the scheduled ATR 72-600 aircraft (PP-PTM). You need to execute the 'Aircraft Upgauge Protocol' to substitute a larger aircraft. Assign the B737-800 with tail number PR-GOL, which is available at ATL, to operate this flight. Use technician TECH005 and work order WO-UPG-240518-01 for the mandatory Line Maintenance pre-flight check and notify Scheduling and Flight_Dispatch. Provide the tail number of the new, larger aircraft assigned to the flight.",
        actions=[
                Action(name="get_flight_by_number", kwargs={
                       "flight_number": "HAT010", "date": "2024-05-18"}),
                Action(name="get_aircraft_by_tail_number",
                       kwargs={"tail_number": "PP-PTM"}),
                Action(name="get_aircraft_by_tail_number",
                       kwargs={"tail_number": "PR-GOL"}),
                Action(name="update_aircraft_status", kwargs={
                       "aircraft_id": "AC008", "new_status": "Standby"}),
                Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC001",
                        "maintenance_type": "Line Maintenance",
                        "description": "Pre-flight check for upgauge assignment of aircraft AC001 to flight HAT010.",
                        "status": "Completed",
                        "technician_id": "TECH005",
                        "event_date": "2024-05-18",
                        "work_order_id": "WO-UPG-240518-01"
                    }
                ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "AIRCRAFT_UPGAUGE",
                        "airport_id": "ARP_ATL",
                        "details": "Aircraft AC008 on flight HAT010 is being replaced by larger model AC001 due to high passenger demand."
                    }
                ),
            Action(name="assign_aircraft_to_flight", kwargs={
                "flight_number": "HAT010", "date": "2024-05-18", "new_aircraft_id": "AC001"}),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Scheduling",
                        "message": "OPERATIONAL UPDATE: Flight HAT010 on 2024-05-18 will now be operated by aircraft PR-GOL (AC001). Original aircraft PP-PTM is now on Standby at PHX."
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Flight_Dispatch",
                        "message": "AIRCRAFT CHANGE: Flight HAT010 on 2024-05-18 has been upgauged to B737-800 (PR-GOL). Update performance and weight/balance calculations."
                    }
                )
        ],
        outputs=["PR-GOL"]
    ),
    Task(
        annotator="0",
        user_id="task_064",
        instruction="You are the Operations Manager at ARP_ATL. A 'faulty baggage loader' has caused a significant ground service failure, resulting in a 5-hour delay for flight HAT004 to DFW on May 16, 2024. You need to manage this service disruption, which includes executing the 'Service Recovery Compensation Protocol' for all affected passengers on reservations 'MLPSXM', 'D975WV' and 'BMZ6Y9'. The priority of ground notification is NORMAL and Finance and Loyalty also needs to be notified. Provide the ID of the primary operational event logging the initial ground failure as confirmation.",
        actions=[
            Action(
                name="find_reservations_by_flight",
                kwargs={
                    "flight_number": "HAT004",
                    "date": "2024-05-16"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "SERVICE_RECOVERY",
                    "airport_id": "ARP_ATL",
                    "details": "SERVICE RECOVERY INITIATED: Compensation issued for flight HAT004 on 2024-05-16 due to significant delay.",
                    "flight_number": "HAT004",
                    "date": "2024-05-16"
                }
            ),
            Action(name="send_passenger_notification", kwargs={
                "reservation_id": "MLPSXM", "message": "We apologize for the significant delay on your recent flight HAT004. A travel credit has been issued to your account as a gesture of goodwill."}),
            Action(name="send_passenger_notification", kwargs={
                "reservation_id": "D975WV", "message": "We apologize for the significant delay on your recent flight HAT004. A travel credit has been issued to your account as a gesture of goodwill."}),
            Action(name="send_passenger_notification", kwargs={
                "reservation_id": "BMZ6Y9", "message": "We apologize for the significant delay on your recent flight HAT004. A travel credit has been issued to your account as a gesture of goodwill."}),
            Action(name="send_department_notification", kwargs={
                "department_name": "Finance", "message": "FINANCE NOTICE: Service recovery credits have been issued for all passengers on flight HAT004 (2024-05-16). Please process."}),
            Action(name="send_department_notification", kwargs={
                "department_name": "Loyalty", "message": "LOYALTY NOTICE: Service recovery credits issued for passengers on flight HAT004 (2024-05-16). Please update member accounts accordingly."}),
            Action(
                name="send_ground_notification",
                kwargs={
                    "airport_id": "ARP_ATL",
                    "priority": "NORMAL",
                    "message": "STATION NOTICE: Service recovery compensation issued for passengers on flight HAT004 which operated from/to your station."
                }
            ),
            Action(
                name="send_ground_notification",
                kwargs={
                    "airport_id": "ARP_DFW",
                    "priority": "NORMAL",
                    "message": "STATION NOTICE: Service recovery compensation issued for passengers on flight HAT004 which operated from/to your station."
                }
            )
        ],
        outputs=["OE026"]
    ),
    Task(
        annotator="0",
        user_id="task_065",
        instruction=(
                "You are the dispatcher at ATL. You need to apply the AOG Repair and Crew Compliance Protocol for aircraft PR-GOL on flight "
                "HAT004 dated 2024-05-18 you need to update the flight status to DELAYED, document the repair completion under TECH005 with work order WO-240518-HYD-RPR"
                "with a 3-hour delay and check for assigned captain CM001 duty-time compliance for 2024-05-18."
        ),
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={"tail_number": "PR-GOL"}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": "AC001",
                        "new_status": "Active"}
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "AOG_REPAIR",
                    "description": "Maintenance Completed",
                    "status": "Completed",
                    "technician_id": "TECH005",
                    "event_date": "2024-05-18",
                    "work_order_id": "WO-240518-HYD-RPR"
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                    "flight_number": "HAT004",
                    "flight_date": "2024-05-18",
                    "delay_hours": 3,
                    "new_status": "DELAYED"
                }
            ),
            Action(
                name="find_crew_member",
                kwargs={"employee_code": "EMP001"}
            ),
            Action(
                name="verify_crew_duty_time",
                kwargs={"crew_member_id": "CM001",
                        "reference_date": "2024-05-18"}
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Flight_Dispatch",
                    "message": "AOG RECOVERY UPDATE: Aircraft PR-GOL is active after repair for flight HAT004. New ETD: 17:00:00. Crew member CM001 compliance check passed: True."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_066",
        instruction=(
                "You are the Operations Controller at CLT. Using the Gate Conflict Protocol, you need to record a gate reassignment for flight HAT015 on 2024-05-17 at ARP_CLT, move the flight to gate D12 with a 10-minute incremental delay and status DELAYED."
        ),
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "GATE_CONFLICT",
                    "airport_id": "ARP_CLT",
                    "flight_number": "HAT015",
                    "date": "2024-05-17",
                    "details": "Gate conflict for flight HAT015. Reassigning gate D12 with 10-minute delay for passenger movement."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                    "flight_number": "HAT015",
                    "flight_date": "2024-05-17",
                    "new_gate": "D12",
                    "delay_minutes": 10,
                    "new_status": "DELAYED",
                    "reason_event_id": "OE026"
                }
            ),
            Action(
                name="send_ground_notification",
                kwargs={
                    "airport_id": "ARP_CLT",
                    "priority": "HIGH",
                    "message": "GATE CHANGE ALERT: Flight HAT015 has been reassigned to Gate D12. Update all systems and signage immediately."
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                    "flight_number": "HAT015",
                    "date": "2024-05-17"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "4MB0L3",
                    "message": "FLIGHT UPDATE for reservation 4MB0L3: Your flight HAT015 on 2024-05-17 has a new gate D12 and a 10-minute delay. We apologize for any inconvenience."
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "RNL6HR",
                    "message": "FLIGHT UPDATE for reservation RNL6HR: Your flight HAT015 on 2024-05-17 has a new gate D12 and a 10-minute delay. We apologize for any inconvenience."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_067",
        instruction="You are the Operations Controller at ATL (ARP_ATL). Using the Gate Conflict Protocol, you need to record a gate conflict for flight HAT004 on 2024-05-16, move the flight to gate C25 with a 15-minute incremental delay  and status DELAYED and also notify the impacted reservations D975WV and BMZ6Y9",
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "GATE_CONFLICT",
                    "airport_id": "ARP_ATL",
                    "flight_number": "HAT004",
                    "date": "2024-05-16",
                    "details": "Gate conflict for flight HAT004. Reassigning gate C25 with 15-minute delay for passenger movement."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                    "flight_number": "HAT004",
                    "flight_date": "2024-05-16",
                    "new_gate": "C25",
                    "delay_minutes": 15,
                    "new_status": "DELAYED",
                    "reason_event_id": "OE026"
                }
            ),
            Action(
                name="send_ground_notification",
                kwargs={
                    "airport_id": "ARP_ATL",
                    "priority": "HIGH",
                    "message": "GATE CHANGE ALERT: Flight HAT004 has been reassigned to Gate C25. Update all systems and signage immediately."
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                    "flight_number": "HAT004",
                    "date": "2024-05-16"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "D975WV",
                    "message": "FLIGHT UPDATE for reservation D975WV: Your flight HAT004 on 2024-05-16 has a new gate C25 and a 15-minute delay. We apologize for any inconvenience."
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "BMZ6Y9",
                    "message": "FLIGHT UPDATE for reservation BMZ6Y9: Your flight HAT004 on 2024-05-16 has a new gate C25 and a 15-minute delay. We apologize for any inconvenience."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_068",
        instruction=(
                "You are the Operations Controller at ARP_ATL. Using the Route Retiming Protocol, you need to record a "
                "SCHEDULE_CHANGE for flight HAT004 (ATL-DFW) on 2024-05-17 with details 'Route HAT004 (ATL-DFW) retiming process initiated. New schedule: 13:20:00-15:20:00.', adjust the schedule to a new departure of 13:20:00 and a new "
                "arrival of 15:20:00, and notify the impacted reservation KKKYCG."
        ),
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "SCHEDULE_CHANGE",
                    "airport_id": "ARP_ATL",
                    "flight_number": "HAT004",
                    "date": "2024-05-17",
                    "details": "Route HAT004 (ATL-DFW) retiming process initiated. New schedule: 13:20:00-15:20:00."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                    "flight_number": "HAT004",
                    "flight_date": "2024-05-17",
                    "new_departure_time_est": "13:20:00",
                    "new_arrival_time_est": "15:20:00",
                    "reason_event_id": "OE026"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                    "flight_number": "HAT004",
                    "date": "2024-05-17"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "KKKYCG",
                    "message": "FLIGHT UPDATE for reservation KKKYCG: Your flight HAT004 on 2024-05-17 has been rescheduled. New departure is 13:20:00 and new arrival is 15:20:00. We apologize for any inconvenience."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_069",
        instruction="You are the dispatcher at ATL. Applying the AOG Repair and Crew Compliance Protocol to PR-GOL for flight HAT004 on 2024-05-18, you need to document completion under TECH005 (WO-240518-HYD-RPR) reflecting a 3-hour delay with status 'DELAYED' for HAT004 on 2024-05-18, verify captain CM001 duty-time compliance, and confirm the aircraft returns to 'Active'.",
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={"tail_number": "PR-GOL"}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": "AC001",
                        "new_status": "Active"}
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "AOG_REPAIR",
                    "description": "Maintenance Completed",
                    "status": "Completed",
                    "technician_id": "TECH005",
                    "event_date": "2024-05-18",
                    "work_order_id": "WO-240518-HYD-RPR"
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={"flight_number": "HAT004", "flight_date": "2024-05-18",
                        "delay_hours": 3, "new_status": "DELAYED"}
            ),
            Action(
                name="find_crew_member",
                kwargs={"employee_code": "EMP001"}
            ),
            Action(
                name="verify_crew_duty_time",
                kwargs={"crew_member_id": "CM001",
                        "reference_date": "2024-05-18"}
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Flight_Dispatch",
                    "message": "AOG RECOVERY UPDATE: Aircraft PR-GOL is active after repair for flight HAT004. New ETD: 17:00:00. Crew member CM001 compliance check passed: True."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_070",
        instruction="You are the Operations Controller at ARP_JFK. Using the Route Retiming Protocol, you need to record a SCHEDULE_CHANGE for flight HAT014 (JFK-MIA) on 2024-05-16 with details 'Route HAT014 (JFK-MIA) retiming process initiated. New schedule: 18:10:00-21:10:00.', set a new departure of 18:10:00 and a new arrival of 21:10:00 and notify the impacted reservation OK5IEN.",
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "SCHEDULE_CHANGE",
                    "airport_id": "ARP_JFK",
                    "flight_number": "HAT014",
                    "date": "2024-05-16",
                    "details": "Route HAT014 (JFK-MIA) retiming process initiated. New schedule: 18:10:00-21:10:00."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={"flight_number": "HAT014", "flight_date": "2024-05-16", "new_departure_time_est": "18:10:00",
                        "new_arrival_time_est": "21:10:00", "reason_event_id": "OE026"}
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={"flight_number": "HAT014", "date": "2024-05-16"}
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "OK5IEN",
                    "message": "FLIGHT UPDATE for reservation OK5IEN: Your flight HAT014 on 2024-05-16 has been rescheduled. New departure is 18:10:00 and new arrival is 21:10:00. We apologize for any inconvenience."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_071",
        instruction="You are the Operations Manager at LGA. Using the Route Suspension Protocol, you need to suspend flight HAT002 (LGA-PHX) for 2024-05-18 today. Notify reservations BU71UY, HDUF3Q and CC80AJ. A $100 compensation travel voucher must be issued per-reservation.",
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "ROUTE_SUSPENSION",
                    "airport_id": "ARP_LGA",
                    "flight_number": "HAT002",
                    "details": "Route HAT002 (LGA-PHX) has been suspended. All flights from 2024-05-18 to 2024-05-18 are cancelled.",
                    "date": "2024-05-18"
                }
            ),
            Action(
                name="update_flight_status",
                kwargs={"flight_number": "HAT002",
                        "date": "2024-05-18", "new_status": "cancelled"}
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={"flight_number": "HAT002", "date": "2024-05-18"}
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                    "reservation_id": "BU71UY",
                    "new_status": "CANCELLED_ROUTE_SUSPENSION"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                    "reservation_id": "HDUF3Q",
                    "new_status": "CANCELLED_ROUTE_SUSPENSION"
                }
            ),
            Action(
                name="update_reservation_status",
                kwargs={
                    "reservation_id": "CC80AJ",
                    "new_status": "CANCELLED_ROUTE_SUSPENSION"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={"reservation_id": "BU71UY", "message": "FLIGHT CANCELLATION: Your flight HAT002 on 2024-05-18 has been cancelled due to a route suspension. A $100 travel voucher has been issued to your account."}
            ),
            Action(
                name="send_passenger_notification",
                kwargs={"reservation_id": "HDUF3Q", "message": "FLIGHT CANCELLATION: Your flight HAT002 on 2024-05-18 has been cancelled due to a route suspension. A $100 travel voucher has been issued to your account."}
            ),
            Action(
                name="send_passenger_notification",
                kwargs={"reservation_id": "CC80AJ", "message": "FLIGHT CANCELLATION: Your flight HAT002 on 2024-05-18 has been cancelled due to a route suspension. A $100 travel voucher has been issued to your account."}
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Finance",
                    "message": "FINANCE NOTICE: Route HAT002 suspended. Total of $300.00 in vouchers issued for 3 affected reservations."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_072",
        instruction="You are the Operations Manager at ARP_DFW. You need to execute the “Fleet Swap Protocol” for flight HAT022 on 2024-05-19, assigning aircraft AC005 and applying a 25-minute delay with new gate E18. Notify reservation K9TQ4P.",
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "FLEET_SWAP",
                    "airport_id": "ARP_DFW",
                    "flight_number": "HAT022",
                    "date": "2024-05-19",
                    "details": "Fleet swap executed for flight HAT022 on 2024-05-19. New aircraft assigned: AC005."
                }
            ),
            Action(
                name="assign_aircraft_to_flight",
                kwargs={"flight_number": "HAT022",
                        "date": "2024-05-19", "new_aircraft_id": "AC005"}
            ),
            Action(
                name="update_aircraft_location",
                kwargs={"aircraft_id": "AC005",
                        "new_location_airport_id": "ARP_DFW"}
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                    "flight_number": "HAT022",
                    "flight_date": "2024-05-19",
                    "new_gate": "E18",
                    "delay_minutes": 25,
                    "new_status": "DELAYED",
                    "reason_event_id": "OE026"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "K9TQ4P",
                    "message": "FLEET SWAP UPDATE: Flight HAT022 on 2024-05-19 will now depart from Gate E18 with a 25-minute delay."
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_073",
        instruction=(
                "You are the Operations Controller at ARP_DFW. Using the Gate Return Protocol, you need to log a GATE_RETURN for "
                "flight HAT022 on 2024-05-20 due to operational check, apply a 2-hour and 10-minute operational delay with new gate E22 and status DELAYED, "
                "also validate CM004 duty-time for 2024-05-20 after retrieving the flight crew list."
        ),
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "GATE_RETURN",
                    "airport_id": "ARP_DFW",
                    "flight_number": "HAT022",
                    "date": "2024-05-20",
                    "details": "Flight HAT022 returned to gate on 2024-05-20 due to operational check. Initiating operational recovery procedures."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                    "flight_number": "HAT022",
                    "flight_date": "2024-05-20",
                    "delay_hours": 2,
                    "delay_minutes": 10,
                    "new_gate": "E22",
                    "new_status": "DELAYED",
                    "reason_event_id": "OE026"
                }
            ),
            Action(
                name="find_flight_crew",
                kwargs={"flight_number": "HAT022"}
            ),
            Action(
                name="verify_crew_duty_time",
                kwargs={"crew_member_id": "CM004",
                        "reference_date": "2024-05-20"}
            ),
            Action(
                name="send_ground_notification",
                kwargs={
                    "airport_id": "ARP_DFW",
                    "priority": "HIGH",
                    "message": "GATE CHANGE ALERT: Flight HAT022 has been reassigned to Gate E22. Update all systems and signage immediately."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_074",
        instruction="You are the dispatcher at ATL. The aircraft for flight HAT004 to DFW on May 18, 2024, (PR-GOL) has just completed a minor repair, resulting in a 3-hour delay. The assigned Captain is Mia Li (EMP001). You need apply the 'AOG Repair and Crew Compliance Protocol'.You need to update the flight status to DELAYED, use technician 'TECH005' and work order 'WO-240518-HYD-RPR' for the maintenance log. Provide the captain's final duty time compliance status (True/False) as confirmation.",
        actions=[
            Action(name="get_aircraft_by_tail_number",
                    kwargs={"tail_number": "PR-GOL"}),
            Action(name="update_aircraft_status", kwargs={
                "aircraft_id": "AC001", "new_status": "Active"}),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "AOG_REPAIR",
                    "description": "Maintenance Completed",
                    "status": "Completed",
                    "technician_id": "TECH005",
                    "event_date": "2024-05-18",
                    "work_order_id": "WO-240518-HYD-RPR"
                }
            ),
            Action(name="update_flight_schedule", kwargs={
                "flight_number": "HAT004", "flight_date": "2024-05-18", "delay_hours": 3, "new_status": "DELAYED"}),
            Action(name="find_crew_member", kwargs={
                "employee_code": "EMP001"}),
            Action(name="verify_crew_duty_time", kwargs={
                "crew_member_id": "CM001", "reference_date": "2024-05-18"}),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Flight_Dispatch",
                    "message": "AOG RECOVERY UPDATE: Aircraft PR-GOL is active after repair for flight HAT004. New ETD: 17:00:00. Crew member CM001 compliance check passed: True."
                }
            )
        ],
        outputs=["True"]
    ),
    Task(
        annotator="0",
        user_id="task_075",
        instruction=(
                "You are the Operations Controller at LGA. Using the Route Retiming Protocol, you need to record a SCHEDULE_CHANGE at ARP_LGA for flight HAT002 (LGA-PHX) on 2024-05-18 with details 'Route HAT002 (LGA-PHX) retiming process initiated. New schedule: 22:45:00-03:15:00.', adjust the schedule to a new departure of 22:45:00 and a new arrival of 03:15:00 on the following calendar day (explicitly next day), and notify the impacted reservation J3SAZF."
        ),
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "SCHEDULE_CHANGE",
                    "airport_id": "ARP_LGA",
                    "flight_number": "HAT002",
                    "date": "2024-05-18",
                    "details": "Route HAT002 (LGA-PHX) retiming process initiated. New schedule: 22:45:00-03:15:00."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                    "flight_number": "HAT002",
                    "flight_date": "2024-05-18",
                    "new_arrival_date": "2024-05-19",
                    "new_departure_time_est": "22:45:00",
                    "new_arrival_time_est": "03:15:00",
                    "reason_event_id": "OE026"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                    "flight_number": "HAT002",
                    "date": "2024-05-18"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "J3SAZF",
                    "message": "FLIGHT UPDATE for reservation J3SAZF: Your flight HAT002 on 2024-05-18 has been rescheduled. New departure is 22:45:00 and new arrival is 03:15:00. We apologize for any inconvenience."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_076",
        instruction="You are the Operations Manager at ATL. The B737-800 (PR-GOL) scheduled for flight HAT010 to MCO on May 18, 2024, is now AOG due to an avionics fault. The only available substitute is the smaller A220-300 (G-E-SKM), which lacks a business class cabin. You need to execute the 'Involuntary Downgrade and Compensation Protocol' for the affected business class passengers on reservation 'BWHHHG'. As a mandatory service recovery gesture, issue a $200 travel certificate to the primary user. Use technician 'TECH005' and work order 'WO-240518-AOG-AVN' for the AOG log. Provide the ID of the new maintenance log as confirmation.",
        actions=[
                Action(name="get_aircraft_by_tail_number",
                       kwargs={"tail_number": "PR-GOL"}),
                Action(name="update_aircraft_status", kwargs={
                       "aircraft_id": "AC001", "new_status": "Grounded"}),
                Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC001",
                        "maintenance_type": "Unscheduled",
                        "description": "Last-minute maintenance issue.",
                        "status": "In Progress",
                        "technician_id": "TECH005",
                        "event_date": "2024-05-18",
                        "work_order_id": "WO-240518-AOG-AVN"
                    }
                ),
            Action(name="get_aircraft_by_tail_number",
                   kwargs={"tail_number": "G-E-SKM"}),
            Action(name="assign_aircraft_to_flight", kwargs={
                "flight_number": "HAT010", "date": "2024-05-18", "new_aircraft_id": "AC025"}),
            Action(name="find_reservation_by_code",
                   kwargs={"reservation_code": "BWHHHG"}),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "INVOLUNTARY_DOWNGRADE",
                        "airport_id": "ARP_ATL",
                        "details": "Aircraft downgrade on flight HAT010 from B737-800 to A220-300 due to maintenance. Downgrade and compensation required for reservation BWHHHG.",
                        "flight_number": "HAT010",
                        "date": "2024-05-18"
                    }
                ),
            Action(name="update_reservation_status", kwargs={
                "reservation_id": "BWHHHG", "new_status": "REBOOKED_DOWNGRADE"}),
            Action(name="get_user_details", kwargs={
                "user_id": "liam_johnson_6488"}),
            Action(name="send_passenger_notification", kwargs={
                "reservation_id": "BWHHHG", "message": "FLIGHT CHANGE NOTICE: Due to an aircraft change on flight HAT010, we could not accommodate your Business Class seat. You have been moved to Economy and a travel certificate has been issued for the inconvenience. Ref: BWHHHG."}),
            Action(name="send_certificate", kwargs={
                "user_email": "liam.johnson5509@example.com", "amount": 200})
        ],
        outputs=["ML026"]
    ),
    Task(
        annotator="0",
        user_id="task_077",
        instruction="You are the Operations Controller at ATL (ARP_ATL). You need to resolve a gate conflict that emerged after an initial delay on flight HAT004 for 2024-05-16. Using the Gate Conflict Protocol, you need to record the conflict for HAT004 on 2024-05-16, apply an operational recovery that moves the flight to gate C27 with a 15-minute incremental delay and also notify the impacted reservations D975WV and BMZ6Y9.",
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "GATE_CONFLICT",
                    "airport_id": "ARP_ATL",
                    "flight_number": "HAT004",
                    "date": "2024-05-16",
                    "details": "Gate conflict for flight HAT004. Reassigning gate C27 with 15-minute delay for passenger movement."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                    "flight_number": "HAT004",
                    "flight_date": "2024-05-16",
                    "new_gate": "C27",
                    "delay_minutes": 15,
                    "new_status": "DELAYED",
                    "reason_event_id": "OE026"
                }
            ),
            Action(
                name="send_ground_notification",
                kwargs={
                    "airport_id": "ARP_ATL",
                    "priority": "HIGH",
                    "message": "GATE CHANGE ALERT: Flight HAT004 has been reassigned to Gate C27. Update all systems and signage immediately."
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                    "flight_number": "HAT004",
                    "date": "2024-05-16"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "D975WV",
                    "message": "FLIGHT UPDATE for reservation D975WV: Your flight HAT004 on 2024-05-16 has a new gate C27 and a 15-minute delay. We apologize for any inconvenience."
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "BMZ6Y9",
                    "message": "FLIGHT UPDATE for reservation BMZ6Y9: Your flight HAT004 on 2024-05-16 has a new gate C27 and a 15-minute delay. We apologize for any inconvenience."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_078",
        instruction="You are the Customer Experience Manager for CLT. To improve goodwill on the CLT–EWR route, you need to apply the Service Upgrade Protocol on flight HAT015 for 2024-05-18 and 2024-05-19: record the initiative at ARP_CLT, upgrade the impacted bookings from basic_economy to economy with status 'Upgraded'.",
        actions=[
            Action(
                name="get_flight_by_number",
                kwargs={
                    "flight_number": "HAT015",
                    "date": "2024-05-18"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                    "flight_number": "HAT015",
                    "date": "2024-05-18"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                    "flight_number": "HAT015",
                    "date": "2024-05-19"
                }
            ),
            Action(
                name="update_reservation_details",
                kwargs={
                    "reservation_id": "W8DUJ8",
                    "new_cabin": "economy",
                    "new_status": "Upgraded"
                }
            ),
            Action(
                name="update_reservation_details",
                kwargs={
                    "reservation_id": "UHDAHF",
                    "new_cabin": "economy",
                    "new_status": "Upgraded"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "W8DUJ8",
                    "message": "SERVICE UPGRADE for reservation W8DUJ8: As a valued customer, your booking for flight HAT015 has been upgraded to economy. Enjoy your flight!"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "UHDAHF",
                    "message": "SERVICE UPGRADE for reservation UHDAHF: As a valued customer, your booking for flight HAT015 has been upgraded to economy. Enjoy your flight!"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "PROMOTIONAL_UPGRADE",
                    "airport_id": "ARP_CLT",
                    "flight_number": "HAT015",
                    "details": "Promotional upgrade initiative applied to flight HAT015 on 2024-05-18. All basic_economy passengers upgraded."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_079",
        instruction=(
                "You are the dispatcher at ARP_LAX. After a successful repair on aircraft PP-LTM for flight HAT022 dated 2024-05-18, "
                "you need to apply the AOG Repair and Crew Compliance Protocol reflecting a 3-hour delay with a new ETD 15:00:00 on HAT022 for 2024-05-18, verify the "
                "assigned captain CM004 duty-time compliance for 2024-05-18. Use technician TECH017 and work order WO-2024-05-18-LAX-02 for the maintenance log."
        ),
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={
                    "tail_number": "PP-LTM"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                    "aircraft_id": "AC003",
                    "new_status": "Active"
                }
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC003",
                    "maintenance_type": "AOG_REPAIR",
                    "description": "Maintenance Completed",
                    "status": "Completed",
                    "technician_id": "TECH017",
                    "event_date": "2024-05-18",
                    "work_order_id": "WO-2024-05-18-LAX-02"
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                    "flight_number": "HAT022",
                    "flight_date": "2024-05-18",
                    "delay_hours": 3,
                    "new_status": "DELAYED"
                }
            ),
            Action(
                name="find_crew_member",
                kwargs={
                    "employee_code": "EMP004"
                }
            ),
            Action(
                name="verify_crew_duty_time",
                kwargs={
                    "crew_member_id": "CM004",
                    "reference_date": "2024-05-18"
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={
                    "department_name": "Flight_Dispatch",
                    "message": "AOG RECOVERY UPDATE: Aircraft PP-LTM is active after repair for flight HAT022. New ETD: 15:00:00. Crew member CM004 compliance check passed: True."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_080",
        instruction="You are the Station Manager at ATL. A last-minute maintenance issue has grounded the B737-800 (PR-GOL) for flight HAT010 to MCO on May 18, 2024. The only available substitute is the smaller A220-300 (G-E-SKM), which has insufficient Business Class seating. You need handle this aircraft substitution and its consequences by executing the 'Multi-Passenger Downgrade Protocol' for the two passengers on reservation 'BWHHHG'. For the AOG log, use technician 'TECH005' and work order 'WO-240518-AOG-SUB'. You need calculate the total fare difference for the refund based on the current 'economy' price of $183. Provide the total refund amount for the reservation as confirmation.",
        actions=[
                Action(name="get_aircraft_by_tail_number",
                       kwargs={"tail_number": "PR-GOL"}),
                Action(name="get_aircraft_by_tail_number",
                       kwargs={"tail_number": "G-E-SKM"}),
                Action(name="update_aircraft_status", kwargs={
                       "aircraft_id": "AC001", "new_status": "Grounded"}),
                Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC001",
                        "maintenance_type": "Unscheduled",
                        "description": "Last-minute maintenance issue.",
                        "status": "In Progress",
                        "technician_id": "TECH005",
                        "event_date": "2024-05-18",
                        "work_order_id": "WO-240518-AOG-SUB"
                    }
                ),
            Action(name="assign_aircraft_to_flight", kwargs={
                "flight_number": "HAT010", "date": "2024-05-18", "new_aircraft_id": "AC025"}),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "AIRCRAFT_DOWNGRADE",
                        "airport_id": "ARP_ATL",
                        "details": "Aircraft on flight HAT010 for 2024-05-18 downgraded from B737-800 to A220-300 due to maintenance. Multiple passenger downgrades required.",
                        "date": "2024-05-18",
                        "flight_number": "HAT010"
                    }
                ),
            Action(name="find_reservation_by_code",
                   kwargs={"reservation_code": "BWHHHG"}),
            Action(name="update_reservation_details", kwargs={
                "reservation_id": "BWHHHG", "new_cabin": "economy", "new_status": "DOWNGRADED"}),
            Action(name="calculate", kwargs={
                "expression": "(1380 - 183) * 2"}),
            Action(name="send_passenger_notification", kwargs={
                "reservation_id": "BWHHHG", "message": "AIRCRAFT CHANGE: Due to an aircraft change on flight HAT010, your Business Class seat could not be accommodated. You have been moved to an Economy seat. A refund for the fare difference has been processed. We apologize for the inconvenience."})
        ],
        outputs=["2394"]
    ),
    Task(
        annotator="0",
        user_id="task_081",
        instruction="You are the Fleet Manager. As part of a strategic initiative to standardize the MIA base for the A220-300 fleet by August 20, 2025, you need to execute the 'Fleet Uniformity Mandate Protocol'. Your task is to reposition the two non-standard aircrafts currently at MIA, G-E-OMN (E175) and F-G-KQZ (CRJ900), to the storage facility at PHX. For this operation, all ferry flights should be scheduled with a 10:00 departure and a 12:30 arrival. As a final confirmation, provide the flight number of the ferry flight created for aircraft F-G-KQZ.",
        actions=[
            Action(name="get_aircraft_by_tail_number",
                   kwargs={"tail_number": "G-E-OMN"}),
            Action(name="create_flight", kwargs={"flight_number": "HAT9001", "origin": "MIA", "destination": "PHX",
                                                 "scheduled_departure_time_est": "10:00:00", "scheduled_arrival_time_est": "12:30:00"}),
            Action(name="update_aircraft_location", kwargs={
                "aircraft_id": "AC017", "new_location_airport_id": "ARP_PHX"}),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "FLEET_UNIFORMITY_MANDATE",
                    "airport_id": "ARP_MIA",
                    "details": "Fleet Uniformity Mandate initiated at MIA. Non-standard aircraft models are being repositioned."
                }
            ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Fleet Management",
                        "message": "FLEET UPDATE: As part of the MIA fleet uniformity mandate, aircraft G-E-OMN (AC017) has been repositioned to PHX."
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Scheduling",
                        "message": "FLEET UPDATE: As part of the MIA fleet uniformity mandate, aircraft G-E-OMN (AC017) has been repositioned to PHX."
                    }
                ),
            Action(name="get_aircraft_by_tail_number",
                   kwargs={"tail_number": "F-G-KQZ"}),
            Action(name="create_flight", kwargs={"flight_number": "HAT9002", "origin": "MIA", "destination": "PHX",
                                                 "scheduled_departure_time_est": "10:00:00", "scheduled_arrival_time_est": "12:30:00"}),
            Action(name="update_aircraft_location", kwargs={
                "aircraft_id": "AC019", "new_location_airport_id": "ARP_PHX"}),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Fleet Management",
                        "message": "FLEET UPDATE: As part of the MIA fleet uniformity mandate, aircraft F-G-KQZ (AC019) has been repositioned to PHX."
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Scheduling",
                        "message": "FLEET UPDATE: As part of the MIA fleet uniformity mandate, aircraft F-G-KQZ (AC019) has been repositioned to PHX."
                    }
                )
        ],
        outputs=["HAT9004"]
    ),
    Task(
        annotator="0",
        user_id="task_082",
        instruction="You are the Fleet Manager at MIA. We have an AOG situation with aircraft PR-XTD due to 'Navigation System Failure', which was scheduled for flight HAT014 to JFK on May 18, 2024. The only available substitute is the smaller PR-YJB, forcing a downgrade. Please execute the 'Involuntary Downgrade Protocol' for the passenger on reservation 'QS2N5D'. Use technician 'TECH009' and work order 'WO-2024-05-18-811' for the maintenance log. As a final confirmation, please provide the reservation ID of the passenger whose booking status was changed.",
        actions=[
                Action(name="get_aircraft_by_tail_number",
                       kwargs={"tail_number": "PR-XTD"}),
                Action(name="get_aircraft_by_tail_number",
                       kwargs={"tail_number": "PR-YJB"}),
                Action(name="update_aircraft_status", kwargs={
                       "aircraft_id": "AC005", "new_status": "Grounded"}),
                Action(name="assign_aircraft_to_flight", kwargs={
                       "flight_number": "HAT014", "date": "2024-05-18", "new_aircraft_id": "AC007"}),
                Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC005",
                        "maintenance_type": "Unscheduled",
                        "description": "Aircraft is AOG.",
                        "status": "In Progress",
                        "technician_id": "TECH009",
                        "event_date": "2024-05-18",
                        "work_order_id": "WO-2024-05-18-811"
                    }
                ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "INVOLUNTARY_DOWNGRADE",
                        "airport_id": "ARP_MIA",
                        "flight_number": "HAT014",
                        "date": "2024-05-18",
                        "details": "Aircraft downgrade on flight HAT014 from A350-900 to A220-300 due to maintenance. Rebooking required."
                    }
                ),
            Action(name="find_reservations_by_flight",
                   kwargs={"flight_number": "HAT014", "date": "2024-05-18"}),
            Action(name="update_reservation_status", kwargs={
                "reservation_id": "QS2N5D", "new_status": "REBOOKED_DOWNGRADE"}),
            Action(
                    name="send_passenger_notification",
                    kwargs={
                        "reservation_id": "QS2N5D",
                        "message": "FLIGHT CHANGE NOTICE: Due to an aircraft substitution on flight HAT014, we could not accommodate your original booking. A service agent will contact you shortly to arrange rebooking. We apologize for the inconvenience. Ref: QS2N5D."
                    }
                )
        ],
        outputs=["QS2N5D"]
    ),
    Task(
        annotator="0",
        user_id="task_083",
        instruction="You are the Crew Scheduler for the LAX base. You need to execute the 'Crew Unavailability Protocol' for Captain Liam Santos (employee code EMP004). You have reported a 'Personal Emergency' and is unable to work his shift for flight HAT008 on 2024-05-18. If no other active Captains are available at the LAX base, the flight must be cancelled.",
        actions=[
                Action(
                    name="find_crew_member",
                    kwargs={
                        "employee_code": "EMP004"
                    }
                ),
            Action(
                    name="update_crew_member_status",
                    kwargs={
                        "crew_member_id": "CM004",
                        "new_status": "On Sick Leave"
                    }
                ),
            Action(
                    name="find_crew_assignments",
                    kwargs={
                        "crew_member_id": "CM004"
                    }
                ),
            Action(
                    name="get_airport_by_code",
                    kwargs={
                        "iata_code": "LAX"
                    }
                ),
            Action(
                    name="find_available_crew",
                    kwargs={
                        "role": "Captain",
                        "home_base_iata": "LAX",
                        "status": "Active"
                    }
                ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "CREW_UNAVAILABLE",
                        "details": "Crew replacement failed for flight HAT008 on 2024-05-18. Original crew member CM004 is unavailable.",
                        "airport_id": "ARP_LAX",
                        "flight_number": "HAT008",
                        "date": "2024-05-18"
                    }
                ),
            Action(
                    name="update_flight_status",
                    kwargs={
                        "flight_number": "HAT008",
                        "date": "2024-05-18",
                        "new_status": "cancelled"
                    }
                )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_084",
        instruction="You are the Fleet Manager at MIA. As part of the fleet modernization plan, you need permanently decommission one of the older CRJ900 aircraft, tail number F-G-KQZ. You need to execute the 'Aircraft Decommissioning Protocol' for this aircraft using the date August 11, 2025. The final Decommissioning maintenance log must be assigned to technician TECH011 with work order 'WO-2025-DECOM-003'. You need to notify Finance, Scheduling and MRO_Planning departments.",
        actions=[
                Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={
                        "tail_number": "F-G-KQZ"
                    }
                ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                        "aircraft_id": "AC019",
                        "new_status": "Decommissioned"
                    }
                ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC019",
                        "maintenance_type": "Decommissioning",
                        "description": "Final log entry for aircraft decommissioning and permanent retirement from service.",
                        "status": "Completed",
                        "technician_id": "TECH011",
                        "event_date": "2025-08-11",
                        "work_order_id": "WO-2025-DECOM-003"
                    }
                ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "AIRCRAFT_DECOMMISSIONED",
                        "airport_id": "ARP_MIA",
                        "details": "Aircraft AC019 (F-G-KQZ), model CRJ900, has been officially decommissioned and removed from the active fleet at MIA."
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Finance",
                        "message": "AIRCRAFT ALERT: Aircraft F-G-KQZ (AC019) has been officially decommissioned. Please update all relevant asset and scheduling records."
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "Scheduling",
                        "message": "AIRCRAFT ALERT: Aircraft F-G-KQZ (AC019) has been officially decommissioned. Please update all relevant asset and scheduling records."
                    }
                ),
            Action(
                    name="send_department_notification",
                    kwargs={
                        "department_name": "MRO_Planning",
                        "message": "AIRCRAFT ALERT: Aircraft F-G-KQZ (AC019) has been officially decommissioned. Please update all relevant asset and scheduling records."
                    }
                )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_085",
        instruction="You are the Fleet Manager at ARP_MCO. To service a new regional route, you need to execute the 'Return to Service Protocol' for aircraft with tail number G-E-RKI, which is currently in storage. The new route will be from Orlando (MCO) to Charlotte (CLT) under flight number HAT453, with a scheduled departure of 10:00:00 and arrival of 11:45:00. The process must be logged with technician ID TECH003, work order 'WO-2025-08-12-006', and use the maintenance date 2025-08-11.",
        actions=[
                Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={
                        "tail_number": "G-E-RKI"
                    }
                ),
            Action(
                    name="create_flight",
                    kwargs={
                        "flight_number": "HAT453",
                        "origin": "MCO",
                        "destination": "CLT",
                        "scheduled_departure_time_est": "10:00:00",
                        "scheduled_arrival_time_est": "11:45:00"
                    }
                ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                        "aircraft_id": "AC015",
                        "new_status": "Maintenance"
                    }
                ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC015",
                        "maintenance_type": "Return to Service Inspection",
                        "description": "Return to Service inspection for flight operations.",
                        "technician_id": "TECH003",
                        "work_order_id": "WO-2025-08-12-006",
                        "event_date": "2025-08-11",
                        "status": "Completed"
                    }
                ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                        "aircraft_id": "AC015",
                        "new_status": "Active"
                    }
                ),
            Action(
                    name="get_airport_by_code",
                    kwargs={
                        "iata_code": "MCO"
                    }
                ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "AIRCRAFT_ACTIVATED",
                        "details": "Aircraft AC015 (G-E-RKI) activated from storage at MCO for new flight route HAT453.",
                        "airport_id": "ARP_MCO",
                        "flight_number": "HAT453"
                    }
                )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_086",
        instruction="You are the Operations Controller for the PHX hub. The cabin crew on flight HAT002, currently en route from LGA to PHX on 2024-05-18, has reported that passenger Sophia Taylor requires medical assistance upon arrival due to severe dehydration. You need log the event and retrieve flight details to prepare the ground team. Also send a high priority notification to the PHX ground team.",        actions=[
            Action(
                name="get_flight_by_number",
                kwargs={
                    "flight_number": "HAT002",
                    "date": "2024-05-18"
                }
            ),
            Action(
                name="get_airport_by_code",
                kwargs={
                    "iata_code": "PHX"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "MEDICAL_ASSISTANCE",
                    "airport_id": "ARP_PHX",
                    "flight_number": "HAT002",
                    "date": "2024-05-18",
                    "details": "Medical assistance requested for passenger Sophia Taylor on flight HAT002 upon arrival at PHX."
                }
            ),
            Action(
                name="send_ground_notification",
                kwargs={
                    "airport_id": "ARP_PHX",
                    "priority": "HIGH",
                    "message": "MEDICAL ALERT: Flight HAT002 arriving from LGA requires immediate medical assistance for passenger Sophia Taylor at the gate. Awaiting arrival."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_087",
        instruction="You are the Maintenance Controller at ARP_JFK. Aircraft PR-XTD has reported a issue ahead of its scheduled flight, HAT014, on 2024-05-18. The issue is quickly repairable. You need to execute the 'AOG Protocol' with a 'repair and reinstate' override: instead of cancelling, the flight will be delayed. Log the maintenance event with technician ID TECH008 and work order 'WO-2024-05-18-916'.",
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={
                    "tail_number": "PR-XTD"
                }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                    "aircraft_id": "AC005",
                    "new_status": "Grounded"
                }
            ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC005",
                        "maintenance_type": "Unscheduled",
                        "description": "Aircraft is AOG.",
                        "status": "In Progress",
                        "technician_id": "TECH008",
                        "event_date": "2024-05-18",
                        "work_order_id": "WO-2024-05-18-916"
                    }
            ),
            Action(
                name="update_aircraft_status",
                kwargs={
                    "aircraft_id": "AC005",
                    "new_status": "Active"
                }
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "AOG_REPAIR",
                    "airport_id": "ARP_JFK",
                    "flight_number": "HAT014",
                    "date": "2024-05-18",
                    "details": "Aircraft AC005 returned to service after repair. Flight HAT014 on 2024-05-18 delayed due to unscheduled maintenance: Aircraft is AOG."
                }
            ),
            Action(
                name="update_flight_status",
                kwargs={
                    "flight_number": "HAT014",
                    "date": "2024-05-18",
                    "new_status": "delayed",
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_088",
        instruction="You are the Fleet Manager at MCO. The airline is launching a new route from Orlando (MCO) to Charlotte (CLT) under flight number HAT452, with a scheduled departure of 09:00:00 and arrival of 10:30:00. To service this route, you need to execute the 'Return to Service Protocol' for aircraft with tail number PS-MND. The process must be logged with technician ID TECH016, work order 'WO-2025-08-12-006', and use the maintenance date 2025-08-11.",
        actions=[
                Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={
                        "tail_number": "PS-MND"
                    }
                ),
            Action(
                    name="create_flight",
                    kwargs={
                        "flight_number": "HAT452",
                        "origin": "MCO",
                        "destination": "CLT",
                        "scheduled_departure_time_est": "09:00:00",
                        "scheduled_arrival_time_est": "10:30:00"
                    }
                ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                        "aircraft_id": "AC012",
                        "new_status": "Maintenance"
                    }
                ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC012",
                        "maintenance_type": "Return to Service Inspection",
                        "description": "Return to Service inspection for flight operations.",
                        "technician_id": "TECH016",
                        "work_order_id": "WO-2025-08-12-006",
                        "event_date": "2025-08-11",
                        "status": "Completed"
                    }
                ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                        "aircraft_id": "AC012",
                        "new_status": "Active"
                    }
                ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "AIRCRAFT_ACTIVATED",
                        "details": "Aircraft AC012 (PS-MND) activated from storage at MCO for new flight route HAT452.",
                        "airport_id": "ARP_MCO",
                        "flight_number": "HAT452"
                    }
                )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_089",
        instruction="You are the Fleet Manager at PHX. To meet high demand, you are launching a new route from Phoenix (PHX) to Denver (DEN) with flight number HAT453, scheduled for a 14:00:00 departure and 16:00:00 arrival. You need to execute the 'Return to Service Protocol' for aircraft N-DXJ. Log the process with technician ID TECH018, work order 'WO-2025-09-01-007', and a maintenance date of 2025-08-31.",
        actions=[
                Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={
                        "tail_number": "N-DXJ"
                    }
                ),
            Action(
                    name="create_flight",
                    kwargs={
                        "flight_number": "HAT453",
                        "origin": "PHX",
                        "destination": "DEN",
                        "scheduled_departure_time_est": "14:00:00",
                        "scheduled_arrival_time_est": "16:00:00"
                    }
                ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                        "aircraft_id": "AC016",
                        "new_status": "Maintenance"
                    }
                ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC016",
                        "maintenance_type": "Return to Service Inspection",
                        "description": "Return to Service inspection for flight operations.",
                        "technician_id": "TECH018",
                        "work_order_id": "WO-2025-09-01-007",
                        "event_date": "2025-08-31",
                        "status": "Completed"
                    }
                ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                        "aircraft_id": "AC016",
                        "new_status": "Active"
                    }
                ),
            Action(
                    name="get_airport_by_code",
                    kwargs={
                        "iata_code": "PHX"
                    }
                ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "AIRCRAFT_ACTIVATED",
                        "details": "Aircraft AC016 (N-DXJ) activated from storage at PHX for new flight route HAT453.",
                        "airport_id": "ARP_PHX",
                        "flight_number": "HAT453"
                    }
                )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_090",
        instruction="You are the ARP_ATL Operations Controller. The aircraft PR-GOL has been grounded due to a 'pressurization system alert'. You need to execute the 'AOG Protocol'. This impacts flight HAT004 on 2024-05-17 today. The maintenance log requires technician ID TECH002 and work order 'WO-2024-05-17-411'. Update the affected passenger reservation, KKKYCG.",
        actions=[
                Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={
                        "tail_number": "PR-GOL"
                    }
                ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                        "aircraft_id": "AC001",
                        "new_status": "Grounded"
                    }
                ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC001",
                        "maintenance_type": "Unscheduled",
                        "event_date": "2024-05-17",
                        "description": "Aircraft is AOG.",
                        "status": "In Progress",
                        "technician_id": "TECH002",
                        "work_order_id": "WO-2024-05-17-411"
                    }
                ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "AOG",
                        "details": "Aircraft AC001 grounded. Flight HAT004 on 2024-05-17 cancelled due to unscheduled maintenance: Aircraft is AOG.",
                        "flight_number": "HAT004",
                        "airport_id": "ARP_ATL",    
                        "date": "2024-05-17"
                    }
                ),
            Action(
                    name="update_flight_status",
                    kwargs={
                        "flight_number": "HAT004",
                        "date": "2024-05-17",
                        "new_status": "cancelled"
                    }
                ),
            Action(
                    name="find_reservations_by_flight",
                    kwargs={
                        "flight_number": "HAT004",
                        "date": "2024-05-17"
                    }
                ),
            Action(
                    name="update_reservation_status",
                    kwargs={
                        "reservation_id": "KKKYCG",
                        "new_status": "CANCELLED_AOG"
                    }
                )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_091",
        instruction="You are the Operations Controller at ATL. The aircraft PR-GOL has been grounded due to a 'cracked windshield'. You need to execute the 'AOG Protocol'. This impacts flight HAT010 on 2024-05-13 (today is the day before). The maintenance log requires technician ID TECH002 and work order 'WO-2024-05-13-412'. Update the affected passenger reservation, 9G0PVB.",
        actions=[
                Action(
                    name="get_aircraft_by_tail_number",
                    kwargs={
                        "tail_number": "PR-GOL"
                    }
                ),
            Action(
                    name="update_aircraft_status",
                    kwargs={
                        "aircraft_id": "AC001",
                        "new_status": "Grounded"
                    }
                ),
            Action(
                    name="create_maintenance_log",
                    kwargs={
                        "aircraft_id": "AC001",
                        "maintenance_type": "Unscheduled",
                        "event_date": "2024-05-13",
                        "description": "Aircraft is AOG.",
                        "status": "In Progress",
                        "technician_id": "TECH002",
                        "work_order_id": "WO-2024-05-13-412"
                    }
                ),
            Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "AOG",
                        "details": "Aircraft AC001 grounded. Flight HAT010 on 2024-05-13 cancelled due to unscheduled maintenance: Aircraft is AOG.",
                        "flight_number": "HAT010",
                        "airport_id": "ARP_ATL",
                        "date": "2024-05-12"
                    }
                ),
            Action(
                    name="update_flight_status",
                    kwargs={
                        "flight_number": "HAT010",
                        "date": "2024-05-13",
                        "new_status": "cancelled"
                    }
                ),
            Action(
                    name="update_reservation_status",
                    kwargs={
                        "reservation_id": "9G0PVB",
                        "new_status": "CANCELLED_AOG"
                    }
                )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_092",
        instruction="You are a Schedule Planner. Due to ATC constraints at DFW, you need to execute the 'Route Retiming Protocol' for flight HAT004 (ATL-DFW). The new schedule will be a 15:15:00 departure and a 17:15:00 arrival. Apply this change for the dates 2024-05-15 and 2024-05-16, and ensure all affected passengers on reservations MLPSXM, D975WV, and BMZ6Y9 are notified.",
        actions=[
                Action(
                    name="create_operational_event",
                    kwargs={
                        "event_type": "SCHEDULE_CHANGE",
                        "airport_id": "ARP_ATL",
                        "flight_number": "HAT004",
                        "details": "Route HAT004 (ATL-DFW) retiming process initiated. New schedule: 15:15:00-17:15:00."
                    }
                ),
            Action(
                    name="update_flight_schedule",
                    kwargs={
                        "flight_number": "HAT004",
                        "flight_date": "2024-05-15",
                        "new_departure_time_est": "15:15:00",
                        "new_arrival_time_est": "17:15:00",
                        "reason_event_id": "OE026"
                    }
                ),
            Action(
                    name="find_reservations_by_flight",
                    kwargs={
                        "flight_number": "HAT004",
                        "date": "2024-05-15"
                    }
                ),
            Action(
                    name="send_passenger_notification",
                    kwargs={
                        "reservation_id": "MLPSXM",
                        "message": "FLIGHT UPDATE for reservation MLPSXM: Your flight HAT004 on 2024-05-15 has been rescheduled. New departure is 15:15:00 and new arrival is 17:15:00. We apologize for any inconvenience."
                    }
                ),
            Action(
                    name="update_flight_schedule",
                    kwargs={
                        "flight_number": "HAT004",
                        "flight_date": "2024-05-16",
                        "new_departure_time_est": "15:15:00",
                        "new_arrival_time_est": "17:15:00",
                        "reason_event_id": "OE026"
                    }
                ),
            Action(
                    name="find_reservations_by_flight",
                    kwargs={
                        "flight_number": "HAT004",
                        "date": "2024-05-16"
                    }
                ),
            Action(
                    name="send_passenger_notification",
                    kwargs={
                        "reservation_id": "D975WV",
                        "message": "FLIGHT UPDATE for reservation D975WV: Your flight HAT004 on 2024-05-16 has been rescheduled. New departure is 15:15:00 and new arrival is 17:15:00. We apologize for any inconvenience."
                    }
                ),
            Action(
                    name="send_passenger_notification",
                    kwargs={
                        "reservation_id": "BMZ6Y9",
                        "message": "FLIGHT UPDATE for reservation BMZ6Y9: Your flight HAT004 on 2024-05-16 has been rescheduled. New departure is 15:15:00 and new arrival is 17:15:00. We apologize for any inconvenience."
                    }
                )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_093",
        instruction="You are the Operations Controller at the ATL airport (ARP_ATL). You need to recover operations after a pushback-and-return-to-gate for flight HAT010 on 2024-05-18 caused by a ground equipment fault. Using the Gate Return Protocol, record a 'GATE_RETURN' incident for HAT010 on 2024-05-18 at ARP_ATL, apply an operational recovery reflecting a 2-hour and 15-minute delay with gate C25 and status 'DELAYED', also verify the original captain CM004 duty-time compliance for 2024-05-18. Only set CM004 to Standby if the duty-time check is not compliant; if compliant, keep the assignment unchanged. Passenger messaging is out of scope for this task.",
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "GATE_RETURN",
                    "airport_id": "ARP_ATL",
                    "flight_number": "HAT010",
                    "date": "2024-05-18",
                    "details": "Flight HAT010 returned to gate on 2024-05-18 due to ground equipment fault. Initiating operational recovery procedures."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                    "flight_number": "HAT010",
                    "flight_date": "2024-05-18",
                    "delay_hours": 2,
                    "delay_minutes": 15,
                    "new_gate": "C25",
                    "new_status": "DELAYED",
                    "reason_event_id": "OE026"
                }
            ),
            Action(
                name="find_flight_crew",
                kwargs={
                    "flight_number": "HAT010"
                }
            ),
            Action(
                name="verify_crew_duty_time",
                kwargs={
                    "crew_member_id": "CM004",
                    "reference_date": "2024-05-18"
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_094",
        instruction=(
                "You are the Operations Controller at JFK. Using the Route Retiming Protocol, you need to record a SCHEDULE_CHANGE at ARP_JFK for flight HAT014 (JFK-MIA) on 2024-05-18 with details 'Route HAT014 (JFK-MIA) retiming process initiated. New schedule: 18:30:00-21:30:00.', adjust the schedule to a new departure of 18:30:00 and a new arrival of 21:30:00 and notify the impacted reservation QS2N5D."
        ),
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "SCHEDULE_CHANGE",
                    "airport_id": "ARP_JFK",
                    "flight_number": "HAT014",
                    "date": "2024-05-18",
                    "details": "Route HAT014 (JFK-MIA) retiming process initiated. New schedule: 18:30:00-21:30:00."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                    "flight_number": "HAT014",
                    "flight_date": "2024-05-18",
                    "new_departure_time_est": "18:30:00",
                    "new_arrival_time_est": "21:30:00",
                    "reason_event_id": "OE026"
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={
                    "flight_number": "HAT014",
                    "date": "2024-05-18"
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "QS2N5D",
                    "message": "FLIGHT UPDATE for reservation QS2N5D: Your flight HAT014 on 2024-05-18 has been rescheduled. New departure is 18:30:00 and new arrival is 21:30:00. We apologize for any inconvenience."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_095",
        instruction="You are a Schedule Planner. To improve connectivity with European arrivals, the departure time for route HAT004 from ATL to DFW is being permanently moved one hour earlier, from 14:00:00 to 13:00:00 (use these exact timestamps). You need to execute the 'Route Retiming Protocol' for the upcoming flights on May 16 and May 17, 2024. Ensure the schedules for both dates are updated and all affected passengers on reservations D975WV, BMZ6Y9, and KKKYCG are notified of the new schedule. Provide a list of the reservation IDs for the passengers you notified.",
        actions=[
                Action(name="create_operational_event", kwargs={"event_type": "SCHEDULE_CHANGE", "airport_id": "ARP_ATL",
                       "details": "Route HAT004 (ATL-DFW) retiming process initiated. New schedule: 13:00:00-14:00:00."}),
                Action(name="update_flight_schedule", kwargs={"flight_number": "HAT004", "flight_date": "2024-05-16",
                       "new_departure_time_est": "13:00:00", "new_arrival_time_est": "14:00:00", "reason_event_id": "OE026"}),
                Action(name="find_reservations_by_flight", kwargs={
                       "flight_number": "HAT004", "date": "2024-05-16"}),
                Action(name="send_passenger_notification", kwargs={
                       "reservation_id": "D975WV", "message": "FLIGHT UPDATE for reservation D975WV: Your flight HAT004 on 2024-05-16 has been rescheduled. New departure is 13:00:00 and new arrival is 14:00:00. We apologize for any inconvenience."}),
                Action(name="send_passenger_notification", kwargs={
                       "reservation_id": "BMZ6Y9", "message": "FLIGHT UPDATE for reservation BMZ6Y9: Your flight HAT004 on 2024-05-16 has been rescheduled. New departure is 13:00:00 and new arrival is 14:00:00. We apologize for any inconvenience."}),
                Action(name="update_flight_schedule", kwargs={
                       "flight_number": "HAT004", "flight_date": "2024-05-17", "new_departure_time_est": "13:00:00", "new_arrival_time_est": "14:00:00", "reason_event_id": "OE026"}),
                Action(name="find_reservations_by_flight", kwargs={
                       "flight_number": "HAT004", "date": "2024-05-17"}),
                Action(name="send_passenger_notification", kwargs={
                       "reservation_id": "KKKYCG", "message": "FLIGHT UPDATE for reservation KKKYCG: Your flight HAT004 on 2024-05-17 has been rescheduled. New departure is 13:00:00 and new arrival is 14:00:00. We apologize for any inconvenience."})
        ],
        outputs=["D975WV", "BMZ6Y9", "KKKYCG"]
    ),
    Task(
        annotator="0",
        user_id="task_096",
        instruction=(
                "You are the Operations Controller at ATL (ARP_ATL). Using the GATE_CONFLICT Protocol, you need to resolve a gate issue "
                "for flight HAT004 on 2024-05-16 by moving the flight to gate C25 with a 15-minute incremental delay and status "
                "DELAYED, send a HIGH-priority alert at ARP_ATL, and notify the impacted reservations D975WV and BMZ6Y9."
        ),
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "GATE_CONFLICT",
                    "airport_id": "ARP_ATL",
                    "flight_number": "HAT004",
                    "date": "2024-05-16",
                    "details": "Gate conflict for flight HAT004. Reassigning gate C25 with 15-minute delay for passenger movement."
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={
                    "flight_number": "HAT004",
                    "flight_date": "2024-05-16",
                    "new_gate": "C25",
                    "delay_minutes": 15,
                    "new_status": "DELAYED",
                    "reason_event_id": "OE026"
                }
            ),
            Action(
                name="send_ground_notification",
                kwargs={
                    "airport_id": "ARP_ATL",
                    "priority": "HIGH",
                    "message": "GATE CHANGE ALERT: Flight HAT004 has been reassigned to Gate C25. Update all systems and signage immediately."
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={"flight_number": "HAT004", "date": "2024-05-16"}
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "D975WV",
                    "message": "FLIGHT UPDATE for reservation D975WV: Your flight HAT004 on 2024-05-16 has a new gate C25 and a 15-minute delay. We apologize for any inconvenience."
                }
            ),
            Action(
                name="send_passenger_notification",
                kwargs={
                    "reservation_id": "BMZ6Y9",
                    "message": "FLIGHT UPDATE for reservation BMZ6Y9: Your flight HAT004 on 2024-05-16 has a new gate C25 and a 15-minute delay. We apologize for any inconvenience."
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_097",
        instruction=(
                "You are the Customer Experience Manager at CLT (ARP_CLT). Using the Service Upgrade Protocol, you need to register a "
                "PROMOTIONAL_UPGRADE for HAT015 on 2024-05-18 and upgrade the reservations from basic_economy to economy."
        ),
        actions=[
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "PROMOTIONAL_UPGRADE",
                    "airport_id": "ARP_CLT",
                    "flight_number": "HAT015",
                    "date": "2024-05-18",
                    "details": "Promotional upgrade initiative applied to flight HAT015 on 2024-05-18. All basic_economy passengers upgraded."
                }
            ),
            Action(
                name="find_reservations_by_flight",
                kwargs={"flight_number": "HAT015", "date": "2024-05-18"}
            ),
            Action(
                name="update_reservation_details",
                kwargs={"reservation_id": "W8DUJ8",
                        "new_cabin": "economy", "new_status": "Upgraded"}
            ),
            Action(
                name="send_passenger_notification",
                kwargs={"reservation_id": "W8DUJ8", "message": "SERVICE UPGRADE for reservation W8DUJ8: As a valued customer, your booking for flight HAT015 has been upgraded to economy. Enjoy your flight!"}
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_098",
        instruction=(
                "You are the Operations Controller at PHX (ARP_PHX). Using the MEDICAL_ASSISTANCE standard, you need to register a "
                "MEDICAL_ASSISTANCE event for passenger Sophia Taylor on HAT002 on 2024-05-18 at ARP_PHX. Notify ground with priority HIGH and notify Flight_Dispatch department."
        ),
        actions=[
            Action(
                name="get_flight_by_number",
                kwargs={"flight_number": "HAT002", "date": "2024-05-18"}
            ),
            Action(
                name="get_airport_by_code",
                kwargs={"iata_code": "PHX"}
            ),
            Action(
                name="create_operational_event",
                kwargs={
                    "event_type": "MEDICAL_ASSISTANCE",
                    "airport_id": "ARP_PHX",
                    "flight_number": "HAT002",
                    "date": "2024-05-18",
                    "details": "Medical assistance requested for passenger Sophia Taylor on flight HAT002 upon arrival at PHX."
                }
            ),
            Action(
                name="send_ground_notification",
                kwargs={
                    "airport_id": "ARP_PHX",
                    "priority": "HIGH",
                    "message": "MEDICAL ALERT: Flight HAT002 arriving from LGA requires immediate medical assistance for passenger Sophia Taylor at the gate. Awaiting arrival."
                }
            ),
            Action(
                name="send_department_notification",
                kwargs={"department_name": "Flight_Dispatch",
                        "message": "MEDICAL ASSISTANCE logged for HAT002 at PHX; ground notified (HIGH)."}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_099",
        instruction=(
                "You are the dispatcher at ATL. Using the 'AOG Repair and Crew Compliance Protocol' approach for PR-GOL on "
                "HAT004 dated 2024-05-18, you need to reflect a 3-hour delay with status DELAYED on HAT004 for 2024-05-18,"
                "document the repair completion under TECH005 with work order WO-240518-HYD-RPR and verify the captain via EMP001 and confirm CM001 duty-time compliance."
        ),
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={"tail_number": "PR-GOL"}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": "AC001",
                        "new_status": "Active"}
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC001",
                    "maintenance_type": "AOG_REPAIR",
                    "description": "Maintenance Completed",
                    "status": "Completed",
                    "technician_id": "TECH005",
                    "event_date": "2024-05-18",
                    "work_order_id": "WO-240518-HYD-RPR"
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={"flight_number": "HAT004", "flight_date": "2024-05-18",
                        "delay_hours": 3, "new_status": "DELAYED"}
            ),
            Action(
                name="find_crew_member",
                kwargs={"employee_code": "EMP001"}
            ),
            Action(
                name="verify_crew_duty_time",
                kwargs={"crew_member_id": "CM001",
                        "reference_date": "2024-05-18"}
            ),
            Action(
                name="send_department_notification",
                kwargs={"department_name": "Flight_Dispatch",
                        "message": "AOG recovery at ATL complete for PR-GOL on HAT004; 3-hour delay; CM001 compliance verified."}
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_100",
        instruction=(
                "You are the dispatcher at LAX. You want to use the 'AOG Repair and Crew Compliance Protocol' approach for PP-LTM (AC003) on "
                "HAT022 dated 2024-05-18, you need to reflect a 3-hour delay with status DELAYED"
                "on HAT022 for 2024-05-18, verify via EMP004 and confirm CM004 duty-time compliance with technician TECH017 and work order WO-2024-05-18-LAX-02."
        ),
        actions=[
            Action(
                name="get_aircraft_by_tail_number",
                kwargs={"tail_number": "PP-LTM"}
            ),
            Action(
                name="update_aircraft_status",
                kwargs={"aircraft_id": "AC003",
                        "new_status": "Active"}
            ),
            Action(
                name="create_maintenance_log",
                kwargs={
                    "aircraft_id": "AC003",
                    "maintenance_type": "AOG_REPAIR",
                    "description": "Maintenance Completed",
                    "status": "Completed",
                    "technician_id": "TECH017",
                    "event_date": "2024-05-18",
                    "work_order_id": "WO-2024-05-18-LAX-02"
                }
            ),
            Action(
                name="update_flight_schedule",
                kwargs={"flight_number": "HAT022", "flight_date": "2024-05-18",
                        "delay_hours": 3, "new_status": "DELAYED"}
            ),
            Action(
                name="find_crew_member",
                kwargs={"employee_code": "EMP004"}
            ),
            Action(
                name="verify_crew_duty_time",
                kwargs={"crew_member_id": "CM004",
                        "reference_date": "2024-05-18"}
            ),
            Action(
                name="send_department_notification",
                kwargs={"department_name": "Flight_Dispatch",
                        "message": "AOG recovery at LAX complete for PP-LTM on HAT022; 3-hour delay; CM004 compliance verified."}
            )
        ],
        outputs=[]
    ),
]
