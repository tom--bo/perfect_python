def show_message(f):
    """ 関数fを受け取って、ログを出力してから関数fを呼び出す関数。wrapperを返す"""
    def wrapper():
        print("function called")
        return f()

    return wrapper

@show_message
def spam1():
    print("spam1 called")
    aa = 2
    return aa

@show_message
def spam2():
    a = 10
    return a

if __name__ == "__main__":
    print("before spam1 call")
    spam1()
    print("after spam1 call")

