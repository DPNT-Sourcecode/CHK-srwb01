

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

    p = int(sd['A'] / 5) * 200
    sd['A'] %= 5
    p += int(sd['A'] / 3) * 130 + (sd['A'] % 3) * 50
    p += 20 * sd['C']
    p += 15 * sd['D']
    p += 40 * sd['E']
    nb = max(0, sd['B']-int(sd['E']/2))
    p += int(nb / 2) * 45 + (nb % 2) * 30
    ff = int(sd['F'] / 3)
    nf = max(0, sd['F']-ff)
    p += 10 * nf
    p += 20 * sd['G']
    p += int(sd['H']/10) * 80
    sd['H'] %= 10
    p += int(sd['H']/5) * 45
    sd['H'] %= 5
    p += sd['H'] * 10
    p += sd['I'] * 35
    p += sd['J'] * 60
    p += int(sd['K']/2) * 150
    sd['K'] %= 2
    p += sd['K'] * 80
    p += sd['L'] * 90

    return int(p)






