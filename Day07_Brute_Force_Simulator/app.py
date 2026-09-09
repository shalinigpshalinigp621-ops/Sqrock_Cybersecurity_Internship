from flask import Flask, request

app = Flask(__name__)

# Dummy training account
VALID_USERNAME = "admin"
VALID_PASSWORD = "Training123!"

# Rate-limiting settings
MAX_ATTEMPTS = 3
failed_attempts = {}


@app.route("/login", methods=["POST"])
def login():

    client_ip = request.remote_addr

    # Check rate limit
    if failed_attempts.get(client_ip, 0) >= MAX_ATTEMPTS:
        return "Too many failed attempts. Rate limit activated.", 429

    username = request.form.get("username")
    password = request.form.get("password")

    # Check credentials
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        failed_attempts[client_ip] = 0
        return "Login successful - Training Account", 200

    # Record failed attempt
    failed_attempts[client_ip] = failed_attempts.get(client_ip, 0) + 1

    return "Invalid username or password", 401


if __name__ == "__main__":
    print("======================================")
    print("   LOCAL LOGIN TRAINING SERVER")
    print("======================================")
    print("Server running at http://127.0.0.1:5000")
    print("Training username: admin")
    print("Training password: Training123!")
    print("Rate limit: 3 failed attempts")
    print("======================================")

    app.run(host="127.0.0.1", port=5000)