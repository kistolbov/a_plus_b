def a_plus_b(a, b) -> int:
    return a + b


def main():
    a, b = map(int, input().split())
    print(a_plus_b(a, b))


if __name__ == "__main__":
    main()
