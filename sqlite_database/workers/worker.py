"""Worker thread"""

# pylint: disable=wildcard-import,unused-wildcard-import

try:
    from luminadb.workers.worker import *  # type: ignore
except ImportError:
    raise ImportError(
        "Cannot find LuminaDB worker extra module, please install luminadb-workers"
    ) from None
