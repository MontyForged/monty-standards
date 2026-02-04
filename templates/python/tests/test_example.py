"""Tests for my project."""
from my_project import hello, add


def test_hello_default():
    """Test greeting with default name."""
    assert hello() == "Hello, World!"


def test_hello_custom():
    """Test greeting with custom name."""
    assert hello("Monty") == "Hello, Monty!"


def test_add_positive():
    """Test adding positive numbers."""
    assert add(2, 3) == 5


def test_add_negative():
    """Test adding with negative number."""
    assert add(-1, 1) == 0
