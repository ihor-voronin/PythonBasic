from abc import ABC, abstractmethod


class BaseCounter(ABC):

    @abstractmethod
    def increment(self):
        pass

    @abstractmethod
    def current(self) -> int:
        pass


class Counter(BaseCounter):
    # ToDo: implement
    pass
