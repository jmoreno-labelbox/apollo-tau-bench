import json
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool

FIXED_NOW = "2025-08-15T09:00:00+00:00"
DYNAMIC_NOW = None




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


class GetEmployeeId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], first_name: str = None, last_name: str = None) -> str:
        if first_name is None or last_name is None:
            payload = {"error": "first_name and last_name are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        employees = data.get("employees", [])

        for employee in employees:
            if (
                employee["first_name"] == first_name
                and employee["last_name"] == last_name
            ):
                payload = employee["employee_id"]
                out = json.dumps(payload, indent=2)
                return out
        payload = {
                "status": "error",
                "reason": f"Employee {first_name} {last_name} not found.",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getEmployeeId",
                "description": "Finds an employee's id using their first name and last name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "The first name of the employee to search for.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "The last name of the employee to search for.",
                        },
                    },
                    "required": ["first_name", "last_name"],
                },
            },
        }


class EmployeeAccountExists(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], first_name: str = None, last_name: str = None) -> str:
        if first_name is None or last_name is None:
            payload = {"error": "first_name and last_name are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        employees = data.get("employees", [])

        for employee in employees:
            if (
                employee["first_name"] == first_name
                and employee["last_name"] == last_name
            ):
                payload = {"account_exists": True}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"account_exists": False}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "employeeAccountExists",
                "description": "Checks whether an employee account exists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "The first name of the employee to search for.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "The last name of the employee to search for.",
                        },
                    },
                    "required": ["first_name", "last_name"],
                },
            },
        }


class GetEmployeeInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        if employee_id is None:
            payload = {"status": "error", "reason": "The employee_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        employees = data.get("employees", [])

        for employee in employees:
            if employee["employee_id"] == employee_id:
                payload = employee
                out = json.dumps(payload)
                return out
        payload = {"status": "error", "reason": "Employee not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getEmployeeInfo",
                "description": "Finds an employee's info using their id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to search for.",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }


class MailboxExists(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        if employee_id is None:
            payload = {"status": "error", "reason": "The employee_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        employees = data.get("employees", [])

        for employee in employees:
            if employee["employee_id"] == employee_id:
                payload = {"mailbox_exists": True}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"mailbox_exists": False}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "mailboxExists",
                "description": "Determines whether or not an employee mailbox exists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to search for.",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }


class GetEmployeeLicenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        if employee_id is None:
            payload = {"status": "error", "reason": "The employee_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        license_assignments = data.get("license_assignments", [])
        licenses = []

        for assignment in license_assignments:
            if assignment["employee_id"] == employee_id:
                licenses.append(assignment["license_id"])
        payload = licenses
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getEmployeeLicenses",
                "description": "Finds licenses associated with a specified employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to search for.",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }


class FilterEmployees(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        first_name: str = None,
        last_name: str = None,
        department: str = None,
        job_title: str = None,
        manager_id: str = None,
        status: str = None
    ) -> str:
        employees = data.get("employees")

        if all(
            [
                attribute is None
                for attribute in [
                    first_name,
                    last_name,
                    department,
                    job_title,
                    manager_id,
                    status,
                ]
            ]
        ):
            payload = {"status": "error", "reason": "No criteria specified"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        temp_employees = employees.copy()

        if first_name is not None:
            temp_employees = [
                employee
                for employee in temp_employees
                if employee["first_name"] == first_name
            ]

        if last_name is not None:
            temp_employees = [
                employee
                for employee in temp_employees
                if employee["last_name"] == last_name
            ]

        if department is not None:
            temp_employees = [
                employee
                for employee in temp_employees
                if employee["department"] == department
            ]

        if job_title is not None:
            temp_employees = [
                employee
                for employee in temp_employees
                if employee["job_title"] == job_title
            ]

        if manager_id is not None and manager_id != "None":
            temp_employees = [
                employee
                for employee in temp_employees
                if employee["manager_id"] == manager_id
            ]

        if manager_id is not None and manager_id == "None":
            temp_employees = [
                employee
                for employee in temp_employees
                if employee["manager_id"] is None
            ]

        if status is not None:
            temp_employees = [
                employee for employee in temp_employees if employee["status"] == status
            ]
        payload = temp_employees
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filterEmployees",
                "description": "Finds employees based on certain criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "The first name to search for.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "The last name to search for.",
                        },
                        "department": {
                            "type": "string",
                            "description": "The department to search for.",
                        },
                        "job_title": {
                            "type": "string",
                            "description": "The job title to search for.",
                        },
                        "manager_id": {
                            "type": "string",
                            "description": "The manager to search for.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status to search for.",
                        },
                    },
                },
            },
        }


