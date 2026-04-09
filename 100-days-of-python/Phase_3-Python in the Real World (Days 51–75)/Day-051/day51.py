# Day 51 — Real-World Python & Code Quality

print("REAL-WORLD PYTHON — CODE QUALITY\n")

def calculate_average(numbers: list[int]) -> float:
    """
    Calculates the average of a list of numbers.

    Raises:
        ValueError: if the list is empty
    """
    if not numbers:
        raise ValueError("Numbers list cannot be empty")

    return sum(numbers) / len(numbers)


def main():
    scores = [85, 90, 78, 92]
    average = calculate_average(scores)
    print(f"Average score: {average:.2f}")


if __name__ == "__main__":
    main()

print("\nDay 51 completed successfully!")
