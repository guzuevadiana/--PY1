from pprint import pprint


def numeral_system_dict(number: int) -> dict:
    return {"dec": number,
            "bin": bin(number),
            "oct": oct(number),
            "hex": hex(number)
            }


list_of_dictionary = [numeral_system_dict(number) for number in range(0, 16)]

pprint(list_of_dictionary)
