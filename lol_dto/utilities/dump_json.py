import json
import dataclasses

from lol_dto.classes.game import LolGame


def dump_json(lol_game: LolGame, filename: str, remove_empty: bool = True):
    """
    Dump the given LolGame to a local file

    Args:
        lol_game: the LolGame object to dump
        filename: the file to dump to
        remove_empty: whether or not to dump None fields in the JSON. True by default to lighten the object.

    Returns:
        -

    """

    output_dict = dataclasses.asdict(lol_game)

    if remove_empty:
        output_dict = delete_empty_fields(output_dict)

    with open(filename, "w+") as file:
        json.dump(output_dict, file)


def delete_empty_fields(d: dict) -> dict:
    for key, value in list(d.items()):
        if isinstance(value, dict):
            delete_empty_fields(value)
        elif value is None or value is []:
            d.pop(key)
        elif isinstance(value, list):
            # It's not empty because of the previous test
            for list_value in value:
                if isinstance(list_value, dict):
                    delete_empty_fields(list_value)

    return d
