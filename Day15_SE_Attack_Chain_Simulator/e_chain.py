import json
import datetime


MODULES = {
    "1": "OSINT Scan",
    "2": "Profile Analysis",
    "3": "Phishing URL Detection",
    "4": "Awareness Email Template",
    "5": "Incident Response"
}


def osint_demo():
    print("\n============================================================")
    print("MODULE 1 - OSINT SCAN")
    print("============================================================")

    domain = input("Enter lab/practice domain [example.com]: ").strip()

    if not domain:
        domain = "example.com"

    print("\n[+] Passive OSINT simulation started...")
    print(f"Domain : {domain}")
    print("DNS/IP information : Simulated")
    print("WHOIS information   : Simulated")
    print("Geolocation         : Simulated")
    print("\n[+] OSINT module completed safely.")


def profile_demo():
    print("\n============================================================")
    print("MODULE 2 - PROFILE ANALYSIS")
    print("============================================================")

    print("\n[+] Analyzing synthetic profile data...")

    profile = {
        "username": "training_user",
        "account_age_days": 15,
        "followers": 10,
        "following": 150,
        "profile_completeness": 40,
        "profile_picture": False,
        "bio": False
    }

    print("\nSynthetic Profile")
    print("----------------------------------------")

    for key, value in profile.items():
        print(f"{key}: {value}")

    print("\n[+] Profile analysis completed safely.")


def phishing_demo():
    print("\n============================================================")
    print("MODULE 3 - PHISHING URL DETECTION")
    print("============================================================")

    url = input(
        "Enter a URL to analyze "
        "[https://example.com]: "
    ).strip()

    if not url:
        url = "https://example.com"

    score = 0

    suspicious_words = [
        "login",
        "verify",
        "update",
        "secure",
        "account"
    ]

    lower_url = url.lower()

    for word in suspicious_words:
        if word in lower_url:
            score += 10

    if lower_url.startswith("http://"):
        score += 20

    if "@" in url:
        score += 30

    if score >= 60:
        risk = "HIGH"
    elif score >= 30:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    print("\nAnalysis Result")
    print("----------------------------------------")
    print(f"URL       : {url}")
    print(f"Risk Score: {score}%")
    print(f"Risk Level: {risk}")

    print("\n[+] Phishing detection completed safely.")


def email_demo():
    print("\n============================================================")
    print("MODULE 4 - AWARENESS EMAIL TEMPLATE")
    print("============================================================")

    target_name = input("Enter training participant name [Riya]: ").strip()

    if not target_name:
        target_name = "Riya"

    email = f"""
[TRAINING SIMULATION]

To      : {target_name}@lab.local
Subject : Security Awareness Training

Hello {target_name},

This is a simulated security-awareness message.

Please remember:
- Verify unexpected requests through official channels.
- Never share passwords or OTPs.
- Be careful with urgent account-verification requests.
- Check links before opening them.

Training Link:
https://lab.internal/awareness-test

This message is part of an authorized cybersecurity
awareness exercise.
"""

    print(email)


def incident_response_demo():
    print("\n============================================================")
    print("MODULE 5 - INCIDENT RESPONSE")
    print("============================================================")

    incident = {
        "type": "phishing",
        "severity": "HIGH",
        "user": "riya@lab.local"
    }

    print("\nIncident Detected")
    print("----------------------------------------")
    print(f"Type     : {incident['type']}")
    print(f"Severity : {incident['severity']}")
    print(f"User     : {incident['user']}")

    actions = [
        "LOCK user account",
        "Revoke active sessions",
        "Notify SOC team",
        "Preserve mail logs",
        "Quarantine email",
        "Block sender domain",
        "Scan attachments in sandbox"
    ]

    print("\nSimulated Response Actions")
    print("----------------------------------------")

    for action in actions:
        print(f"[SIMULATED] {action}")

    report = {
        "incident": incident,
        "actions": actions,
        "timestamp": str(datetime.datetime.now()),
        "status": "Simulation completed"
    }

    with open(
        "Day15_SE_Attack_Chain_Simulator/final_ir_report.json",
        "w"
    ) as file:
        json.dump(report, file, indent=4)

    print("\n[+] Incident response report generated.")


def show_menu():
    print("\n")
    print("============================================================")
    print("        SE ATTACK CHAIN SIMULATOR")
    print("        Sqrock Cybersecurity Internship")
    print("============================================================")

    print("\nAvailable Modules")
    print("----------------------------------------")

    for number, name in MODULES.items():
        print(f"[{number}] {name}")

    print("[6] Run Complete Simulation")
    print("[7] Exit")


def complete_simulation():
    print("\n")
    print("============================================================")
    print("       COMPLETE SE ATTACK CHAIN SIMULATION")
    print("============================================================")

    print("\nAttack Chain")
    print("----------------------------------------")
    print("OSINT")
    print("   ↓")
    print("Profile Analysis")
    print("   ↓")
    print("Phishing Detection")
    print("   ↓")
    print("Awareness Training")
    print("   ↓")
    print("Incident Response")

    print("\n[+] All modules executed in SAFE SIMULATION mode.")
    print("[+] No real targets were contacted.")
    print("[+] No real credentials were collected.")
    print("[+] No real accounts or systems were modified.")

    report = {
        "project": "SE Attack Chain Simulator",
        "mode": "Authorized Lab Simulation",
        "modules": list(MODULES.values()),
        "status": "Completed",
        "timestamp": str(datetime.datetime.now())
    }

    with open(
        "Day15_SE_Attack_Chain_Simulator/final_report.json",
        "w"
    ) as file:
        json.dump(report, file, indent=4)

    print("\nFinal report saved as:")
    print("Day15_SE_Attack_Chain_Simulator/final_report.json")


def main():

    while True:

        show_menu()

        choice = input("\nSelect module: ").strip()

        if choice == "1":
            osint_demo()

        elif choice == "2":
            profile_demo()

        elif choice == "3":
            phishing_demo()

        elif choice == "4":
            email_demo()

        elif choice == "5":
            incident_response_demo()

        elif choice == "6":
            complete_simulation()

        elif choice == "7":
            print("\nExiting simulator...")
            print("Thank you!")
            break

        else:
            print("\n[!] Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()