class GetLicenseAvailability(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str = None) -> str:
        inventory = data.get("license_inventory")

        if license_id is None:
            payload = {"status": "error", "reason": "The license_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        for license in inventory:
            if license["license_id"] == license_id:
                if (
                    license["total_seats"]
                    - license["reserved_seats"]
                    - license["used_seats"]
                    > 0
                ):
                    payload = {"available": True}
                    out = json.dumps(payload, indent=2)
                    return out
                else:
                    payload = {"available": False}
                    out = json.dumps(payload, indent=2)
                    return out
        payload = {"status": "error", "reason": f"License {license_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLicenseAvailability",
                "description": "Checks if a license with a designated id is available.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {
                            "type": "string",
                            "description": "The id of the license to search for.",
                        }
                    },
                },
            },
        }


class AssignLicenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, job_title: str = None,
    license_ids: Any = None,
    ) -> str:
        if employee_id is None:
            payload = {"status": "error", "reason": "The employee_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        licenses = set()

        license_assignments = data.get("license_assignments", [])
        for assignment in license_assignments:
            if assignment["employee_id"] == employee_id:
                licenses.add(assignment["license_id"])

        group_map = data.get("rbac_group_map", [])
        if job_title is None:
            for group in group_map:
                if group["job_title"] == job_title:
                    for license in group["default_license_bundle"]:
                        licenses.add(license)

        inventory = data.get("license_inventory")

        for license in inventory:
            if license["license_id"] in licenses:
                license["used_seats"] += 1
                last_id = license_assignments[-1]["assignment_id"]
                last_id = last_id.split("_")
                new_id_num = str(int(last_id[1])).zfill(4)
                new_license_assignment = {
                    "assignment_id": f"{last_id[0]}_{new_id_num}",
                    "account_id": "acc_000000",  # Allocate a distinct account identifier for every user
                    "employee_id": "emp_0001",
                    "license_id": employee_id,
                    "status": "active",
                    "assigned_at": FIXED_NOW,
                }
                license_assignments.append(new_license_assignment)
        payload = {
            "status": "ok",
            "reason": f"Licenses successfully added for {employee_id}.",
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assignLicenses",
                "description": "Assigns licenses in the rbac_group_map or licenses provided to an employee, verifying license availability before assignment. Takes the employee_id as input as well as license_ids and or job_title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee.",
                        },
                        "license_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of license ids to assign to the employee.",
                        },
                        "job_title": {
                            "type": "string",
                            "description": "The job title to assign default licenses from.",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }


class GetLicenseInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_name: str = None) -> str:
        if license_name is None:
            payload = {"status": "error", "reason": "The license_name field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        inventory = data.get("license_inventory")
        assignments = data.get("license_assignments")

        for license in inventory:
            if license["name"] == license_name:
                assigned_licenses = []
                for assignment in assignments:
                    if assignment["license_id"] == license["license_id"]:
                        assigned_licenses.append(assignment)
                license_overview = {"info": license, "assignments": assigned_licenses}
                payload = license_overview
                out = json.dumps(payload, indent=2)
                return out
        payload = {"status": "error", "reason": "Could not find specified license."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLicenseInfo",
                "description": "Gets all info associated with a specific license.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_name": {
                            "type": "string",
                            "description": "The name of the license.",
                        },
                    },
                    "required": ["license_name"],
                },
            },
        }


class GetJobLicenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], job_title: str = None) -> str:
        if job_title is None:
            payload = {"status": "error", "reason": "The job_title parameter is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        group_data = data.get("rbac_group_map")

        for group in group_data:
            if group["job_title"] == job_title:
                payload = group["default_license_bundle"]
                out = json.dumps(payload, indent=2)
                return out
        payload = {"status": "error", "reason": "Unable to find specified job_title."}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getJobLicenses",
                "description": "Gets all default licenses for a specific job title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_title": {
                            "type": "string",
                            "description": "The name of the job.",
                        },
                    },
                    "required": ["job_title"],
                },
            },
        }


class CreateJiraTicket(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], issue_type: str = None, summary: str = None, priority: str = None) -> str:
        jira_tickets = data.get("jira_tickets")

        if len(jira_tickets) > 0:
            last_jira_id = jira_tickets[-1]["jira_id"]
        else:
            last_jira_id = "ITSD-1000"

        id_components = last_jira_id.split("-")
        new_jira_id = f"{id_components[0]}-{str(int(id_components[1])+1).zfill(4)}"

        if issue_type is None:
            payload = {"status": "error", "reason": "issue_type parameter is required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if summary is None:
            payload = {"status": "error", "reason": "summary parameter is required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if priority is None:
            payload = {"status": "error", "reason": "priority parameter is required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        new_jira_ticket = {
            "jira_id": new_jira_id,
            "issue_type": issue_type,
            "summary": summary,
            "priority": priority,
            "status": "To Do",
            "created_at": "2025-07-10T13:00:00+00:00",
            "updated_at": "2025-07-14T15:30:00+00:00",
        }

        jira_tickets.append(new_jira_ticket)
        payload = {
                "status": "ok",
                "reason": f"Successfully created a new Jira ticket {new_jira_id}.",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createJiraTicket",
                "description": "Creates a new Jira ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "issue_type": {
                            "type": "string",
                            "description": "The type of issue to assign to the Jira ticket",
                        },
                        "summary": {
                            "type": "string",
                            "description": "A description of the issue.",
                        },
                        "priority": {
                            "type": "string",
                            "description": "The priority of the issue.",
                        },
                    },
                    "required": ["issue_type", "summary", "priority"],
                },
            },
        }


class FilterHRMemos(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        first_name: str = None,
        last_name: str = None,
        memo_type: str = None,
        type: Any = None
    ) -> str:
        memos = data.get("hr_memos")

        if first_name is None or last_name is None:
            if memo_type is not None:
                temp_memos = [memo for memo in memos if memo["type"] == memo_type]
            else:
                payload = {
                    "status": "error",
                    "reason": "Insufficient information to filter memos.",
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        else:
            temp_memos = [
                memo
                for memo in memos
                if memo["first_name"] == first_name and memo["last_name"] == last_name
            ]

        if len(temp_memos) == 0:
            payload = {"status": "error", "reason": "Unable to find specified memos"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = temp_memos
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filterHrMemos",
                "description": "Filters HR memos for matching criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "The first name of the person being searched for.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "The last name of the person being searched for.",
                        },
                        "type": {
                            "type": "string",
                            "description": "The type of memo being searched for.",
                        },
                    },
                },
            },
        }


