from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс"""

    @abstractmethod
    def __add__(self, other):
        pass
