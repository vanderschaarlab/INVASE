import sys

from . import logger  # noqa: F401
from .method import INVASE  # noqa: F401

logger.add(sink=sys.stderr, level="CRITICAL")
