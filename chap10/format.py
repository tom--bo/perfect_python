class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == "__main__":
    print("{0:04} {1:02}".format(2,8))
    print("{0:,}".format(999999))

    p = Point(4,5)
    print("({0.x}, {0.y})".format(p))

    data = {'x': 2, 'y': 3}
    print("({0[x]}, {0[y]})".format(data))
