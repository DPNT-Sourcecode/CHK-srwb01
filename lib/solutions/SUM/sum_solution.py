# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if x < 0 or x > 100 or y < 0 or y > 100:
        raise ValueError()
    return x + y

