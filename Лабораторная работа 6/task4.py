import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename="input.csv", delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as f:
        text = f.read()

    text = text.split(new_line)
    result = [dict(zip(text[0].split(delimiter), line.split(delimiter))) for line in text[1:]]
    return result


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
