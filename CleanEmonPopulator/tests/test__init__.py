import os

from CleanEmonPopulator import CONFIG_FILE
from CleanEmonPopulator import SCHEMA_FILE


def test_files():
    assert os.path.exists(CONFIG_FILE)
    assert os.path.isfile(CONFIG_FILE)

    assert os.path.exists(SCHEMA_FILE)
    assert os.path.isfile(SCHEMA_FILE)
