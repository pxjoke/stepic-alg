def fib_mod(n, m):
    a = 0
    b = 1
    res = '0 1 '
    for i in range(2, int(n + 1)):
        tmp = b
        b = (a + b) % m
        a = tmp
        if a == 0 and b == 1:
            break
    return res


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
