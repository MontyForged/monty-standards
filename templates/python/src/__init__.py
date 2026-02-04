"""My Project - Main module."""


def hello(name: str = "World") -> str:
    """Return a greeting.

    Args:
        name: Name to greet.

    Returns:
        Greeting string.
    """
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Sum of a and b.
    """
    return a + b


if __name__ == "__main__":
    print(hello("Python"))
