class WriteFile(object):
    def __init__(self, file_name):
        print('__init__が呼ばれました')
        self.file_name = file_name
    def __enter__(self):
        print('__enter__が呼ばれました')
        self.f = open(self.file_name, 'w')
        print('ファイルを開きました')
        return self.f
    def __exit__(self, type, value, traceback):
        print('__exit__が呼ばれました')
        self.f.close()

if __name__ == "__main__":
    with WriteFile('test3.txt') as f:
        print('withのブロックに入りました')
        f.write('はっはっは')
        print('withのブロックからでます')

