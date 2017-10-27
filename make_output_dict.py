from json_save_load import save_to_json
from validate_jsons import fix_keys_in_jsons


def check_if_item_in_output_dict(output_dict, item):

    for key in output_dict:
        output_item = output_dict[key]

        if output_item.get('phone') and item.get('phone'):
            if output_item['phone'] == item['phone'] and output_item['phone'] != None:
                return True

        if output_item.get('email') and item.get('email'):
            if output_item['email'] == item['email']:
                return True

    return False


def update_output_dict(merged_output_dict, json):
    for key in json:
        if not check_if_item_in_output_dict(merged_output_dict, json[key]):
            merged_output_dict[key] = json[key]

    return merged_output_dict


def make_merged_output_dict(json_files, jsons_path, output_path):
    merged_output_dict = {}
    for json in json_files:
        json_dict = fix_keys_in_jsons(json, jsons_path)
        print('appending {0} to output dict'.format(json))
        merged_output_dict = update_output_dict(merged_output_dict, json_dict)

    save_to_json(merged_output_dict, output_path)
    return merged_output_dict
