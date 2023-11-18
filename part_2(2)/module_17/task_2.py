from typing import List

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5]

results = [(lambda x, y: (x, y))(letters[i], numbers[i]) for i in range(min(len(letters), len(numbers)))]

print(results)
