# 基底クラス
class Base:
    def spam(self):
        print("Base.spam()")

    def ham(self):
        print("ham")

class Derived(Base):
    def spam(self):   # Base.spam()をオーバライド
        print("Derived.spam()")
        self.ham()

if __name__ == "__main__":
    obj1 = Base()
    obj1.spam()

    obj2 = Derived()
    obj2.spam()



