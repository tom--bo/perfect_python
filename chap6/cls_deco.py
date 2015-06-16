import sys

#pythonのバージョンをチェックするデコレータ
def py_version(major, minor, micro):
    def deco(cls):
        if(major, minor, micro) > sys.version_info[:3]:
            raise RuntimeError(
                "class {O!r}はpyhton {1}.{2}.{3}が必要です。".format(cls, major, minor, micro))
        return cls
    return deco

# Python 3.1.0以上でのみ利用可能なクラス
#@py_version(3,5,0)
@py_version(3,1,0)
class Spam:
    pass
