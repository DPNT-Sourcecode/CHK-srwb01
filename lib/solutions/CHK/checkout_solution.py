

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sd = dict()
    for sku in skus:
        if sku in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if sku in sd:
                sd[sku] += 1
            else:
                sd[sku] = 1
        else:
            return -1

    pa = int(sd['A'] / 5) * 200
    sd['A'] %= 5
    pa += int(sd['A'] / 3) * 130 + (sd['A'] % 3) * 50
    pc = 20 * nc
    pd = 15 * nd
    pe = 40 * ne
    nb = max(0, nb-int(ne/2))
    pb = int(nb / 2) * 45 + (nb % 2) * 30
    ff = int(nf / 3)
    nf = max(0, nf-ff)
    pf = 10 * nf
    return int(pa + pb + pc + pd + pe + pf)



