from collections.abc import Callable
from typing import Any, Protocol
from time import time, sleep
from functools import wraps


class SpellCast(Protocol):
    def __call__(self, power: int, spell_name: str) -> str:
        ...


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("Casting ", func.__name__, "...", sep="")
        time1 = time()
        result = func(*args, **kwargs)
        time2 = time()
        print(f"Spell completed in {time2 - time1:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[[SpellCast], SpellCast]:
    def pow_val(func: SpellCast,
                ) -> SpellCast:
        @wraps(func)
        def wrapper(power: int, *args: Any, **kwargs: Any) -> Any:
            if (power >= min_power):
                return func(power, *args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return pow_val


def retry_spell(max_attempts: int
                ) -> Callable[[Callable[..., str]], Callable[..., str]]:
    def trials(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            attempts = 1
            while attempts <= max_attempts:
                try:
                    x = func(*args, **kwargs)
                    return x
                except Exception:
                    if attempts == max_attempts:
                        break
                    print("Spell failed, retrying... " +
                          f"(attempt {attempts}/{max_attempts})")
                finally:
                    attempts += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return trials


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        if not all(x.isalpha() or x.isspace() for x in name):
            return False
        return True

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(10)
        def meow(power: int, spell_name: str) -> str:
            return f"Successfully cast {spell_name} with {power} power"
        return meow(power, spell_name)


@spell_timer
def fireball() -> str:
    sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def explosion() -> str:
    raise ValueError
    return str


def main() -> None:
    print("Testing spell timer...")
    print("Result:", fireball())

    print("\nTesting retrying spell...")
    print(explosion())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Kanana"))
    print(MageGuild.validate_mage_name("Meow@Killer"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 7))


if __name__ == "__main__":
    main()
