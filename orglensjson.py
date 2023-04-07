import json


def compare_jsons(json1, json2):
    diff = {}
    for key in json1.keys():
        if key in json2.keys():
            if json1[key] != json2[key]:
                if isinstance(json1[key], dict) and isinstance(json2[key], dict):
                    inner_diff = compare_jsons(json1[key], json2[key])
                    if inner_diff:
                        diff[key] = inner_diff
                else:
                    diff[key] = [json1[key], json2[key]]
        else:
            diff[key] = [json1[key], None]
    for key in json2.keys():
        if key not in json1.keys():
            diff[key] = [None, json2[key]]
    return diff


json1_str = '{ "x": 10.1, "y": 20, "name": "Anu", "dob": "2010-10-10" }'
json2_str = '{ "x": 10, "y": 20, "name": "Ani", "dob": "2010-10-11", "z": 100 }'

json1 = json.loads(json1_str)
json2 = json.loads(json2_str)

diff = compare_jsons(json1, json2)
print(json.dumps(diff, indent=4))
