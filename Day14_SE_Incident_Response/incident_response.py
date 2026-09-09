import datetime
import json


def ir_response(incident):
    print("\n============================================================")
    print("DAY 14 - SE INCIDENT RESPONSE PLAN")
    print("============================================================")

    print("\nINCIDENT DETAILS")
    print("----------------------------------------")
    print(f"Time     : {datetime.datetime.now()}")
    print(f"Type     : {incident['type']}")
    print(f"Severity : {incident['severity']}")
    print(f"User     : {incident['user']}")

    actions = []

    # High/Critical severity containment actions
    if incident["severity"] in ("HIGH", "CRITICAL"):
        actions += [
            "LOCK user account",
            "Revoke active sessions",
            "Notify SOC team",
            "Preserve mail logs"
        ]

    # Phishing-specific response actions
    if incident["type"].lower() == "phishing":
        actions += [
            "Quarantine email",
            "Block sender domain",
            "Scan attachments in sandbox"
        ]

    print("\nCONTAINMENT ACTIONS")
    print("----------------------------------------")

    for action in actions:
        print(f"[SIMULATED] {action}")

    # Generate incident response report
    report = {
        "incident": incident,
        "actions": actions,
        "timestamp": str(datetime.datetime.now()),
        "status": "Containment actions simulated successfully"
    }

    with open("Day14_SE_Incident_Response/ir_report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("\n============================================================")
    print("REPORT GENERATED")
    print("============================================================")
    print("\nIR report saved as: Day14_SE_Incident_Response/ir_report.json")
    print("\nDay 14 completed successfully!")


# Safe lab incident
incident = {
    "type": "phishing",
    "severity": "HIGH",
    "user": "riya@lab.local"
}

ir_response(incident)