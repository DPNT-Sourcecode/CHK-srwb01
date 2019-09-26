

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    na, nb, nc, nd, ne = 0, 0, 0, 0, 0
    for sku in skus:
        if 'A' == sku:
            na += 1
        elif 'B' == sku:
            nb += 1
        elif 'C' == sku:
            nc += 1
        elif 'D' == sku:
            nd += 1
        elif 'E' == sku:
            ne += 1
        else:
            return -1
    pa = int(na / 3) * 130 + (na % 3) * 50
    pc = 20 * nc
    pd = 15 * nd
    pe = 40 * ne
    nb = max(0, nb-ne/2)
    pb = int(nb / 2) * 45 + (nb % 2) * 30
    return int(pa + pb + pc + pd + pe)

