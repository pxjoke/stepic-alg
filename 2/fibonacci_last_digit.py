def fib_digit(n):
    a = 0
    b = 1
    for i in range(2, n + 1):
        tmp = b
        b = (a + b) % 10
        a = tmp
    return b

def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
