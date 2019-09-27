

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
    p += 15 * sd.get('D', 0)

    ne = sd.get('E', 0)
    p += 40 * ne
    nb = max(0, sd.get('B', 0)-int(ne/2))
    p += int(nb / 2) * 45 + (nb % 2) * 30
    ff = int(sd.get('F', 0) / 3)
    nf = max(0, sd.get('F', 0)-ff)
    p += 10 * nf
    p += 20 * sd.get('G', 0)

    nh = sd.get('H', 0)
    p += int(nh/10) * 80
    nh %= 10
    p += int(nh/5) * 45
    nh %= 5
    p += nh * 10

    p += sd.get('I', 0) * 35
    p += sd.get('J', 0) * 60

    nk = sd.get('K', 0)
    p += int(nk/2) * 120
    nk %= 2
    p += nk * 70
    p += sd.get('L', 0) * 90

    nn = sd.get('N', 0)
    p += 40 * nn
    nm = max(0, sd.get('M', 0)-int(nn/3))
    p += nm * 15
 
    p += sd.get('O', 0) * 10
    np = sd.get('P', 0)
    p += int(np/5) * 200
    np %= 5
    p += np * 50

    nr = sd.get('R', 0)
    p += nr * 50
    fq = int(nr/3)
    nq = max(0, sd.get('Q', 0)-fq)

    p += int(nq/3) * 80
    p += (nq%3) * 30
    

    fu = int(sd.get('U', 0) / 4)
    nu = max(0, sd.get('U', 0)-fu)
    p += 40 * nu

    nv = sd.get('V', 0)
    p += int(nv/3) * 130
    nv %= 3
    p += int(nv/2) * 90
    nv %= 2
    p += nv * 50

    p += 20 * sd.get('W', 0)

    ns = sd.get('S', 0)
    nt = sd.get('T', 0)
    nx = sd.get('X', 0)
    ny = sd.get('Y', 0)
    nz = sd.get('Z', 0)

    # cut lowest priced first then others (XSTYZ)
    ngrp = ns + nt + nx + ny + nz
    p += int(ngrp/3) * 45
    fgrp = ngrp % 3
    while fgrp > 0:
        if nz > 0:
            p += 21
            nz -= 1
        elif ny > 0:
            p += 20
            ny -= 1
        elif nt > 0:
            p += 20
            nt -= 1
        elif ns > 0:
            p += 20
            ns -= 1
        elif nx > 0:
            p += 17
            nx -= 1
        fgrp -= 1

    return int(p)






