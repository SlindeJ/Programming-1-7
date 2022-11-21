class Shape:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = 0
        self.perim = 0

    def calc(self):
        self.area = self.length * self.width
        self.perim = self.length * 2 + self.width * 2

    def getarea(self):
        return self.area

    def getperim(self):
        return self.perim

    pass


def main():
    len = int(input("Enter length: "))
    wid = int(input("Enter width: "))
    shape = Shape(len, wid)
    shape.calc()
    area = shape.getarea()
    perim = shape.getperim()
    print("Area:", area)
    print("Perimiter", perim)
    pass


if __name__ == "__main__":
    main()
