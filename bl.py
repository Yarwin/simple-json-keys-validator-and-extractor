from os import listdir

from make_output_dict import make_merged_output_dict


if __name__ == '__main__':


    jsons_path = './INPUT_DATA/AGENCJE/'
    output_path = './OUTPUT_DATA/agencje.json'

    jsons = [f for f in listdir(jsons_path) if f.endswith('.json')]
    make_merged_output_dict(jsons, jsons_path, output_path)
