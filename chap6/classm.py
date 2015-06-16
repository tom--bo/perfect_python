class Spam:
    def method(self):
        """通常のインスタンスメソッド"""
        print(self)

    @classmethod
    def clsmethod(cls):
        """クラス・メソッド"""
        print(cls)

if __name__ == "__main__":
    spam = Spam()
    spam.method()
#    spam.clsmethod
    Spam.clsmethod()
