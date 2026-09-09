def generate_vishing_script(target_company, attacker_role, pretext):
    script = f"""
========================================
       VISHING AWARENESS SIMULATION
========================================

Caller Role : {attacker_role}
Target Org  : {target_company}
Pretext     : {pretext}

[OPENER - SIMULATION]
"Hello, this is the {attacker_role} team at {target_company}.
This is an awareness-training simulation."

[HOOK]
"The scenario claims that unusual activity has been
detected on an account."

[RED FLAGS]
- The caller creates urgency or fear.
- The caller asks for sensitive information.
- The caller uses authority to gain trust.

[SAFE RESPONSE]
Do not provide passwords, OTPs, PINs, or other
sensitive information.

Verify the request through an official channel.

========================================
"""
    return script


def generate_smishing_script(company, scenario):
    return f"""
========================================
       SMISHING AWARENESS SIMULATION
========================================

Organization : {company}
Scenario     : {scenario}

[SIMULATED MESSAGE]

"This is an awareness-training example.
A suspicious message claims that immediate
account verification is required.

RED FLAGS:
- Unexpected message
- Urgent language
- Suspicious link
- Request for sensitive information

SAFE RESPONSE:
Do not click suspicious links.
Do not share passwords or OTPs.
Verify through the organization's official channel.

========================================
"""


# Three awareness-training scenarios

print(generate_vishing_script(
    "Sqrock IT",
    "IT Support",
    "Password Reset"
))

print(generate_vishing_script(
    "Example Bank",
    "Bank Support",
    "Suspicious Account Activity"
))

print(generate_vishing_script(
    "Example Government Department",
    "Government Support",
    "Document Verification"
))

print(generate_smishing_script(
    "Example Organization",
    "Account verification"
))