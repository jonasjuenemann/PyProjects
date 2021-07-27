from typing import Union, List


def test(x: int) -> int:
    return x + x


def test2(x: Union[int, float]) -> int:
    return x ** x


y: int = 1

print(y)
print(test(4))
print(test("string"))  # IDE gibt ne warning, funktioniert aber trotzdem.

y = "hey"

print(y)

y = test2(4.5)
print(y)

z: list = []

c: List[int] = []  # In 3.9 dürfte man hier die Standard list verwenden

c = ["hey", "hey"]

print(c)
