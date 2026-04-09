# Day 80 — repository.py
# Simulates a data access layer


def get_user_name(user_id: int) -> str:
    fake_db = {
        1: "alice",
        2: "bob",
        3: "charlie"
    }
    return fake_db.get(user_id, "")
