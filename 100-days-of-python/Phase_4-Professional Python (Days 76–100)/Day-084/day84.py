# Day 84 — user_service.py
# Purpose: Demonstrate intentional error handling

class UserNotFoundError(Exception):
    pass


def get_user_email(user_id: int) -> str:
    fake_users = {
        1: "aahish@example.com",
        2: "aayan@example.com"
    }

    if user_id not in fake_users:
        raise UserNotFoundError(f"User with id {user_id} not found")

    return fake_users[user_id]


def send_email(user_id: int):
    email = get_user_email(user_id)
    print(f"Sending email to {email}")


def main():
    try:
        send_email(99)
    except UserNotFoundError as e:
        print(f"Handled error: {e}")


if __name__ == "__main__":
    main()
