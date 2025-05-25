def main():
    values = [x ** 2 for x in range(10)]
    a = 1
    b = 1

    values = [b+x for x in values]
    print(values)


if __name__ == '__main__':
    main()
