"""Database"""

from warnings import warn


from . import models
from .models import BaseModel, model, Foreign, Primary, Unique, hook, validate
from .database import Database
from .utils import Row, Null
from .column import Column, text, integer, blob, real
from .signature import op
from .operators import this
from .table import Table
from .index import Index

def test_installed():
    """Is the module installed?"""
    return True

warn("This package is now renamed to LuminaDB. Please upgrade to LuminaDB", DeprecationWarning)

__version__ = "0.7.13"
__all__ = [
    "Database",
    "Table",
    "this",
    "op",
    "Column",
    "Null",
    "Row",
    "text",
    "integer",
    "real",
    "blob",
    "BaseModel",
    "models",
    "Foreign",
    "Primary",
    "Unique",
    "model",
    "hook",
    "validate",
    "Index"
]
