import re

from abc import ABC
from abc import abstractmethod

class SelectABC(ABC):
    """
    SelectABC implementations determine if a source is selected.
    """

    @abstractmethod
    def select(self, source):
        """
        Return True to select this source.
        """


class SelectPathPattern(SelectABC):
    """
    Select source by path with a pattern.
    """

    def __init__(self, pattern, flags=0):
        self.pattern = re.compile(pattern, flags=flags)

    def select(self, source):
        """
        Return True to indicate this source should be kept.
        """
        return bool(self.pattern.match(source))
