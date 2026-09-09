def fake_profile_score(profile):
    score = 0
    reasons = []

    # Account age
    if profile["account_age_days"] < 30:
        score += 25
        reasons.append("Very new account")

    # Followers / following ratio
    if profile["following"] > 0:
        ratio = profile["followers"] / profile["following"]

        if ratio < 0.2:
            score += 20
            reasons.append("Very low follower/following ratio")

    # Profile completeness
    if profile["profile_completeness"] < 50:
        score += 20
        reasons.append("Incomplete profile")

    # Profile picture
    if not profile["has_profile_picture"]:
        score += 15
        reasons.append("No profile picture")

    # Bio
    if not profile["has_bio"]:
        score += 10
        reasons.append("No profile bio")

    # Activity
    if profile["posts"] < 3:
        score += 10
        reasons.append("Very low posting activity")

    score = min(score, 100)

    if score >= 70:
        risk = "HIGH"
    elif score >= 40:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return score, risk, reasons


profiles = [
    {
        "username": "new_user_123",
        "account_age_days": 10,
        "followers": 15,
        "following": 200,
        "profile_completeness": 30,
        "has_profile_picture": False,
        "has_bio": False,
        "posts": 1
    },
    {
        "username": "normal_user",
        "account_age_days": 900,
        "followers": 500,
        "following": 300,
        "profile_completeness": 90,
        "has_profile_picture": True,
        "has_bio": True,
        "posts": 120
    },
    {
        "username": "suspicious_account",
        "account_age_days": 20,
        "followers": 40,
        "following": 250,
        "profile_completeness": 45,
        "has_profile_picture": True,
        "has_bio": False,
        "posts": 2
    }
]


print("======================================")
print("       FAKE PROFILE SCORER")
print("======================================")

for profile in profiles:

    score, risk, reasons = fake_profile_score(profile)

    print(f"\nUsername : {profile['username']}")
    print(f"Risk Score: {score}%")
    print(f"Risk Level: {risk}")

    if reasons:
        print("Indicators:")
        for reason in reasons:
            print(f" - {reason}")
    else:
        print("Indicators: No major suspicious indicators")
        