class DeviceAssignment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, unassign: bool = False) -> str:
        if employee_id is None:
            payload = {"status": "error", "reason": "The employee_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        assets = data.get("it_assets")
        assigned_assets = []

        for asset in assets:
            if asset["assigned_to"] == employee_id:
                if unassign:
                    asset["status"] = "in_stock"
                    asset["assigned_to"] = None
                assigned_assets.append(asset)

        if unassign:
            payload = {
                    "status": "ok",
                    "reason": f"Successfully unassigned all devices from {employee_id}.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = assigned_assets
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deviceAssignment",
                "description": "Updates or returns a list of devices assigned to an employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee.",
                        },
                        "unassign": {
                            "type": "boolean",
                            "description": "Whether to unassign devices.",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }


class LicenseRequiresRenewal(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], num_days: int = None) -> str:
        if num_days is None:
            payload = {"status": "error", "reason": "The num_days field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        inventory = data.get("license_inventory")
        licenses = []

        dt_now = datetime.fromisoformat(FIXED_NOW)

        for license in inventory:
            dt_audit = datetime.fromisoformat(license["last_audit_at"])
            if (dt_now - dt_audit).days > num_days:
                licenses.append(license["license_id"])
        payload = licenses
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "licenseRequiresRenewal",
                "description": "Returns the license_id of any license audited over num_days ago.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "num_days": {
                            "type": "string",
                            "description": "The number of days to filter by.",
                        },
                    },
                    "required": ["num_days"],
                },
            },
        }


class GetEmployeeByLicense(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str = None, status: str = None) -> str:
        if license_id is None or status is None:
            payload = {
                    "status": "error",
                    "reason": "The license_id and status fields are required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        license_assignments = data.get("license_assignments")

        assignment_data = []

        for license in license_assignments:
            if license["license_id"] == license_id and license["status"] == status:
                assignment_data.append(license["employee_id"])
        payload = assignment_data
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getEmployeeByLicense",
                "description": "Returns the employees with licenses and statuses that match status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {
                            "type": "string",
                            "description": "The license to filter by.",
                        },
                        "status": {
                            "type": "string",
                            "desctiption": "The status of the license to filter by.",
                        },
                    },
                    "required": ["license_id", "status"],
                },
            },
        }


class FilterLicenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], utilization: float = None) -> str:
        if all([param is None for param in [utilization]]):
            payload = {
                "status": "error",
                "reason": "Input parameters to filter by are required.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        licenses = data.get("license_inventory")
        filtered_licenses = []

        for license in licenses:
            util = (license["used_seats"] + license["reserved_seats"]) / license[
                "total_seats"
            ]
            if util < utilization:
                filtered_licenses.append(license["license_id"])
        payload = filtered_licenses
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filterLicenses",
                "description": "Reterns the licenses that match input criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "utilization": {
                            "type": "number",
                            "description": "Filters liceses by utilization.",
                        },
                    },
                },
            },
        }


class ExportUnderutilizedLicenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], output_data: Any = None) -> str:
        csv_data = output_data
        if csv_data is None:
            payload = {"status": "error", "description": "The data field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        csv_path = "reports/underutilized_licenses.csv"
        payload = {"path": csv_path, "licenses": csv_data}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "exportUnderutilizedLicenses",
                "description": "Exports a CSV underutilized licenses",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "output_data": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "The data to be written to a CSV.",
                        },
                    },
                    "required": ["output_data"],
                },
            },
        }


class UpdateLicenseAudit(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str = None) -> str:
        if license_id is None:
            payload = {"status": "error", "description": "The license_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        inventory = data.get("license_inventory")

        for license in inventory:
            if license["license_id"] == license_id:
                license["last_audit_at"] = FIXED_NOW
                payload = {
                        "status": "ok",
                        "description": f"Successfully updated {license_id}.",
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"status": "error", "description": f"Unable to find {license_id}."}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateLicenseAudit",
                "description": "Updates a liscense's audit date",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {
                            "type": "string",
                            "description": "The license to update.",
                        },
                    },
                    "required": ["license_id"],
                },
            },
        }


