"""Sanity-check tests used in the Week 01 lectures."""


def inc(x: int) -> int:
    """Increment ``x`` and return the new value."""

    return x + 1


def test_answer():
    """The increment helper should add a single unit."""

    assert inc(3) == 4
