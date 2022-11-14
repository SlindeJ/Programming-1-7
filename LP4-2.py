def main():
    weight = int(input("Enter Package Weight(Kg): "))
    length = int(input("Enter Package Length(centimeters): "))
    width = int(input("Enter Package Width(centimeters): "))
    height = int(input("Enter Package Height(centimeters): "))
    cms3 = length * width * height
    if weight > 27:
        print("Too Heavy")
    if cms3 > 100000:
        print("Too Large")
    if not weight > 27 and not cms3 > 100000:
        print("Accepted")
    pass


if __name__ == "__main__":
    main()