class ArchiveMailbox(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, department: str = None) -> str:
        if employee_id is None or department is None:
            payload = {
                    "status": "error",
                    "description": "The employee_id and department fields are required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        mailboxes = data.get("mailboxes")
        archives = data.get("data_archives")

        for mailbox in mailboxes:
            if mailbox["employee_id"] == employee_id:
                archive = {
                    "archive_id": "arch_000000",
                    "employee_id": employee_id,
                    "mailbox_id": mailbox["mailbox_id"],
                    "archive_path": f"s3://corp-archives/mail/{employee_id}/{FIXED_NOW.split('T')[0]}",
                    "retention_policy": None,
                    "created_at": FIXED_NOW,
                }
                if department == "Finance":
                    archive["retention_policy"] = "finance_7y"
                else:
                    archive["retention_policy"] = "std_2y"

                archives.append(archive)
                payload = {"status": "ok", "description": "Successfully created mailbox"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"status": "error", "description": "Employee mailbox not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "archiveMailbox",
                "description": "Archives an employee's mailbox",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to archive.",
                        },
                        "department": {
                            "type": "string",
                            "description": "The employee's department.",
                        },
                    },
                    "required": ["employee_id", "department"],
                },
            },
        }


class LogLifecycle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, memo_id: str = None, event: str = None) -> str:
        if any([param is None for param in [employee_id, memo_id, event]]):
            payload = {
                    "status": "error",
                    "description": "The employee_id, memo_id, and event fields are required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        lifecycle_items = data.get("lifecycle_queue")

        id = lifecycle_items[-1]["lifecycle_id"].split("_")
        new_lifecycle_id = f"{id[0]}_{str(int(id[1])+1).zfill(5)}"

        lifecycle = {
            "lifecycle_id": new_lifecycle_id,
            "memo_id": memo_id,
            "employee_ref": employee_id,
            "event": event,
            "status": "completed",
            "created_at": FIXED_NOW,
        }

        lifecycle_items.append(lifecycle)
        payload = {
                "status": "ok",
                "description": "Successfully added log to lifecycle_queue",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "logLifecycle",
                "description": "Logs data to lifecycle_queue",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee.",
                        },
                        "memo_id": {
                            "type": "string",
                            "description": "The id of the memo referenced.",
                        },
                        "event": {
                            "type": "string",
                            "description": "The event type of the log",
                        },
                    },
                    "required": ["employee_id", "memo_id", "event"],
                },
            },
        }


class MissingLicenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, job_title: str = None) -> str:
        if employee_id is None or job_title is None:
            payload = {
                "status": "error",
                "description": "The employee_id and job_title fields are required.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        employee_licenses = []
        license_assignments = data.get("license_assignments", [])

        for assignment in license_assignments:
            if assignment["employee_id"] == employee_id:
                employee_licenses.append(assignment["license_id"])

        group_map = data.get("rbac_group_map")
        missing = []

        for group in group_map:
            if group["job_title"] == job_title:
                licenses = group["default_license_bundle"]
                for license in licenses:
                    if license not in employee_licenses:
                        missing.append(license)
                payload = missing
                out = json.dumps(payload, indent=2)
                return out
        payload = {"status": "error", "description": "Unable to find specified job_title."}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "missingLicenses",
                "description": "Finds any licenses a job's default licenses from the rbac_group_map database that are not assigned to an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee to verify licenses for.",
                        },
                        "job_title": {
                            "type": "string",
                            "description": "The job title to compare licenses against.",
                        },
                    },
                    "required": ["employee_id", "job_title"],
                },
            },
        }


class GenerateReviewandLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], log_data: Any = None) -> str:
        if log_data is None:
            payload = {"status": "error", "description": "The log_data field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        formatted_date = FIXED_NOW.split("T")[0].replace("-", "_")
        new_report = {
            "run_id": f"rpt_{formatted_date}_0000",
            "report_type": "review_log",
            "started_at": FIXED_NOW,
            "completed_at": FIXED_NOW,
            "output_path_pdf": f"s3://reports/Report_{formatted_date}.pdf",
        }

        reports = data.get("validation_issues", [])
        reports.append(new_report)
        payload = {
                "status": "ok",
                "description": "Successfully created pdf and added report to validation_issues.",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateReviewAndLog",
                "description": "Generates a review packet pdf from input data and creates a log in validation_issues.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_data": {
                            "type": "string",
                            "description": "The data to log in the report.",
                        },
                    },
                    "required": ["log_data"],
                },
            },
        }


class GetTicketInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None) -> str:
        if ticket_id is None:
            payload = {"status": "error", "description": "The ticket_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        tickets = data.get("tickets")

        for ticket in tickets:
            if ticket["ticket_id"] == ticket_id:
                payload = ticket
                out = json.dumps(payload, indent=2)
                return out
        payload = {"status": "error", "description": "The ticket was not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTicketInfo",
                "description": "Gets info for a ticket based on ticket_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "The id of the ticket to search for.",
                        },
                    },
                    "required": ["ticket_id"],
                },
            },
        }


class GetTicketsBacklog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], snapshot_id: str = None) -> str:
        snapshots = data.get("backlog_snapshot_open")

        if snapshot_id is None:
            if len(snapshots) > 0:
                target_snapshot = snapshots[-1]
            else:
                payload = {
                    "status": "error",
                    "description": "The snapshot could not be found.",
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        else:
            target_snapshot = None
            for snapshot in snapshots:
                if snapshot["snapshot_id"] == snapshot_id:
                    target_snapshot = snapshot
            if target_snapshot is None:
                payload = {
                    "status": "error",
                    "description": "The snapshot could not be found.",
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = target_snapshot["open_ticket_ids"]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTicketsBacklog",
                "description": "Gets a list of tickets from a snapshot, the default being the last snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {
                            "type": "string",
                            "description": "The id of the snapshot to look for.",
                        },
                    },
                },
            },
        }


class FilterTickets(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ids: list = None, status: str = None, not_status: str = None) -> str:
        if ids is None:
            ids = []

        if len(ids) == 0 and all([param is None for param in [status, not_status]]):
            payload = {
                "status": "error",
                "description": "Input parameters to search for are required.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        tickets = data.get("tickets")
        temp_tickets = tickets.copy()

        if len(ids) != 0:
            temp_tickets = [
                ticket for ticket in temp_tickets if ticket["ticket_id"] in ids
            ]
        if status is not None:
            temp_tickets = [
                ticket for ticket in temp_tickets if ticket["status"] == status
            ]
        if not_status is not None:
            temp_tickets = [
                ticket for ticket in temp_tickets if ticket["status"] != not_status
            ]
        payload = temp_tickets
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filterTickets",
                "description": "Filters tickets by input criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "An array of ticket ids to search for.",
                        },
                        "status": {
                            "type": "string",
                            "description": "A status to search for.",
                        },
                        "not_status": {
                            "type": "string",
                            "description": "A status to exclude from search results.",
                        },
                    },
                },
            },
        }


class SaveReport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], save_data: list = None) -> str:
        if save_data is None:
            save_data = []

        if len(save_data) == 0:
            payload = {
                "status": "error",
                "description": "The save_data and file_path parameters are required.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        new_report = {
            "save_data": save_data,
            "file_path": "/IT/Reports/Backlog/Backlog_Status.pdf",
        }
        payload = new_report
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "saveReport",
                "description": "Saves a report containing data called Backlog_Status.pdf",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "save_data": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "An array containing data to save",
                        },
                    },
                    "required": ["save_data"],
                },
            },
        }


class AssignAppAccount(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, app_id: str = None) -> str:
        if employee_id is None or app_id is None:
            payload = {
                    "status": "error",
                    "description": "The employee_id and app_id fields are required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        accounts = data.get("app_accounts")

        new_account = {
            "app_account_id": "appacc_000000",
            "employee_id": employee_id,
            "app_id": app_id,
            "status": "active",
            "created_at": FIXED_NOW,
        }

        accounts.append(new_account)
        payload = {
                "status": "ok",
                "description": f"Added {app_id} account for {employee_id}",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assignAppAccount",
                "description": "Assigns an app to a user by appending to the app_accounts database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to assign licenses to.",
                        },
                        "app_id": {
                            "type": "string",
                            "description": "The id of the app to assign.",
                        },
                    },
                    "required": ["employee_id", "app_id"],
                },
            },
        }


