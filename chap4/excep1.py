try:
    10/0
except ZeroDivisionError as e:
    # print('ZeroDivisionError occured!!')
    print(type(e))
    #print(format_tb(e.__traceback__))
    #print('メッセージ：{O}'.format(e.args))
