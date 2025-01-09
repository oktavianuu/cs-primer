def verify (digits):
    total = 0
    for i, d in enumerate(reversed(digits[:-1])): # iterating in reverse but not the last one
        if i % 2 == 0:
            multiplier = 2 # double
        else:
            multiplier = 1 # not double
        x = int(d) * multiplier
        total += x // 10 + x % 10
    return 10 - (total % 10) == int(digits[-1])
    return False

if __name__ == '__main__':
    assert verify('17893729974')
    assert not verify('17893729975')
    print('ok')