class AssignRBACLicense(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str = None, job_title: str = None) -> str:
        if license_id is None or job_title is None:
            payload = {
                    "status": "error",
                    "description": "The license_id and job_title fields are required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        group_map = data.get("rbac_group_map")

        for group in group_map:
            if group["job_title"] == job_title:
                group["default_license_bundle"].append(license_id)
                payload = group["default_license_bundle"]
                out = json.dumps(payload)
                return out
        payload = {
                "status": "error",
                "description": "The job title could not be found with an rbac group association.",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assignRbacLicense",
                "description": "Assigns a license to be default in the rbac_group_map for a job_title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {
                            "type": "string",
                            "description": "The id of the license to add.",
                        },
                        "job_title": {
                            "type": "string",
                            "description": "The job title to assign the license to.",
                        },
                    },
                    "required": ["license_id", "job_title"],
                },
            },
        }


class ReportRun(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], report_type: str = None, run_data: Any = None) -> str:
        if report_type is None or run_data is None:
            payload = {
                "status": "error",
                "description": "The report_type and data fields are required.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        run_date = FIXED_NOW.split("T")[0].replace("-", "_")
        new_report = {
            "run_id": f"rpt_{run_date}_0000",
            "report_type": report_type,
            "started_at": FIXED_NOW,
            "completed_at": FIXED_NOW,
            "output_path_pdf": f"s3://reports/{report_type}_{run_date}.pdf",
        }

        reports = data.get("report_runs")
        reports.append(new_report)
        payload = {
            "status": "ok",
            "description": "Successfully created report pdf and saved a log in report_runs.",
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reportRun",
                "description": "Creates a report log in report_runs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_type": {
                            "type": "string",
                            "description": "The type of the report to write.",
                        },
                        "run_data": {
                            "type": "array",
                            "items": {"type": "string"},
                            "item": {"type": "string"},
                            "description": "The data to include in the run.",
                        },
                    },
                    "required": ["report_type", "run_data"],
                },
            },
        }


class UpdateDirectoryAccount(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, status: str = None) -> str:
        if employee_id is None:
            payload = {
                    "status": "error",
                    "description": "The employee_id field is required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if all([param is None for param in [status]]):
            payload = {
                    "status": "error",
                    "description": "At least one parameter to be changed is required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        directory_accounts = data.get("directory_accounts")

        for account in directory_accounts:
            if account["employee_id"] == employee_id:
                if status is not None:
                    account["status"] = status
                    if status == "disabled":
                        account["disabled_at"] = FIXED_NOW
        payload = {
                "status": "ok",
                "description": f"Successfully updated account for {employee_id}.",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateDirectoryAccount",
                "description": "Allows updates for directory accounts, including disabling accounts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to update.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status to set.",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }


class UnassignLicenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, license_ids: list = None) -> str:
        if employee_id is None:
            payload = {"status": "error", "reason": "The employee_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if license_ids is None:
            license_ids = []

        assignments = data.get("license_assignments")
        inventory = data.get("license_inventory")

        for assignment in assignments:
            if assignment["employee_id"] == employee_id and (
                len(license_ids) == 0 or assignment["license_id"] in license_ids
            ):
                assignment["status"] = "inactive"
                license_ids.append(assignment["license_id"])

        license_ids = set(license_ids)

        for license in inventory:
            if license["license_id"] in license_ids:
                license["used_seats"] -= 1
        payload = {
                "status": "ok",
                "reason": f"Licenses successfully removed for {employee_id}",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "unassignLicenses",
                "description": "Unssigns licenses from an employee and updates license_inventory. Takes the employee_id and license_ids as input. If no license_ids are supplied, removes all licenses from the employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee.",
                        },
                        "license_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of license ids to unassign from the employee.",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }


class Notify(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipient_ids: list = None, summary: str = None) -> str:
        if recipient_ids is None:
            recipient_ids = []

        if len(recipient_ids) == 0 or summary is None:
            payload = {
                "status": "error",
                "reason": "The recipient_ids and summary fields are required.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"status": "ok", "recipients": recipient_ids, "summary": summary}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "notify",
                "description": "Notifies employees in recipient_ids with the contents of summary.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "The ids of the recipients to notify.",
                        },
                        "summary": {
                            "type": "string",
                            "description": "The summary to send to each recipient.",
                        },
                    },
                    "required": ["recipient_ids", "summary"],
                },
            },
        }


