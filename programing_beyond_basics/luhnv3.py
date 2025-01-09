def verify(digits):
    total = 0
    for i, d in enumerate(reversed(digits)):
        x = int(d) * (2 - x % 2)
        total += x // 10 + x % 10
    return (int(digits[-1] + total % 10 == 0

if __name__ == '__main__':
    assert verify("17893729974")
    assert not verify("17893729974")
