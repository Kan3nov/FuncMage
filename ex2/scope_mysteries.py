from typing import Any
from collections.abc import Callable


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
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> str:
        if (vault.get(key)):
            return vault[key]
        return "Memory not found"
    return {"store": store, "recall": recall}


def main():
    print("Testing mage counter...")
    counter_a = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    counter_b = mage_counter()
    print("counter_b call 1:", counter_b())

    print("\nTesting spell accumulator")
    acum = spell_accumulator(100)
    print("Base 100, add 20:", acum(20))
    print("Base 100, add 30:", acum(30))

    print("\nTesting enchantment factory...")
    en1 = enchantment_factory("Flaming")
    en2 = enchantment_factory("Frozen")
    print(en1("Sword"))
    print(en2("Shield"))

    print("\nTesting memory vault...")
    mem_vault = memory_vault()
    print("Store 'secret' = 42")
    mem_vault["store"]("secret", 42)
    print("Recall 'secret':", mem_vault["recall"]("secret"))
    print("Recall 'unknown':", mem_vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
