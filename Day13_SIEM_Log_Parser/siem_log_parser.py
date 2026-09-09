import re
import json
from collections import Counter


# ============================================================
# DAY 13 - SIEM LOG PARSER
# ============================================================

LOG_FILE = "Day13_SIEM_Log_Parser/sample_auth.log"
REPORT_FILE = "Day13_SIEM_Log_Parser/siem_report.json"

FAILED_LOGIN_THRESHOLD = 3


print("=" * 60)
print("DAY 13 - SIEM LOG PARSER")
print("=" * 60)


# ------------------------------------------------------------
# 1. Read log file
# ------------------------------------------------------------

try:
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        logs = file.readlines()

except FileNotFoundError:
    print("\n[ERROR] sample_auth.log not found.")
    exit()


print(f"\nLog file loaded successfully.")
print(f"Total log entries: {len(logs)}")


# ------------------------------------------------------------
# 2. Parse log entries
# ------------------------------------------------------------

successful_logins = 0
failed_logins = 0

failed_ips = Counter()
successful_ips = Counter()
failed_users = Counter()

parsed_entries = []


pattern = re.compile(
    r"(?P<timestamp>\S+\s+\S+)\s+"
    r"(?P<level>\w+)\s+"
    r"Login\s+(?P<status>successful|failed)\s+"
    r"user=(?P<user>\S+)\s+"
    r"ip=(?P<ip>\S+)"
)


for line in logs:

    match = pattern.search(line)

    if not match:
        continue

    timestamp = match.group("timestamp")
    level = match.group("level")
    status = match.group("status")
    user = match.group("user")
    ip = match.group("ip")

    entry = {
        "timestamp": timestamp,
        "level": level,
        "status": status,
        "user": user,
        "ip": ip
    }

    parsed_entries.append(entry)

    if status == "failed":
        failed_logins += 1
        failed_ips[ip] += 1
        failed_users[user] += 1

    elif status == "successful":
        successful_logins += 1
        successful_ips[ip] += 1


# ------------------------------------------------------------
# 3. Detect suspicious IPs
# ------------------------------------------------------------

suspicious_ips = {
    ip: count
    for ip, count in failed_ips.items()
    if count >= FAILED_LOGIN_THRESHOLD
}


# ------------------------------------------------------------
# 4. Display results
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("LOG ANALYSIS")
print("=" * 60)

print(f"\nSuccessful logins : {successful_logins}")
print(f"Failed logins     : {failed_logins}")

print("\nFailed Login Attempts by IP")
print("-" * 40)

for ip, count in failed_ips.items():
    print(f"{ip:<18} {count} failed attempts")


print("\nSuspicious IP Addresses")
print("-" * 40)

if suspicious_ips:

    for ip, count in suspicious_ips.items():
        print(
            f"[ALERT] {ip} -> "
            f"{count} failed login attempts"
        )

else:
    print("No suspicious IP addresses detected.")


# ------------------------------------------------------------
# 5. Display failed users
# ------------------------------------------------------------

print("\nFailed Login Attempts by User")
print("-" * 40)

for user, count in failed_users.items():
    print(f"{user:<15} {count} failed attempts")


# ------------------------------------------------------------
# 6. Generate SIEM report
# ------------------------------------------------------------

report = {
    "project": "Day 13 - SIEM Log Parser",
    "total_log_entries": len(logs),
    "parsed_entries": len(parsed_entries),
    "successful_logins": successful_logins,
    "failed_logins": failed_logins,
    "failed_login_threshold": FAILED_LOGIN_THRESHOLD,
    "failed_logins_by_ip": dict(failed_ips),
    "failed_logins_by_user": dict(failed_users),
    "suspicious_ips": suspicious_ips
}


with open(REPORT_FILE, "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4)


# ------------------------------------------------------------
# 7. Completion message
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("REPORT GENERATED")
print("=" * 60)

print(f"\nReport saved as: {REPORT_FILE}")

print("\nDay 13 completed successfully!")