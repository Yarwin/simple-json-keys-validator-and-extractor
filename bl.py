from os import listdir

from json_save_load import save_to_json
from make_output_dict import make_merged_output_dict, return_common_dict_entry

if __name__ == '__main__':

    jsons_path = './INPUT_DATA/'
    output_path = './OUTPUT_DATA/result.json'

    jsons = [f for f in listdir(jsons_path) if f.endswith('.json')]
    data = make_merged_output_dict(jsons, jsons_path)
    save_to_json(data, output_path)
    print(return_common_dict_entry.items_rejected)
