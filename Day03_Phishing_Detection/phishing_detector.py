import re
from urllib.parse import urlparse


KEYWORDS = [
    "login",
    "verify",
    "secure",
    "update",
    "account",
    "bank",
    "paypal"
]


def phish_score(url):
    parsed_url = urlparse(url)
    score = 0

    # Check HTTPS
    if not url.startswith("https"):
        score += 30

    # Check suspicious keywords in domain
    for keyword in KEYWORDS:
        if keyword in parsed_url.netloc.lower():
            score += 20

    # Check excessive subdomains
    if parsed_url.netloc.count(".") > 3:
        score += 25

    # Check if IP address is used instead of a domain
    if re.search(
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
        parsed_url.netloc
    ):
        score += 40

    return min(score, 100)


# Test URLs
# Test 10 sample URLs
urls = [
    "https://paypal-login.evil.com/verify",
    "https://github.com",
    "http://example.com/login",
    "https://account-update.example.com",
    "https://example.com",
    "http://secure-login.example.com",
    "https://bank-verify.example.com",
    "http://192.168.1.100/login",
    "https://secure.example.com/account",
    "https://example.com/update"
]

print("===== PHISHING URL DETECTOR =====")

for url in urls:
    score = phish_score(url)

    if score >= 70:
        risk = "HIGH"
    elif score >= 40:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    print(f"\nURL    : {url}")
    print(f"Risk   : {score}%")
    print(f"Level  : {risk}")
