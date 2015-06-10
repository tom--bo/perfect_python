def simple_func(arg1, arg2):
    print('simple_func', arg1, arg2)

def spam():
    pass

def spam2(): return "ham"

def append_number(items=[]):
    items.append(1)
    return items

if __name__ == "__main__":
    simple_func('引数1', '引数2')
    spam()
    print(spam2())

    #デフォルト引数の再利用
    append_number()
    append_number()
    ret = append_number()
    print(ret)


