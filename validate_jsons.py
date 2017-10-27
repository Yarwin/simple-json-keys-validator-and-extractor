import re

from interface import keys_to_merge, keys_to_extract, output_keys
from json_save_load import load_from_json


def validate_value(value, key):
    phone = re.compile('((\+?\(?[0-9]+\)?)'
                       '?[ -]?(([\d]{2}[ -]?[\d]{3}[ -]?[\d]{2}[ -]?[\d]{2})|'
                       '([\d]{3}[ -]?[\d]{3}[ -][\d]{3})))')

    if type(value) == list:
        value = "; ".join(value)

    if key == 'phone':
        result = ''
        for number in phone.findall(value):
            result += number[0] + '; '
        return result

    value = re.sub(' +', ' ', value.replace('\n', ''))
    return value


def fix_key(data_to_fix, output_dict, key_to_fix):

    key_to_append = key_to_fix
    value = data_to_fix[key_to_fix]

    if key_to_append in keys_to_merge:
        key_to_append = keys_to_merge[key_to_append]

    if key_to_append in keys_to_extract:
        return fix_record_in_json(data_to_fix[key_to_append])

    for fixed_key in output_keys:
        if key_to_fix in output_keys[fixed_key]:
            key_to_append = fixed_key

    if type(value) == dict:
        output_dict[key_to_append] = fix_record_in_json(value)
    else:
        if not output_dict.get(key_to_append):
            output_dict[key_to_append] = ''
        if value:
            value = validate_value(value, key_to_append)
            output_dict[key_to_append] += value
        else:
            output_dict[key_to_append] = None

    return output_dict


def fix_record_in_json(data_to_fix):
    output_dict = {}

    for key_to_fix in data_to_fix:

        output_dict = fix_key(data_to_fix, output_dict, key_to_fix)

    return output_dict


def fix_keys_in_jsons(json_file, jsons_path):
    print('fixing {0}'.format(json_file))
    output_dict = dict()
    json_file = load_from_json(jsons_path + json_file)
    for key in json_file:
        better_key = re.sub(' +', ' ', key.replace('\n', ' '))

        if not output_dict.get(better_key):
            output_dict[better_key] = {}

        output_dict[better_key] = fix_record_in_json(json_file[key])

    return output_dict
