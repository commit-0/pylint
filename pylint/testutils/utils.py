from __future__ import annotations
import contextlib
import os
import sys
from collections.abc import Generator, Iterator
from copy import copy
from pathlib import Path
from typing import TextIO

@contextlib.contextmanager
def _patch_streams(out: TextIO) -> Iterator[None]:
    """Patch and subsequently reset a text stream."""
    pass

def create_files(paths: list[str], chroot: str='.') -> None:
    """Creates directories and files found in <path>.

    :param list paths: list of relative paths to files or directories
    :param str chroot: the root directory in which paths will be created

    >>> from os.path import isdir, isfile
    >>> isdir('/tmp/a')
    False
    >>> create_files(['a/b/foo.py', 'a/b/c/', 'a/b/c/d/e.py'], '/tmp')
    >>> isdir('/tmp/a')
    True
    >>> isdir('/tmp/a/b/c')
    True
    >>> isfile('/tmp/a/b/c/d/e.py')
    True
    >>> isfile('/tmp/a/b/foo.py')
    True
    """
    pass