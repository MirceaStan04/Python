def unique_pair_sum(numbers, target):
    seen = set()
    pairs = set()

    for x in numbers:
        y = target - x
        if y in seen:
            a = x
            b = y
            if a > b:
                a, b = b, a
            pairs.add((a, b))
        seen.add(x)

    return pairs


numbers = [1, 2, 3, 4, 3, 5, 6]
target = 7
print(unique_pair_sum(numbers, target))
