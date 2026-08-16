from zimzam.transforms import greet


def test_greet() -> None:
    assert greet("zimzam") == "hello, zimzam"
