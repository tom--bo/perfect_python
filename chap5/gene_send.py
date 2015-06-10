def gen(step):
    val = 0
    while True:
        val = val + step
        step = yield val

if __name__ == '__main__':
    g = gen(3)
    ret = g.__next__()
    print(ret)

    ret = g.send(10)
    print(ret)

    ''' error
    ret = g.__next__()
    print(ret)
    '''
    


