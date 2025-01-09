def verify_imperative(digits):
    total = 0
    for i, d in enumerate(reversed(digits)):
        x = int(d) * (1 + i % 2)
        total += x // 10 + x
    return total % 10 == 0


def f(args):
    i, d = args
    x = int(d) * (1 + i % 2)
    return x // 10 + x

def verify_functional(digits):
    return sum([f(i, d) for i, d in enumerate(reversed(digits))]) % 10 == 0

if __name__ == '__main__':
    for verify in (verify_imperative, verify_functional):
        assert verify("17893729974")
        assert not verify("17893729975")
    print("ok")
