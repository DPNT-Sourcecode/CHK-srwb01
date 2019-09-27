

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

    na = sd.get('A', 0)
    p = int(na/5) * 200
    na %= 5
    p += int(na/3) * 130 + (na%3) * 50
    p += 20 * sd.get('C', 0)
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

    p += 40 * sd['N']
    nm = max(0, sd['M']-int(sd['N']/3))
    p += nm * 15
 
    p += sd['O'] * 10
    p += int(sd['P']/5) * 200
    sd['P'] %= 5
    p += sd['P'] * 50

    p += sd['R'] * 50
    fq = int(sd['R']/3)
    nq = max(0, sd['Q']-fq)

    p += int(nq/3) * 80
    p += (nq%3) * 30
    
    p += 30 * sd['S']
    p += 20 * sd['T']

    fu = int(sd['U'] / 4)
    nu = max(0, sd['U']-fu)
    p += 40 * nu

    p += int(sd['V']/3) * 130
    sd['V'] %= 3
    p += int(sd['V']/2) * 90
    sd['V'] %= 2
    p += sd['V'] * 50

    p += 20 * sd['W']
    p += 90 * sd['X']
    p += 10 * sd['Y']
    p += 50 * sd['Z']

    return int(p)




