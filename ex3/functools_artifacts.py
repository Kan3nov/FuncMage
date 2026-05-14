from typing import Any, Protocol
from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


class EnchantmentFunc(Protocol):
    def __call__(self, target: str, power: int, element: str) -> str:
        ...


def main() -> None:
    def spell_reducer(spells: list[int], operation: str) -> int:
        if len(spells) == 0:
            return 0
        if operation == "add":
            return reduce(add, spells)

        elif operation == "multiply":
            return reduce(mul, spells)
        elif operation == "max":
            return reduce(lambda x, y: x if x > y else y, spells)
        elif operation == "min":
            return reduce(lambda x, y: x if x < y else y, spells)
        else:
            print("Error: Unknown Operation")
            return (-1)

    def partial_enchanter(base_enchantment: EnchantmentFunc
                          ) -> dict[str, Callable[[str], str]]:
        base1 = partial(base_enchantment, power=50, element="fire")
        base2 = partial(base_enchantment, power=50, element="water")
        base3 = partial(base_enchantment, power=50, element="air")
        return {"base1": base1, "base2": base2,
                "base3": base3}

    @lru_cache(maxsize=None)
    def memoized_fibonacci(n: int) -> int:
        if n < 2:
            return n
        return memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1)

    def spell_dispatcher() -> Callable[[Any], str]:
        @singledispatch
        def func(meow: Any) -> str:
            return "Unknown spell type"

        @func.register(int)
        def _(meow: int) -> str:
            return f"{meow} damage"

        @func.register(str)
        def _(meow: str) -> str:
            return meow

        @func.register(list)
        def _(meow: list[Any]) -> str:
            return f"{len(meow)} spells"
        return func

    def meow(target: str, power: int, element: str) -> str:
        return f"{element} spell is cast upon {target} " +\
               f"with a mana power of {power}"

    print("Testing spell reducer...")
    print("list to be reduced : ", [22, 33, 38, 31, 50, 47])
    print("Sum: ", spell_reducer([22, 33, 38, 31, 50, 47], "add"))
    print("Product: ", spell_reducer([22, 33, 38, 31, 50, 47], "multiply"))
    print("Max: ", spell_reducer([22, 33, 38, 31, 50, 47], "max"))

    print("\nTesting partial enchanter...")
    print("Using 3 versions of the same function but " +
          "with different preset arguments")
    for x in partial_enchanter(meow).values():
        print(x("Dragon"))

    print("\nTesting memoized fibonacci...")
    print("Fib(0)", memoized_fibonacci(0))
    print("Fib(1)", memoized_fibonacci(1))
    print("Fib(10)", memoized_fibonacci(10))
    print("Fib(15)", memoized_fibonacci(15))

    func = spell_dispatcher()
    print("\nTesting spell dispatcher...")
    print("Damage spell:", func(42))
    print("Enchantment:", func("fireball"))
    print("Multi-cast:", func(["meow", "meow", "mewo"]))
    print(func(("meow", "high")))


if __name__ == "__main__":
    main()
