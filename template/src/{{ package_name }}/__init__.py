"""Copyright 2025 Bundesdruckerei GmbH.

Licensed under Apache-2.0, see the accompanying file LICENSE
"""

__all__ = [
    "__version__",
]

import importlib.metadata

__version__ = importlib.metadata.version(__name__)
