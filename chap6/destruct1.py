class Spam: 
    def __del__(self):
        print("削除されました")

spam1 = Spam()
spam2 = Spam()
spam3 = Spam()

# 循環参照を作る
spam1.other = spam2
spam2.other = spam1

#オブジェクトへの参照を削除する
del spam1, spam2, spam3

import gc 
gc.collect()

# spam1, spam2が解法されず、gc.garbageに格納される
print(gc.garbage)


