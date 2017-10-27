from interface import common_items_in_dicts
from json_save_load import save_to_json
from statistics import DoubledItemsCounter
from validate_jsons import fix_keys_in_jsons


@DoubledItemsCounter
def return_common_dict_entry(output_dict, item):
    for key in output_dict:

        output_item = output_dict[key]

        for common_item_key in common_items_in_dicts.keys():
            if output_item.get(common_item_key) and item.get(common_item_key):

                if common_items_in_dicts.get(common_item_key):
                    search_pattern = common_items_in_dicts.get(common_item_key)
                    x = search_pattern.findall(output_item[common_item_key])
                    y = search_pattern.findall(item[common_item_key])

                    for item1 in x:
                        for item2 in y:
                            if item1[0] == item2[0]:
                                return output_dict[key]

                elif output_item[common_item_key] == item[common_item_key]:
                    return output_dict[key]
    return None


def merge_records(d1, d2):
    output_dict = d2.copy()
    for key, value in d1.items():
        if d2.get(key) is None:
            output_dict[key] = value
        elif type(d2.get(key)) is bool or type(d1.get(key)) is bool:
            output_dict[key] = value
        elif len(d2[key]) > len(d2[key]):
            output_dict[key] = value

    return output_dict


def update_output_dict(merged_output_dict, json):
    for key in json:
        item = return_common_dict_entry(merged_output_dict, json[key])
        if not item:
            merged_output_dict[key] = json[key]
        else:
            merged_output_dict[key] = merge_records(item, json[key])

    return merged_output_dict


def make_merged_output_dict(json_files, jsons_path):
    merged_output_dict = {}
    for json in json_files:
        json_dict = fix_keys_in_jsons(json, jsons_path)
        print('appending {0} to output dict'.format(json))
        merged_output_dict = update_output_dict(merged_output_dict, json_dict)

    return merged_output_dict
