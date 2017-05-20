def fib_mod(n, m):
    if n == 1 and n == 2:
        return 1

    pizano = [0, 1, 1]

    for i in range(3, n + 1):
        tmp = (pizano[i - 1] + pizano[i - 2]) % m
        if pizano[i - 1] == pizano[0] and tmp == pizano[1]:
            break
        if i == n:
            return tmp
        pizano.append(tmp)

    period = len(pizano) - 1
    position = n % period
    return pizano[position]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
