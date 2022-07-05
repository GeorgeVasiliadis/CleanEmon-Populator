import json

from CleanEmonCore.dotfiles import get_dotfile
from CleanEmonCore.dotfiles import _CONFIG_FILENAME

from .. import _SCHEMA_FILENAME
from ..EmonPiAdapter import EmonPiAdapter


def generate_schema(schema_file=_SCHEMA_FILENAME):
    emon = EmonPiAdapter(get_dotfile(_CONFIG_FILENAME))
    list_ = emon.get_feed_list()

    print("Listing available feeds:\n")

    map_ = {}

    for position_id, feed in enumerate(list_):
        name = feed["name"]
        print(f"#{feed['id']} {name}: {feed['value']}")
        ans = input(f"Rename {name} to: ")
        if ans:
            name = ans
        map_[position_id] = name
        print("---")

    with open(schema_file, "w", encoding="utf8") as f_out:
        json.dump(map_, f_out)

    print(f"File was generated successfully at: {schema_file}!")
