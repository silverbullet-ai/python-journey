# Day 81 — buggy_service.py
# Purpose: Practice reading tracebacks and debugging mindset


def parse_user_age(data):
    return int(data["age"])


def process_user(data):
    age = parse_user_age(data)
    return f"User is {age} years old"


def main():
    user = {
        "name": "Aahish",
        "age": None
    }
    print(process_user(user))


if __name__ == "__main__":
    main()
