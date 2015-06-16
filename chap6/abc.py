from abc import ABCMeta, abstractmethod

class AbstractSpam(metaclass=ABCMeta):
    @abstractmethod
    def ham(self):
        pass

    @abstractmethod
    def egg(self):
        pass

class StillAbstractSpam(AbstractSpam):
    def ham(self):
        pass

class ConcreateSpam(StillAbstractSpam):
    def egg(self):
        pass

