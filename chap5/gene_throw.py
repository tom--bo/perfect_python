def gen():
    for i in range(10):
        yield i

if __name__ == "__main__":
    g = gen()
    for v in g:
        print(v)
        if v > 2:
            g.throw(ValueError("Invalid value"))
