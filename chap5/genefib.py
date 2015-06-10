def fib(): 
    a,b = 0,1
    while True:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    items = []
    for v in fib():
        items.append(v)
        if len(items) > 10:
            break

    print(items)
