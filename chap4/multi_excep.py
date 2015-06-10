def write(file_name, dict_input):
    f = None
    try:
        f = open(file_name, 'w')
        data = dict_input['data']
        f.write(data)
        f.close()
    except KeyError as e:
        print('エラー種別：{0}'.format(type(e)))
        print(e)
        print('キーが見つかりませんでした：{0}'.format(str(dict_input)))
    except(FileNotFoundError, TypeError) as e:
        print('エラー種別：{0}'.format(type(e)))
        print(e)
        print('キーが見つかりませんでした：{0}'.format(file_name))
    except:
        print('何かのエラーが発生')
    else:
        print('問題なく処理が終了しました。')
    finally:
        if f is not None:
            print('ファイルを閉じます')
            f.close()

if __name__ == "__main__":
    d = {'meta': '寿限無', 'data': 'すりきれ'}
    a = ''
    # write('test.txt', d)
    # write(None, d)
    write('test.txt', a)

