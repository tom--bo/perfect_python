def show_message(text):
    def deco(f):
        """
        関数fを受け取ってログを出力してから関数fを呼び出す関数
        wrapperを返す
        """
        def wrapper():
            print(text)
            return f()
        return wrapper
    return deco

@show_message("spam() called!")
def spam():
    i = 0
    return i

if __name__ == "__main__":
    spam()
    print("finish")


