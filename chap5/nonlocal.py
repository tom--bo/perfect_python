def outer():
    var1 = '外側の変数'
    var2 = 'これも外側の変数'
    count = 0

    def inner():
        nonlocal var1, count

        count += 1
        var1 = '内側で変更'
        var3 = '内側の変数'
        return (var1, var2, var3, count)
    return inner()

if __name__ == "__main__":
    print(outer())
    print(outer())

