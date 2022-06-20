"""A simple integration set of utilities connecting EmonPi's ecosystem with CouchDB"""

import os

from .EmonPiAdapter import EmonPiAdapter
from CleanEmonCore.dotfiles import get_dotfile

_CONFIG_FILENAME = "clean.cfg"
_SCHEMA_FILENAME = "schema.json"

PACKAGE_DIR = os.path.dirname(__file__)

# Check if config-file lies in directory of execution
# If not, consider working with the global one
if os.path.exists(_CONFIG_FILENAME):
    CONFIG_FILE = os.path.abspath(_CONFIG_FILENAME)
else:
    # If there is no global file, generate a new one
    from .setup import generate_config
    CONFIG_FILE = get_dotfile(_CONFIG_FILENAME, generate_config)

# Check if schema-file lies in directory of execution
# If not, consider working with the global one
if os.path.exists(_SCHEMA_FILENAME):
    SCHEMA_FILE = os.path.abspath(_SCHEMA_FILENAME)
else:
    # If there is no global file, generate a new one
    from .setup import generate_schema
    SCHEMA_FILE = get_dotfile(_SCHEMA_FILENAME, generate_schema)
