from abc import ABC
from abc import abstractmethod

class TransformABC(ABC):

    @abstractmethod
    def transform(self, source):
        """
        Transform a source.
        """
        # this is too vague
        # what should return?
        # select worksheets
        # select rows/cells
        # transform sheet
        # transform cells
