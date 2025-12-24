def sum_two_numbers(a: int, b: int) -> int:
    """
    Returns the sum of two integers.
    """
    return a + b


def get_user_input() -> tuple[int, int]:
    """
    Reads two integers from user input.
    """
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return x, y


def main():
    x, y = get_user_input()
    result = sum_two_numbers(x, y)
    print(f"Sum of two numbers: {result}")


if __name__ == "__main__":
    main()
