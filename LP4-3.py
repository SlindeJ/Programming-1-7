def main():
    eggs = int(input("Number of eggs: "))
    dozen = 0
    if 48 > eggs > 0:
        dozen = eggs // 12
        eggsleft = eggs - (dozen * 12)
        cost = 0.50
    if 72 > eggs >= 48:
        dozen = eggs // 12
        eggsleft = eggs - (dozen * 12)
        cost = 0.45
    if 132 > eggs >= 72:
        dozen = eggs // 12
        eggsleft = eggs - (dozen * 12)
        cost = 0.40
    if eggs >= 132:
        dozen = eggs // 12
        eggsleft = eggs - (dozen * 12)
        cost = 0.35
    extra = eggsleft / 12 * cost
    extra = round(extra, 2)
    pay = cost * dozen + extra
    print("The amount to be paid is :" + str(pay))
    pass


if __name__ == "__main__":
    main()
