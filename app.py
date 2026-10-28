def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_even(number):
    return number % 2 == 0


def main():
    print("Welcome to the Pytest Demo App!")
    print("Addition: 2 + 3 =", add(2, 3))
    print("Division: 10 / 2 =", divide(10, 2))
    print("Is 4 even?", is_even(4))


if __name__ == "__main__":
    main()