class TicketStatistics(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        field: str = None,
        stat_type: str = None,
        type: Any = None
    ) -> str:
        if field is None or stat_type is None:
            payload = {
                "status": "error",
                "reason": "The field and type parameters are required.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if field not in [
            "tickets_opened",
            "tickets_closed",
            "closed_within_24h",
            "avg_open_age_hours",
        ]:
            payload = {
                "status": "error",
                "reason": "The specified field could not be found in daily_metrics.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if stat_type not in ["avg", "sum"]:
            payload = {"status": "error", "reason": "Unknown statistic type."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        daily_metrics = data.get("daily_metrics")

        pulled_data = []
        for metrics in daily_metrics:
            pulled_data.append(metrics[field])

        if stat_type == "sum":
            payload = {"result": sum(pulled_data)}
            out = json.dumps(payload)
            return out
        elif stat_type == "avg":
            payload = {"result": sum(pulled_data) / len(pulled_data)}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ticketStatistics",
                "description": "Calculates various statistics for ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "field": {
                            "type": "string",
                            "description": "The field in daily_metrics to target.",
                        },
                        "type": {
                            "type": "string",
                            "description": "The type of statistic to produce.",
                        },
                    },
                    "required": ["field", "type"],
                },
            },
        }


class AssignDevice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, asset_type: str = None) -> str:
        if employee_id is None or asset_type is None:
            payload = {
                    "status": "error",
                    "reason": "The employee_id and asset_type fields are required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        assets = data.get("it_assets")

        for asset in assets:
            if asset["asset_type"] == asset_type and asset["status"] == "in_stock":
                asset["status"] = "assigned"
                asset["assigned_to"] = employee_id
                payload = {"status": "ok", "device": asset}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"status": "error", "description": "Unable to find available asset."}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assignDevice",
                "description": "Assigns an employee a device of a specified type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee.",
                        },
                        "asset_type": {
                            "type": "string",
                            "description": "The type of asset to assign to an employee.",
                        },
                    },
                    "required": ["employee_id", "asset_type"],
                },
            },
        }


TOOLS = [
    GetEmployeeId(),
    EmployeeAccountExists(),
    MailboxExists(),
    GetEmployeeLicenses(),
    FilterHRMemos(),
    GetLicenseInfo(),
    GetLicenseAvailability(),
    AssignLicenses(),
    LicenseRequiresRenewal(),
    FilterLicenses(),
    ExportUnderutilizedLicenses(),
    CreateJiraTicket(),
    UpdateLicenseAudit(),
    GetEmployeeInfo(),
    DeviceAssignment(),
    LogLifecycle(),
    FilterEmployees(),
    GetJobLicenses(),
    GenerateReviewandLog(),
    GetTicketInfo(),
    GetTicketsBacklog(),
    FilterTickets(),
    SaveReport(),
    GetEmployeeByLicense(),
    ArchiveMailbox(),
    MissingLicenses(),
    AssignAppAccount(),
    AssignRBACLicense(),
    ReportRun(),
    UpdateDirectoryAccount(),
    UnassignLicenses(),
    Notify(),
    TicketStatistics(),
    AssignDevice(),
]
