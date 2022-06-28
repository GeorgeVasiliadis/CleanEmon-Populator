from .. import CONFIG_FILE
from .. import SCHEMA_FILE

from .generate_config import generate_config
from .generate_schema import generate_schema


def setup():
    generate_config(CONFIG_FILE)
    generate_schema(CONFIG_FILE, SCHEMA_FILE)
