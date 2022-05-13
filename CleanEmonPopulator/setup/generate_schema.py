import json

from ..EmonPiAdapter import EmonPiAdapter


def generate_schema(config_file, schema_file):
    emon = EmonPiAdapter(config_file)
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
