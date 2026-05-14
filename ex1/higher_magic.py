from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def electrify(target: str, power: int) -> str:
    return f"Electrify strikes {target} with a {power} volt lightning bolt"


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]
                   ) -> Callable[[str, int], tuple[str, str]]:
    def combination(target: str, power: int) -> tuple[str, str]:
        str1 = spell1(target, power)
        str2 = spell2(target, power)
        return (str1, str2)
    return combination


def power_amplifier(base_spell: Callable[[str, int], str], multiplier: int
                    ) -> Callable[[str, int], str]:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int], str]
                       ) -> Callable[[str, int], str]:
    def cond_caster(target: str, power: int) -> str:
        if (condition(target, power)):
            return spell(target, power)
        return "Spell fizzled"
    return cond_caster


def spell_sequence(spells: list[Callable[[str, int], str]]
                   ) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return sequence


def is_strong(target: str, value: int) -> bool:
    if value > 5 and target:
        return True
    return False


def main() -> None:
    print("=== Higher Magic ===")
    print("Using the first spell (heal): ", heal("Dragon", 12))
    print("Using the second spell (electrify): ", electrify("Goblin", 7))
    print("Testing the spell combiner...")
    print("Combined spell result: ",
          spell_combiner(heal, electrify)("Wizard", 14))
    print()
    print("Testing power amplifier...")
    print(f"Original: {heal("Knight", 3)}," +
          f" Amplified: {power_amplifier(heal, 3)("Knight", 3)}")
    print()
    print("Testing conditional caster :")
    print(f"Original: {electrify("Dragon", 4)}, " +
          "Conditional (fails if power is weak): " +
          f"{conditional_caster(is_strong, electrify)("Dragon", 4)}")
    print()
    print("Testing spell sequence: " +
          f"{spell_sequence([heal, electrify])("Knight", 6)}")


if __name__ == "__main__":
    main()
