import os

from CleanEmonPopulator import PACKAGE_DIR
from CleanEmonPopulator import CONFIG_FILE
from CleanEmonPopulator import SCHEMA_FILE


def test_dirs():
    assert os.path.exists(PACKAGE_DIR)
    assert os.path.isdir(PACKAGE_DIR)


def test_files():
    assert os.path.exists(CONFIG_FILE)
    assert os.path.isfile(CONFIG_FILE)

    assert os.path.exists(SCHEMA_FILE)
    assert os.path.isfile(SCHEMA_FILE)
