"""Database"""

from warnings import warn


from . import models
from .models import *
from .database import *
from .utils import *
from .column import *
from .signature import *
from .operators import *
from .table import *
from .index import *

warn("This package is now renamed to LuminaDB. Please upgrade to LuminaDB", DeprecationWarning)

__version__ = "0.7.15"
__all__ = [
    "Database",
    "Table",
    "this",
    "op",
    "Column",
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
