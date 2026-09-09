def spear_phish_template(target):
    return f"""
========================================
   PHISHING AWARENESS EMAIL SIMULATION
========================================

From    : awareness@lab.local
To      : {target['email']}
Subject : [TRAINING] Action Required: Account Verification

Hi {target['name']},

This is a cybersecurity awareness-training simulation.

Scenario:
A suspicious email claims that unusual login activity
has been detected on your {target['company']} account.

The simulated message asks the user to verify the account
through a link.

[SIMULATED TRAINING LINK]
https://lab.internal/awareness-test

RED FLAGS:
- Unexpected account verification request
- Urgent language
- Suspicious login-location claim
- Link requesting account verification
- Possible sender impersonation

SAFE RESPONSE:
- Do not click suspicious links.
- Do not provide passwords or OTPs.
- Verify the request through an official channel.
- Report suspicious emails to the security team.

Regards,
Cybersecurity Awareness Team

========================================
"""


targets = [
    {
        "name": "Riya Sharma",
        "email": "riya@lab.local",
        "company": "Sqrock",
        "location": "Bangalore, India"
    },
    {
        "name": "Arun Kumar",
        "email": "arun@lab.local",
        "company": "Example Bank",
        "location": "Mysore, India"
    },
    {
        "name": "Priya Rao",
        "email": "priya@lab.local",
        "company": "Example Organization",
        "location": "Chennai, India"
    }
]

print("===== PHISHING AWARENESS EMAIL TEMPLATES =====")

for target in targets:
    print(spear_phish_template(target))