import requests
import re


def harvest_emails(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        html = response.text

        emails = set(
            re.findall(
                r'[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}',
                html
            )
        )

        return emails

    except requests.RequestException as e:
        print(f"Error accessing website: {e}")
        return set()


# Use only your own or authorized lab website
url = "https://example.com"

found = harvest_emails(url)

print("\n===== EMAIL HARVESTING RESULTS =====")

if found:
    for email in sorted(found):
        print(email)
else:
    print("No email addresses found.")