import whois
import socket
import requests


def osint_scan(domain):
    try:
        # WHOIS information
        w = whois.whois(domain)

        # Find IP address
        ip = socket.gethostbyname(domain)

        # IP geolocation
        geo = requests.get(
            f"http://ip-api.com/json/{ip}",
            timeout=10
        ).json()

        print("\n===== OSINT SCAN RESULTS =====")
        print(f"Domain   : {domain}")
        print(f"Registrar: {w.registrar}")
        print(f"IP       : {ip}")
        print(
            f"Location : {geo.get('city')}, "
            f"{geo.get('country')}"
        )

    except Exception as e:
        print(f"Error: {e}")


# Use an authorized practice domain only
osint_scan("example.com")