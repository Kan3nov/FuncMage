from typing import Any, TypedDict
from collections.abc import Callable


class MemoryVault(TypedDict):
    store: Callable[[str, Any], None]
    recall: Callable[[str], Any]


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power = initial_power

    def counter(add_power: int) -> int:
        nonlocal power
        power += add_power
        return power
    return counter


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def apply_enchant(item_name: str) -> str:
        return enchantment_type + " " + item_name
    return apply_enchant


def memory_vault(
            ) -> MemoryVault:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        if (key in vault):
            return vault[key]
        return "Memory not found"
    return {"store": store, "recall": recall}


def main() -> None:
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
