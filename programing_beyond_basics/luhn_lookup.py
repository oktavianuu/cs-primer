LOOKUPS = [
    dict(zip('0123456789', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))),
    dict(zip('0123456789', (0, 2, 4, 6, 8, 1, 3, 5, 7, 9))),
]

def verify(digits):
    return sum(LOOKUPS[i % 2][d] for i, d in enumerate(reversed(digits))) % 10 == 0

if __name__ == '__main__':
    assert verify('17893729974')
    assert not verify('17893729975')
    print('ok')


