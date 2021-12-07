import argparse
import os

from pathlib import Path

from .generatesource import GenerateDirectory
from .selectsource import SelectPathPattern

def director_from_pattern(pattern):
    path = Path(pattern)
    while not path.is_dir():
        path = path.parent
    return path

def main(argv=None):
    """
    Scrape and manipulate Excel files.
    """
    parser = argparse.ArgumentParser(
        description = main.__doc__,
        prog = 'exceltransformer',
    )

    parser.add_argument('--select-path', metavar='pattern')

    args = parser.parse_args(argv)

    path = director_from_pattern(args.select_path)
    generator = GenerateDirectory(path, recursive=True)
    selector = SelectPathPattern(args.select_path)

    for path in generator.generate():
        if selector.select(path):
            print(path)
