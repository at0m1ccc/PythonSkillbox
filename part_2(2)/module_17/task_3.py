from collections import Counter


def can_be_poly(text: str) -> bool:
    counts_collect = Counter(text)
    odd_count = sum(1 for count in counts_collect.values() if count % 2 != 0)
    return odd_count <= 1


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
