from typing import Any

StatsValues = list[dict[str, Any]]


def get_not_found_error_msg(name: str) -> str:
    return f"Pokemon {name} was not found. Check the spelling and try again. In case of composite pokemon names, use hyphen (e.g. wormadam-plant)"


def get_stat_value_from_all_stats(name: str, stats: StatsValues):
    for s in stats:
        if s["stat__name"] == name:
            return s["value"]


def get_stat_values_from_all_stats(
    name: str, first_stats: StatsValues, second_stats: StatsValues
) -> tuple[int, int]:
    first = get_stat_value_from_all_stats(name, first_stats)
    second = get_stat_value_from_all_stats(name, second_stats)
    return first, second
