def artifact_sorter(artifacts: list[dict[str, int | str]]
                    ) -> list[dict[str, int | str]]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict[str, int | str]],
                 min_power: int) -> list[dict[str, int | str]]:
    return list(filter(lambda x: int(x["power"]) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict[str, int | str]]
               ) -> dict[str, float | dict[str, int | str]]:
    stats: dict[str, float | dict[str, int | str]] = {}
    stats["max_power"] = max(mages, key=lambda x: x["power"])
    stats["min_power"] = min(mages, key=lambda x: x["power"])
    stats["avg_power"] = round(sum(list(map(lambda x: int(x["power"]), mages)))
                               / len(mages), 2)
    return stats


print("=== Lambda Sanctum ===")
print("\nTesting artifact sorter...")
artifacts: \
          list[dict[str, str | int]] = [{'name': 'Crystal Orb',
                                        'power': 79, 'type': 'weapon'},
                                        {'name': 'Wind Cloak',
                                        'power': 67, 'type': 'relic'},
                                        {'name': 'Crystal Orb',
                                        'power': 115, 'type': 'focus'},
                                        {'name': 'Earth Shield',
                                        'power': 105, 'type': 'relic'}]
print("artifacts before sorting: ", artifacts)
print("artifacts after sorting: ", artifact_sorter(artifacts))
print()

mages: list[dict[str, str | int]] = \
                             [
                              {'name': 'Luna', 'power': 89, 'element': 'ice'},
                              {'name': 'Morgan', 'power': 88,
                               'element': 'water'},
                              {'name': 'Sage', 'power': 67,
                               'element': 'shadow'},
                              {'name': 'Riley', 'power': 75, 'element': 'ice'},
                              {'name': 'Alex', 'power': 85, 'element': 'fire'}
                            ]
print("filtering the mages out of the ones with power less than 80...")
print("mages before filtering: ", mages)
print("mages after filtering: ", power_filter(mages, 80))
print()

print("Transforming spell names to have '*' as a prefix and a suffix")
spells = ['tsunami', 'darkness', 'tornado', 'fireball']
print("spells before tranforming: ", spells)
print("spells after transforming: ", spell_transformer(spells))
print()

print("Calculating mages stats...")
stats = mage_stats(mages)
print("Max power : ", stats["max_power"])
print("Min power : ", stats["min_power"])
print("Avg power : ", stats["avg_power"])
