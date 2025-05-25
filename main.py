def main():
    values = [x ** 2 for x in range(10)]
    a = 1
    values2 = [x + a for x in values]
    print(values2)

    b = 1
    values3 = [x + b for x in values]
    print(values3)


if __name__ == '__main__':
    main()
