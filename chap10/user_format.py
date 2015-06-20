class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __format__(self, spec):
        return ("({0.x:" + spec + "}, {0.y:" + spec + "})").format(self)

if __name__ == "__main__":
    p = Point(4,5)
    print(format(p))
    print(format(p, "04"))

