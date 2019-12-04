def create_size(amounts):
    min_a, max_a = float("inf"), 0
    sizes = []
    for a in amounts:
        min_a = min(min_a, a)
        max_a = max(max_a, a)
    for a in amounts:
        sizes.append(10 + (a - min_a) / (max_a - min_a) * 25)
    return sizes