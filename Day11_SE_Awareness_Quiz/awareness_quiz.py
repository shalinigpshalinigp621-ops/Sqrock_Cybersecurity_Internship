import json
from datetime import datetime

QUESTIONS = [
    {
        "q": "An email asks you to verify your password through a link. What should you do?",
        "opts": [
            "A) Click the link",
            "B) Contact IT through an official channel",
            "C) Reply with your password"
        ],
        "ans": "B",
        "exp": "Never provide passwords through email links. Verify through official channels."
    },

    {
        "q": "You find an unknown USB drive in the parking lot. What should you do?",
        "opts": [
            "A) Plug it into your computer",
            "B) Give it to security or IT",
            "C) Take it home"
        ],
        "ans": "B",
        "exp": "Unknown USB devices can be used as baiting attacks."
    },

    {
        "q": "Someone claiming to be IT asks for your password over the phone. What should you do?",
        "opts": [
            "A) Give the password",
            "B) Verify their identity through an official channel",
            "C) Ignore all security procedures"
        ],
        "ans": "B",
        "exp": "Legitimate IT staff should not ask for your password."
    },

    {
        "q": "You receive a message saying your account will be locked in 10 minutes. What is the safest action?",
        "opts": [
            "A) Immediately click the provided link",
            "B) Verify the message independently",
            "C) Forward it to everyone"
        ],
        "ans": "B",
        "exp": "Urgency is a common social engineering technique."
    },

    {
        "q": "A stranger follows you closely through a restricted office door. What should you do?",
        "opts": [
            "A) Hold the door open",
            "B) Politely ask them to use their access method",
            "C) Ignore the situation"
        ],
        "ans": "B",
        "exp": "Tailgating can allow unauthorized people into restricted areas."
    },

    {
        "q": "Which is a common sign of a phishing message?",
        "opts": [
            "A) Unexpected urgency",
            "B) Normal communication from a verified channel",
            "C) A message you were expecting"
        ],
        "ans": "A",
        "exp": "Urgency and pressure are common phishing indicators."
    },

    {
        "q": "Someone asks for confidential company information on social media. What should you do?",
        "opts": [
            "A) Share the information",
            "B) Refuse and report the request if necessary",
            "C) Share only part of it"
        ],
        "ans": "B",
        "exp": "Confidential information should not be shared with unverified people."
    },

    {
        "q": "You receive an unexpected attachment from an unknown sender. What should you do?",
        "opts": [
            "A) Open it immediately",
            "B) Verify the sender before opening",
            "C) Forward it to a friend"
        ],
        "ans": "B",
        "exp": "Unexpected attachments can be dangerous."
    },

    {
        "q": "Which psychological trigger is commonly used in social engineering?",
        "opts": [
            "A) Urgency",
            "B) File compression",
            "C) Screen brightness"
        ],
        "ans": "A",
        "exp": "Attackers often use urgency, fear, authority, or trust."
    },

    {
        "q": "What should you do if you accidentally provide information to a suspicious person?",
        "opts": [
            "A) Hide the incident",
            "B) Report it immediately to the appropriate security team",
            "C) Continue communicating with them"
        ],
        "ans": "B",
        "exp": "Early reporting helps security teams respond quickly."
    },

    {
        "q": "A caller claims to be from your bank and asks for an OTP. What should you do?",
        "opts": [
            "A) Provide the OTP",
            "B) End the call and contact the bank through its official number",
            "C) Send the OTP by SMS"
        ],
        "ans": "B",
        "exp": "Never share OTPs with unexpected callers."
    },

    {
        "q": "What is the safest response to a suspicious login alert?",
        "opts": [
            "A) Use the link in the message",
            "B) Open the official website or app independently",
            "C) Give your password to the sender"
        ],
        "ans": "B",
        "exp": "Access services through trusted official channels instead of suspicious links."
    }
]


def run_quiz():
    score = 0
    results = []

    print("=" * 60)
    print("       SOCIAL ENGINEERING AWARENESS QUIZ")
    print("=" * 60)

    print("\nAnswer each question with A, B, or C.\n")

    for i, question in enumerate(QUESTIONS, 1):

        print(f"\nQ{i}. {question['q']}")

        for option in question["opts"]:
            print("   " + option)

        while True:
            answer = input("Your answer (A/B/C): ").strip().upper()

            if answer in ["A", "B", "C"]:
                break

            print("Invalid input. Please enter A, B, or C.")

        if answer == question["ans"]:
            print("✓ Correct!")
            score += 1
            result = "Correct"
        else:
            print("✗ Wrong.")
            print("Explanation:", question["exp"])
            result = "Wrong"

        results.append({
            "question_number": i,
            "answer": answer,
            "correct_answer": question["ans"],
            "result": result
        })

    percentage = (score / len(QUESTIONS)) * 100

    if percentage >= 80:
        level = "Excellent"
    elif percentage >= 60:
        level = "Good"
    elif percentage >= 40:
        level = "Needs Improvement"
    else:
        level = "High Awareness Risk"

    report = {
        "quiz": "Social Engineering Awareness Training",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_questions": len(QUESTIONS),
        "correct_answers": score,
        "wrong_answers": len(QUESTIONS) - score,
        "percentage": round(percentage, 2),
        "awareness_level": level,
        "results": results
    }

    with open("quiz_report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("\n" + "=" * 60)
    print("                 QUIZ COMPLETED")
    print("=" * 60)
    print(f"Score       : {score}/{len(QUESTIONS)}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Awareness   : {level}")
    print("\nReport saved as: quiz_report.json")
    print("=" * 60)


if __name__ == "__main__":
    run_quiz()