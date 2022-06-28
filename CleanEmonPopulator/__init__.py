"""A simple integration set of utilities connecting EmonPi's ecosystem with CouchDB"""

import os

from CleanEmonCore.dotfiles import get_dotfile

from .EmonPiAdapter import EmonPiAdapter

_CONFIG_FILENAME = "clean.cfg"
_SCHEMA_FILENAME = "schema.json"

# Check if config-file lies in directory of execution
# If not, consider working with the global one
if os.path.exists(_CONFIG_FILENAME):
    CONFIG_FILE = os.path.abspath(_CONFIG_FILENAME)
else:
    CONFIG_FILE = get_dotfile(_CONFIG_FILENAME)

# Check if schema-file lies in directory of execution
# If not, consider working with the global one
if os.path.exists(_SCHEMA_FILENAME):
    SCHEMA_FILE = os.path.abspath(_SCHEMA_FILENAME)
else:
    SCHEMA_FILE = get_dotfile(_SCHEMA_FILENAME)
