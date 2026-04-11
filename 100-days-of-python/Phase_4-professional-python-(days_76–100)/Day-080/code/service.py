# Day 80 — service.py
# Business logic layer

from code.repository import get_user_name


def get_uppercase_user_name(user_id: int) -> str:
    name = get_user_name(user_id)
    return name.upper()
