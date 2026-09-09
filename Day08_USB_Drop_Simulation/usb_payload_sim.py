import platform
import socket
import datetime
import os


def usb_payload_sim(output_file="recon_log.txt"):

    info = {
        "timestamp": str(datetime.datetime.now()),
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "version": platform.version(),
        "user": os.getenv("USERNAME") or os.getenv("USER"),
        "cwd": os.getcwd()
    }

    with open(output_file, "w") as f:
        for key, value in info.items():
            f.write(f"{key}: {value}\n")

    print("======================================")
    print("     USB DROP AWARENESS SIMULATION")
    print("======================================")

    print("\nSystem information collected:")

    for key, value in info.items():
        print(f"{key}: {value}")

    print("\nLog saved to:", output_file)
    print("\n[+] Simulation completed successfully.")


usb_payload_sim()
