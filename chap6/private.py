class Spam:
    def __init__(self):
        self.__attr = 999
    def method(self):
#        print(self.__attr) #ここでもOK
        self.__method()
    def __method(self):
        print(self.__attr)

if __name__ == "__main__":
    spam = Spam()
    spam.method()
#    print(spam.__attr)
#    spam.__method()
