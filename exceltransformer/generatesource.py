from abc import ABC
from abc import abstractmethod
from pathlib import Path

class GenerateABC(ABC):

    @abstractmethod
    def generate(self):
        """
        Generate sources.
        """


class GenerateDirectory(GenerateABC):
    """
    Generate directory listing.
    """

    def __init__(
        self,
        root,
        recursive = False,
    ):
        self.root = root
        self.recursive = recursive

    def _generate(self, root):
        for path in Path(root).iterdir():
            if path.is_dir():
                if self.recursive:
                    yield from self._generate(path)
                else:
                    yield path
            elif path.is_file():
                yield path

    def generate(self):
        yield from map(str, self._generate(self.root))
