from typing import List, Set, Dict, Tuple


def active_users_per_country(
    users: List[Tuple[int, str]],  # user_id / country pairs
    test_users: Set[int],          # don't count test users
) -> Dict[str, int]:
    counter = defaultdict(int)
    for user_id, country in users:
        if user_id not in test_users
            counter[country] += 1
    return counter
