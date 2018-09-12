from cs50 import get_int


def main():

    i = 0

    while i == 0:
        height = get_int("Введите высоту горки ")

        if (height < 0) or (height > 23):
            print("Число не входит в диапазон")
        else:
            break

    if height == 0:
        return False

    for i in range(1, height + 1):
        print(" " * (height - i), end='')
        print("#" * i, end='  ')
        print("#" * i)


if __name__ == "__main__":
    main()