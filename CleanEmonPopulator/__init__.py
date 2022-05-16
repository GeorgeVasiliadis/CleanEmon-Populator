"""A simple integration set of utilities connecting EmonPi's ecosystem with CouchDB"""

import os
from .EmonPiAdapter import EmonPiAdapter

_DATA_DIR_NAME = "data"
_CONFIG_FILENAME = "emon.cfg"
_SCHEMA_FILENAME = "schema.json"

PACKAGE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(PACKAGE_DIR, _DATA_DIR_NAME)

# Ensure that the `$PACKAGE/data` dir exists
if not os.path.isdir(DATA_DIR):
    os.mkdir(DATA_DIR)

# Check if config-file lies in directory of execution
# If not, consider working with the global one
if os.path.exists(_CONFIG_FILENAME):
    CONFIG_FILE = os.path.abspath(_CONFIG_FILENAME)
else:
    CONFIG_FILE = os.path.join(DATA_DIR, _CONFIG_FILENAME)

    # If there is no global file, generate a new one
    if not os.path.isfile(CONFIG_FILE):
        from .setup import generate_config
        generate_config(CONFIG_FILE)

# Check if schema-file lies in directory of execution
# If not, consider working with the global one
if os.path.exists(_SCHEMA_FILENAME):
    SCHEMA_FILE = os.path.abspath(_SCHEMA_FILENAME)
else:
    SCHEMA_FILE = os.path.join(DATA_DIR, _SCHEMA_FILENAME)

    # If there is no global file, generate a new one
    if not os.path.isfile(SCHEMA_FILE):
        from .setup import generate_schema
        generate_schema(CONFIG_FILE, SCHEMA_FILE)
