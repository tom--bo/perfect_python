
var1 = 'グローバル'

def spam():
    #var1 = 'ローカルで代入'
    global var1
    var1 = 'ローカルからglobalを変更'
    var2 = 'ローカル'
    return (var1, var2)

if __name__ == '__main__':
    ret = spam()
    # print(var1)
    print(ret)


