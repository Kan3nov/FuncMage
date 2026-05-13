from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def counter(add_power) -> int:
        nonlocal power
        power += add_power
        return power
    return counter


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply_enchant(item_name: str):
        return enchantment_type + " " + item_name
    return apply_enchant


def memory_vault() -> dict[str, Callable]:
    pass


def main():
    meow = mage_counter()
    print(meow())
    print(meow())
    print(meow())
    print("=== accumulator : ")
    meow = spell_accumulator(12)
    print(meow(2))
    print(meow(5))


if __name__ == "__main__":
    main()
